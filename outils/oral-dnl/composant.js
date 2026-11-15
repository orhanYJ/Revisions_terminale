/* ==== ORAL — onglet « Oral » de chaque chapitre (15/11/2026) ====
   Liste officielle des Key Issues et Key Terms par thème (ORAL_SYLLABUS, feuille du professeur) et, pour les thèmes
   traités en classe, un exposé d'environ 5 minutes par question et par notion (ORAL : plan, texte à dire, questions du jury).
   L'oral se passe en anglais ; le bouton de langue du site affiche la traduction française. */
const oralTheme = code => ORAL_SYLLABUS.find(t => t.chap.indexOf(code) >= 0);
/* les questions et notions du chapitre, telles que la feuille les range (champs keyIssues / keyTerms du chapitre) */
const oralChap = code => {
  const th = oralTheme(code), ch = CHAPTERS[code], d = th && ORAL[th.id];
  if (!d || !ch) return null;
  const miens = (ch.keyIssues || []).concat(ch.keyTerms || []);
  const f = l => l.filter(it => miens.indexOf(it.q) >= 0);
  const r = { th, issues: f(d.issues), terms: f(d.terms) };
  return r.issues.length + r.terms.length ? r : null;
};
const oralMots = it => (it.en.blocs || []).reduce((n, b) => n + (b.p || "").split(/\s+/).filter(Boolean).length, 0);
const OralChrono = ({ FR }) => {
  const [t, setT] = React.useState(300), [on, setOn] = React.useState(false);
  React.useEffect(() => { if (!on) return; const h = setInterval(() => setT(v => { if (v <= 1) { setOn(false); return 0; } return v - 1; }), 1000); return () => clearInterval(h); }, [on]);
  const mm = Math.floor(t / 60), ss = String(t % 60).padStart(2, "0");
  return React.createElement("div", { className: "or-chrono" + (t === 0 ? " fini" : "") },
    React.createElement("div", { className: "or-chr-bar" }, React.createElement("i", { style: { width: (100 - t / 3) + "%" } })),
    React.createElement("span", { className: "or-chr-t" }, t === 0 ? (FR ? "Temps écoulé" : "Time's up") : mm + ":" + ss),
    React.createElement("button", { onClick: () => { if (t === 0) setT(300); setOn(o => !o); } }, on ? (FR ? "⏸ Pause" : "⏸ Pause") : (t === 300 ? (FR ? "▶ S'entraîner 5 min" : "▶ Practise 5 min") : (FR ? "▶ Reprendre" : "▶ Resume"))),
    t !== 300 && React.createElement("button", { className: "ghost", onClick: () => { setOn(false); setT(300); } }, FR ? "↺" : "↺"));
};
const OralItem = ({ it, FR, ouvert, basculer }) => {
  const L = FR ? it.fr : it.en, mots = oralMots(it), min = Math.max(1, Math.round(mots / 140 * 2) / 2);
  const [jury, setJury] = React.useState(false);
  return React.createElement("div", { className: "or-item" + (ouvert ? " open" : ""), id: "oral-" + it.id },
    React.createElement("button", { className: "or-head", onClick: basculer, "aria-expanded": ouvert },
      React.createElement("span", { className: "or-kind " + it.kind }, it.kind === "issue" ? "Key Issue" : "Key Term"),
      React.createElement("span", { className: "or-q" }, FR ? it.q_fr : it.q),
      FR && React.createElement("span", { className: "or-qen" }, it.q),
      React.createElement("span", { className: "or-meta" }, "≈ " + String(min).replace(".", FR ? "," : ".") + " min · " + mots + (FR ? " mots (anglais)" : " words")),
      React.createElement("span", { className: "or-chev", "aria-hidden": true }, ouvert ? "▲" : "▼")),
    ouvert && React.createElement("div", { className: "or-body" },
      React.createElement("div", { className: "or-plan" },
        React.createElement("div", { className: "or-lab" }, FR ? "Le plan à retenir (préparation)" : "The outline to remember (preparation)"),
        React.createElement("ol", null, L.plan.map((p, i) => React.createElement("li", { key: i }, p)))),
      React.createElement(OralChrono, { FR }),
      React.createElement("div", { className: "or-lab" }, FR ? (it.kind === "issue" ? "L'exposé, prêt à dire" : "La présentation, prête à dire") : (it.kind === "issue" ? "The presentation, ready to say" : "The presentation, ready to say")),
      L.blocs.map((b, i) => React.createElement("div", { key: i, className: "or-bloc " + b.k },
        (b.t || b.k === "intro" || b.k === "conclusion" || b.k === "definition") && React.createElement("div", { className: "or-bt" },
          b.t || ({ intro: FR ? "Introduction" : "Introduction", conclusion: FR ? "Conclusion" : "Conclusion", definition: FR ? "Définition" : "Definition" })[b.k]),
        React.createElement("p", null, glT(b.p)))),
      React.createElement("button", { className: "or-jury-btn", onClick: () => setJury(j => !j) }, (jury ? "▲ " : "▼ ") + (FR ? "Questions possibles du jury" : "Possible questions from the jury")),
      jury && React.createElement("div", { className: "or-jury" }, L.jury.map((j, i) => React.createElement("div", { key: i, className: "or-jq" },
        React.createElement("b", null, j[0]), React.createElement("p", null, j[1]))))));
};
function OralTab({ code, lang }) {
  const FR = lang === "fr", data = oralChap(code), th = data && data.th;
  const [ouvert, setOuvert] = React.useState(null), [tirage, setTirage] = React.useState(null);
  if (!th) return null;
  const tirer = () => {
    const faits = ORAL_SYLLABUS.filter(t => ORAL[t.id]);
    const iss = [].concat(...faits.map(t => ORAL[t.id].issues)), trm = [].concat(...faits.map(t => ORAL[t.id].terms));
    if (!iss.length || !trm.length) return;
    const a = iss[Math.floor(Math.random() * iss.length)], b = trm[Math.floor(Math.random() * trm.length)];
    setTirage([a, b]);
  };
  const bloc = (titre, liste, kind) => React.createElement("section", { className: "or-group" },
    React.createElement("h3", null, titre, React.createElement("span", null, liste.length)),
    liste.map(it => React.createElement(OralItem, { key: it.id, it, FR, ouvert: ouvert === it.id, basculer: () => setOuvert(o => o === it.id ? null : it.id) })));
  return React.createElement("div", { className: "oral-root" },
    React.createElement("div", { className: "or-intro" },
      React.createElement("div", { className: "or-kicker" }, FR ? "L'oral de DNL" : "The DNL oral"),
      React.createElement("h2", null, FR ? th.theme[1] : th.theme[0]),
      React.createElement("p", { className: "or-chap" }, FR ? "Dans cet onglet : les key issues et key terms que la feuille du professeur range sous ce chapitre. Les autres questions du thème sont dans l'onglet Oral des autres chapitres." : "In this tab: the key issues and key terms that the teacher's sheet lists under this chapter. The theme's other questions are in the Oral tab of the other chapters."),
      React.createElement("p", null, FR
        ? "À l'oral (coefficient 10) : 20 minutes de préparation, puis 5 minutes d'exposé sur une key issue tirée au sort, 5 minutes de questions, et 5 minutes sur un key term — le tirage croise l'histoire et la géographie. Chaque réponse ci-dessous est calibrée pour environ 5 minutes en anglais (650 à 750 mots, environ 140 mots par minute)."
        : "At the oral (coefficient 10): 20 minutes of preparation, then a 5-minute presentation on a key issue drawn at random, 5 minutes of questions, and 5 minutes on a key term — the draw crosses history and geography. Each answer below is designed for about 5 minutes in English (650 to 750 words, about 140 words a minute)."),
      React.createElement("button", { className: "or-tirer", onClick: tirer }, FR ? "🎲 Tirer un sujet au sort (histoire + géographie)" : "🎲 Draw a topic at random (history + geography)"),
      tirage && React.createElement("div", { className: "or-tirage" },
        tirage.map((it, i) => React.createElement("div", { key: i },
          React.createElement("span", { className: "or-kind " + it.kind }, it.kind === "issue" ? "Key Issue" : "Key Term"),
          React.createElement("b", null, it.q),
          FR && React.createElement("em", null, it.q_fr))),
        React.createElement("p", null, FR ? "Prépare-les en 20 minutes sans regarder les réponses, puis retrouve-les dans l'onglet Oral du chapitre concerné. Le tirage ne porte que sur les questions déjà rédigées." : "Prepare them in 20 minutes without looking at the answers, then find them in the Oral tab of the chapter concerned. The draw only uses the questions already written."))),
    [data.issues.length ? bloc("Key Issues", data.issues) : null, data.terms.length ? bloc("Key Terms", data.terms) : null].filter(Boolean).map((x, i) => React.createElement(React.Fragment, { key: i }, x)),
    React.createElement("details", { className: "or-syll" },
      React.createElement("summary", null, FR ? "La liste officielle complète (tous les thèmes)" : "The full official list (all themes)"),
      ["hist", "geo"].map(sub => React.createElement("div", { key: sub, className: "or-syll-sub" },
        React.createElement("h4", null, sub === "hist" ? (FR ? "Histoire" : "History") : (FR ? "Géographie" : "Geography")),
        ORAL_SYLLABUS.filter(t => t.subject === sub).map(t => React.createElement("div", { key: t.id, className: "or-syll-th" + (t.fait ? " fait" : "") },
          React.createElement("div", { className: "or-syll-t" }, FR ? t.theme[1] : t.theme[0], React.createElement("span", null, t.fait ? (FR ? "traité" : "taught") : (FR ? "à venir" : "to come"))),
          t.issues.length ? React.createElement("ul", null, t.issues.map((q, i) => React.createElement("li", { key: i }, q))) : React.createElement("p", { className: "or-none" }, FR ? "Pas de key issue sur la feuille." : "No key issue on the sheet."),
          React.createElement("p", { className: "or-terms" }, React.createElement("b", null, FR ? "Key Terms : " : "Key Terms: "), t.terms.length ? t.terms.join(" · ") : (FR ? "aucun sur la feuille" : "none on the sheet"))))))));
}
