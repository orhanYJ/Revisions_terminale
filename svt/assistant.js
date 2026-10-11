/* Assistant de révision — bouton « Poser une question » et panneau de discussion.
   Maintenu à part du contenu, comme la couche de mouvement : le même fichier est
   copié dans svt/, pc/ et dnl/ ; seul le bloc CONFIG change d'un site à l'autre.
   Les questions partent vers le relais Cloudflare (assistant-relais/worker.js).
   Tant que RELAIS est vide, rien n'apparaît. La conversation reste en mémoire
   (rien n'est enregistré dans le navigateur) et disparaît à la fermeture du site. */
(function () {
  "use strict";

  /* ---------- CONFIG (propre à chaque site) ---------- */
  var MATIERE = "svt";
  var NOM = "SVT";
  var RELAIS = "https://assistant-revisions.orhanyildizm.workers.dev/";
  var MODELE = "@cf/openai/gpt-oss-120b";   /* parmi la liste MODELES du relais */
  var COULEURS = {
    fond: "var(--panel, #FFFDF8)", fond2: "var(--paper, #F7F4EC)",
    encre: "var(--ink, #17281E)", encre2: "var(--ink-2, #5E7263)", ligne: "var(--line, #E2DFD1)",
    accent: "var(--leaf, #2F7D52)", surAccent: "var(--panel, #FFFDF8)"
  };
  var EVITER = "nav.bottom";   /* élément fixé en bas d'écran à ne pas recouvrir */
  /* ---------- fin CONFIG ---------- */

  if (!RELAIS || !window.fetch) return;

  var MESSAGES = {
    quota: "L'assistant a atteint sa limite pour aujourd'hui. Il sera de nouveau disponible demain matin. En attendant, utilise la recherche du site.",
    limite: "Tu as posé beaucoup de questions en peu de temps. Réessaie dans une heure.",
    occupe: "L'assistant est très sollicité en ce moment. Réessaie dans quelques secondes.",
    horsligne: "L'assistant a besoin d'internet. Le reste du site fonctionne hors ligne.",
    erreur: "L'assistant n'a pas pu répondre. Réessaie dans un moment."
  };

  var historique = [];
  var enCours = false;
  var bouton, panneau, fil, champ, envoyer;

  /* ---------- styles ---------- */
  var c = COULEURS;
  var css =
    ".asr-btn,.asr-pan,.asr-pan *{box-sizing:border-box}" +
    ".asr-btn{position:fixed;left:14px;bottom:calc(14px + env(safe-area-inset-bottom,0px));z-index:70;width:52px;height:52px;border-radius:50%;border:0;" +
    "background:" + c.accent + ";color:" + c.surAccent + ";display:flex;align-items:center;justify-content:center;cursor:pointer;" +
    "box-shadow:0 2px 6px rgba(0,0,0,.18),0 8px 22px rgba(0,0,0,.14);-webkit-tap-highlight-color:transparent}" +
    ".asr-btn:focus-visible{outline:3px solid " + c.encre + ";outline-offset:3px}" +
    ".asr-btn svg{width:26px;height:26px}" +
    ".asr-pan{position:fixed;z-index:80;display:none;flex-direction:column;background:" + c.fond + ";color:" + c.encre + ";" +
    "border:1px solid " + c.ligne + ";box-shadow:0 12px 40px rgba(0,0,0,.22);overflow:hidden;" +
    "left:0;right:0;bottom:0;height:90vh;border-radius:16px 16px 0 0}" +
    "@media (min-width:700px){.asr-pan{left:18px;right:auto;bottom:18px;width:420px;height:min(620px,calc(100vh - 36px));border-radius:14px}}" +
    ".asr-pan.on{display:flex}" +
    ".asr-tete{display:flex;align-items:center;gap:10px;padding:12px 12px 12px 16px;border-bottom:1px solid " + c.ligne + "}" +
    ".asr-titre{flex:1;min-width:0;font-weight:700;font-size:16px;line-height:1.2}" +
    ".asr-titre small{display:block;font-weight:400;font-size:12px;color:" + c.encre2 + ";margin-top:2px}" +
    ".asr-ic{flex:none;margin:0;border:1px solid " + c.ligne + ";background:transparent;color:" + c.encre + ";border-radius:8px;height:36px;padding:0 10px;font:inherit;font-size:13px;cursor:pointer}" +
    ".asr-ic:focus-visible,.asr-env:focus-visible{outline:2px solid " + c.accent + ";outline-offset:2px}" +
    ".asr-fil{position:relative;flex:1;min-height:0;overflow-y:auto;padding:14px 14px 6px;background:" + c.fond2 + ";-webkit-overflow-scrolling:touch}" +
    ".asr-note{font-size:13px;line-height:1.45;color:" + c.encre2 + ";margin:0 2px 12px}" +
    ".asr-m{margin:0 0 12px;padding:10px 13px;border-radius:12px;font-size:15px;line-height:1.5;max-width:92%;overflow-wrap:anywhere}" +
    ".asr-m.moi{margin-left:auto;background:" + c.accent + ";color:" + c.surAccent + ";white-space:pre-wrap;border-bottom-right-radius:4px}" +
    ".asr-m.ia{background:" + c.fond + ";border:1px solid " + c.ligne + ";border-bottom-left-radius:4px}" +
    ".asr-verif{margin:.7em 0 0;padding:8px 10px;border-radius:8px;border:1px solid #D9A441;background:rgba(217,164,65,.14);font-size:14px;line-height:1.45}" +
    ".asr-verif b{display:block;font-size:12px;letter-spacing:.04em;text-transform:uppercase;margin-bottom:2px}" +
    ".asr-mention{display:block;margin-top:.7em;padding-top:.5em;border-top:1px solid " + c.ligne + ";font-size:12px;line-height:1.4;color:" + c.encre2 + "}" +
    ".asr-m.err{background:transparent;border:1px dashed " + c.ligne + ";color:" + c.encre2 + "}" +
    ".asr-m p{margin:0 0 .6em}.asr-m p:last-child,.asr-m ul:last-child,.asr-m ol:last-child{margin-bottom:0}" +
    ".asr-m ul,.asr-m ol{margin:0 0 .6em;padding-left:1.3em}.asr-m li{margin:.15em 0}" +
    ".asr-m code{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.9em;background:" + c.fond2 + ";padding:0 .25em;border-radius:4px}" +
    ".asr-m pre{white-space:pre-wrap;background:" + c.fond2 + ";padding:8px;border-radius:6px;margin:0 0 .6em}" +
    ".asr-m pre code{background:none;padding:0}" +
    ".asr-tab{overflow-x:auto;margin:0 0 .6em;-webkit-overflow-scrolling:touch}" +
    ".asr-tab table{border-collapse:collapse;font-size:13.5px;line-height:1.35;min-width:100%;width:max-content}" +
    ".asr-tab th,.asr-tab td{border:1px solid " + c.ligne + ";padding:5px 7px;text-align:left;vertical-align:top;min-width:7em;max-width:15em;overflow-wrap:normal;word-break:normal;hyphens:auto}" +
    ".asr-tab th{background:" + c.fond2 + ";font-weight:700}" +
    ".asr-m .asr-h{font-weight:700;margin:.4em 0 .3em}" +
    ".asr-att{display:inline-flex;gap:4px;padding:4px 0}.asr-att i{width:7px;height:7px;border-radius:50%;background:" + c.encre2 + ";opacity:.5}" +
    "@media (prefers-reduced-motion:no-preference){.asr-att i{animation:asr-p 1s infinite ease-in-out}.asr-att i:nth-child(2){animation-delay:.15s}.asr-att i:nth-child(3){animation-delay:.3s}}" +
    ".asr-pat{margin-left:8px;font-size:13px;color:" + c.encre2 + "}" +
    "@keyframes asr-p{0%,80%,100%{opacity:.25}40%{opacity:.9}}" +
    ".asr-pied{display:flex;gap:8px;align-items:flex-end;padding:10px 12px calc(10px + env(safe-area-inset-bottom,0px));border-top:1px solid " + c.ligne + ";background:" + c.fond + "}" +
    ".asr-champ{flex:1;min-width:0;width:100%;margin:0;resize:none;min-height:44px;max-height:140px;padding:11px 12px;border:1px solid " + c.ligne + ";border-radius:10px;" +
    "background:" + c.fond2 + ";color:" + c.encre + ";font:inherit;font-size:16px;line-height:1.35}" +
    ".asr-champ:focus{outline:2px solid " + c.accent + ";outline-offset:0;border-color:transparent}" +
    ".asr-env{flex:none;margin:0;height:44px;min-width:44px;padding:0 14px;border:0;border-radius:10px;background:" + c.accent + ";color:" + c.surAccent + ";font:inherit;font-weight:700;cursor:pointer}" +
    ".asr-env:disabled{opacity:.5;cursor:default}" +
    "@media print{.asr-btn,.asr-pan{display:none!important}}";

  /* ---------- mise en forme des réponses (markdown simple, échappé) ---------- */
  function echapper(t) {
    return t.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }
  function enLigne(t) {
    return t
      .replace(/`([^`\n]+)`/g, "<code>$1</code>")
      .replace(/\*\*([^*\n]+)\*\*/g, "<b>$1</b>")
      .replace(/(^|[\s(])\*([^*\s][^*\n]*?)\*(?=[\s).,;:!?]|$)/g, "$1<i>$2</i>")
      .replace(/(^|[\s(])_([^_\s][^_\n]*?)_(?=[\s).,;:!?]|$)/g, "$1<i>$2</i>");
  }
  // Les modèles écrivent parfois leurs formules en LaTeX malgré la consigne : on les ramène
  // à du texte lisible (σ, λ, 2^23, H₂O…). Seuls les passages délimités comme formules sont touchés,
  // et un « $ » n'ouvre une formule que s'il contient \, ^, _ ou { (les montants en dollars restent).
  var SYMBOLES = { sigma: "σ", lambda: "λ", kappa: "κ", Delta: "Δ", delta: "δ", mu: "µ", alpha: "α", beta: "β",
    gamma: "γ", pi: "π", rho: "ρ", theta: "θ", omega: "ω", Omega: "Ω", epsilon: "ε", varepsilon: "ε", tau: "τ",
    nu: "ν", eta: "η", chi: "χ", phi: "φ", times: "×", cdot: "·", approx: "≈", simeq: "≃", leq: "≤", le: "≤",
    geq: "≥", ge: "≥", neq: "≠", to: "→", rightarrow: "→", longrightarrow: "→", leftarrow: "←", Rightarrow: "⇒",
    rightleftharpoons: "⇌", leftrightarrow: "↔", sum: "Σ", infty: "∞", pm: "±", degree: "°", circ: "°",
    propto: "∝", ell: "ℓ", quad: " ", qquad: "  " };
  var INDICES = { "0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄", "5": "₅", "6": "₆", "7": "₇", "8": "₈", "9": "₉", "+": "₊", "-": "₋" };
  function formule(f) {
    var avant;
    f = f.replace(/\\(?:text|mathrm|mathbf|mathit|operatorname)\s*\{([^{}]*)\}/g, "$1")
      .replace(/\\left|\\right/g, "")
      .replace(/\\[,;:!]|~/g, " ")
      .replace(/\{,\}/g, ",");
    do {
      avant = f;
      f = f.replace(/\\[dt]?frac\s*\{([^{}]*)\}\s*\{([^{}]*)\}/g, "($1)/($2)")
        .replace(/\\sqrt\s*\{([^{}]*)\}/g, "√($1)");
    } while (f !== avant);
    f = f.replace(/\\([A-Za-z]+)/g, function (t, nom) { return SYMBOLES.hasOwnProperty(nom) ? SYMBOLES[nom] : nom; })
      .replace(/_\{([0-9+-]+)\}|_([0-9])/g, function (t, a, b) { return (a || b).split("").map(function (c) { return INDICES[c] || c; }).join(""); })
      .replace(/_\{([^{}]*)\}/g, "_$1")
      .replace(/\^\{([^{}]*)\}/g, function (t, e) { return /^-?[0-9a-z]$|^-?[0-9]+$/i.test(e) ? "^" + e : "^(" + e + ")"; })
      .replace(/[{}]/g, "")
      .replace(/\(([^()\s]+)\)\/\(([^()\s]+)\)/g, "$1/$2")
      .replace(/[ \t]{2,}/g, " ");
    return f.trim();
  }
  function sansLatex(t) {
    return t
      .replace(/\\\[([\s\S]*?)\\\]/g, function (x, f) { return "\n" + formule(f) + "\n"; })
      .replace(/\$\$([\s\S]*?)\$\$/g, function (x, f) { return "\n" + formule(f) + "\n"; })
      .replace(/\\\(([\s\S]*?)\\\)/g, function (x, f) { return formule(f); })
      .replace(/\$([^$\n]*?[\\^_{][^$\n]*?)\$/g, function (x, f) { return formule(f); });
  }

  // Tableau markdown (lignes « | a | b | ») : la ligne de tirets est sautée, la première ligne sert d'en-tête.
  function cellules(l) {
    return l.trim().replace(/^\|/, "").replace(/\|$/, "").split("|").map(function (c) { return enLigne(c.trim()); });
  }
  function tableau(lignes) {
    var html = '<div class="asr-tab"><table>', tete = true;
    for (var i = 0; i < lignes.length; i++) {
      if (/^\s*\|?\s*:?-{2,}/.test(lignes[i])) continue;
      var c = cellules(lignes[i]), bal = tete ? "th" : "td";
      html += "<tr><" + bal + ">" + c.join("</" + bal + "><" + bal + ">") + "</" + bal + "></tr>";
      tete = false;
    }
    return html + "</table></div>";
  }

  function miseEnForme(texte) {
    var blocs = echapper(sansLatex(texte)).split(/```/);
    var html = "";
    for (var b = 0; b < blocs.length; b++) {
      if (b % 2 === 1) { html += "<pre><code>" + blocs[b].replace(/^[a-z]*\n/, "") + "</code></pre>"; continue; }
      var lignes = blocs[b].split("\n"), liste = null, para = [];
      var finPara = function () { if (para.length) { html += "<p>" + enLigne(para.join("<br>")) + "</p>"; para = []; } };
      var finListe = function () { if (liste) { html += "</" + liste + ">"; liste = null; } };
      for (var i = 0; i < lignes.length; i++) {
        var l = lignes[i], m;
        if (!l.trim()) { finPara(); finListe(); continue; }
        if (/^\s*([-*_])(\s*\1){2,}\s*$/.test(l)) { finPara(); finListe(); continue; }
        if (/^\s*\|.*\|\s*$/.test(l)) {
          finPara(); finListe();
          var tab = [];
          while (i < lignes.length && /^\s*\|.*\|\s*$/.test(lignes[i])) tab.push(lignes[i++]);
          i--;
          html += tableau(tab);
          continue;
        }
        if ((m = l.match(/^\s*#{1,6}\s+(.*)$/))) { finPara(); finListe(); html += '<div class="asr-h">' + enLigne(m[1]) + "</div>"; continue; }
        if ((m = l.match(/^\s*[-*•]\s+(.*)$/)) || (m = l.match(/^\s*\d+[.)]\s+(.*)$/))) {
          var type = /^\s*\d/.test(l) ? "ol" : "ul";
          finPara();
          if (liste !== type) { finListe(); html += "<" + type + ">"; liste = type; }
          html += "<li>" + enLigne(m[1]) + "</li>";
          continue;
        }
        finListe();
        para.push(l);
      }
      finPara(); finListe();
    }
    return html;
  }

  // Met à part la dernière ligne « À vérifier : … » (« To check: … » en anglais) que le relais demande
  // à l'IA quand un point de sa réponse est incertain, et ajoute la mention commune.
  function estAnglais(t) {
    var en = (t.match(/\b(the|and|of|was|were|is|in)\b/gi) || []).length;
    var fr = (t.match(/\b(le|la|les|des|est|et|une|du)\b/gi) || []).length;
    return en > fr;
  }
  var A_VERIFIER = /^\s*\**\s*(à vérifier|a verifier|to check|to verify)\s*\**\s*:\s*\**\s*/i;
  function rendreReponse(texte) {
    var lignes = texte.replace(/\s+$/, "").split("\n"), doute = "", anglais = estAnglais(texte);
    for (var i = lignes.length - 1; i >= 0 && i >= lignes.length - 3; i--) {
      if (A_VERIFIER.test(lignes[i])) {
        doute = lignes.slice(i).join(" ").replace(A_VERIFIER, "").trim();
        lignes = lignes.slice(0, i);
        break;
      }
    }
    var html = miseEnForme(lignes.join("\n"));
    if (doute && !/^(aucun|aucune|rien|néant|none|nothing|n\/a)\b/i.test(doute)) {
      html += '<div class="asr-verif"><b>' + (anglais ? "⚠ To check" : "⚠ À vérifier") + "</b>" + enLigne(echapper(doute)) + "</div>";
    }
    html += '<span class="asr-mention">' + (anglais
      ? "AI answer: it can be wrong, even when it sounds sure. Check dates, figures and definitions in your course."
      : "Réponse d'IA : elle peut se tromper, même quand elle a l'air sûre. Vérifie les dates, chiffres et définitions dans ton cours.") + "</span>";
    return html;
  }

  /* ---------- interface ---------- */
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
    bouton.setAttribute("aria-label", "Poser une question à l'assistant");
    bouton.setAttribute("aria-haspopup", "dialog");
    bouton.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
      '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20.5l1.4-4.9A8 8 0 1 1 21 12z"/>' +
      '<path d="M10.1 9.6a2 2 0 1 1 2.9 1.8c-.6.3-1 .8-1 1.4v.4"/><circle cx="12" cy="16" r=".6" fill="currentColor"/></svg>';
    bouton.addEventListener("click", ouvrir);

    panneau = el("div", "asr-pan");
    panneau.setAttribute("role", "dialog");
    panneau.setAttribute("aria-label", "Assistant de révision");

    var tete = el("div", "asr-tete");
    var titre = el("div", "asr-titre", "Assistant · " + NOM);
    titre.appendChild(el("small", "", "Questions de cours, réponses par IA"));
    var nouvelle = el("button", "asr-ic", "Effacer");
    nouvelle.type = "button";
    nouvelle.setAttribute("aria-label", "Effacer la conversation");
    nouvelle.addEventListener("click", effacer);
    var fermer = el("button", "asr-ic", "Fermer");
    fermer.type = "button";
    fermer.addEventListener("click", fermerPanneau);
    tete.appendChild(titre); tete.appendChild(nouvelle); tete.appendChild(fermer);

    fil = el("div", "asr-fil");
    fil.setAttribute("aria-live", "polite");

    var pied = el("form", "asr-pied");
    champ = el("textarea", "asr-champ");
    champ.rows = 1;
    champ.maxLength = 1500;
    champ.placeholder = MATIERE === "dnl" ? "Ta question (en français ou en anglais)…" : "Ta question de cours…";
    champ.setAttribute("aria-label", "Ta question");
    envoyer = el("button", "asr-env", "Envoyer");
    envoyer.type = "submit";
    pied.appendChild(champ); pied.appendChild(envoyer);
    pied.addEventListener("submit", function (e) { e.preventDefault(); poser(); });
    champ.addEventListener("input", ajusterChamp);
    champ.addEventListener("keydown", function (e) {
      var tactile = window.matchMedia && window.matchMedia("(pointer:coarse)").matches;
      if (e.key === "Enter" && !e.shiftKey && !tactile) { e.preventDefault(); poser(); }
    });
    panneau.addEventListener("keydown", function (e) { if (e.key === "Escape") fermerPanneau(); });

    panneau.appendChild(tete); panneau.appendChild(fil); panneau.appendChild(pied);
    document.body.appendChild(bouton);
    document.body.appendChild(panneau);
    effacer();
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

  // Sur téléphone, cale le panneau sur la zone visible : elle rétrécit quand le clavier
  // s'ouvre, et reste juste même si la page déborde en largeur.
  function caler() {
    var vv = window.visualViewport;
    if (!vv || !panneau.classList.contains("on") || window.innerWidth >= 700 && vv.width >= 700) {
      panneau.style.left = panneau.style.top = panneau.style.width = panneau.style.height = "";
      return;
    }
    var h = vv.height * (vv.height < 500 ? 1 : 0.9);
    panneau.style.left = vv.offsetLeft + "px";
    panneau.style.width = vv.width + "px";
    panneau.style.top = (vv.offsetTop + vv.height - h) + "px";
    panneau.style.height = h + "px";
    fil.scrollTop = fil.scrollHeight;
  }

  function ajusterChamp() {
    champ.style.height = "auto";
    champ.style.height = Math.min(champ.scrollHeight + 2, 140) + "px";
  }

  function ouvrir() {
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

  function effacer() {
    if (enCours) return;
    historique = [];
    fil.innerHTML = "";
    var note = el("p", "asr-note",
      "Pose une question de cours ; l'IA répond. Elle peut se tromper : vérifie avec ton cours. " +
      "N'écris rien de personnel : les questions passent par un service en ligne.");
    fil.appendChild(note);
  }

  function ajouter(cls, html, texte) {
    var m = el("div", "asr-m " + cls);
    if (html != null) m.innerHTML = html; else m.textContent = texte;
    fil.appendChild(m);
    fil.scrollTop = fil.scrollHeight;
    return m;
  }

  function poser() {
    var q = champ.value.trim();
    if (!q || enCours) return;
    if (navigator.onLine === false) { ajouter("err", null, MESSAGES.horsligne); return; }
    enCours = true;
    envoyer.disabled = true;
    champ.value = "";
    ajusterChamp();
    ajouter("moi", null, q);
    historique.push({ role: "user", content: q });
    var attente = ajouter("ia", '<span class="asr-att" aria-label="L\'assistant rédige"><i></i><i></i><i></i></span>');
    var patience = setTimeout(function () {
      var a = attente.querySelector(".asr-att");
      if (a) a.insertAdjacentHTML("afterend", '<span class="asr-pat">' + (MATIERE === "dnl" ? "Thinking… (up to 30 s)" : "L'assistant réfléchit… (jusqu'à 30 s)") + "</span>");
    }, 4000);

    var ctrl = window.AbortController ? new AbortController() : null;
    var minuterie = setTimeout(function () { if (ctrl) ctrl.abort(); }, 90000);

    fetch(RELAIS, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ matiere: MATIERE, modele: MODELE, messages: historique.slice(-7) }),
      signal: ctrl ? ctrl.signal : undefined
    })
      .then(function (r) { return r.json().catch(function () { return { erreur: "erreur" }; }); })
      .then(function (d) {
        if (d && typeof d.reponse === "string") {
          attente.innerHTML = rendreReponse(d.reponse);
          historique.push({ role: "assistant", content: d.reponse });
          // une longue réponse se lit depuis son début : on y ramène le fil
          fil.scrollTop = Math.max(0, attente.offsetTop - 12);
          return;
        } else {
          throw new Error((d && d.erreur) || "erreur");
        }
      })
      .catch(function (e) {
        historique.pop();
        var code = e && e.message;
        attente.className = "asr-m err";
        attente.textContent = MESSAGES[code] || (navigator.onLine === false ? MESSAGES.horsligne : MESSAGES.erreur);
        fil.scrollTop = fil.scrollHeight;
      })
      .then(function () {
        clearTimeout(minuterie);
        clearTimeout(patience);
        enCours = false;
        envoyer.disabled = false;
      });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", construire);
  else construire();
})();
