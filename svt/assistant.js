/* Demander à une IA — bouton rond en bas à gauche et petit panneau de saisie.
   Maintenu à part du contenu, comme la couche de mouvement : le même fichier est
   copié dans svt/, pc/ et dnl/ ; seul le bloc CONFIG change d'un site à l'autre.
   La question, précédée d'une consigne de niveau Terminale, s'ouvre au choix dans :
   - ChatGPT, en discussion temporaire (temporary-chat=true), hors historique ;
   - Perplexity, qui cite ses sources ; sans compte, rien n'est rattaché à un
     historique (avec un compte : mode Incognito).
   Le site ne conserve rien : ni stockage dans le navigateur, ni envoi ailleurs ;
   le champ est vidé dès que l'IA est ouverte. */
(function () {
  "use strict";

  /* ---------- CONFIG (propre à chaque site) ---------- */
  var MATIERE = "svt";
  var NOM = "SVT";
  var CONSIGNE = "Je suis élève de Terminale en France, en spécialité SVT (sciences de la vie et de la Terre). " +
    "Réponds à ma question au niveau du programme de Terminale, de façon précise et concise : vocabulaire exact, " +
    "mécanismes, dates, chiffres, et calculs détaillés avec les unités. Si tu n'es pas sûr d'un point, dis-le clairement.";
  var COULEURS = {
    fond: "var(--panel, #FFFDF8)", fond2: "var(--paper, #F7F4EC)",
    encre: "var(--ink, #17281E)", encre2: "var(--ink-2, #5E7263)", ligne: "var(--line, #E2DFD1)",
    accent: "var(--leaf, #2F7D52)", surAccent: "var(--panel, #FFFDF8)"
  };
  var EVITER = "nav.bottom";   /* élément fixé en bas d'écran à ne pas recouvrir */
  var DEFAUT = "chatgpt";   /* IA proposée en premier : "chatgpt" ou "perplexity" */
  /* ---------- fin CONFIG ---------- */

  var DNL = MATIERE === "dnl";
  var IAS = {
    chatgpt: {
      nom: "ChatGPT",
      adresse: "https://chatgpt.com/?temporary-chat=true&q=",
      note: DNL ? "Opens as a temporary chat: not saved in ChatGPT's history."
                : "S'ouvre en discussion temporaire : rien n'est gardé dans l'historique de ChatGPT."
    },
    perplexity: {
      nom: "Perplexity",
      adresse: "https://www.perplexity.ai/search?q=",
      note: DNL ? "Cites its sources, so you can check each fact. Use it without signing in (or in Incognito mode) so nothing is kept."
                : "Cite ses sources : tu peux vérifier chaque fait. Utilise-le sans te connecter (ou en mode Incognito) pour que rien ne soit gardé."
    }
  };
  var TEXTES = DNL ? {
    titre: "Ask an AI · " + NOM,
    sous: "ChatGPT or Perplexity, nothing kept on this site",
    choix: "AI",
    note: "The AI can be wrong: check dates and figures in your course. Do not write anything personal.",
    champ: "Your question (in English or in French)…",
    bouton: "Open in ",
    fermer: "Close",
    vide: "Write your question first.",
    horsligne: "The AI needs an internet connection."
  } : {
    titre: "Demander à une IA · " + NOM,
    sous: "ChatGPT ou Perplexity, rien n'est gardé sur le site",
    choix: "IA",
    note: "L'IA peut se tromper : vérifie avec ton cours. N'écris rien de personnel.",
    champ: "Ta question de cours…",
    bouton: "Ouvrir dans ",
    fermer: "Fermer",
    vide: "Écris d'abord ta question.",
    horsligne: "L'IA a besoin d'internet."
  };

  var bouton, panneau, champ, info, envoyer, noteIa, choisie = IAS[DEFAUT] ? DEFAUT : "chatgpt", choixBoutons = {};

  /* ---------- styles ---------- */
  var c = COULEURS;
  var css =
    ".asr-btn,.asr-pan,.asr-pan *{box-sizing:border-box}" +
    ".asr-btn{position:fixed;left:14px;bottom:calc(14px + env(safe-area-inset-bottom,0px));z-index:70;width:52px;height:52px;border-radius:50%;border:0;" +
    "background:" + c.accent + ";color:" + c.surAccent + ";display:flex;align-items:center;justify-content:center;cursor:pointer;" +
    "box-shadow:0 2px 6px rgba(0,0,0,.18),0 8px 22px rgba(0,0,0,.14);-webkit-tap-highlight-color:transparent}" +
    ".asr-btn:focus-visible{outline:3px solid " + c.encre + ";outline-offset:3px}" +
    ".asr-btn svg{width:26px;height:26px}" +
    ".asr-pan{position:fixed;z-index:80;display:none;flex-direction:column;gap:12px;margin:0;background:" + c.fond + ";color:" + c.encre + ";" +
    "border:1px solid " + c.ligne + ";box-shadow:0 12px 40px rgba(0,0,0,.22);padding:14px 14px calc(14px + env(safe-area-inset-bottom,0px));" +
    "left:0;right:0;bottom:0;border-radius:16px 16px 0 0;max-height:90vh;overflow-y:auto}" +
    "@media (min-width:700px){.asr-pan{left:18px;right:auto;bottom:18px;width:420px;border-radius:14px;padding-bottom:14px}}" +
    ".asr-pan.on{display:flex}" +
    ".asr-tete{display:flex;align-items:flex-start;gap:10px}" +
    ".asr-titre{flex:1;min-width:0;font-weight:700;font-size:16px;line-height:1.25}" +
    ".asr-titre small{display:block;font-weight:400;font-size:12px;color:" + c.encre2 + ";margin-top:2px}" +
    ".asr-ic{flex:none;margin:0;border:1px solid " + c.ligne + ";background:transparent;color:" + c.encre + ";border-radius:8px;height:36px;padding:0 10px;font:inherit;font-size:13px;cursor:pointer}" +
    ".asr-note{margin:0;font-size:13px;line-height:1.45;color:" + c.encre2 + "}" +
    ".asr-choix{display:flex;gap:6px;margin:0;padding:4px;border:1px solid " + c.ligne + ";border-radius:12px;background:" + c.fond2 + "}" +
    ".asr-choix button{flex:1;margin:0;height:40px;border:0;border-radius:9px;background:transparent;color:" + c.encre + ";font:inherit;font-size:14px;font-weight:600;cursor:pointer}" +
    ".asr-choix button[aria-checked=true]{background:" + c.accent + ";color:" + c.surAccent + "}" +
    ".asr-choix button:focus-visible{outline:2px solid " + c.encre + ";outline-offset:1px}" +
    ".asr-champ{display:block;width:100%;min-height:96px;max-height:40vh;resize:vertical;margin:0;padding:11px 12px;border:1px solid " + c.ligne + ";border-radius:10px;" +
    "background:" + c.fond2 + ";color:" + c.encre + ";font:inherit;font-size:16px;line-height:1.4}" +
    ".asr-champ:focus{outline:2px solid " + c.accent + ";outline-offset:0;border-color:transparent}" +
    ".asr-env{display:flex;align-items:center;justify-content:center;gap:8px;width:100%;height:46px;margin:0;border:0;border-radius:10px;background:" + c.accent + ";" +
    "color:" + c.surAccent + ";font:inherit;font-weight:700;font-size:15px;cursor:pointer}" +
    ".asr-env svg{width:18px;height:18px}" +
    ".asr-ic:focus-visible,.asr-env:focus-visible{outline:2px solid " + c.encre + ";outline-offset:2px}" +
    ".asr-info{margin:0;font-size:13px;color:" + c.encre2 + "}" +
    ".asr-info:empty{display:none}" +
    "@media print{.asr-btn,.asr-pan{display:none!important}}";

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
      '<path d="M10.1 9.6a2 2 0 1 1 2.9 1.8c-.6.3-1 .8-1 1.4v.4"/><circle cx="12" cy="16" r=".6" fill="currentColor"/></svg>';
    bouton.addEventListener("click", ouvrir);

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

    var choix = el("div", "asr-choix");
    choix.setAttribute("role", "radiogroup");
    choix.setAttribute("aria-label", TEXTES.choix);
    Object.keys(IAS).forEach(function (cle) {
      var b = el("button", "", IAS[cle].nom);
      b.type = "button";
      b.setAttribute("role", "radio");
      b.addEventListener("click", function () { choisir(cle); });
      choixBoutons[cle] = b;
      choix.appendChild(b);
    });
    noteIa = el("p", "asr-note");

    envoyer = el("button", "asr-env");
    envoyer.type = "submit";

    info = el("p", "asr-info");
    info.setAttribute("aria-live", "polite");

    panneau.appendChild(tete);
    panneau.appendChild(choix);
    panneau.appendChild(noteIa);
    panneau.appendChild(champ);
    panneau.appendChild(envoyer);
    panneau.appendChild(info);
    panneau.appendChild(el("p", "asr-note", TEXTES.note));
    choisir(choisie);
    panneau.addEventListener("submit", function (e) { e.preventDefault(); demander(); });
    panneau.addEventListener("keydown", function (e) { if (e.key === "Escape") fermerPanneau(); });
    champ.addEventListener("keydown", function (e) {
      var tactile = window.matchMedia && window.matchMedia("(pointer:coarse)").matches;
      if (e.key === "Enter" && !e.shiftKey && !tactile) { e.preventDefault(); demander(); }
    });

    document.body.appendChild(bouton);
    document.body.appendChild(panneau);
    placer();
    window.addEventListener("resize", function () { placer(); caler(); });
    if (window.visualViewport) {
      window.visualViewport.addEventListener("resize", caler);
      window.visualViewport.addEventListener("scroll", caler);
    }
    setInterval(placer, 1500);
  }

  function choisir(cle) {
    choisie = cle;
    Object.keys(choixBoutons).forEach(function (k) { choixBoutons[k].setAttribute("aria-checked", k === cle ? "true" : "false"); });
    noteIa.textContent = IAS[cle].note;
    envoyer.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
      '<path d="M14 4h6v6"/><path d="M20 4l-9 9"/><path d="M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/></svg>';
    envoyer.appendChild(document.createTextNode(TEXTES.bouton + IAS[cle].nom));
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

  function ouvrir() {
    info.textContent = "";
    panneau.classList.add("on");
    bouton.style.visibility = "hidden";
    caler();
    setTimeout(function () { champ.focus(); }, 30);
  }

  function fermerPanneau() {
    panneau.classList.remove("on");
    bouton.style.visibility = "";
    bouton.focus();
  }

  function demander() {
    var q = champ.value.trim();
    if (!q) { info.textContent = TEXTES.vide; champ.focus(); return; }
    if (navigator.onLine === false) { info.textContent = TEXTES.horsligne; return; }
    var invite = CONSIGNE + "\n\n" + (DNL ? "My question: " : "Ma question : ") + q;
    var adresse = IAS[choisie].adresse + encodeURIComponent(invite);
    var onglet = window.open(adresse, "_blank");
    if (onglet) {
      try { onglet.opener = null; } catch (e) { /* rien */ }
    } else {
      // ouverture d'onglet bloquée (certaines applis installées) : on y va directement
      window.location.href = adresse;
    }
    // rien n'est gardé côté site : le champ est vidé et le panneau refermé
    champ.value = "";
    fermerPanneau();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", construire);
  else construire();
})();
