#!/usr/bin/env node
/* Exécute chaque extrait de code du site avec python3 et compare la sortie à celle qui est affichée.
   Usage : node outils/specialites/nsi/verifier_code.js [motif]  */
const fs = require("fs"), path = require("path"), os = require("os"), cp = require("child_process");
const SRC = path.join(__dirname, "src");
/* même liste et même ordre que build.py (DONNEES) */
const ORDRE = JSON.parse(fs.readFileSync(path.join(__dirname, "build.py"), "utf8").match(/^DONNEES\s*=\s*(\[[^\]]*\])/m)[1]);
let js = ORDRE.filter(f => fs.existsSync(path.join(SRC, f))).map(f => fs.readFileSync(path.join(SRC, f), "utf8")).join("\n");
const ctx = {};
new Function("ctx", js + "\nctx.CODE = CODE; ctx.CH = CH;")(ctx);
const CODE = ctx.CODE, motif = process.argv[2] || "";
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "nsi-"));
const norm = s => s.replace(/\r/g, "").split("\n").map(l => l.replace(/\s+$/, "")).join("\n").replace(/^\n+|\n+$/g, "");
let ok = 0, ko = 0, saut = 0;
const DOCTEST = `
import doctest, sys
texte = open(sys.argv[1], encoding="utf-8").read()
globs = {"__name__": "__main__"}
pre = open(sys.argv[2], encoding="utf-8").read()
exec(compile(pre, "deps", "exec"), globs)
t = doctest.DocTestParser().get_doctest(texte, globs, "extrait", None, 0)
r = doctest.DocTestRunner(optionflags=doctest.ELLIPSIS)
r.run(t)
sys.exit(1 if r.failures else 0)
`;
fs.writeFileSync(path.join(tmp, "_doctest.py"), DOCTEST);
/* SQL : exécuté par sqlite3 ; chaque SELECT affiche son en-tête puis ses lignes, valeurs séparées par " | " */
const SQL = `
import sqlite3, sys
base = sqlite3.connect(":memory:")
base.execute("PRAGMA foreign_keys = ON")
base.executescript(open(sys.argv[1], encoding="utf-8").read())
texte = open(sys.argv[2], encoding="utf-8").read()
for req in [r.strip() for r in texte.split(";") if r.strip() and not all(l.strip().startswith("--") for l in r.strip().splitlines())]:
    cur = base.execute(req)
    if cur.description:
        print(" | ".join(d[0] for d in cur.description))
        for ligne in cur.fetchall():
            print(" | ".join("NULL" if v is None else str(v) for v in ligne))
base.commit()
`;
fs.writeFileSync(path.join(tmp, "_sql.py"), SQL);
for (const id of Object.keys(CODE)) {
  if (motif && !id.includes(motif)) continue;
  const c = CODE[id];
  if (c.run === false) { saut++; continue; }
  const dir = fs.mkdtempSync(path.join(tmp, "x"));
  const deps = (c.deps || []).map(d => { if (!CODE[d]) throw new Error("dep inconnue " + d + " dans " + id); return CODE[d].src; }).join("\n\n");
  for (const [nom, ref] of Object.entries(c.files || {})) fs.writeFileSync(path.join(dir, nom), CODE[ref] ? CODE[ref].src : ref);
  let res, attendu, obtenu, bon;
  if (c.sql) {
    fs.writeFileSync(path.join(dir, "deps.sql"), deps);
    fs.writeFileSync(path.join(dir, "req.sql"), c.src);
    res = cp.spawnSync("python3", [path.join(tmp, "_sql.py"), "deps.sql", "req.sql"], { cwd: dir, encoding: "utf8" });
    obtenu = norm(res.stdout);
    attendu = c.out === undefined ? null : norm(c.out);
    bon = attendu === null || obtenu === attendu;
    if (c.err) { const der = norm(res.stderr).split("\n").filter(Boolean).pop() || ""; if (!der.includes(c.err)) { bon = false; obtenu += "\n[stderr] " + der; } }
    else if (res.status !== 0) { bon = false; obtenu += "\n[stderr] " + res.stderr.slice(-600); }
  } else if (c.console) {
    fs.writeFileSync(path.join(dir, "t.txt"), c.src);
    fs.writeFileSync(path.join(dir, "deps.py"), deps);
    res = cp.spawnSync("python3", [path.join(tmp, "_doctest.py"), "t.txt", "deps.py"], { cwd: dir, encoding: "utf8" });
    bon = res.status === 0;
    obtenu = res.stdout + res.stderr;
  } else {
    fs.writeFileSync(path.join(dir, "prog.py"), (c.verif ? "" : "") + (deps ? "import sys as _s, io as _io\n_v = _s.stdout\n_s.stdout = _io.StringIO()\n" + deps + "\n_s.stdout = _v\n\n" : "") + c.src + (c.verif ? "\n" + c.verif : ""));
    res = cp.spawnSync("python3", ["prog.py"], { cwd: dir, encoding: "utf8", timeout: 60000 });
    obtenu = norm(res.stdout);
    attendu = c.out === undefined ? null : norm(c.out);
    bon = true;
    if (attendu !== null && obtenu !== attendu) bon = false;
    if (c.err) {
      const der = norm(res.stderr).split("\n").filter(Boolean).pop() || "";
      if (!der.startsWith(c.err)) { bon = false; obtenu += "\n[stderr] " + der; }
    } else if (res.status !== 0) { bon = false; obtenu += "\n[stderr] " + res.stderr.slice(-600); }
    if (c.warn && !res.stderr.includes(c.warn)) { bon = false; obtenu += "\n[warning manquant] " + res.stderr; }
  }
  if (bon) ok++;
  else { ko++; console.log("✘ " + id + "\n--- attendu ---\n" + (attendu === undefined ? "(doctest)" : attendu) + "\n--- obtenu ---\n" + obtenu + "\n"); }
}
console.log(`${ok} extraits conformes, ${ko} en échec, ${saut} non exécutés (code à compléter).`);
process.exit(ko ? 1 : 0);
