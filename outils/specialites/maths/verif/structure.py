"""Contrôle de structure de chaque chapitre rédigé : champs présents, nombre de QCM, renvois « Revoir le
paragraphe » valides, animations déclarées, réponses de QCM dans les bornes.

Usage : python3 outils/specialites/maths/verif/structure.py
"""
import json, os, re, subprocess, sys
ICI = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ICI, "..", "src")
NUMS = sorted(int(f[2:-3]) for f in os.listdir(SRC) if f.startswith("ch") and f[2:-3].isdigit())
autres = [f for f in sorted(os.listdir(SRC)) if f.endswith(".js") and not re.match(r"ch\d+\.js$", f) and f not in ("app.js", "programme.js", "pages.js", "mathml.js", "widgets.js")]
MOTEUR = "var R=String.raw;var TeX={fmt:x=>x,math:x=>x};var document={documentElement:{classList:{contains:()=>false}}};var ICONES={};var WIDGETS={};"
js = MOTEUR + "\n".join(open(os.path.join(SRC, f), encoding="utf-8").read() for f in autres)
js += "\n".join(open(os.path.join(SRC, "ch%d.js" % i), encoding="utf-8").read() for i in NUMS)
js += "\nconsole.log(JSON.stringify({anims:Object.keys(ANIMS),ch:[" + ",".join("CH%d" % i for i in NUMS) + "]}));"
r = subprocess.run(["node", "-"], input=js, capture_output=True, text=True)
if r.returncode:
    print(r.stderr[:800]); sys.exit(1)
d = json.loads(r.stdout)
CHAMPS = ["essentiel", "attendus", "cours", "pieges", "demos", "algos", "methodes", "exos", "retenir", "qcm", "cartes"]
ok = True
for c in d["ch"]:
    pb = []
    for k in CHAMPS:
        if k not in c or not c[k]:
            pb.append("champ " + k + " manquant ou vide")
    ids = {s["id"] for s in c.get("cours", [])} | {"pieges"}
    for q in c.get("qcm", []):
        if q.get("ref") and q["ref"] not in ids:
            pb.append("renvoi inconnu : " + q["ref"])
        if not (0 <= q["r"] < len(q["c"])):
            pb.append("réponse hors bornes : " + q["q"][:40])
    html = json.dumps(c)
    for a in re.findall(r'data-anim=\\"([A-Za-z0-9_-]+)\\"', html):
        if a not in d["anims"]:
            pb.append("animation inconnue : " + a)
    n_anim = len(re.findall(r'data-anim=', html))
    if not (12 <= len(c.get("qcm", [])) <= 15):
        pb.append("QCM : %d questions" % len(c.get("qcm", [])))
    print("%-5s %-45s QCM %2d  cartes %2d  exos %d  anims %d  %s" % (c["id"], c["titre"][:45], len(c.get("qcm", [])), len(c.get("cartes", [])), len(c.get("exos", [])), n_anim, "OK" if not pb else "; ".join(pb)))
    ok = ok and not pb
sys.exit(0 if ok else 1)
