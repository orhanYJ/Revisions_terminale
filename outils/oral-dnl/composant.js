/* ==== ORAL — onglet « Oral » des chapitres (15/11/2026 ; notes à puces depuis le 16/11/2026) ====
   Liste officielle des Key Issues et Key Terms par thème (ORAL_SYLLABUS) et, pour les thèmes traités, des notes à puces
   par question et par notion (ORAL : sections {t, d, pts} — d = durée conseillée en secondes, total 270 = 4 min 30 —,
   questions du jury). On parle à partir des notes, on ne récite pas : 4 min 30 visées, 5 min au maximum.
   L'oral se passe en anglais ; le bouton de langue du site affiche la traduction française. */
const oralTheme = code => ORAL_SYLLABUS.find(t => t.chap.indexOf(code) >= 0);
/* identifiant du thème (h-t1, g-t1…) d'après sa place dans STRUCTURE ; null si rien n'est publié */
const oralThemeId = (subj, t) => { const m = /^Theme (\d+)/.exec(t.name); return m ? (subj === "hist" ? "h" : "g") + "-t" + m[1] : null; };
const oralPret = id => { const d = id && ORAL[id]; return !!(d && d.issues.length + d.terms.length); };
const oralOuvrir = id => window.dispatchEvent(new CustomEvent("open-oral", { detail: id }));
/* l'onglet Oral porte tout le thème : toutes ses key issues et tous ses key terms, dans chaque chapitre du thème */
const oralChap = code => {
  const th = oralTheme(code), d = th && ORAL[th.id];
  if (!d || !(d.issues.length + d.terms.length)) return null;
  return { th, issues: d.issues, terms: d.terms };
};
const ORAL_CIBLE = 270, ORAL_MAX = 300;
const oralDuree = L => (L.sections || []).reduce((n, s) => n + (s.d || 0), 0);
const oralPuces = L => (L.sections || []).reduce((n, s) => n + s.pts.length, 0);
const oralMots = l => l.reduce((n, b) => n + b.p.split(/\s+/).filter(Boolean).length, 0);
const oralMmss = t => Math.floor(t / 60) + ":" + String(t % 60).padStart(2, "0");
const oralMin = d => d < 60 ? d + " s" : Math.floor(d / 60) + " min" + (d % 60 ? " " + String(d % 60).padStart(2, "0") : "");
const OralChrono = ({ FR, t, on, basculer, remettre }) => {
  const fini = t >= ORAL_MAX;
  return React.createElement("div", { className: "or-chrono" + (t > ORAL_CIBLE ? " depasse" : "") + (fini ? " fini" : "") },
    React.createElement("div", { className: "or-chr-bar" },
      React.createElement("i", { style: { width: (t / ORAL_MAX * 100) + "%" } }),
      React.createElement("b", { className: "or-chr-cible", title: "4:30" })),
    React.createElement("span", { className: "or-chr-t" }, fini ? (FR ? "5:00 — temps écoulé" : "5:00 — time's up") : oralMmss(t) + " / 4:30"),
    React.createElement("button", { onClick: basculer }, on ? "⏸ Pause" : fini ? (FR ? "↺ Recommencer" : "↺ Start again") : t === 0 ? (FR ? "▶ S'entraîner (4 min 30)" : "▶ Practise (4 min 30)") : (FR ? "▶ Reprendre" : "▶ Resume")),
    t > 0 && !fini && React.createElement("button", { className: "ghost", onClick: remettre, "aria-label": FR ? "Remettre à zéro" : "Reset" }, "↺"));
};
const OralItem = ({ it, FR, ouvert, basculer }) => {
  const L = FR ? it.fr : it.en, total = oralDuree(L);
  const [jury, setJury] = React.useState(false), [disc, setDisc] = React.useState(false), [t, setT] = React.useState(0), [on, setOn] = React.useState(false);
  React.useEffect(() => {
    if (!on) return;
    const h = setInterval(() => setT(v => Math.min(ORAL_MAX, v + 1)), 1000);
    return () => clearInterval(h);
  }, [on]);
  React.useEffect(() => { if (t >= ORAL_MAX) setOn(false); }, [t]);
  React.useEffect(() => { if (!ouvert) setOn(false); }, [ouvert]);
  let cum = 0;
  const bornes = L.sections.map(s => { const d0 = cum; cum += s.d; return [d0, cum]; });
  const cour = (on || t > 0) ? Math.max(0, bornes.findIndex(b => t < b[1])) : -1;
  const actif = cour < 0 ? -1 : (t >= cum ? L.sections.length - 1 : cour);
  return React.createElement("div", { className: "or-item" + (ouvert ? " open" : ""), id: "oral-" + it.id },
    React.createElement("button", { className: "or-head", onClick: basculer, "aria-expanded": ouvert },
      React.createElement("span", { className: "or-kind " + it.kind }, it.kind === "issue" ? "Key Issue" : "Key Term"),
      React.createElement("span", { className: "or-q" }, FR ? it.q_fr : it.q),
      FR && React.createElement("span", { className: "or-qen" }, it.q),
      React.createElement("span", { className: "or-meta" }, "≈ " + oralMin(total) + " · " + oralPuces(L) + (FR ? " puces" : " bullet points"),
        (it.chapitres || []).slice().sort().map(c => React.createElement("i", { key: c, className: "or-ch" }, c))),
      React.createElement("span", { className: "or-chev", "aria-hidden": true }, ouvert ? "▲" : "▼")),
    ouvert && React.createElement("div", { className: "or-body" },
      React.createElement(OralChrono, { FR, t, on,
        basculer: () => { if (t >= ORAL_MAX) { setT(0); setOn(true); } else setOn(o => !o); },
        remettre: () => { setOn(false); setT(0); } }),
      React.createElement("p", { className: "or-conseil" }, FR
        ? "Ne lis pas : développe chaque puce avec tes mots, en 10 à 20 secondes. Le temps conseillé est donné pour chaque partie ; pendant l'entraînement, la partie où tu devrais en être s'allume."
        : "Don't read: develop each bullet point in your own words, in 10 to 20 seconds. A suggested time is given for each part; while you practise, the part you should be on lights up."),
      React.createElement("div", { className: "or-secs" }, L.sections.map((s, k) => React.createElement("div", { key: k, className: "or-sec" + (k === actif ? " on" : "") + (k === 0 && it.kind === "term" ? " definition" : "") },
        React.createElement("div", { className: "or-sec-h" },
          React.createElement("span", { className: "or-sec-t" }, s.t),
          React.createElement("span", { className: "or-sec-d" }, "≈ " + oralMin(s.d), React.createElement("small", null, oralMmss(bornes[k][0]) + " → " + oralMmss(bornes[k][1])))),
        React.createElement("ul", null, s.pts.map((p, i) => React.createElement("li", { key: i, className: /^(Judgement|Jugement|In short|En bref)\s*:/.test(p) ? "jug" : null }, glT(p))))))),
      L.discours && React.createElement("button", { className: "or-jury-btn or-disc-btn", onClick: () => setDisc(d => !d), "aria-expanded": disc },
        (disc ? "▲ " : "▼ ") + (FR ? "📝 Le discours rédigé (≈ " : "📝 The written speech (≈ ") + oralMin(Math.round(oralMots(it.en.discours || L.discours) / 140 * 60 / 10) * 10) + (FR ? " à voix haute)" : " out loud)")),
      disc && L.discours && React.createElement("div", { className: "or-disc" },
        React.createElement("p", { className: "or-disc-n" }, FR
          ? "Un exemple de ce que donnent les notes une fois développées à voix haute. À lire pour comprendre l'enchaînement, pas à apprendre par cœur."
          : "An example of the notes developed out loud. Read it to see how the ideas link up, not to learn it by heart."),
        L.discours.map((b, k) => React.createElement("div", { key: k, className: "or-disc-b" },
          React.createElement("div", { className: "or-disc-t" }, b.t),
          b.p.split("\n\n").map((x, i) => React.createElement("p", { key: i }, glT(x)))))),
      L.discours && React.createElement("a", { className: "or-jury-btn or-pdf", href: "fiches/oral/" + it.id + "-" + (FR ? "fr" : "en") + ".pdf", target: "_blank", rel: "noopener",
        title: FR ? "Fiche A4 recto-verso : les notes et les réponses courtes au jury, puis le discours rédigé" : "Double-sided A4 sheet: the notes and short jury answers, then the written speech" },
        FR ? "⎙ Fiche PDF recto-verso" : "⎙ Double-sided PDF sheet"),
      React.createElement("button", { className: "or-jury-btn", onClick: () => setJury(j => !j) }, (jury ? "▲ " : "▼ ") + (FR ? "Questions possibles du jury" : "Possible questions from the jury")),
      jury && React.createElement("div", { className: "or-jury" }, L.jury.map((j, i) => React.createElement("div", { key: i, className: "or-jq" },
        React.createElement("b", null, j[0]), React.createElement("p", null, j[1]))))));
};
function OralTab({ code, themeId, lang }) {
  const FR = lang === "fr";
  const th0 = themeId ? ORAL_SYLLABUS.find(t => t.id === themeId) : oralTheme(code);
  const data = th0 && oralPret(th0.id) ? { th: th0, issues: ORAL[th0.id].issues, terms: ORAL[th0.id].terms } : null, th = data && data.th;
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
      React.createElement("p", { className: "or-chap" }, FR ? "Toutes les key issues et tous les key terms du thème, d'après la liste officielle. Les pastilles indiquent les chapitres à mobiliser." : "All the key issues and key terms of the theme, from the official list. The badges show which chapters to draw on."),
      React.createElement("p", null, FR
        ? "À l'oral (coefficient 10) : 20 minutes de préparation, puis 5 minutes d'exposé sur une key issue tirée au sort, 5 minutes de questions, et 5 minutes sur un key term — le tirage croise l'histoire et la géographie. Chaque réponse ci-dessous est un jeu de notes à puces, à développer en anglais en 4 min 30 (5 minutes au maximum), avec un temps conseillé par partie."
        : "At the oral (coefficient 10): 20 minutes of preparation, then a 5-minute presentation on a key issue drawn at random, 5 minutes of questions, and 5 minutes on a key term — the draw crosses history and geography. Each answer below is a set of bullet-point notes, to develop in English in 4 min 30 (5 minutes at most), with a suggested time for each part."),
      React.createElement("button", { className: "or-tirer", onClick: tirer }, FR ? "🎲 Tirer un sujet au sort" : "🎲 Draw a topic at random"),
      tirage && React.createElement("div", { className: "or-tirage" },
        tirage.map((it, i) => React.createElement("div", { key: i },
          React.createElement("span", { className: "or-kind " + it.kind }, it.kind === "issue" ? "Key Issue" : "Key Term"),
          React.createElement("b", null, it.q),
          FR && React.createElement("em", null, it.q_fr))),
        React.createElement("p", null, FR ? "Prépare-les en 20 minutes sans regarder les réponses, puis retrouve-les dans la page Oral du thème concerné. Le tirage ne porte que sur les questions déjà rédigées." : "Prepare them in 20 minutes without looking at the answers, then find them on the Oral page of the theme concerned. The draw only uses the questions already written."))),
    [data.issues.length ? bloc("Key Issues", data.issues) : null, data.terms.length ? bloc("Key Terms", data.terms) : null].filter(Boolean).map((x, i) => React.createElement(React.Fragment, { key: i }, x)),
    React.createElement("details", { className: "or-syll" },
      React.createElement("summary", null, FR ? "La liste officielle complète (tous les thèmes)" : "The full official list (all themes)"),
      ["hist", "geo"].map(sub => React.createElement("div", { key: sub, className: "or-syll-sub" },
        React.createElement("h4", null, sub === "hist" ? (FR ? "Histoire" : "History") : (FR ? "Géographie" : "Geography")),
        ORAL_SYLLABUS.filter(t => t.subject === sub).map(t => React.createElement("div", { key: t.id, className: "or-syll-th" + (t.fait ? " fait" : "") },
          React.createElement("div", { className: "or-syll-t" }, FR ? t.theme[1] : t.theme[0], React.createElement("span", null, t.fait ? (FR ? "traité" : "taught") : (FR ? "à venir" : "to come"))),
          t.issues.length ? React.createElement("ul", null, t.issues.map((q, i) => React.createElement("li", { key: i }, q))) : React.createElement("p", { className: "or-none" }, FR ? "Pas de key issue dans la liste." : "No key issue in the list."),
          React.createElement("p", { className: "or-terms" }, React.createElement("b", null, FR ? "Key Terms : " : "Key Terms: "), t.terms.length ? t.terms.join(" · ") : (FR ? "aucun dans la liste" : "none in the list"))))))));
}
/* page Oral d'un thème (ouverte depuis l'accueil ou le menu : événement « open-oral ») */
function OralPage({ id, lang }) {
  const FR = lang === "fr", th = ORAL_SYLLABUS.find(t => t.id === id);
  if (!th) return null;
  return React.createElement("div", { className: "chap-root oral-page" },
    React.createElement("div", { className: "chap-hero" },
      React.createElement("div", { className: "hero-cartouche" },
        React.createElement("span", { className: "hero-icon " + th.subject }, React.createElement("span", { className: "or-mic", "aria-hidden": true }, "🎤")),
        React.createElement("div", null,
          React.createElement("div", { className: "train-kicker" }, (th.subject === "hist" ? (FR ? "Histoire" : "History") : (FR ? "Géographie" : "Geography")) + " · " + (FR ? "Préparer l'oral" : "Oral preparation")),
          React.createElement("h1", { className: "hero-title" }, "Oral")))),
    React.createElement(OralTab, { themeId: id, lang: lang }));
}
/* bouton « Oral » d'un thème (accueil, menu) */
const OralBouton = ({ id, FR, petit }) => oralPret(id) && React.createElement("button", {
  className: petit ? "or-btn-menu" : "or-btn-theme", title: FR ? "Préparer l'oral de ce thème : key issues et key terms" : "Prepare the oral for this theme: key issues and key terms",
  onClick: e => { e.stopPropagation(); oralOuvrir(id); } }, "🎤 ", petit ? "Oral" : (FR ? "Oral du thème" : "Theme oral"));
