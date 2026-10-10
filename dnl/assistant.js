/* Assistant de révision — bouton « Poser une question » et panneau de discussion.
   Maintenu à part du contenu, comme la couche de mouvement : le même fichier est
   copié dans svt/, pc/ et dnl/ ; seul le bloc CONFIG change d'un site à l'autre.
   Les questions partent vers le relais Cloudflare (assistant-relais/worker.js).
   Tant que RELAIS est vide, rien n'apparaît. La conversation reste en mémoire
   (rien n'est enregistré dans le navigateur) et disparaît à la fermeture du site. */
(function () {
  "use strict";

  /* ---------- CONFIG (propre à chaque site) ---------- */
  var MATIERE = "dnl";
  var NOM = "DNL Histoire-Géo";
  var RELAIS = "";
  var COULEURS = {
    fond: "#FBF8F0", fond2: "var(--paper, #F2ECDE)",
    encre: "var(--ink, #1F2433)", encre2: "var(--muted, #6B6350)", ligne: "var(--line, #CBBFA3)",
    accent: "var(--slate, #17233F)", surAccent: "#FBF8F0"
  };
  var EVITER = "";   /* élément fixé en bas d'écran à ne pas recouvrir */
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
    ".asr-fil{flex:1;min-height:0;overflow-y:auto;padding:14px 14px 6px;background:" + c.fond2 + ";-webkit-overflow-scrolling:touch}" +
    ".asr-note{font-size:13px;line-height:1.45;color:" + c.encre2 + ";margin:0 2px 12px}" +
    ".asr-m{margin:0 0 12px;padding:10px 13px;border-radius:12px;font-size:15px;line-height:1.5;max-width:92%;overflow-wrap:anywhere}" +
    ".asr-m.moi{margin-left:auto;background:" + c.accent + ";color:" + c.surAccent + ";white-space:pre-wrap;border-bottom-right-radius:4px}" +
    ".asr-m.ia{background:" + c.fond + ";border:1px solid " + c.ligne + ";border-bottom-left-radius:4px}" +
    ".asr-m.err{background:transparent;border:1px dashed " + c.ligne + ";color:" + c.encre2 + "}" +
    ".asr-m p{margin:0 0 .6em}.asr-m p:last-child,.asr-m ul:last-child,.asr-m ol:last-child{margin-bottom:0}" +
    ".asr-m ul,.asr-m ol{margin:0 0 .6em;padding-left:1.3em}.asr-m li{margin:.15em 0}" +
    ".asr-m code{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.9em;background:" + c.fond2 + ";padding:0 .25em;border-radius:4px}" +
    ".asr-m pre{white-space:pre-wrap;background:" + c.fond2 + ";padding:8px;border-radius:6px;margin:0 0 .6em}" +
    ".asr-m pre code{background:none;padding:0}" +
    ".asr-m .asr-h{font-weight:700;margin:.4em 0 .3em}" +
    ".asr-att{display:inline-flex;gap:4px;padding:4px 0}.asr-att i{width:7px;height:7px;border-radius:50%;background:" + c.encre2 + ";opacity:.5}" +
    "@media (prefers-reduced-motion:no-preference){.asr-att i{animation:asr-p 1s infinite ease-in-out}.asr-att i:nth-child(2){animation-delay:.15s}.asr-att i:nth-child(3){animation-delay:.3s}}" +
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
  function miseEnForme(texte) {
    var blocs = echapper(texte).split(/```/);
    var html = "";
    for (var b = 0; b < blocs.length; b++) {
      if (b % 2 === 1) { html += "<pre><code>" + blocs[b].replace(/^[a-z]*\n/, "") + "</code></pre>"; continue; }
      var lignes = blocs[b].split("\n"), liste = null, para = [];
      var finPara = function () { if (para.length) { html += "<p>" + enLigne(para.join("<br>")) + "</p>"; para = []; } };
      var finListe = function () { if (liste) { html += "</" + liste + ">"; liste = null; } };
      for (var i = 0; i < lignes.length; i++) {
        var l = lignes[i], m;
        if (!l.trim()) { finPara(); finListe(); continue; }
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

    var ctrl = window.AbortController ? new AbortController() : null;
    var minuterie = setTimeout(function () { if (ctrl) ctrl.abort(); }, 45000);

    fetch(RELAIS, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ matiere: MATIERE, messages: historique.slice(-7) }),
      signal: ctrl ? ctrl.signal : undefined
    })
      .then(function (r) { return r.json().catch(function () { return { erreur: "erreur" }; }); })
      .then(function (d) {
        if (d && typeof d.reponse === "string") {
          attente.innerHTML = miseEnForme(d.reponse);
          historique.push({ role: "assistant", content: d.reponse });
        } else {
          throw new Error((d && d.erreur) || "erreur");
        }
      })
      .catch(function (e) {
        historique.pop();
        var code = e && e.message;
        attente.className = "asr-m err";
        attente.textContent = MESSAGES[code] || (navigator.onLine === false ? MESSAGES.horsligne : MESSAGES.erreur);
      })
      .then(function () {
        clearTimeout(minuterie);
        enCours = false;
        envoyer.disabled = false;
        fil.scrollTop = fil.scrollHeight;
      });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", construire);
  else construire();
})();
