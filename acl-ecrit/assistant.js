/* Demander à une IA — bouton rond en bas d'écran et petit panneau de saisie.
   Maintenu à part du contenu, comme la couche de mouvement : le même fichier est
   copié dans chaque site ; seul le bloc CONFIG change d'un site à l'autre.
   L'élève choisit l'IA (ChatGPT, Gemini, Le Chat de Mistral, Claude) ; la question,
   précédée d'une consigne de niveau Terminale, s'ouvre dans un nouvel onglet.
   ChatGPT s'ouvre en discussion temporaire (temporary-chat=true). ChatGPT, Claude et
   Le Chat reçoivent la question dans l'adresse (?q=) ; Gemini ne sait pas la recevoir :
   elle est copiée dans le presse-papiers, à coller. Pour toutes, la question est aussi
   copiée, au cas où le pré-remplissage échouerait.
   Le site ne conserve rien : ni stockage dans le navigateur, ni envoi ailleurs ;
   le champ est vidé dès que l'IA est ouverte.
   Mouvement : tout ce qui bouge est rangé sous html.mo (classe posée par la couche de
   mouvement du site) et coupé si l'appareil demande moins d'animations. */
(function () {
  "use strict";

  /* ---------- CONFIG (propre à chaque site) ---------- */
  var NOM = "ACL écrit";
  var LANGUE = "fr";   /* langue du panneau : "fr" ou "en" */
  var COTE = "gauche";   /* bouton en bas à "gauche" ou à "droite" */
  var CONSIGNE = "I am a French Terminale student in the British section of the Baccalauréat français international, preparing the English literature exam (ACL). My course covers Brian Friel's Dancing at Lughnasa, Monica Ali's Brick Lane and Shakespeare's Twelfth Night, and the methods of the commentary and the essay. Answer precisely: exact references to the text (act, scene, chapter or page when possible), literary terms used accurately, context. Never invent a quotation, and say clearly when you paraphrase. If you are unsure of a point, say so clearly. Answer in the language of my question.";
  var COULEURS = {
    fond: "var(--page, #FBF9F3)", fond2: "var(--page-2, #F2EEE3)",
    encre: "var(--ink, #1E2330)", encre2: "var(--ink-2, #5B6272)", ligne: "var(--rule, #DCD5C4)",
    accent: "var(--cloth, #16233F)", surAccent: "var(--gilt-2, #E6CB8B)"
  };
  var EVITER = "";   /* élément fixé en bas d'écran à ne pas recouvrir */
  /* ---------- fin CONFIG ---------- */

  /* IA proposées : url + question encodée (q:true), ou page seule et question à coller (q:false). */
  var IAS = [
    { id: "chatgpt", nom: "ChatGPT", url: "https://chatgpt.com/?temporary-chat=true&q=", q: true,
      fr: "S'ouvre en discussion temporaire : rien n'est gardé dans l'historique de ChatGPT.",
      en: "Opens as a temporary chat: nothing is saved in ChatGPT's history." },
    { id: "gemini", nom: "Gemini", url: "https://gemini.google.com/app", q: false,
      fr: "Gemini ne reçoit pas la question tout seul : elle est copiée, il suffit de la coller (appui long dans la zone de saisie, puis « Coller »). Pour ne rien garder, ouvre une discussion temporaire.",
      en: "Gemini cannot receive the question by itself: it is copied, just paste it (long-press in the input box, then Paste). To keep nothing, start a temporary chat." },
    { id: "mistral", nom: "Le Chat", url: "https://chat.mistral.ai/chat?q=", q: true,
      fr: "Le Chat de Mistral, l'IA française. La question est pré-remplie ; si tu es connecté, la discussion reste dans ton historique.",
      en: "Le Chat by Mistral, the French AI. The question is prefilled; if you are signed in, the chat stays in your history." },
    { id: "claude", nom: "Claude", url: "https://claude.ai/new?q=", q: true,
      fr: "La question est pré-remplie. Pour ne rien garder, active la discussion incognito (icône fantôme). Claude est réservé aux 18 ans et plus.",
      en: "The question is prefilled. To keep nothing, switch on incognito chat (ghost icon). Claude is for users aged 18 and over." }
  ];
  var ia = IAS[0];   /* choix gardé en mémoire le temps de la page seulement */
  var EN = LANGUE === "en";
  var COTE_CSS = COTE === "droite" ? "right" : "left";
  var TEXTES = EN ? {
    titre: "Ask an AI · " + NOM,
    sous: "Choose the AI, write your question",
    choix: "Which AI?",
    note: "The AI can be wrong: check dates and figures in your course. Do not write anything personal.",
    champ: "Your question (in English or in French)…",
    bouton: "Open in ",
    fermer: "Close",
    vide: "Write your question first.",
    horsligne: "The AI needs an internet connection.",
    copie: "Question copied: if it does not appear, paste it."
  } : {
    titre: "Demander à une IA · " + NOM,
    sous: "Choisis l'IA, écris ta question",
    choix: "Quelle IA ?",
    note: "L'IA peut se tromper : vérifie avec ton cours. N'écris rien de personnel.",
    champ: "Ta question de cours…",
    bouton: "Ouvrir dans ",
    fermer: "Fermer",
    vide: "Écris d'abord ta question.",
    horsligne: "L'IA a besoin d'internet.",
    copie: "Question copiée : si elle n'apparaît pas, colle-la."
  };

  var bouton, panneau, voile, champ, info, envoyer, libelle, noteIA, choix = [], sortie = null;

  // Le mouvement n'est joué que si le site l'a autorisé (html.mo) et que l'appareil ne demande pas moins d'animations.
  function mouvement() {
    var reduit = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    return document.documentElement.classList.contains("mo") && !reduit;
  }

  /* ---------- styles ---------- */
  var c = COULEURS;
  var css =
    ".asr-btn,.asr-pan,.asr-pan *{box-sizing:border-box}" +
    ".asr-btn{position:fixed;" + COTE_CSS + ":14px;bottom:calc(14px + env(safe-area-inset-bottom,0px));z-index:70;width:52px;height:52px;border-radius:50%;border:0;" +
    "background:" + c.accent + ";color:" + c.surAccent + ";display:flex;align-items:center;justify-content:center;cursor:pointer;" +
    "box-shadow:0 2px 6px rgba(0,0,0,.18),0 8px 22px rgba(0,0,0,.14);-webkit-tap-highlight-color:transparent}" +
    ".asr-btn:focus-visible{outline:3px solid " + c.encre + ";outline-offset:3px}" +
    ".asr-btn svg{position:relative;width:26px;height:26px}" +
    ".asr-btn::before{content:'';position:absolute;inset:0;border-radius:50%;border:2px solid " + c.accent + ";opacity:0;pointer-events:none}" +
    ".asr-voile{position:fixed;inset:0;z-index:79;display:none;background:rgba(0,0,0,.28);-webkit-backdrop-filter:blur(2px);backdrop-filter:blur(2px)}" +
    ".asr-voile.on{display:block}" +
    ".asr-pan{position:fixed;z-index:80;display:none;flex-direction:column;gap:12px;margin:0;background:" + c.fond + ";color:" + c.encre + ";" +
    "border:1px solid " + c.ligne + ";box-shadow:0 12px 40px rgba(0,0,0,.22);padding:14px 14px calc(14px + env(safe-area-inset-bottom,0px));" +
    "left:0;right:0;bottom:0;border-radius:16px 16px 0 0;max-height:90vh;overflow-y:auto}" +
    "@media (min-width:700px){.asr-pan{left:auto;right:auto;" + COTE_CSS + ":18px;bottom:18px;width:420px;border-radius:14px;padding-bottom:14px}}" +
    ".asr-pan.on{display:flex}" +
    ".asr-tete{display:flex;align-items:flex-start;gap:10px}" +
    ".asr-titre{flex:1;min-width:0;font-weight:700;font-size:16px;line-height:1.25}" +
    ".asr-titre small{display:block;font-weight:400;font-size:12px;color:" + c.encre2 + ";margin-top:2px}" +
    ".asr-ic{flex:none;margin:0;border:1px solid " + c.ligne + ";background:transparent;color:" + c.encre + ";border-radius:8px;height:36px;padding:0 10px;font:inherit;font-size:13px;cursor:pointer}" +
    ".asr-note{margin:0;font-size:13px;line-height:1.45;color:" + c.encre2 + "}" +
    ".asr-champ{display:block;width:100%;min-height:96px;max-height:40vh;resize:vertical;margin:0;padding:11px 12px;border:1px solid " + c.ligne + ";border-radius:10px;" +
    "background:" + c.fond2 + ";color:" + c.encre + ";font:inherit;font-size:16px;line-height:1.4}" +
    ".asr-champ:focus{outline:2px solid " + c.accent + ";outline-offset:0;border-color:transparent}" +
    ".asr-env{position:relative;overflow:hidden;display:flex;align-items:center;justify-content:center;gap:8px;width:100%;height:46px;margin:0;border:0;border-radius:10px;background:" + c.accent + ";" +
    "color:" + c.surAccent + ";font:inherit;font-weight:700;font-size:15px;cursor:pointer}" +
    ".asr-env svg{width:18px;height:18px}" +
    ".asr-ic:focus-visible,.asr-env:focus-visible{outline:2px solid " + c.encre + ";outline-offset:2px}" +
    ".asr-info{margin:0;font-size:13px;color:" + c.encre2 + "}" +
    ".asr-ias{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:6px;margin:0;padding:0;border:0}" +
    ".asr-ias legend{padding:0;margin:0 0 6px;font-size:13px;font-weight:700;color:" + c.encre2 + "}" +
    ".asr-ia{margin:0;min-width:0;height:38px;padding:0 4px;border:1px solid " + c.ligne + ";border-radius:9px;background:" + c.fond2 + ";color:" + c.encre + ";" +
    "font:inherit;font-size:14px;font-weight:600;cursor:pointer;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;-webkit-tap-highlight-color:transparent}" +
    ".asr-ia[aria-pressed=true]{background:" + c.accent + ";border-color:" + c.accent + ";color:" + c.surAccent + "}" +
    ".asr-ia:focus-visible{outline:2px solid " + c.encre + ";outline-offset:2px}" +
    ".asr-info:empty{display:none}" +
    "@media print{.asr-btn,.asr-pan,.asr-voile{display:none!important}}" +
    /* ---------- mouvement (html.mo, sans réduction demandée) ---------- */
    "@media (prefers-reduced-motion:no-preference){" +
      // bouton : arrivée en rebond, halo qui respire, point d'interrogation qui hoche
      "html.mo .asr-btn{animation:asr-pop .7s cubic-bezier(.34,1.56,.64,1);transition:transform .35s cubic-bezier(.34,1.56,.64,1),box-shadow .3s}" +
      "html.mo .asr-btn:hover{transform:scale(1.08) rotate(-4deg);box-shadow:0 4px 10px rgba(0,0,0,.2),0 12px 30px rgba(0,0,0,.18)}" +
      "html.mo .asr-btn:active{transform:scale(.92)}" +
      "html.mo .asr-btn::before{animation:asr-halo 3.6s cubic-bezier(.2,.6,.3,1) 1.4s infinite}" +
      "html.mo .asr-btn .asr-q{transform-origin:12px 13px;animation:asr-hoche 7s ease-in-out 2.5s infinite}" +
      // voile et panneau : fondu du voile, montée avec léger rebond, éléments en cascade
      "html.mo .asr-voile.on{animation:asr-fondu .35s ease both}" +
      "html.mo .asr-pan.on{animation:asr-monte .55s cubic-bezier(.2,.9,.25,1.08) both}" +
      "@media (min-width:700px){html.mo .asr-pan.on{transform-origin:" + (COTE === "droite" ? "calc(100% - 24px)" : "24px") + " 100%;animation-name:asr-gonfle}}" +
      "html.mo .asr-pan.on>*{animation:asr-cascade .5s cubic-bezier(.2,.8,.2,1) both}" +
      "html.mo .asr-pan.on>:nth-child(2){animation-delay:.05s}html.mo .asr-pan.on>:nth-child(3){animation-delay:.1s}" +
      "html.mo .asr-pan.on>:nth-child(4){animation-delay:.15s}html.mo .asr-pan.on>:nth-child(5){animation-delay:.2s}" +
      "html.mo .asr-pan.on>:nth-child(n+6){animation-delay:.25s}" +
      "html.mo .asr-pan.sort{animation:asr-descend .28s cubic-bezier(.4,0,1,1) both}" +
      "@media (min-width:700px){html.mo .asr-pan.sort{animation-name:asr-degonfle}}" +
      "html.mo .asr-voile.sort{animation:asr-fondu .28s ease reverse both}" +
      // champ : halo à la saisie, secousse s'il est vide
      "html.mo .asr-champ{transition:box-shadow .3s}" +
      "html.mo .asr-champ:focus{box-shadow:0 0 0 5px rgba(0,0,0,.06)}" +
      "html.mo .asr-champ.asr-secoue{animation:asr-secoue .45s cubic-bezier(.36,.07,.19,.97) both}" +
      // bouton d'envoi : reflet qui balaie quand une question est prête, envol de la flèche au départ
      "html.mo .asr-ia{transition:background-color .2s,color .2s,border-color .2s,transform .25s cubic-bezier(.34,1.56,.64,1)}" +
      "html.mo .asr-ia:active{transform:scale(.94)}" +
      "html.mo .asr-env{transition:transform .25s cubic-bezier(.34,1.56,.64,1)}" +
      "html.mo .asr-env:active{transform:scale(.97)}" +
      "html.mo .asr-env::after{content:'';position:absolute;top:0;bottom:0;left:0;width:45%;pointer-events:none;" +
        "background:linear-gradient(100deg,transparent,rgba(255,255,255,.32),transparent);transform:translateX(-130%);opacity:0}" +
      "html.mo .asr-env.pret::after{opacity:1;animation:asr-reflet 2.8s ease-in-out .3s infinite}" +
      "html.mo .asr-env.decolle svg{animation:asr-envol .45s cubic-bezier(.5,0,.75,0) both}" +
      "html.mo .asr-env.decolle{animation:asr-impulsion .45s ease-out both}" +
    "}" +
    "@keyframes asr-pop{0%{opacity:0;transform:scale(.3) rotate(-30deg)}100%{opacity:1;transform:none}}" +
    "@keyframes asr-halo{0%{opacity:.55;transform:scale(1)}70%,100%{opacity:0;transform:scale(1.55)}}" +
    "@keyframes asr-hoche{0%,86%,100%{transform:none}89%{transform:rotate(-14deg)}92%{transform:rotate(11deg)}95%{transform:rotate(-6deg)}}" +
    "@keyframes asr-fondu{from{opacity:0}to{opacity:1}}" +
    "@keyframes asr-monte{from{transform:translateY(105%)}to{transform:none}}" +
    "@keyframes asr-descend{from{transform:none;opacity:1}to{transform:translateY(105%);opacity:.6}}" +
    "@keyframes asr-gonfle{from{opacity:0;transform:translateY(18px) scale(.86)}to{opacity:1;transform:none}}" +
    "@keyframes asr-degonfle{from{opacity:1;transform:none}to{opacity:0;transform:translateY(14px) scale(.9)}}" +
    "@keyframes asr-cascade{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}" +
    "@keyframes asr-secoue{10%,90%{transform:translateX(-2px)}20%,80%{transform:translateX(4px)}30%,50%,70%{transform:translateX(-7px)}40%,60%{transform:translateX(7px)}}" +
    "@keyframes asr-reflet{0%{transform:translateX(-130%)}55%,100%{transform:translateX(260%)}}" +
    "@keyframes asr-envol{0%{transform:none}30%{transform:translate(-3px,3px)}100%{transform:translate(26px,-26px) scale(.6);opacity:0}}" +
    "@keyframes asr-impulsion{0%{box-shadow:0 0 0 0 rgba(0,0,0,.25)}100%{box-shadow:0 0 0 14px rgba(0,0,0,0)}}";

  function el(tag, cls, txt) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (txt) e.textContent = txt;
    return e;
  }

  function construire() {
    var st = document.createElement("style");
    st.textContent = css;
    document.head.appendChild(st);

    bouton = el("button", "asr-btn");
    bouton.type = "button";
    bouton.setAttribute("aria-label", TEXTES.titre);
    bouton.setAttribute("aria-haspopup", "dialog");
    bouton.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
      '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20.5l1.4-4.9A8 8 0 1 1 21 12z"/>' +
      '<g class="asr-q"><path d="M10.1 9.6a2 2 0 1 1 2.9 1.8c-.6.3-1 .8-1 1.4v.4"/><circle cx="12" cy="16" r=".6" fill="currentColor"/></g></svg>';
    bouton.addEventListener("click", ouvrir);

    voile = el("div", "asr-voile");
    voile.addEventListener("click", fermerPanneau);

    panneau = el("form", "asr-pan");
    panneau.setAttribute("role", "dialog");
    panneau.setAttribute("aria-label", TEXTES.titre);

    var tete = el("div", "asr-tete");
    var titre = el("div", "asr-titre", TEXTES.titre);
    titre.appendChild(el("small", "", TEXTES.sous));
    var fermer = el("button", "asr-ic", TEXTES.fermer);
    fermer.type = "button";
    fermer.addEventListener("click", fermerPanneau);
    tete.appendChild(titre);
    tete.appendChild(fermer);

    champ = el("textarea", "asr-champ");
    champ.maxLength = 1400;
    champ.placeholder = TEXTES.champ;
    champ.setAttribute("aria-label", TEXTES.champ);

    envoyer = el("button", "asr-env");
    envoyer.type = "submit";
    envoyer.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
      '<path d="M14 4h6v6"/><path d="M20 4l-9 9"/><path d="M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/></svg>';
    libelle = document.createTextNode("");
    envoyer.appendChild(libelle);

    var groupe = el("fieldset", "asr-ias");
    groupe.appendChild(el("legend", "", TEXTES.choix));
    IAS.forEach(function (x) {
      var b = el("button", "asr-ia", x.nom);
      b.type = "button";
      b.addEventListener("click", function () { choisir(x); });
      choix.push(b);
      groupe.appendChild(b);
    });
    noteIA = el("p", "asr-note");

    info = el("p", "asr-info");
    info.setAttribute("aria-live", "polite");

    panneau.appendChild(tete);
    panneau.appendChild(groupe);
    panneau.appendChild(noteIA);
    panneau.appendChild(champ);
    panneau.appendChild(envoyer);
    panneau.appendChild(info);
    panneau.appendChild(el("p", "asr-note", TEXTES.note));
    panneau.addEventListener("submit", function (e) { e.preventDefault(); demander(); });
    panneau.addEventListener("keydown", function (e) { if (e.key === "Escape") fermerPanneau(); });
    champ.addEventListener("input", function () { info.textContent = ""; envoyer.classList.toggle("pret", !!champ.value.trim()); });
    champ.addEventListener("animationend", function () { champ.classList.remove("asr-secoue"); });
    champ.addEventListener("keydown", function (e) {
      var tactile = window.matchMedia && window.matchMedia("(pointer:coarse)").matches;
      if (e.key === "Enter" && !e.shiftKey && !tactile) { e.preventDefault(); demander(); }
    });

    choisir(ia);
    document.body.appendChild(bouton);
    document.body.appendChild(voile);
    document.body.appendChild(panneau);
    placer();
    window.addEventListener("resize", function () { placer(); caler(); });
    if (window.visualViewport) {
      window.visualViewport.addEventListener("resize", caler);
      window.visualViewport.addEventListener("scroll", caler);
    }
    setInterval(placer, 1500);
  }

  // Remonte le bouton au-dessus d'une barre fixée en bas (barre de navigation SVT sur téléphone).
  function placer() {
    var bas = 14, gene = EVITER && document.querySelector(EVITER);
    if (gene) {
      var r = gene.getBoundingClientRect(), s = getComputedStyle(gene);
      if (s.display !== "none" && s.visibility !== "hidden" && r.height > 0 && r.bottom >= window.innerHeight - 40) {
        bas = Math.round(window.innerHeight - r.top) + 10;
      }
    }
    bouton.style.bottom = bas === 14 ? "" : bas + "px";
  }

  // Sur téléphone, garde le panneau dans la zone visible, au-dessus du clavier.
  function caler() {
    var vv = window.visualViewport;
    if (!vv || !panneau.classList.contains("on") || window.innerWidth >= 700 && vv.width >= 700) {
      panneau.style.left = panneau.style.width = panneau.style.bottom = panneau.style.maxHeight = "";
      return;
    }
    panneau.style.left = vv.offsetLeft + "px";
    panneau.style.width = vv.width + "px";
    panneau.style.bottom = Math.max(0, window.innerHeight - vv.offsetTop - vv.height) + "px";
    panneau.style.maxHeight = Math.round(vv.height * 0.9) + "px";
  }

  function choisir(x) {
    ia = x;
    choix.forEach(function (b, i) { b.setAttribute("aria-pressed", IAS[i] === x ? "true" : "false"); });
    noteIA.textContent = EN ? x.en : x.fr;
    libelle.nodeValue = TEXTES.bouton + x.nom;
    if (info) info.textContent = "";
  }

  // Copie la question (Gemini ne la reçoit pas par l'adresse ; pour les autres, secours si le pré-remplissage échoue).
  function copier(texte) {
    try {
      if (navigator.clipboard && window.isSecureContext) { navigator.clipboard.writeText(texte).catch(function () {}); return; }
    } catch (e) { /* on passe au secours */ }
    try {
      var t = document.createElement("textarea");
      t.value = texte; t.setAttribute("readonly", ""); t.style.position = "fixed"; t.style.opacity = "0";
      document.body.appendChild(t); t.select(); document.execCommand("copy"); document.body.removeChild(t);
    } catch (e) { /* rien */ }
  }

  function ouvrir() {
    if (sortie) { clearTimeout(sortie); sortie = null; }
    info.textContent = "";
    envoyer.classList.remove("decolle");
    envoyer.classList.toggle("pret", !!champ.value.trim());
    panneau.classList.remove("sort");
    voile.classList.remove("sort");
    panneau.classList.add("on");
    voile.classList.add("on");
    bouton.style.visibility = "hidden";
    caler();
    setTimeout(function () { champ.focus(); }, 30);
  }

  function fermerPanneau() {
    if (!panneau.classList.contains("on") || sortie) return;
    var fin = function () {
      sortie = null;
      panneau.classList.remove("on", "sort");
      voile.classList.remove("on", "sort");
      bouton.style.visibility = "";
      bouton.focus();
    };
    if (mouvement()) {
      panneau.classList.add("sort");
      voile.classList.add("sort");
      sortie = setTimeout(fin, 280);
    } else {
      fin();
    }
  }

  function demander() {
    var q = champ.value.trim();
    if (!q) {
      info.textContent = TEXTES.vide;
      champ.classList.remove("asr-secoue"); void champ.offsetWidth; champ.classList.add("asr-secoue");
      champ.focus();
      return;
    }
    if (navigator.onLine === false) { info.textContent = TEXTES.horsligne; return; }
    var invite = CONSIGNE + "\n\n" + (EN ? "My question: " : "Ma question : ") + q;
    copier(invite);
    var adresse = ia.q ? ia.url + encodeURIComponent(invite) : ia.url;
    var onglet = window.open(adresse, "_blank");
    if (onglet) {
      try { onglet.opener = null; } catch (e) { /* rien */ }
    } else {
      // ouverture d'onglet bloquée (certaines applis installées) : on y va directement
      window.location.href = adresse;
    }
    // rien n'est gardé côté site : le champ est vidé et le panneau refermé (après l'envol de la flèche)
    champ.value = "";
    envoyer.classList.remove("pret");
    if (mouvement()) {
      envoyer.classList.add("decolle");
      setTimeout(fermerPanneau, 380);
    } else {
      fermerPanneau();
    }
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", construire);
  else construire();
})();
