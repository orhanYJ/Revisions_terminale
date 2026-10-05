/* =====================================================================
   COUCHE DE MOUVEMENT — « la chouette de Minerve prend son envol »
   A. l'accueil pense : les dix-sept notions flottent derrière le titre,
      se relient en constellation, fuient la main et s'éparpillent au
      toucher ; le titre s'écrit, les chiffres tombent, les cartes de
      l'index se distribuent et s'inclinent sous la main
   B. la chouette du filigrane se pose à chaque page et suit la main du
      regard
   C. changer de page : la nouvelle s'ouvre en cercle depuis le doigt ;
      les onglets glissent ; changer de thème se fait dans le même cercle
   D. une notion s'ouvre : numéro frappé, titre tracé, onglets distribués ;
      chaque débat se joue en trois temps — la thèse entre par la gauche,
      l'antithèse par la droite, la synthèse s'élève entre elles
   E. les blocs arrivent quand on les atteint ; les citations s'écrivent ;
      les volets « Approfondir » se déplient
   F. les flashcards : chaque première carte retournée fait tomber des
      feuilles d'olivier ; toutes retournées, la chouette s'envole ; son
      de lyre coupable
   G. le vol de lecture : une petite chouette suit la lecture
   Application React : ce script n'écrit jamais un attribut géré par
   React. Il observe le DOM, anime par l'API Web Animations, ajoute ses
   propres éléments décoratifs et rejoue les clics de navigation dans une
   transition de vue. Il ne cache jamais rien sans être là pour le
   révéler. Aucune persistance.
   ===================================================================== */
(function(){
"use strict";
var R = document.documentElement;
var mq = window.matchMedia ? window.matchMedia("(prefers-reduced-motion: reduce)") : null;
function calme(){ return !!(mq && mq.matches); }
R.classList.toggle("mo", !calme());
if(mq && mq.addEventListener){ mq.addEventListener("change", function(){ R.classList.toggle("mo", !calme()); }); }
var survol = window.matchMedia ? window.matchMedia("(hover: hover) and (pointer: fine)") : null;

var root = document.getElementById("root");
if(!root) return;
var NS = "http://www.w3.org/2000/svg";
var RESSORT = "cubic-bezier(.2,.9,.3,1.15)", DOUX = "cubic-bezier(.2,.8,.2,1)";
function couleur(v){ return getComputedStyle(R).getPropertyValue(v).trim(); }

/* ---------- outils ---------- */
function anim(el, kf, o){
  if(!el || !el.animate || calme()) return null;
  try{ return el.animate(kf, o); }catch(e){ return null; }
}
function centre(el){ var r = el.getBoundingClientRect(); return [r.left + r.width / 2, r.top + r.height / 2]; }
var $ = function(s, r){ return (r || document).querySelector(s); };
var $$ = function(s, r){ return [].slice.call((r || document).querySelectorAll(s)); };

/* ---------- révéler en arrivant : animations préparées en pause ---------- */
var attente = new Map();
var io = ("IntersectionObserver" in window) ? new IntersectionObserver(function(es){
  es.forEach(function(e){
    if(!e.isIntersecting) return;
    var l = attente.get(e.target);
    if(l){
      /* les délais servaient à l'entrée de page : au défilement, on part tout de suite
         en gardant l'échelonnement interne */
      var min = Infinity;
      l.forEach(function(a){ try{ min = Math.min(min, a.effect.getTiming().delay || 0); }catch(x){} });
      var recul = isFinite(min) ? Math.max(0, min - 40) : 0;
      l.forEach(function(a){
        try{ if(recul) a.effect.updateTiming({delay:Math.max(0, (a.effect.getTiming().delay || 0) - recul)}); a.play(); }catch(x){}
      });
    }
    attente.delete(e.target);
    io.unobserve(e.target);
  });
}, {rootMargin:"0px 0px -8% 0px"}) : null;
function bas(el){ return el.getBoundingClientRect().top > innerHeight * .92; }
/* sous la ligne de flottaison, les animations attendent en pause (leur première image
   tient l'état de départ) ; sinon elles partent tout de suite */
function differer(cible, anims){
  anims = anims.filter(Boolean);
  if(!anims.length || !io || !bas(cible)) return;
  anims.forEach(function(a){ a.pause(); });
  var deja = attente.get(cible);
  attente.set(cible, deja ? deja.concat(anims) : anims);
  io.observe(cible);
}
function liberer(){
  attente.forEach(function(l){ l.forEach(function(a){ try{ a.finish(); }catch(x){} }); });
  attente.clear();
}
addEventListener("beforeprint", liberer);
/* tout en bas, la marge de l'observateur ne peut plus être franchie : on joue ce qui reste */
function auBout(){
  attente.forEach(function(l, el){
    if(el.getBoundingClientRect().top >= innerHeight) return;
    l.forEach(function(a){ try{ a.play(); }catch(x){} });
    attente.delete(el); if(io) io.unobserve(el);
  });
}

/* ---------- la couche des éclats ---------- */
var couche = document.createElement("div");
couche.id = "mo-couche"; couche.setAttribute("aria-hidden", "true");
document.body.appendChild(couche);
function ephemere(el, ms){ couche.appendChild(el); setTimeout(function(){ el.remove(); }, ms); return el; }
var OLIVIER = ["var(--saffron)", "var(--teal)", "#7d8b4a", "var(--saffron-deep)", "#a3b06a"];
function feuilles(x, y, n, o){
  if(calme()) return;
  o = o || {};
  var c = o.couleurs || OLIVIER, f = o.force || 1;
  for(var k = 0; k < n; k++){
    var p = document.createElement("i");
    var a = o.angle != null ? o.angle + (Math.random() - .5) * (o.ouverture || 1.6) : Math.random() * Math.PI * 2;
    var d = f * (50 + Math.random() * 90);
    p.className = "mo-feuille";
    p.style.left = x + "px"; p.style.top = y + "px";
    p.style.setProperty("--c", c[k % c.length]);
    p.style.setProperty("--s", ((12 + Math.random() * 12) * (o.taille || 1)).toFixed(1) + "px");
    p.style.setProperty("--dx", (Math.cos(a) * d).toFixed(1) + "px");
    p.style.setProperty("--dy", (Math.sin(a) * d).toFixed(1) + "px");
    p.style.setProperty("--r", ((Math.random() - .5) * 540).toFixed(0) + "deg");
    p.style.setProperty("--g", (o.gravite != null ? o.gravite : 46) + "px");
    p.style.setProperty("--t", (o.duree || (1 + Math.random() * .5)).toFixed(2) + "s");
    p.style.animationDelay = ((o.etale || 90) * Math.random() | 0) + "ms";
    ephemere(p, 2000);
  }
}
function onde(x, y, c, k){
  if(calme()) return;
  var o = document.createElement("i"); o.className = "mo-onde";
  o.style.left = x + "px"; o.style.top = y + "px";
  o.style.setProperty("--c", c || "var(--saffron)"); o.style.setProperty("--k", k || 7);
  ephemere(o, 900);
}
function ruban(x, y, html){
  if(calme()) return;
  var o = document.createElement("span"); o.className = "mo-ruban"; o.innerHTML = html;
  o.style.left = Math.max(140, Math.min(innerWidth - 140, x)) + "px"; o.style.top = y + "px";
  ephemere(o, 2400);
}
/* la chouette s'envole à travers l'écran */
var CHOUETTE = '<svg viewBox="0 0 74 46">'
  + '<path class="aile g" d="M30 22 C20 8 8 6 1 10 C8 14 14 20 18 28 C22 27 27 26 30 26 Z" fill="currentColor" opacity=".85"/>'
  + '<path class="aile d" d="M44 22 C54 8 66 6 73 10 C66 14 60 20 56 28 C52 27 47 26 44 26 Z" fill="currentColor" opacity=".85"/>'
  + '<path d="M37 12 C45 12 47 20 46 28 C45 36 41 42 37 42 C33 42 29 36 28 28 C27 20 29 12 37 12 Z" fill="currentColor"/>'
  + '<path d="M30 13 L32 7 L35 12 M44 13 L42 7 L39 12" fill="currentColor"/>'
  + '<circle class="oeil" cx="33.5" cy="19" r="2.6"/><circle class="oeil" cx="40.5" cy="19" r="2.6"/>'
  + '<path d="M37 21 L35.6 24 L38.4 24 Z" fill="var(--saffron,#c8862a)"/></svg>';
function envol(x0, y0){
  if(calme()) return;
  var o = document.createElement("span"); o.className = "mo-envol"; o.innerHTML = CHOUETTE;
  ephemere(o, 3400);
  var W = innerWidth, H = innerHeight, x1 = W + 90, y1 = -80;
  var pts = [];
  for(var i = 0; i <= 10; i++){
    var t = i / 10, x = x0 + (x1 - x0) * t, y = y0 + (y1 - y0) * t * t - Math.sin(t * Math.PI) * H * .12;
    var s = .7 + t * .7;
    pts.push({transform:"translate(" + (x - 37).toFixed(0) + "px," + (y - 23).toFixed(0) + "px) rotate(" + (-8 - t * 10).toFixed(0) + "deg) scale(" + s.toFixed(2) + ")", opacity:t > .92 ? 0 : 1});
  }
  anim(o, pts, {duration:3200, easing:"cubic-bezier(.45,.05,.55,.95)", fill:"forwards"});
}

/* ---------- le son : une lyre, coupable ---------- */
var son = {actif:true, ctx:null};
function ctx(){
  if(!son.actif) return null;
  if(!son.ctx){
    var C = window.AudioContext || window.webkitAudioContext;
    if(!C) return null;
    try{ son.ctx = new C(); }catch(e){ return null; }
  }
  if(son.ctx.state === "suspended"){ try{ son.ctx.resume(); }catch(e){} }
  return son.ctx;
}
/* une corde pincée : attaque nette, extinction rapide, harmoniques légères */
function corde(f, dt, d, vol){
  var c = ctx(); if(!c) return;
  var t = c.currentTime + (dt || 0), g = c.createGain();
  g.gain.setValueAtTime(.0001, t);
  g.gain.exponentialRampToValueAtTime(vol || .08, t + .005);
  g.gain.exponentialRampToValueAtTime(.0001, t + d);
  var filtre = c.createBiquadFilter(); filtre.type = "lowpass"; filtre.frequency.setValueAtTime(f * 6, t); filtre.frequency.exponentialRampToValueAtTime(f * 1.5, t + d);
  filtre.connect(g); g.connect(c.destination);
  [[1, "triangle", 1], [2, "sine", .3], [3, "sine", .12]].forEach(function(p){
    var o = c.createOscillator(), gg = c.createGain();
    o.type = p[1]; o.frequency.setValueAtTime(f * p[0], t); gg.gain.value = p[2];
    o.connect(gg); gg.connect(filtre); o.start(t); o.stop(t + d + .05);
  });
}
var MODE = [293.66, 329.63, 349.23, 392, 440, 493.88, 523.25, 587.33, 659.25];   /* le mode de ré, dorien */
son.carte = function(k){ var i = k % (MODE.length - 2); corde(MODE[i], 0, 1.1, .075); corde(MODE[i + 2], .06, 1.2, .05); };
son.accord = function(){ [293.66, 392, 440, 587.33, 783.99].forEach(function(f, i){ corde(f, i * .09, 1.8, .065); }); };
var ICONE_SON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9h3l5-4v14l-5-4H4z"/><path class="ondes" d="M16 9.5a3.5 3.5 0 0 1 0 5M18.5 7a7 7 0 0 1 0 10"/><path class="barre" d="M16 9l5 6M21 9l-5 6"/></svg>';
var boutonSon = document.createElement("button");
boutonSon.type = "button"; boutonSon.className = "mo-son"; boutonSon.innerHTML = ICONE_SON;
function majSon(){
  var t = son.actif ? "Couper le son des cartes" : "Activer le son des cartes";
  boutonSon.setAttribute("aria-pressed", String(son.actif)); boutonSon.title = t; boutonSon.setAttribute("aria-label", t);
}
majSon();
boutonSon.addEventListener("click", function(){ son.actif = !son.actif; majSon(); if(son.actif) son.carte(2); });
document.body.appendChild(boutonSon);

/* ---------- C. changer de page dans une transition de vue ---------- */
var px = null, py = null, passe = false;
addEventListener("pointerdown", function(e){ px = e.clientX; py = e.clientY; }, {capture:true, passive:true});
var NAVIGUE = ".navitem, .index-cell, .authlink, .backlink, .dom-notion-link, .acard, .txcard, .rc-auteur, .tp-item";
document.addEventListener("click", function(ev){
  if(passe || calme() || !document.startViewTransition || !window.ReactDOM || !ReactDOM.flushSync) return;
  var t = ev.target.closest ? ev.target.closest(NAVIGUE + ", .btnrow .pill, .chap-tabs .chap-tab") : null;
  if(!t || !root.contains(t) || t.disabled) return;
  var onglet = t.classList.contains("pill") || t.classList.contains("chap-tab");
  if(onglet && t.classList.contains("on")) return;
  if(t.classList.contains("navitem") && t.classList.contains("on")) return;
  ev.preventDefault(); ev.stopImmediatePropagation();
  var r = t.getBoundingClientRect();
  R.style.setProperty("--vx", (px == null ? r.left + r.width / 2 : px) + "px");
  R.style.setProperty("--vy", (py == null ? r.top + r.height / 2 : py) + "px");
  if(onglet){
    /* l'onglet suivant arrive du côté où il se trouve */
    var freres = [].slice.call(t.parentNode.children), avant = freres.indexOf(t.parentNode.querySelector(":scope > .on"));
    R.style.setProperty("--vs", freres.indexOf(t) < avant ? "-1" : "1");
    R.setAttribute("data-mo-vt", "onglet");
  } else R.removeAttribute("data-mo-vt");
  try{
    var vt = document.startViewTransition(function(){
      passe = true;
      try{ ReactDOM.flushSync(function(){ t.click(); }); } finally { passe = false; }
      return new Promise(function(ok){ setTimeout(ok, 30); });
    });
    vt.finished.then(function(){ R.removeAttribute("data-mo-vt"); }, function(){ R.removeAttribute("data-mo-vt"); });
  }catch(e){ passe = true; try{ t.click(); } finally { passe = false; } }
}, true);

/* ---------- A. l'accueil ---------- */
var idees = null;
function constellation(hero){
  var cv = document.createElement("canvas");
  cv.className = "mo-idees"; cv.setAttribute("aria-hidden", "true");
  hero.insertBefore(cv, hero.firstChild);
  var c = cv.getContext && cv.getContext("2d");
  if(!c) return null;
  var mots = $$(".index-cell .nm").map(function(n){ return n.textContent.trim(); });
  if(!mots.length) mots = ["La conscience", "La liberté", "La vérité", "Le temps", "La justice"];
  var W = 0, H = 0, dpr = 1, enCours = 0, visible = true, souris = {x:-999, y:-999}, attenue = 1;
  var encre = "", or = "";
  function teintes(){ encre = couleur("--ink") || "#1c2438"; or = couleur("--saffron-deep") || couleur("--saffron") || "#a5661b"; }
  teintes();
  var g = 11;
  function hasard(){ g = (g * 9301 + 49297) % 233280; return g / 233280; }
  var points = mots.map(function(m, i){
    return {m:m, x:hasard(), y:hasard(), vx:(hasard() - .5) * .25, vy:(hasard() - .5) * .25, t0:hasard(), t:16, a:.1 + hasard() * .14, ph:hasard() * 6.3, vu:true};
  });
  function taille(){
    var r = cv.getBoundingClientRect();
    dpr = Math.min(2, window.devicePixelRatio || 1);
    W = r.width; H = r.height;
    cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr);
    /* les idées flottent autour du texte, jamais dessus ; sur téléphone elles sont plus pâles */
    attenue = W > 820 ? 1 : .6;
    /* sur un écran étroit, moins d'idées et plus petites */
    points.forEach(function(p, i){ p.vu = W > 820 || i % 2 === 0; p.t = (W > 820 ? 13 : 10) + p.t0 * (W > 820 ? 9 : 5); });
    mesurer();
    points.forEach(function(p){ if(p.x <= 1){ p.x = 20 + p.x * (W - 40); p.y = p.y * H; } });
  }
  var textes = [], mesure = 0;
  function mesurer(){
    var rc = cv.getBoundingClientRect();
    textes = $$(".kicker, h1, .tag, .stat", hero).map(function(e){
      var r = e.getBoundingClientRect();
      /* le texte réel d'un bloc large : on borne à la longueur de ses lignes */
      var rg = document.createRange(); rg.selectNodeContents(e);
      var rr = rg.getBoundingClientRect();
      var droite = Math.min(r.right, rr.width ? rr.right : r.right);
      return {g:r.left - rc.left - 10, d:droite - rc.left + 10, h:r.top - rc.top - 8, b:r.bottom - rc.top + 6};
    });
    mesure = Date.now();
  }
  function image(ts){
    enCours = 0;
    if(!cv.isConnected){ return; }
    if(!visible || document.hidden || calme()){ dessiner(0); return; }
    if(Date.now() - mesure > 1500) mesurer();
    dessiner(ts || 0);
    enCours = requestAnimationFrame(image);
  }
  function dessiner(ts){
    c.setTransform(dpr, 0, 0, dpr, 0, 0);
    c.clearRect(0, 0, W, H);
    /* les fils : deux idées proches se relient ; trop proches, elles s'écartent */
    c.lineWidth = .8;
    for(var i = 0; i < points.length; i++){
      if(!points[i].vu) continue;
      for(var j = i + 1; j < points.length; j++){
        var a = points[i], b = points[j];
        if(!b.vu) continue;
        var d = Math.hypot(a.x - b.x, a.y - b.y);
        if(ts && d < 70){ var e = (70 - d) / 70 * .05, ux = (a.x - b.x) / (d || 1), uy = (a.y - b.y) / (d || 1); a.vx += ux * e; a.vy += uy * e; b.vx -= ux * e; b.vy -= uy * e; }
        if(d < 170){
          c.strokeStyle = or; c.globalAlpha = (1 - d / 170) * .22;
          c.beginPath(); c.moveTo(a.x, a.y); c.lineTo(b.x, b.y); c.stroke();
        }
      }
    }
    points.forEach(function(p){
      if(!p.vu) return;
      if(ts){
        /* la main repousse les idées */
        var dx = p.x - souris.x, dy = p.y - souris.y, d2 = dx * dx + dy * dy;
        if(d2 < 18000){ var f = (18000 - d2) / 18000 * .35, d = Math.sqrt(d2) || 1; p.vx += dx / d * f; p.vy += dy / d * f; }
        p.vx *= .965; p.vy *= .965;
        p.vx += Math.cos(ts / 4000 + p.ph) * .004; p.vy += Math.sin(ts / 5200 + p.ph) * .004;
        var v = Math.hypot(p.vx, p.vy); if(v < .12){ p.vx *= 1.04; p.vy *= 1.04; }
        /* un mot qui touche le texte en est doucement repoussé */
        var dm = p.m.length * p.t * .24;
        for(var q = 0; q < textes.length; q++){
          var z = textes[q];
          if(p.x + dm > z.g && p.x - dm < z.d && p.y + 4 > z.h && p.y - p.t < z.b){
            var versG = (p.x + dm) - z.g, versD = z.d - (p.x - dm), versH = (p.y + 4) - z.h, versB = z.b - (p.y - p.t);
            var mn = Math.min(versG, versD, versH, versB);
            if(mn === versG) p.vx -= .25; else if(mn === versD) p.vx += .25; else if(mn === versH) p.vy -= .25; else p.vy += .25;
          }
        }
        p.x += p.vx; p.y += p.vy;
        if(p.x < 20){ p.x = 20; p.vx = Math.abs(p.vx); } if(p.x > W - 20){ p.x = W - 20; p.vx = -Math.abs(p.vx); }
        if(p.y < 14){ p.y = 14; p.vy = Math.abs(p.vy); } if(p.y > H - 10){ p.y = H - 10; p.vy = -Math.abs(p.vy); }
      }
      c.globalAlpha = p.a * attenue;
      c.fillStyle = encre;
      c.font = "italic " + p.t.toFixed(0) + "px Spectral, Georgia, serif";
      c.textAlign = "center";
      c.fillText(p.m, p.x, p.y);
      c.globalAlpha = p.a * 1.6 * attenue; c.fillStyle = or;
      c.beginPath(); c.arc(p.x, p.y - p.t * .9, 1.6, 0, Math.PI * 2); c.fill();
    });
    c.globalAlpha = 1;
  }
  function relancer(){ if(!enCours) enCours = requestAnimationFrame(image); }
  taille();
  if("IntersectionObserver" in window) new IntersectionObserver(function(es){ visible = es[0].isIntersecting; if(visible) relancer(); }).observe(cv);
  document.addEventListener("visibilitychange", relancer);
  addEventListener("resize", function(){ if(cv.isConnected){ taille(); relancer(); } });
  addEventListener("pointermove", function(e){ if(!cv.isConnected) return; var r = cv.getBoundingClientRect(); souris.x = e.clientX - r.left; souris.y = e.clientY - r.top; }, {passive:true});
  /* toucher l'en-tête éparpille les idées */
  hero.addEventListener("pointerdown", function(e){
    var r = cv.getBoundingClientRect(), x = e.clientX - r.left, y = e.clientY - r.top;
    points.forEach(function(p){ var dx = p.x - x, dy = p.y - y, d = Math.hypot(dx, dy) || 1; p.vx += dx / d * 5; p.vy += dy / d * 5; });
    onde(e.clientX, e.clientY, "var(--saffron)", 10);
    relancer();
  });
  relancer();
  return {teintes:teintes, relancer:relancer};
}
function entreeAccueil(inner){
  var hero = $(".hero", inner);
  if(hero){
    idees = constellation(hero);
    var kick = $(".kicker", hero), h1 = $("h1", hero), tag = $(".tag", hero);
    anim(kick, [{opacity:0, letterSpacing:".5em"}, {opacity:1, letterSpacing:".2em"}], {duration:900, easing:DOUX, fill:"backwards"});
    anim(h1, [{clipPath:"inset(0 100% 0 0)", transform:"translateX(-10px)"}, {clipPath:"inset(0 0 0 0)", transform:"none"}], {duration:1100, delay:150, easing:"cubic-bezier(.6,0,.2,1)", fill:"backwards"});
    anim($("em", hero), [{color:couleur("--ink") || "#1c2438"}, {color:couleur("--saffron") || "#c8862a", offset:.6}, {color:couleur("--saffron-deep") || "#a5661b"}], {duration:1400, delay:900, easing:"ease-out"});
    anim(tag, [{opacity:0, transform:"translateY(14px)"}, {opacity:1, transform:"none"}], {duration:800, delay:600, easing:DOUX, fill:"backwards"});
    $$(".stat", hero).forEach(function(s, i){
      anim($(".v", s), [{opacity:0, transform:"translateY(-36px) scale(1.6)"}, {opacity:1, transform:"translateY(3px) scale(.95)", offset:.7}, {opacity:1, transform:"none"}],
        {duration:620, delay:900 + i * 140, easing:"cubic-bezier(.5,0,.4,1)", fill:"backwards"});
      anim($(".l", s), [{opacity:0}, {opacity:1}], {duration:500, delay:1100 + i * 140, fill:"backwards"});
    });
  }
  /* les cartes de l'index se distribuent */
  $$(".index-cell", inner).forEach(function(c, i){
    var a = anim(c, [{opacity:0, transform:"translateY(26px) rotateX(-35deg)"}, {opacity:1, transform:"none"}],
      {duration:650, delay:1100 + i * 55, easing:RESSORT, fill:"backwards"});
    differer(c, [a]);
    if(!c._moTilt){ c._moTilt = true; inclinaison(c); }
  });
}
/* sous la souris, une carte s'incline vers la main (la carte n'a pas d'attribut style géré par React) */
function inclinaison(c){
  if(!survol || !survol.matches) return;
  c.addEventListener("pointermove", function(e){
    if(calme()) return;
    var r = c.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
    c.style.transition = "transform .12s ease-out,background .13s,box-shadow .3s ease";
    c.style.transform = "rotateX(" + (-y * 10).toFixed(2) + "deg) rotateY(" + (x * 12).toFixed(2) + "deg) translateZ(8px)";
  });
  c.addEventListener("pointerleave", function(){
    c.style.transition = "transform .6s cubic-bezier(.3,1.4,.5,1),background .13s,box-shadow .3s ease";
    c.style.transform = "";
  });
}

/* ---------- B. la chouette du filigrane ---------- */
var regard = {x:0, y:0}, regardFil = 0;
function poserChouette(bg){
  var img = $("img", bg);
  if(!img) return;
  anim(img, [{opacity:0, transform:"translate(90px,-120px) rotate(-14deg) scale(.82)"}, {opacity:1, transform:"translate(-6px,6px) rotate(2deg) scale(1.02)", offset:.75}, {opacity:1, transform:"none"}],
    {duration:1300, delay:150, easing:"cubic-bezier(.3,.6,.3,1)"});
}
addEventListener("pointermove", function(e){
  if(calme() || (survol && !survol.matches)) return;
  regard.x = e.clientX / innerWidth - .5; regard.y = e.clientY / innerHeight - .5;
  if(!regardFil) regardFil = requestAnimationFrame(function(){
    regardFil = 0;
    var img = $(".notion-bgicon img", root);
    if(!img) return;
    img.style.transition = "transform 1.2s cubic-bezier(.2,.8,.2,1)";
    img.style.transform = "translate(" + (regard.x * -16).toFixed(1) + "px," + (regard.y * -12).toFixed(1) + "px) rotate(" + (regard.x * 4).toFixed(2) + "deg)";
  });
}, {passive:true});

/* ---------- la pastille de la barre latérale ---------- */
var pastille = null;
function placerPastille(sansAnim){
  var side = $(".sidebar", root);
  if(!side || !side.offsetWidth){ return; }
  var on = $(".navitem.on", side);
  if(!pastille){ pastille = document.createElement("i"); pastille.className = "mo-pastille"; pastille.setAttribute("aria-hidden", "true"); }
  if(pastille.parentNode !== side) side.appendChild(pastille);
  if(!on){ pastille.style.opacity = "0"; side.classList.remove("mo-a-pastille"); return; }
  var rs = side.getBoundingClientRect(), ro = on.getBoundingClientRect();
  var x = ro.left - rs.left + side.scrollLeft, y = ro.top - rs.top + side.scrollTop;
  if(sansAnim || calme()) pastille.style.transition = "none";
  pastille.style.width = ro.width + "px"; pastille.style.height = ro.height + "px";
  pastille.style.transform = "translate(" + x + "px," + y + "px)";
  pastille.style.opacity = "1";
  if(sansAnim || calme()){ void pastille.offsetWidth; pastille.style.transition = ""; }
  side.classList.add("mo-a-pastille");
}

/* ---------- D. une notion s'ouvre ---------- */
function entreeNotion(inner){
  var h = $(".h-notion", inner), idx = h && $(".idx", h);
  anim($(".eyebrow", inner), [{opacity:0, letterSpacing:".4em"}, {opacity:1, letterSpacing:"normal"}], {duration:700, easing:DOUX, fill:"backwards"});
  anim(idx, [{opacity:0, transform:"scale(3) rotate(-20deg)"}, {opacity:1, transform:"scale(.9) rotate(3deg)", offset:.6}, {opacity:1, transform:"none"}], {duration:650, delay:120, easing:"cubic-bezier(.5,0,.3,1)", fill:"backwards"});
  anim(h, [{clipPath:"inset(-10% 100% -10% 0)"}, {clipPath:"inset(-10% 0 -10% 0)"}], {duration:900, delay:260, easing:"cubic-bezier(.6,0,.2,1)", fill:"backwards"});
  anim($(".persp", inner), [{opacity:0, transform:"translateY(14px)"}, {opacity:1, transform:"none"}], {duration:700, delay:650, easing:DOUX, fill:"backwards"});
  $$(".btnrow .pill", inner).forEach(function(p, i){
    anim(p, [{opacity:0, transform:"translateY(12px) scale(.85)"}, {opacity:1, transform:"none"}], {duration:480, delay:800 + i * 80, easing:RESSORT, fill:"backwards"});
  });
}
function entreeVue(inner){
  var tete = $(".eyebrow", inner), titre = $("h1, .h-notion, .h2", inner);
  anim(tete, [{opacity:0, transform:"translateX(-20px)"}, {opacity:1, transform:"none"}], {duration:600, easing:DOUX, fill:"backwards"});
  anim(titre, [{opacity:0, transform:"translateY(18px)"}, {opacity:1, transform:"none"}], {duration:700, delay:100, easing:DOUX, fill:"backwards"});
}

/* ---------- E. chaque bloc à son entrée ---------- */
var vus = new WeakSet();
function monte(el, delai){
  return anim(el, [{opacity:0, transform:"translateY(22px)"}, {opacity:1, transform:"none"}], {duration:700, delay:delai || 0, easing:DOUX, fill:"backwards"});
}
/* un débat en trois temps : thèse à gauche, antithèse à droite, la synthèse s'élève */
function debat(d){
  var anims = [], q = $(".dq", d), t = $(".side.t", d), a = $(".side.a", d), s = $(".synth", d);
  anims.push(anim(q, [{opacity:0, transform:"translateY(-16px)"}, {opacity:1, transform:"none"}], {duration:600, easing:DOUX, fill:"backwards"}));
  anims.push(anim(t, [{opacity:0, transform:"translateX(-46px)"}, {opacity:1, transform:"translateX(4px)", offset:.75}, {opacity:1, transform:"none"}], {duration:750, delay:250, easing:DOUX, fill:"backwards"}));
  anims.push(anim(a, [{opacity:0, transform:"translateX(46px)"}, {opacity:1, transform:"translateX(-4px)", offset:.75}, {opacity:1, transform:"none"}], {duration:750, delay:520, easing:DOUX, fill:"backwards"}));
  if(s){
    anims.push(anim(s, [{opacity:0, transform:"translateY(30px) scale(.97)"}, {opacity:1, transform:"none"}], {duration:800, delay:950, easing:RESSORT, fill:"backwards"}));
    var tl = couleur("--teal-rgb") || "42,110,104";
    anims.push(anim(s, [{boxShadow:"0 0 0 0 rgba(" + tl + ",0)"}, {boxShadow:"0 0 0 7px rgba(" + tl + ",.18)", offset:.4}, {boxShadow:"0 0 0 0 rgba(" + tl + ",0)"}], {duration:1300, delay:1500, easing:"ease-out", fill:"backwards"}));
  }
  /* le choc des deux thèses : une onde quand l'antithèse arrive */
  var sf = couleur("--saffron-rgb") || "200,134,42";
  var choc = anim(d, [{boxShadow:"0 0 0 0 rgba(" + sf + ",0)"}, {boxShadow:"0 0 0 5px rgba(" + sf + ",.2)", offset:.3}, {boxShadow:"0 0 0 0 rgba(" + sf + ",0)"}], {duration:900, delay:900, easing:"ease-out"});
  anims.push(choc);
  differer(d, anims);
}
/* une distinction de M. Bellon : les deux termes arrivent chacun de leur côté, le « ≠ » tombe entre eux */
function maillon(m){
  var cotes = $$(".mln-side", m), vs = $(".mln-vs", m), n = $(".mln-n", m), anims = [];
  anims.push(anim(m, [{opacity:0, transform:"translateY(18px)"}, {opacity:1, transform:"none"}], {duration:600, easing:DOUX, fill:"backwards"}));
  anims.push(anim(n, [{opacity:0, transform:"scale(2.4) rotate(-15deg)"}, {opacity:1, transform:"none"}], {duration:550, delay:120, easing:"cubic-bezier(.5,0,.3,1)", fill:"backwards"}));
  if(cotes[0]) anims.push(anim(cotes[0], [{opacity:0, transform:"translateX(-40px)"}, {opacity:1, transform:"none"}], {duration:650, delay:200, easing:DOUX, fill:"backwards"}));
  if(cotes[1]) anims.push(anim(cotes[1], [{opacity:0, transform:"translateX(40px)"}, {opacity:1, transform:"none"}], {duration:650, delay:340, easing:DOUX, fill:"backwards"}));
  anims.push(anim(vs, [{opacity:0, transform:"translateY(-30px) scale(2) rotate(-90deg)"}, {opacity:1, transform:"scale(.85)", offset:.7}, {opacity:1, transform:"none"}], {duration:600, delay:720, easing:"cubic-bezier(.5,0,.3,1)", fill:"backwards"}));
  differer(m, anims);
}
function citationEcrite(c){
  return anim(c, [{clipPath:"inset(0 100% 0 0)", opacity:.3}, {clipPath:"inset(0 0 0 0)", opacity:1}], {duration:1000, delay:150, easing:"cubic-bezier(.5,0,.3,1)", fill:"backwards"});
}
var BLOCS = ".chap-txt,.chap-oeuv,.mln-verif,.mx-et,.mx-err,.mx-ast,.mx-modele,.mx-choix,.mln-list,.defbox,.callout,.dist,.method-step,.corr-block,.citecard,.acard,.txcard,.mvt,.exitem,.sujet,.fiche,.oppo,.carre,.piege,.domcard,.vidcard,.biobloc,.thbloc,.transv,.faute,.disti,.vocp,.plan-step,.citkey,.oeuvre,.usage";
function balayerBlocs(inner){
  var vague = 0;
  $$(".h2", inner).forEach(function(h){
    if(vus.has(h)) return; vus.add(h);
    var b = $(".bar", h), anims = [];
    anims.push(anim(h, [{opacity:0, transform:"translateX(-26px)"}, {opacity:1, transform:"none"}], {duration:650, easing:DOUX, fill:"backwards"}));
    anims.push(anim(b, [{transform:"rotate(-180deg) scale(.3)", opacity:0}, {transform:"none", opacity:1}], {duration:650, delay:120, easing:RESSORT, fill:"backwards"}));
    differer(h, anims);
  });
  $$(".debate", inner).forEach(function(d){ if(!vus.has(d)){ vus.add(d); debat(d); } });
  $$(".mln", inner).forEach(function(m){ if(!vus.has(m)){ vus.add(m); maillon(m); } });
  $$(BLOCS, inner).forEach(function(el){
    if(vus.has(el)) return; vus.add(el);
    if(el.parentElement && el.parentElement.closest(BLOCS)) return;
    var a = monte(el, bas(el) ? 0 : 300 + Math.min(vague++, 8) * 60);
    differer(el, [a]);
  });
  $$(".dref, .quote", inner).forEach(function(c){
    if(vus.has(c)) return; vus.add(c);
    if(c.closest(".debate") && !bas(c)) return;
    differer(c, [citationEcrite(c)]);
  });
  $$(".flash", inner).forEach(function(f, i){
    if(vus.has(f)) return; vus.add(f);
    differer(f, [anim(f, [{opacity:0, transform:"perspective(900px) rotateX(-50deg) translateY(20px)"}, {opacity:1, transform:"none"}], {duration:650, delay:(i % 4) * 70, easing:RESSORT, fill:"backwards"})]);
  });
  /* les volets qui viennent de s'ouvrir se déplient */
  $$(".approf-body, .dtrans-body, .citecard-approf", inner).forEach(function(b){
    if(vus.has(b)) return; vus.add(b);
    anim(b, [{opacity:0, clipPath:"inset(0 0 100% 0)", transform:"translateY(-8px)"}, {opacity:1, clipPath:"inset(0 0 0 0)", transform:"none"}], {duration:500, easing:DOUX});
  });
}

/* ---------- F. les flashcards ---------- */
var retournees = new WeakSet(), nbRetournees = 0, toutesFete = false;
document.addEventListener("click", function(ev){
  var f = ev.target.closest ? ev.target.closest(".flash") : null;
  if(!f || !root.contains(f)) return;
  requestAnimationFrame(function(){
    if(!f.classList.contains("flip")) return;
    if(retournees.has(f)) return;
    retournees.add(f); nbRetournees++;
    var xy = centre(f);
    feuilles(xy[0], xy[1] - 20, 14, {force:.8, angle:-Math.PI / 2, ouverture:2.4, taille:.8});
    son.carte(nbRetournees);
    var inner = f.closest(".inner"), toutes = inner ? $$(".flash", inner) : [];
    var faites = toutes.filter(function(x){ return retournees.has(x); }).length;
    if(toutes.length > 2 && faites === toutes.length && !toutesFete){
      toutesFete = true;
      setTimeout(function(){
        ruban(innerWidth / 2, innerHeight * .3, "<b>✦</b>Toutes les cartes retournées — la chouette prend son envol");
        feuilles(innerWidth / 2, innerHeight * .3, 50, {force:1.9, taille:1.2, gravite:70, duree:1.5});
        envol(xy[0], xy[1]);
        son.accord();
      }, 350);
    } else if(faites === 5 || faites === 10 || faites === 20){
      ruban(xy[0], Math.max(70, xy[1] - 90), "<b>" + faites + "</b>cartes retournées sur " + toutes.length);
    }
  });
});
/* le bouton du son apparaît quand des flashcards sont à l'écran */
var ioCartes = ("IntersectionObserver" in window) ? new IntersectionObserver(function(es){
  es.forEach(function(e){ e.target._moVisible = e.isIntersecting; });
  boutonSon.classList.toggle("vu", $$(".flash", root).some(function(f){ return f._moVisible; }));
}) : null;

/* ---------- les citations : filtrer redistribue les fiches ---------- */
document.addEventListener("click", function(ev){
  var c = ev.target.closest ? ev.target.closest(".citechip, .citetag, .citereset, .citecard-auteur, .filterbar .pill, .pill:not(.btnrow .pill)") : null;
  if(!c || calme()) return;
  requestAnimationFrame(function(){ requestAnimationFrame(function(){
    var k = 0;
    $$(".citecard, .acard, .txcard, .exitem", root).forEach(function(x){
      var r = x.getBoundingClientRect();
      if(r.bottom < 0 || r.top > innerHeight) return;
      anim(x, [{opacity:0, transform:"translateY(18px) rotate(-.8deg)"}, {opacity:1, transform:"none"}], {duration:480, delay:Math.min(k++, 12) * 40, easing:RESSORT, fill:"backwards"});
    });
  }); });
});

/* ---------- le modèle d'introduction : les quatre étapes s'allument une à une ---------- */
document.addEventListener("click", function(ev){
  var b = ev.target.closest ? ev.target.closest(".mx-hlbtn") : null;
  if(!b || calme()) return;
  requestAnimationFrame(function(){ requestAnimationFrame(function(){
    var mod = b.parentNode && b.parentNode.querySelector(".mx-modele.hl");
    if(!mod) return;
    $$(".mx-sg", mod).forEach(function(sg, i){
      anim(sg, [{filter:"brightness(1)", transform:"none"}, {filter:"brightness(1.25)", transform:"translateY(-2px)", offset:.4}, {filter:"brightness(1)", transform:"none"}], {duration:700, delay:i * 260, easing:"ease-out"});
    });
    $$(".mx-leg-i", b.parentNode).forEach(function(l, i){
      anim(l, [{opacity:0, transform:"translateY(8px)"}, {opacity:1, transform:"none"}], {duration:450, delay:i * 260, easing:DOUX, fill:"backwards"});
    });
  }); });
});

/* ---------- G. le vol de lecture ---------- */
var vol = document.createElement("div");
vol.id = "mo-vol"; vol.setAttribute("aria-hidden", "true");
vol.innerHTML = '<i class="v-fil"></i><span class="v-chouette"><svg viewBox="0 0 24 24">'
  + '<path class="aile g" d="M9 10 C6 7 3 7 1 8 C3 10 5 12 6 15 Z" fill="currentColor" opacity=".8"/>'
  + '<path class="aile d" d="M15 10 C18 7 21 7 23 8 C21 10 19 12 18 15 Z" fill="currentColor" opacity=".8"/>'
  + '<path d="M12 5 C16 5 17 9 16.6 13 C16.2 17 14 20 12 20 C10 20 7.8 17 7.4 13 C7 9 8 5 12 5 Z" fill="currentColor"/>'
  + '<circle cx="10.4" cy="9.6" r="1.5" fill="var(--paper,#fff)"/><circle cx="13.6" cy="9.6" r="1.5" fill="var(--paper,#fff)"/></svg></span>';
document.body.appendChild(vol);
var tick = false, perche = false, arret = 0;
function lecture(){
  tick = false;
  var main = $("main.main", root), h = R.scrollHeight - innerHeight;
  if(!main || h < 600){ vol.classList.remove("on"); return; }
  var tb = $(".topbar", root), haut = 0;
  if(tb && tb.offsetHeight && getComputedStyle(tb).display !== "none") haut = Math.max(0, tb.getBoundingClientRect().bottom);
  var m = main.getBoundingClientRect(), p = Math.max(0, Math.min(1, scrollY / h));
  vol.style.setProperty("--g", (m.left + 16) + "px");
  vol.style.setProperty("--l", Math.max(0, m.width - 32) + "px");
  vol.style.setProperty("--h", (haut + 12) + "px");
  vol.style.setProperty("--p", p.toFixed(4));
  vol.classList.add("on");
  vol.classList.add("vole");
  clearTimeout(arret); arret = setTimeout(function(){ vol.classList.remove("vole"); }, 260);
  if(!perche && p > .993){
    perche = true;
    vol.classList.remove("fin"); void vol.offsetWidth; vol.classList.add("fin");
    var c = centre($(".v-chouette", vol));
    feuilles(c[0], c[1], 14, {force:.7, angle:Math.PI / 2, ouverture:2.6, taille:.7});
  }
  if(p < .9) perche = false;
  if(scrollY >= h - 2) auBout();
}
addEventListener("scroll", function(){ if(!tick){ tick = true; requestAnimationFrame(lecture); } }, {passive:true});
addEventListener("resize", function(){ placerPastille(true); lecture(); });

/* ---------- l'observateur : chaque nouveauté rendue par React ---------- */
var prevu = false, vueCle = null, vueTitre = null, theme = R.getAttribute("data-theme");
/* une page se reconnaît à son titre : changer d'onglet dans une notion ne la rejoue pas,
   passer d'une notion à l'autre (même élément réutilisé par React) la rejoue */
function cleDe(inner){
  var h = $(".h-notion, .hero h1, h1, .eyebrow, .h2", inner);
  return h ? h.textContent.trim() : "";
}
function balayer(){
  prevu = false;
  attente.forEach(function(l, el){ if(!el.isConnected){ l.forEach(function(x){ try{ x.cancel(); }catch(e){} }); attente.delete(el); if(io) io.unobserve(el); } });
  var inner = $("main.main > .inner", root);
  var cle = inner ? cleDe(inner) : null;
  if(inner && (inner !== vueCle || cle !== vueTitre)){
    vueCle = inner; vueTitre = cle; vus = new WeakSet();
    if(!calme()){
      perche = false; toutesFete = false;
      var bg = $(".notion-bgicon", inner);
      if(bg) poserChouette(bg);
      if($(".hero", inner)) entreeAccueil(inner);
      else if($(".h-notion", inner)) entreeNotion(inner);
      else entreeVue(inner);
    }
  }
  if(inner){
    balayerBlocs(inner);
    if(ioCartes) $$(".flash", inner).forEach(function(f){ if(!f._moObs){ f._moObs = true; ioCartes.observe(f); } });
  }
  if(!$(".flash", root)) boutonSon.classList.remove("vu");
  placerPastille(false);
  var t = R.getAttribute("data-theme");
  if(t !== theme){ theme = t; if(idees) idees.teintes(); }
  lecture();
}
new MutationObserver(function(){ if(!prevu){ prevu = true; requestAnimationFrame(balayer); } })
  .observe(root, {childList:true, subtree:true, attributes:true, attributeFilter:["class"]});
new MutationObserver(function(){ if(!prevu){ prevu = true; requestAnimationFrame(balayer); } })
  .observe(R, {attributes:true, attributeFilter:["data-theme"]});
if(document.fonts && document.fonts.ready) document.fonts.ready.then(function(){ placerPastille(true); });
balayer();
placerPastille(true);

window.MO = {son:son, feuilles:feuilles, onde:onde, ruban:ruban, envol:envol, estCalme:calme};
})();
