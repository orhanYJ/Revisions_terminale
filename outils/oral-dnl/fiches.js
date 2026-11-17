/* Fiches PDF de l'oral DNL : une fiche A4 recto-verso par key issue et par key term (17/11/2026).
   Recto : la question, les notes à puces par partie (durée conseillée) et les questions du jury avec réponses courtes (jury_court).
   Verso : le discours rédigé complet.
   Usage, depuis la racine : node outils/oral-dnl/fiches.js            (toutes les fiches, EN et FR)
                             node outils/oral-dnl/fiches.js h-t1-ki-4  (une seule)
   Sortie : dnl/fiches/oral/<id>-<en|fr>.pdf. Chaque page doit tenir sur une face : la taille du texte est réduite
   pas à pas jusqu'à ce que le recto et le verso tiennent (contrôle de deux pages exactement à la fin). */
const fs = require("fs"), path = require("path");
const { chromium } = require("playwright");
const D = __dirname, RACINE = path.join(D, "..", "..");
const SORTIE = path.join(RACINE, "dnl", "fiches", "oral");
const seul = process.argv[2] || null;

const THEMES = { "h-t1": ["History · Theme 1: The fragilisation of democracy, totalitarianism and WWII (1929–1945)", "Histoire · Thème 1 : La fragilisation des démocraties, les totalitarismes et la Seconde Guerre mondiale (1929-1945)"] };
const esc = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const mmss = t => Math.floor(t / 60) + ":" + String(t % 60).padStart(2, "0");
const duree = d => d < 60 ? d + " s" : Math.floor(d / 60) + " min" + (d % 60 ? " " + String(d % 60).padStart(2, "0") : "");
const premiere = a => a.split(/(?<=[.!?])\s+/)[0];

function page(it, lang, theme) {
  const FR = lang === "fr", L = it[lang];
  const kind = it.kind === "issue" ? "Key Issue" : "Key Term";
  let cum = 0;
  const secs = L.sections.map(s => {
    const a = cum; cum += s.d;
    const lis = s.pts.map(p => `<li${/^(Judgement|Jugement|In short|En bref)\s*:/.test(p) ? ' class="jug"' : ""}>${esc(p)}</li>`).join("");
    return `<div class="sec"><div class="sec-h"><span class="sec-t">${esc(s.t)}</span><span class="sec-d">≈ ${duree(s.d)} <small>${mmss(a)} → ${mmss(cum)}</small></span></div><ul>${lis}</ul></div>`;
  }).join("");
  const courtes = L.jury_court || L.jury.map(j => premiere(j[1]));
  const jury = L.jury.map((j, i) => `<div class="jq"><b>${esc(j[0])}</b><span>${esc(courtes[i])}</span></div>`).join("");
  const disc = (L.discours || []).map(b => `<div class="db"><div class="db-t">${esc(b.t)}</div>${b.p.split("\n\n").map(x => `<p>${esc(x)}</p>`).join("")}</div>`).join("");
  const tete = (verso) => `<div class="tete${verso ? " petite" : ""}">
      <div class="kicker">${FR ? "Oral" : "Oral"} · ${kind} · ${esc(theme)}</div>
      <h1>${esc(FR ? it.q_fr : it.q)}</h1>
      ${FR ? `<div class="qen">${esc(it.q)}</div>` : ""}
      ${verso ? "" : `<div class="meta">${FR ? "4 min 30 visées · 5 min au maximum · chapitres à mobiliser :" : "Aim for 4 min 30 · 5 min at most · chapters to draw on:"} ${(it.chapitres || []).slice().sort().map(c => `<i>${c}</i>`).join(" ")}</div>`}
    </div>`;
  return `<!doctype html><html lang="${lang}"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Inter:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
<style>
@page { size: A4; margin: 0; }
:root { --ink:#1F2433; --slate:#17233F; --wine:#8E2F2A; --gold:#B8924F; --gold2:#8E6F37; --paper:#F7F3EA; --line:#CBBFA3; --muted:#6B6350; --fs: 9.4pt; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { margin: 0; font-family: Inter, Arial, sans-serif; color: var(--ink); }
.page { width: 210mm; height: 297mm; padding: 12mm 13mm 11mm; position: relative; overflow: hidden; page-break-after: always; display: flex; flex-direction: column; }
.page:last-child { page-break-after: auto; }
.corps { font-size: var(--fs); line-height: 1.4; flex: 1 1 auto; min-height: 0; overflow: hidden; }
.tete { border: 1.5px solid var(--gold); outline: 1px solid var(--gold); outline-offset: 2px; background: var(--paper); padding: 8px 12px 7px; margin: 3px 3px 9px; }
.kicker { font-size: 7pt; letter-spacing: .08em; text-transform: uppercase; font-weight: 700; color: var(--gold2); }
h1 { margin: 3px 0 0; font-family: 'Cormorant Garamond', Georgia, serif; font-weight: 700; font-size: 16.5pt; line-height: 1.12; color: var(--slate); }
.tete.petite h1 { font-size: 13pt; }
.qen { font-size: 8pt; font-style: italic; color: var(--muted); margin-top: 2px; }
.meta { font-size: 7.6pt; color: var(--gold2); font-weight: 600; margin-top: 4px; }
.meta i { font-style: normal; background: #EFE8D8; color: var(--slate); border-radius: 3px; padding: 0 4px; margin-left: 2px; }
.lab { font-size: 7.2pt; letter-spacing: .09em; text-transform: uppercase; font-weight: 700; color: var(--gold2); margin: 2px 0 4px; }
.sec { border-left: 2.5px solid var(--gold); padding: 1px 0 1px 9px; margin: 0 0 6px; break-inside: avoid; }
.sec-h { display: flex; justify-content: space-between; align-items: baseline; gap: 8px; }
.sec-t { font-family: 'Cormorant Garamond', Georgia, serif; font-weight: 700; font-size: 1.32em; color: var(--slate); }
.sec-d { font-size: .8em; font-weight: 700; color: var(--gold2); white-space: nowrap; }
.sec-d small { font-weight: 500; color: var(--muted); }
.sec ul { margin: 1px 0 0; padding-left: 15px; }
.sec li { margin-bottom: 1.5px; }
.sec li::marker { color: var(--gold); }
.sec li.jug { font-weight: 700; color: var(--slate); }
.jury { margin-top: 8px; background: var(--paper); border: 1px solid var(--line); padding: 6px 10px 4px; break-inside: avoid; }
.jq { margin-bottom: 4px; }
.jq b { display: block; color: var(--slate); }
.jq span { display: block; padding-left: 10px; border-left: 2px solid var(--line); margin-top: 1px; }
.db { margin-bottom: 6px; }
.db-t { font-family: 'Cormorant Garamond', Georgia, serif; font-weight: 700; font-size: 1.28em; color: var(--slate); border-bottom: 1px solid var(--gold); margin-bottom: 2px; }
.db p { margin: 0 0 3px; text-align: justify; hyphens: auto; }
.pied { font-size: 7pt; color: var(--muted); display: flex; justify-content: space-between; border-top: 1px solid var(--line); padding-top: 3px; margin-top: 4px; flex: 0 0 auto; }
</style></head><body>
<div class="page" id="recto">${tete(false)}<div class="corps">
  <div class="lab">${FR ? "Les notes — à développer à voix haute" : "Your notes — to develop out loud"}</div>${secs}
  <div class="jury"><div class="lab">${FR ? "Questions possibles du jury — réponses courtes" : "Possible questions from the jury — short answers"}</div>${jury}</div>
</div><div class="pied"><span>${FR ? "Atlas de révision · Oral" : "Revision Atlas · Oral"}</span><span>${FR ? "Recto · les notes" : "Front · the notes"}</span></div></div>
<div class="page" id="verso">${tete(true)}<div class="corps">
  <div class="lab">${FR ? "Le discours rédigé (≈ 4 min 30 à voix haute)" : "The written speech (≈ 4 min 30 out loud)"}</div>${disc}
</div><div class="pied"><span>${FR ? "Atlas de révision · Oral" : "Revision Atlas · Oral"}</span><span>${FR ? "Verso · le discours" : "Back · the speech"}</span></div></div>
</body></html>`;
}

(async () => {
  fs.mkdirSync(SORTIE, { recursive: true });
  const items = [];
  for (const f of fs.readdirSync(D).filter(f => /^[hg]_t\d+_(issues|terms)\.json$/.test(f))) {
    const theme = f.slice(0, f.indexOf("_", 2)).replace("_", "-");
    for (const it of JSON.parse(fs.readFileSync(path.join(D, f), "utf8"))) if (!seul || it.id === seul) items.push([it, theme]);
  }
  const b = await chromium.launch();
  const p = await b.newPage();
  let n = 0;
  for (const [it, theme] of items) for (const lang of ["en", "fr"]) {
    if (!it[lang].discours) { console.log("sans discours :", it.id, lang); continue; }
    await p.setContent(page(it, lang, THEMES[theme][lang === "fr" ? 1 : 0]), { waitUntil: "networkidle" });
    await p.evaluate(() => document.fonts.ready);
    // réduit le texte jusqu'à ce que chaque face tienne (le corps ne déborde pas)
    let fs_ = 10.2;
    for (; fs_ >= 7.4; fs_ -= 0.1) {
      const ok = await p.evaluate(v => {
        document.documentElement.style.setProperty("--fs", v + "pt");
        return [...document.querySelectorAll(".page")].every(pg => { const c = pg.querySelector(".corps"); return c.scrollHeight <= c.clientHeight + 1; });
      }, fs_.toFixed(1));
      if (ok) break;
    }
    if (fs_ < 7.4) throw new Error("trop long pour une face : " + it.id + " " + lang);
    const f = path.join(SORTIE, it.id + "-" + lang + ".pdf");
    await p.pdf({ path: f, width: "210mm", height: "297mm", printBackground: true, margin: { top: 0, bottom: 0, left: 0, right: 0 } });
    const pages = (fs.readFileSync(f, "latin1").match(/\/Type\s*\/Page[^s]/g) || []).length;
    if (pages !== 2) throw new Error(f + " : " + pages + " pages au lieu de 2");
    console.log(path.relative(RACINE, f), "· texte " + fs_.toFixed(1) + " pt");
    n++;
  }
  await b.close();
  console.log(n, "fiches");
})().catch(e => { console.error(e); process.exit(1); });
