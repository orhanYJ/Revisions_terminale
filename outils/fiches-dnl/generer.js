/* Génère les fiches imprimables du site DNL : dnl/fiches/<CHAPITRE>-<en|fr>.pdf
   Le cours est lu dans dnl/index.html (constantes H1, H2, H3…) ; la frise, la carte et le schéma
   viennent de fiches.js et de cartes/ (produites par cartes.py).
   Usage, depuis la racine du dépôt :  node outils/fiches-dnl/generer.js [H1 H2 …]
   Dépendance : playwright (Chromium). Relancer après toute modification d'un chapitre. */
const fs = require("fs");
const path = require("path");
const ICI = __dirname;
const RACINE = path.resolve(ICI, "..", "..");
const { chromium } = require(process.env.PW || "playwright");
const CONF = require("./fiches.js");

const html = fs.readFileSync(path.join(RACINE, "dnl", "index.html"), "utf8");
const script = [...html.matchAll(/<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)<\/script>/g)].map(m => m[1]).reduce((a, b) => (a.length > b.length ? a : b));
function lire(nom) {
  const i = script.indexOf("const " + nom + " =");
  if (i < 0) throw new Error("constante introuvable : " + nom);
  let j = script.indexOf("{", i), d = 0, k;
  for (k = j; k < script.length; k++) {
    const c = script[k];
    if (c === '"') { k++; while (script[k] !== '"') { if (script[k] === "\\") k++; k++; } continue; }
    if (c === "{") d++; else if (c === "}") { d--; if (!d) break; }
  }
  const src = script.slice(j, k + 1);
  try { return JSON.parse(src); } catch (e) { return Function("return (" + src + ")")(); }
}

const esc = t => String(t == null ? "" : t).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const T = {
  en: { kicker: "DNL History-Geography · Terminale BFI · M. Ros", frise: "Ten dates to know", enjeu: "The big picture", objective: "Objective", ki: "Key Issues", kt: "Key Terms", carte: "Summary map", zoom: "Zoom", serie: "Stage by stage (same colours)", schema: "Summary diagram", cours: "The course", ex: "Example", hors: "outside the course", acteurs: "Key figures", chiffres: "Numbers", vocab: "Vocabulary", partiel: "Partial sheet: only what has been taught in class so far. Still to come: ", genere: "Revision Atlas · printable sheet", pdate: "Generated on " },
  fr: { kicker: "DNL Histoire-Géographie · Terminale BFI · M. Ros", frise: "Dix dates à connaître", enjeu: "L'enjeu", objective: "Objectif", ki: "Key Issues", kt: "Key Terms", carte: "Carte de synthèse", zoom: "Zoom", serie: "Étape par étape (mêmes couleurs)", schema: "Schéma de synthèse", cours: "Le cours", ex: "Exemple", hors: "hors cours", acteurs: "Acteurs", chiffres: "Chiffres clés", vocab: "Vocabulaire", partiel: "Fiche partielle : seulement ce qui a été vu en classe. Reste à venir : ", genere: "Atlas de révision · fiche imprimable", pdate: "Générée le " }
};

/* dates de la frise en français : mois abrégés à la française, « 1er » */
const MOIS = { "Jan.": "janv.", "Feb.": "févr.", "Mar.": "mars", "Apr.": "avr.", "May": "mai", "June": "juin", "July": "juil.", "Aug.": "août", "Sept.": "sept.", "Oct.": "oct.", "Nov.": "nov.", "Dec.": "déc." };
const dateFr = d => d.replace(/\b(Jan\.|Feb\.|Mar\.|Apr\.|May|June|July|Aug\.|Sept\.|Oct\.|Nov\.|Dec\.)/g, m => MOIS[m]).replace(/\b1 (?=[a-zé])/g, "1er ").replace(/–/g, "-");
/* frise : axe horizontal, dates à pas régulier, textes alternés au-dessus et au-dessous */
function frise(items, lang) {
  const L = lang === "fr" ? 2 : 1, n = items.length, W = 1000, H = 330, ax = H / 2, pas = (W - 170) / (n - 1);
  const wrap = (t, max) => { const w = t.split(" "), out = []; let cur = ""; w.forEach(m => { if ((cur + " " + m).trim().length > max) { out.push(cur); cur = m; } else cur = (cur + " " + m).trim(); }); if (cur) out.push(cur); return out; };
  let s = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="100%"><line x1="20" y1="${ax}" x2="${W - 14}" y2="${ax}" stroke="#17233F" stroke-width="3"/><path d="M${W - 14},${ax - 8}L${W},${ax}L${W - 14},${ax + 8}z" fill="#17233F"/>`;
  items.forEach((it, i) => {
    const x = 80 + i * pas, haut = i % 2 === 0, lignes = wrap(it[L], 17);
    const y0 = haut ? ax - 26 : ax + 30;
    s += `<line x1="${x}" y1="${ax}" x2="${x}" y2="${haut ? ax - 18 : ax + 18}" stroke="#B8924F" stroke-width="2"/><circle cx="${x}" cy="${ax}" r="7" fill="#8E2F2A" stroke="#fff" stroke-width="2"/>`;
    const dt = lang === "fr" ? dateFr(it[0]) : it[0];
    const coupe = dt.length > 11 && /[–-]/.test(dt) ? dt.split(/(?<=[–-])/) : [dt];
    const date = coupe.map((l, k) => `<tspan x="${x}"${k ? ' dy="1.1em"' : ""} font-weight="700" fill="#8E2F2A" font-size="17">${esc(l)}</tspan>`).join("");
    const txt = lignes.map((l, k) => `<tspan x="${x}" dy="1.2em">${esc(l)}</tspan>`).join("");
    const dy = haut ? -((lignes.length * 1.2) * 15.5 + (coupe.length - 1) * 18.7) : 0;
    s += `<text x="${x}" y="${y0 + dy}" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="15.5" fill="#1F2433">${date}${txt}</text>`;
  });
  return s + "</svg>";
}

function legendeCle(c, lang) {
  const L = lang === "fr" ? 2 : 1;
  const sw = /^(hatch|line|dots)/.test(c[0]) ? `<i class="sw ${c[0]}"></i>` : `<i class="sw" style="background:${c[0]}"></i>`;
  return `<li>${sw}<span>${esc(c[L])}</span></li>`;
}

function blocCarte(cc, svg, titre, lang, apres) {
  const F = lang === "fr";
  return `<section class="bloc carte large${cc.carre ? " carre" : ""}${cc.petit ? " petit" : ""}"><div class="tete-carte"><h2>${titre} — ${esc(cc.titre[F ? 1 : 0])}</h2><div class="svg">${svg}</div></div>
  <div class="carte-corps">
  <div class="leg"><ul class="cles">${cc.cles.map(k => legendeCle(k, lang)).join("")}</ul>
  <ol class="reperes">${cc.reperes.map(r => `<li>${esc(r[F ? 1 : 0])}</li>`).join("")}</ol>
  <p class="note">${esc(cc.note[F ? 1 : 0])}</p></div></div>${apres || ""}
</section>`;
}

function schema(sc, lang) {
  const F = lang === "fr";
  if (sc.type === "chaine") return `<div class="chaine">${sc.etapes.map((e, i) => `<div class="maillon"><b>${esc(F ? e[2] : e[0])}</b><span>${esc(F ? e[3] : e[1])}</span></div>${i < sc.etapes.length - 1 ? '<div class="fl">→</div>' : ""}`).join("")}</div>`;
  if (sc.type === "tableau") return `<table class="comp"><thead><tr><th></th>${sc.colonnes.map(c => `<th>${esc(c[F ? 1 : 0])}</th>`).join("")}</tr></thead><tbody>${sc.lignes.map(l => `<tr><th>${esc(l[0][F ? 1 : 0])}</th>${l.slice(1).map(c => `<td>${esc(c[F ? 1 : 0])}</td>`).join("")}</tr>`).join("")}</tbody></table>`;
  if (sc.type === "liste") return `<ol class="forces">${sc.items.map(it => `<li>${esc(it[F ? 1 : 0])}</li>`).join("")}</ol>`;
  return "";
}

function fiche(code, lang) {
  const d = lire(code), c = CONF[code], F = lang === "fr", t = T[lang], m = F && d.fr ? d.fr : d;
  const carte = fs.readFileSync(path.join(ICI, "cartes", `${code}-${lang}.svg`), "utf8");
  const vides = d.sections.filter(s => s.num !== "✓" && !(s.ideas || []).length);
  const secs = d.sections.filter(s => s.num !== "✓" && (s.ideas || []).length);
  const horsCours = ex => /outside the course|from outside|hors du cours|hors cours/i.test(ex || "");
  const idee = (it) => {
    const ti = F ? it.fr.title : it.title, tx = F ? it.fr.text : it.text, ex = F ? it.fr.ex : it.example;
    return `<div class="idee"><h4>${esc(ti)}</h4><p>${esc(tx)}</p>${ex ? `<div class="ex"><span class="exl">${t.ex}${horsCours(ex) ? ` · <em>${t.hors}</em>` : ""}</span> ${esc(ex)}</div>` : ""}</div>`;
  };
  const kf = m.keyFigures || d.keyFigures;
  const date = new Date().toLocaleDateString(F ? "fr-FR" : "en-GB", { day: "numeric", month: "long", year: "numeric" });
  return `<!doctype html><html lang="${lang}"><head><meta charset="utf-8"><title>${esc(code)} — ${esc(m.title || d.title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Inter:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
<style>${fs.readFileSync(path.join(ICI, "fiche.css"), "utf8")}</style></head><body>
<header class="tete">
  <div class="kicker">${t.kicker}</div>
  <div class="titre"><span class="code">${esc(code)}</span><h1>${esc(m.title || d.title)}</h1></div>
  <div class="theme">${esc(m.theme || d.theme)}</div>
  <p class="obj"><b>${t.objective}.</b> ${esc(m.objective || d.objective)}</p>
</header>
${vides.length ? `<div class="partiel">${t.partiel}${vides.map(s => esc(s.num + " " + (F && s.frTitle ? s.frTitle : s.title))).join(" · ")}.</div>` : ""}
<section class="bloc"><h2>${t.frise}</h2><div class="frise">${frise(c.frise, lang)}</div></section>
<section class="bloc duo">
  <div><h2>${t.enjeu}</h2><p class="enjeu">${esc(m.bigPicture || d.bigPicture)}</p></div>
  <div class="kik"><h3>${t.ki}</h3><ul>${d.keyIssues.map(k => `<li>${esc(k)}</li>`).join("")}</ul><h3>${t.kt}</h3><p>${d.keyTerms.map(esc).join(" · ")}</p></div>
</section>
<section class="bloc"><h2>${t.schema} — ${esc(c.schema.titre[F ? 1 : 0])}</h2>${schema(c.schema, lang)}</section>
${blocCarte(c.carte, carte, t.carte, lang, c.carte.serie ? `<h3 class="serie-t">${t.serie}</h3>
  <div class="serie${c.carte.monde ? " monde" : ""}" style="--n:${c.carte.serie.length}">${c.carte.serie.map((e, i) => `<figure><div class="svg">${fs.readFileSync(path.join(ICI, "cartes", `${code}-serie${i + 1}-${lang}.svg`), "utf8")}</div><figcaption><b>${esc(e[0][F ? 1 : 0])}</b> ${esc(e[F ? 2 : 1])}</figcaption></figure>`).join("")}</div>` : "")}
${c.zoom ? blocCarte(c.zoom, fs.readFileSync(path.join(ICI, "cartes", `${code}-france-${lang}.svg`), "utf8"), t.zoom, lang) : ""}
<section class="cours"><h2 class="h2c">${t.cours}</h2>
${secs.map(s => `<div class="sec"><div class="tete-sec"><h3><span>${esc(s.num)}</span> ${esc(F && s.frTitle ? s.frTitle : s.title)}</h3>${idee(s.ideas[0])}</div>${s.ideas.slice(1).map(idee).join("")}</div>`).join("")}
</section>
<section class="bloc annexe"><h2>${t.acteurs}</h2><dl class="kf">${kf.people.map(p => `<dt>${esc(p[0])}</dt><dd>${esc(p[1])}</dd>`).join("")}</dl>
<h2>${t.chiffres}</h2><dl class="kf num">${kf.numbers.map(p => `<dt>${esc(p[0])}</dt><dd>${esc(p[1])}</dd>`).join("")}</dl></section>
<section class="bloc annexe"><h2>${t.vocab}</h2>${(d.vocab || []).map(g => `<div class="vg"><h3>${esc(F && g.frGroup ? g.frGroup : g.group)}</h3><dl>${g.items.map(v => `<dt>${esc(v[0])}${F && v[1] && v[1] !== v[0] ? ` <span class="vfr">(${esc(v[1])})</span>` : ""}</dt><dd>${esc(F ? v[3] : v[2])}</dd>`).join("")}</dl></div>`).join("")}</section>
<footer class="fin">${t.genere} · ${t.pdate}${date}</footer>
</body></html>`;
}

(async () => {
  const codes = process.argv.slice(2).length ? process.argv.slice(2) : Object.keys(CONF);
  const out = path.join(RACINE, "dnl", "fiches");
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage();
  for (const code of codes) for (const lang of ["en", "fr"]) {
    const h = fiche(code, lang);
    if (process.env.HTML) fs.writeFileSync(path.join(process.env.HTML, `${code}-${lang}.html`), h);
    await p.setContent(h, { waitUntil: "networkidle" });
    await p.evaluate(() => document.fonts.ready);
    const pied = `<div style="width:100%;font-family:Arial,sans-serif;font-size:7.5px;color:#6B6350;padding:0 13mm;display:flex;justify-content:space-between"><span>${esc(code)} · ${lang === "fr" ? "Atlas de révision" : "Revision Atlas"}</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`;
    const f = path.join(out, `${code}-${lang}.pdf`);
    await p.pdf({ path: f, format: "A4", printBackground: true, displayHeaderFooter: true, headerTemplate: "<span></span>", footerTemplate: pied, margin: { top: "13mm", bottom: "15mm", left: "13mm", right: "13mm" } });
    console.log(path.relative(RACINE, f), Math.round(fs.statSync(f).size / 1024) + " Ko");
  }
  await b.close();
})();
