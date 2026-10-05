/* =====================================================================
   COUCHE DE MOUVEMENT — « chaque bonne réponse trace une route sur l'atlas »
   A. le frontispice vit : la carte se déplie depuis la rose des vents,
      l'aiguille cherche le nord puis suit la main, un navire fait le tour
      du monde d'escale en escale
   B. les planches se distribuent comme sur une table et s'inclinent
   C. changer de page : la nouvelle s'ouvre en cercle depuis le doigt
   D. un chapitre s'ouvre : code frappé comme un tampon, cartouche déplié
   E. onglets et barre latérale : des pastilles glissent
   F. figures qui se dessinent quand on les atteint, idées en cascade
   G. le quiz : étoiles de boussole, séries d'affilée, tampon final,
      cartes qui se retournent ; son de cloche coupable
   H. le voyage : un navire suit la lecture et jette l'ancre au bout
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
if(!calme()) R.classList.add("mo");
if(mq && mq.addEventListener){ mq.addEventListener("change", function(){ R.classList.toggle("mo", !calme()); }); }
var survol = window.matchMedia ? window.matchMedia("(hover: hover) and (pointer: fine)") : null;

var root = document.getElementById("root");
if(!root) return;
function FR(){ return !!document.querySelector(".lang-toggle.fr"); }
var OR = "#B08D4C", OR_C = "#E2C28A", HIST = "#A63D40", GEO = "#3E6259", ARDOISE = "#1B2A4A";
var NS = "http://www.w3.org/2000/svg";

/* ---------- outils ---------- */
function anim(el, kf, o){
  if(!el || !el.animate || calme()) return null;
  try{ return el.animate(kf, o); }catch(e){ return null; }
}
function centre(el){ var r = el.getBoundingClientRect(); return [r.left + r.width / 2, r.top + r.height / 2]; }
function svg(tag, attrs){ var e = document.createElementNS(NS, tag); for(var k in attrs) e.setAttribute(k, attrs[k]); return e; }
var RESSORT = "cubic-bezier(.2,.9,.3,1.15)", DOUX = "cubic-bezier(.2,.8,.2,1)";

/* ---------- révéler en arrivant : animations préparées en pause ---------- */
var attente = new Map();
var io = ("IntersectionObserver" in window) ? new IntersectionObserver(function(es){
  es.forEach(function(e){
    if(!e.isIntersecting) return;
    var l = attente.get(e.target);
    if(l){
      /* les délais servaient à l'entrée de page : au défilement, on part tout de suite
         en gardant l'échelonnement interne (traits d'une figure, lignes d'une planche) */
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
}, {rootMargin:"0px 0px -10% 0px"}) : null;
function bas(el){ return el.getBoundingClientRect().top > innerHeight * .9; }
/* si la cible est sous la ligne de flottaison, ses animations attendent en pause
   (leur première image tient l'état de départ) ; sinon elles partent tout de suite */
function differer(cible, anims){
  anims = anims.filter(Boolean);
  if(!anims.length) return;
  if(!io || !bas(cible)) return;
  anims.forEach(function(a){ a.pause(); });
  var deja = attente.get(cible);
  attente.set(cible, deja ? deja.concat(anims) : anims);
  io.observe(cible);
}
addEventListener("beforeprint", function(){
  attente.forEach(function(l){ l.forEach(function(a){ try{ a.finish(); }catch(x){} }); });
  attente.clear();
});

/* ---------- la couche des éclats ---------- */
var couche = document.createElement("div");
couche.id = "mo-couche"; couche.setAttribute("aria-hidden", "true");
document.body.appendChild(couche);
function ephemere(el, ms){ couche.appendChild(el); setTimeout(function(){ el.remove(); }, ms); return el; }
function astres(x, y, n, o){
  if(calme()) return;
  o = o || {};
  var c = o.couleurs || [OR, OR_C, GEO, ARDOISE, HIST], f = o.force || 1;
  for(var k = 0; k < n; k++){
    var p = document.createElement("i"), a = (o.angle != null ? o.angle : Math.random() * Math.PI * 2) + (o.angle != null ? (Math.random() - .5) * (o.ouverture || 1.6) : 0);
    var d = f * (50 + Math.random() * 90);
    p.className = "mo-astre";
    p.style.left = x + "px"; p.style.top = y + "px";
    p.style.setProperty("--c", c[k % c.length]);
    p.style.setProperty("--s", ((11 + Math.random() * 13) * (o.taille || 1)).toFixed(1) + "px");
    p.style.setProperty("--dx", (Math.cos(a) * d).toFixed(1) + "px");
    p.style.setProperty("--dy", (Math.sin(a) * d).toFixed(1) + "px");
    p.style.setProperty("--r", ((Math.random() - .5) * 400).toFixed(0) + "deg");
    p.style.setProperty("--g", (o.gravite != null ? o.gravite : 34) + "px");
    p.style.setProperty("--t", (o.duree || (.85 + Math.random() * .45)).toFixed(2) + "s");
    p.style.animationDelay = ((o.etale || 80) * Math.random() | 0) + "ms";
    ephemere(p, 1800);
  }
}
function onde(x, y, c, k){
  if(calme()) return;
  var o = document.createElement("i"); o.className = "mo-onde";
  o.style.left = x + "px"; o.style.top = y + "px";
  o.style.setProperty("--c", c || OR); o.style.setProperty("--k", k || 7);
  ephemere(o, 900);
}
function plus(x, y, txt, c){
  if(calme()) return;
  var o = document.createElement("span"); o.className = "mo-plus"; o.textContent = txt;
  o.style.left = x + "px"; o.style.top = y + "px"; o.style.setProperty("--c", c || GEO);
  ephemere(o, 1150);
}
function ruban(x, y, html){
  if(calme()) return;
  var o = document.createElement("span"); o.className = "mo-ruban"; o.innerHTML = html;
  o.style.left = Math.max(110, Math.min(innerWidth - 110, x)) + "px"; o.style.top = y + "px";
  ephemere(o, 2000);
}
function tampon(x, y, d, c){
  if(calme()) return;
  var o = document.createElement("i"); o.className = "mo-tampon";
  o.style.left = x + "px"; o.style.top = y + "px";
  o.style.setProperty("--d", (d || 90) + "px"); o.style.setProperty("--c", c || HIST);
  ephemere(o, 1000);
}

/* ---------- le son : une cloche de bord ---------- */
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
function cloche(f, dt, d, vol){
  var c = ctx(); if(!c) return;
  var t = c.currentTime + (dt || 0), g = c.createGain();
  g.gain.setValueAtTime(.0001, t);
  g.gain.exponentialRampToValueAtTime(vol || .09, t + .008);
  g.gain.exponentialRampToValueAtTime(.0001, t + d);
  g.connect(c.destination);
  /* fondamentale + partiels inharmoniques légers : un timbre de cloche */
  [[1, 1], [2.76, .22], [5.4, .07]].forEach(function(p){
    var o = c.createOscillator(), gg = c.createGain();
    o.type = "sine"; o.frequency.setValueAtTime(f * p[0], t);
    gg.gain.value = p[1];
    o.connect(gg); gg.connect(g); o.start(t); o.stop(t + d + .05);
  });
}
function grave(f, dt, d, vol){
  var c = ctx(); if(!c) return;
  var t = c.currentTime + (dt || 0), o = c.createOscillator(), g = c.createGain();
  o.type = "triangle"; o.frequency.setValueAtTime(f, t); o.frequency.exponentialRampToValueAtTime(f * .8, t + d);
  g.gain.setValueAtTime(.0001, t); g.gain.exponentialRampToValueAtTime(vol || .08, t + .01); g.gain.exponentialRampToValueAtTime(.0001, t + d);
  o.connect(g); g.connect(c.destination); o.start(t); o.stop(t + d + .05);
}
var GAMME = [523.25, 587.33, 659.25, 783.99, 880, 1046.5, 1174.66, 1318.51, 1567.98];
son.bon = function(k){ var i = Math.max(0, Math.min(k, GAMME.length - 2)); cloche(GAMME[i], 0, .9, .085); cloche(GAMME[i + 1], .07, 1, .06); };
son.faux = function(){ grave(196, 0, .32, .08); grave(174.6, .09, .36, .06); };
son.bilan = function(ok){ (ok ? [523.25, 659.25, 783.99, 1046.5, 1318.51] : [392, 493.88, 587.33]).forEach(function(f, i){ cloche(f, i * .11, 1.4, .07); }); };
son.ancre = function(){ cloche(392, 0, 1.6, .06); cloche(587.33, .14, 1.6, .045); };
son.carte = function(ok){ if(ok) cloche(880, 0, .6, .05); else grave(247, 0, .2, .05); };
var ICONE_SON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9h3l5-4v14l-5-4H4z"/><path class="ondes" d="M16 9.5a3.5 3.5 0 0 1 0 5M18.5 7a7 7 0 0 1 0 10"/><path class="barre" d="M16 9l5 6M21 9l-5 6"/></svg>';
function boutonSon(){
  var b = document.createElement("button");
  b.type = "button"; b.className = "mo-son";
  b.innerHTML = ICONE_SON;
  majBoutonSon(b);
  b.addEventListener("click", function(ev){
    ev.stopPropagation();
    son.actif = !son.actif;
    [].forEach.call(document.querySelectorAll(".mo-son"), majBoutonSon);
    if(son.actif) son.bon(2);
  });
  return b;
}
function majBoutonSon(b){
  b.setAttribute("aria-pressed", String(son.actif));
  var t = son.actif ? (FR() ? "Couper le son du quiz" : "Mute the quiz") : (FR() ? "Activer le son du quiz" : "Turn quiz sound on");
  b.title = t; b.setAttribute("aria-label", t);
}

/* ---------- C. changer de page dans une transition de vue ---------- */
var px = null, py = null, passe = false;
addEventListener("pointerdown", function(e){ px = e.clientX; py = e.clientY; }, {capture:true, passive:true});
var NAVIGUE = ".chap-btn, .brand, .tc-chap, .foot-btn, .chaplink, .pb-item, .ps-chip, .srch-row, .fiche-toggle";
document.addEventListener("click", function(ev){
  if(passe || calme() || !document.startViewTransition || !window.ReactDOM || !ReactDOM.flushSync) return;
  var t = ev.target.closest ? ev.target.closest(NAVIGUE) : null;
  if(!t || !root.contains(t) || t.disabled || t.classList.contains("disabled")) return;
  ev.preventDefault(); ev.stopImmediatePropagation();
  var r = t.getBoundingClientRect();
  R.style.setProperty("--vx", (px == null ? r.left + r.width / 2 : px) + "px");
  R.style.setProperty("--vy", (py == null ? r.top + r.height / 2 : py) + "px");
  try{
    document.startViewTransition(function(){
      passe = true;
      try{ ReactDOM.flushSync(function(){ t.click(); }); } finally { passe = false; }
      /* laisse passer l'effet du site qui remonte en haut de page */
      return new Promise(function(ok){ setTimeout(ok, 30); });
    });
  }catch(e){ passe = true; try{ t.click(); } finally { passe = false; } }
}, true);

/* ---------- A. le frontispice ---------- */
var accueilVu = false, rose = null, roseAngle = 0, roseVit = 0, roseCible = 0, roseAnim = 0, retourNord = 0;
/* projection de la carte du site : Web Mercator, x = 349 + 2·lon */
function proj(lon, lat){ return [349 + 2 * lon, 246.4 - 114.6 * Math.log(Math.tan(Math.PI / 4 + lat * Math.PI / 360))]; }
var ESCALES = [["Marseille", 5.37, 43.3], ["New York", -74, 40.7], ["Rio", -43.2, -22.9], ["Le Cap", 18.4, -33.9],
  ["Bombay", 72.9, 19.1], ["Singapour", 103.8, 1.35], ["Shanghai", 121.5, 31.2], ["Sydney", 151.2, -33.9]];
var voyageAccueil = null;
function entreeAccueil(home){
  var frontis = home.querySelector(".frontis");
  if(!frontis) return;
  var premiere = !accueilVu; accueilVu = true;
  rose = frontis.querySelector(".frontis-rose");
  var monde = frontis.querySelector(".frontis-world");
  var rc = rose ? rose.getBoundingClientRect() : null, fr = frontis.getBoundingClientRect();
  var cx = rc ? (rc.left + rc.width / 2 - fr.left) : fr.width / 2, cy = rc ? (rc.top + rc.height / 2 - fr.top) : fr.height / 2;

  /* la carte se déplie en cercle depuis la rose */
  if(monde && premiere){
    anim(monde, [{clipPath:"circle(0px at " + cx + "px " + cy + "px)"}, {clipPath:"circle(" + Math.hypot(fr.width, fr.height) + "px at " + cx + "px " + cy + "px)"}],
      {duration:1500, delay:100, easing:"cubic-bezier(.4,.05,.2,1)", fill:"backwards"});
    var anneau = document.createElement("i");
    anneau.setAttribute("aria-hidden", "true");
    anneau.style.cssText = "position:absolute;left:" + cx + "px;top:" + cy + "px;width:0;height:0;transform:translate(-50%,-50%);border-radius:50%;border:2px solid " + OR + ";box-shadow:0 0 18px rgba(176,141,76,.45),inset 0 0 18px rgba(176,141,76,.3);pointer-events:none;opacity:0";
    frontis.insertBefore(anneau, frontis.querySelector(".frontis-inner"));
    var D = Math.ceil(Math.hypot(fr.width, fr.height) * 2);
    var a = anim(anneau, [{opacity:.95, width:"0px", height:"0px"}, {opacity:.6, width:(D * .85) + "px", height:(D * .85) + "px", offset:.85}, {opacity:0, width:D + "px", height:D + "px"}],
      {duration:1500, delay:100, easing:"cubic-bezier(.4,.05,.2,1)"});
    if(a) a.onfinish = function(){ anneau.remove(); }; else anneau.remove();
  }
  /* l'aiguille cherche le nord */
  var aiguille = rose && rose.querySelector('path[d^="M50 4 L53 50"]');
  if(aiguille){
    anim(aiguille, [0, -62, 44, -27, 16, -9, 4, 0].map(function(d){ return {transform:"rotate(" + d + "deg)", transformOrigin:"50% 50%", transformBox:"fill-box"}; }),
      {duration:2400, delay:premiere ? 500 : 150, easing:"ease-in-out"});
  }
  /* le titre s'encre, le reste suit */
  var titre = frontis.querySelector(".frontis-title");
  anim(titre, [{clipPath:"inset(0 100% 0 0)", transform:"translateY(8px)"}, {clipPath:"inset(0 0 0 0)", transform:"none"}], {duration:900, delay:premiere ? 200 : 60, easing:DOUX, fill:"backwards"});
  [".frontis-kicker", ".frontis-sub", ".frontis-tools", ".frontis-progress"].forEach(function(s, i){
    anim(frontis.querySelector(s), [{opacity:0, transform:"translateY(14px)"}, {opacity:1, transform:"none"}], {duration:600, delay:(premiere ? 300 : 100) + i * 80, easing:DOUX, fill:"backwards"});
  });
  /* la progression se remplit, puis un reflet passe */
  var fill = frontis.querySelector(".fp-fill"), barre = frontis.querySelector(".fp-bar");
  anim(fill, [{transform:"scaleX(0)", transformOrigin:"0 50%"}, {transform:"scaleX(1)", transformOrigin:"0 50%"}], {duration:1200, delay:premiere ? 700 : 350, easing:"cubic-bezier(.3,1.2,.4,1)", fill:"backwards"});
  if(barre && !barre.querySelector(".mo-reflet") && !calme()){
    var reflet = document.createElement("i"); reflet.className = "mo-reflet"; reflet.setAttribute("aria-hidden", "true");
    barre.appendChild(reflet);
    anim(reflet, [{transform:"translateX(0)"}, {transform:"translateX(" + (barre.offsetWidth + 80) + "px)"}], {duration:1400, delay:2000, iterations:Infinity, easing:"ease-in-out", endDelay:1800});
  }
  /* les routes du tour du monde */
  if(monde && !frontis.querySelector(".mo-routes")) routes(frontis, monde, premiere ? 1400 : 400);
  /* B. les planches se distribuent */
  [].forEach.call(home.querySelectorAll(".subj-rule"), function(r, i){
    differer(r, [anim(r, [{transform:"scaleX(0)"}, {transform:"scaleX(1)"}], {duration:800, delay:(premiere ? 350 : 120) + (i % 2) * 100, easing:DOUX, fill:"backwards"})]);
  });
  [].forEach.call(home.querySelectorAll(".subj-title"), function(t){
    differer(t, [anim(t, [{opacity:0, transform:"scale(.85)", letterSpacing:".2em"}, {opacity:1, transform:"none", letterSpacing:"normal"}], {duration:800, delay:premiere ? 380 : 140, easing:DOUX, fill:"backwards"})]);
  });
  var cartes = [].slice.call(home.querySelectorAll(".theme-card"));
  cartes.forEach(function(c, i){
    var col = c.closest(".subj-col"), rang = col ? [].indexOf.call(col.querySelectorAll(".theme-card"), c) : i;
    var cote = (col && col.parentNode && col === col.parentNode.lastElementChild) ? 1 : -1;
    var a1 = anim(c, [{opacity:0, transform:"translate(" + (cote * 30) + "px,46px) rotate(" + (cote * 3.5) + "deg) scale(.93)"},
      {opacity:1, transform:"translate(0,-4px) rotate(" + (-cote * .4) + "deg) scale(1.01)", offset:.7}, {opacity:1, transform:"none"}],
      {duration:780, delay:(premiere ? 420 : 160) + rang * 100 + (cote > 0 ? 60 : 0), easing:DOUX, fill:"backwards"});
    var ico = c.querySelector(".plate-icon");
    var a2 = ico ? anim(ico, [{opacity:0, transform:"scale(.4) rotate(-30deg)", transformOrigin:"50% 50%", transformBox:"fill-box"}, {opacity:1, transform:"scale(1.15)", transformOrigin:"50% 50%", transformBox:"fill-box", offset:.7}, {opacity:1, transform:"none", transformOrigin:"50% 50%", transformBox:"fill-box"}],
      {duration:700, delay:(premiere ? 700 : 400) + rang * 100, easing:DOUX, fill:"backwards"}) : null;
    var lignes = [].map.call(c.querySelectorAll(".tc-chap"), function(l, j){
      return anim(l, [{opacity:0, transform:"translateX(-10px)"}, {opacity:1, transform:"none"}], {duration:450, delay:(premiere ? 650 : 350) + rang * 100 + j * 60, easing:DOUX, fill:"backwards"});
    });
    differer(c, [a1, a2].concat(lignes));
    inclinaison(c);
  });
  [].forEach.call(home.querySelectorAll(".pb-item"), function(p, i){
    differer(p, [anim(p, [{opacity:0, transform:"translateY(16px) scale(.96)"}, {opacity:1, transform:"none"}], {duration:600, delay:200 + (i % 8) * 60, easing:DOUX, fill:"backwards"})]);
  });
  /* la rose suit la main */
  if(rose && !frontis._mo){
    frontis._mo = true;
    frontis.addEventListener("pointermove", function(e){ if(e.pointerType === "mouse") viser(e.clientX, e.clientY); });
    frontis.addEventListener("pointerleave", function(e){ if(e.pointerType === "mouse"){ roseCible = 0; elancer(); } });
    frontis.addEventListener("pointerdown", function(e){
      if(e.pointerType === "mouse") return;
      viser(e.clientX, e.clientY);
      clearTimeout(retourNord);
      retourNord = setTimeout(function(){ roseCible = 0; elancer(); }, 1600);
    });
  }
}
function viser(x, y){
  if(!rose || calme()) return;
  var r = rose.getBoundingClientRect(), dx = x - (r.left + r.width / 2), dy = y - (r.top + r.height / 2);
  if(Math.hypot(dx, dy) < 12) return;
  var cible = Math.atan2(dx, -dy) * 180 / Math.PI;
  /* chemin le plus court vers la cible */
  while(cible - roseAngle > 180) cible -= 360;
  while(cible - roseAngle < -180) cible += 360;
  roseCible = cible;
  elancer();
}
function elancer(){ if(!roseAnim) roseAnim = requestAnimationFrame(ressort); }
function ressort(){
  roseAnim = 0;
  if(!rose || !rose.isConnected) return;
  /* un ressort amorti : la rose dépasse un peu sa cible, comme une vraie aiguille */
  roseVit = (roseVit + (roseCible - roseAngle) * .075) * .84;
  roseAngle += roseVit;
  rose.style.transform = "rotate(" + roseAngle.toFixed(2) + "deg)";
  if(Math.abs(roseVit) > .02 || Math.abs(roseCible - roseAngle) > .05) roseAnim = requestAnimationFrame(ressort);
  else if(roseCible === 0){ roseAngle = 0; rose.style.transform = ""; }
}

function routes(frontis, monde, delai){
  var vb = monde.getAttribute("viewBox") || "0 0 740 400";
  var s = svg("svg", {"class":"mo-routes", viewBox:vb, preserveAspectRatio:"xMidYMid slice", "aria-hidden":"true"});
  var traits = [], ports = [];
  for(var i = 0; i < ESCALES.length; i++){
    var a = proj(ESCALES[i][1], ESCALES[i][2]);
    if(i < ESCALES.length - 1){
      var b = proj(ESCALES[i + 1][1], ESCALES[i + 1][2]);
      var mx = (a[0] + b[0]) / 2, my = (a[1] + b[1]) / 2, dist = Math.hypot(b[0] - a[0], b[1] - a[1]);
      var t = svg("path", {"class":"r-trait", d:"M" + a[0].toFixed(1) + "," + a[1].toFixed(1) + " Q" + mx.toFixed(1) + "," + (my - dist * .28).toFixed(1) + " " + b[0].toFixed(1) + "," + b[1].toFixed(1)});
      t.style.opacity = "0";
      s.appendChild(t); traits.push(t);
    }
    var p = svg("circle", {"class":"r-port", cx:a[0].toFixed(1), cy:a[1].toFixed(1), r:"2.6"});
    s.appendChild(p); ports.push(p);
  }
  var nef = svg("g", {"class":"r-nef"});
  nef.appendChild(svg("circle", {r:"7", fill:"#FBF8F0", stroke:"#B08D4C", "stroke-width":"1"}));
  nef.appendChild(svg("path", {d:"M-4.2,-2.4 L4.8,0 L-4.2,2.4 L-2.2,0 Z", fill:"#1B2A4A"}));
  nef.style.opacity = "0";
  s.appendChild(nef);
  frontis.insertBefore(s, monde.nextSibling);
  if(calme()){ traits.forEach(function(t){ t.style.opacity = ".45"; }); return; }
  ports.forEach(function(p, i){ anim(p, [{opacity:0, transform:"scale(0)", transformOrigin:"50% 50%", transformBox:"fill-box"}, {opacity:1, transform:"none", transformOrigin:"50% 50%", transformBox:"fill-box"}], {duration:500, delay:delai + i * 90, easing:RESSORT, fill:"backwards"}); });
  /* le navire fait escale après escale ; la boucle s'arrête quand l'accueil disparaît */
  var etape = 0, debut = 0, DUREE = 2300, PAUSE = 450, encours = true;
  voyageAccueil = function(){ encours = false; };
  function longueur(t){ try{ return t.getTotalLength(); }catch(e){ return 0; } }
  function boucle(ts){
    if(!encours || !s.isConnected){ voyageAccueil = null; return; }
    if(document.hidden){ requestAnimationFrame(boucle); return; }
    if(!debut) debut = ts;
    var t = traits[etape], L = longueur(t), u = Math.min(1, (ts - debut) / DUREE);
    var e = u < .5 ? 2 * u * u : 1 - Math.pow(-2 * u + 2, 2) / 2;
    t.style.opacity = "1";
    t.style.strokeDashoffset = String(-ts / 60);
    var p = t.getPointAtLength(L * e), q = t.getPointAtLength(Math.min(L, L * e + 1.5));
    var ang = Math.atan2(q.y - p.y, q.x - p.x) * 180 / Math.PI;
    nef.style.opacity = "1";
    nef.setAttribute("transform", "translate(" + p.x.toFixed(2) + "," + p.y.toFixed(2) + ") rotate(" + ang.toFixed(1) + ")");
    if(ts - debut > DUREE + PAUSE){
      t.style.opacity = ".4";
      anim(ports[etape + 1], [{transform:"scale(1)", transformOrigin:"50% 50%", transformBox:"fill-box"}, {transform:"scale(2.6)", transformOrigin:"50% 50%", transformBox:"fill-box"}, {transform:"scale(1)", transformOrigin:"50% 50%", transformBox:"fill-box"}], {duration:600, easing:"ease-out"});
      etape++; debut = ts;
      if(etape >= traits.length){
        etape = 0;
        traits.forEach(function(x){ anim(x, [{opacity:.4}, {opacity:0}], {duration:900, fill:"forwards"}); });
      }
    }
    requestAnimationFrame(boucle);
  }
  setTimeout(function(){ requestAnimationFrame(boucle); }, delai + 400);
}

/* B. inclinaison des planches au survol */
function inclinaison(c){
  if(c._mo || !survol || !survol.matches) return;
  c._mo = true;
  c.addEventListener("pointermove", function(e){
    if(calme()) return;
    var r = c.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
    c.style.transition = "transform .12s ease-out, box-shadow .3s ease";
    c.style.transform = "rotateX(" + (-y * 7).toFixed(2) + "deg) rotateY(" + (x * 9).toFixed(2) + "deg) translateY(-4px)";
    c.style.boxShadow = (-x * 14).toFixed(1) + "px " + (14 - y * 8).toFixed(1) + "px 34px rgba(27,42,74,.16)";
  });
  c.addEventListener("pointerleave", function(){
    c.style.transition = "transform .6s cubic-bezier(.2,.9,.3,1.2), box-shadow .6s ease";
    c.style.transform = ""; c.style.boxShadow = "";
  });
}

/* ---------- D. un chapitre s'ouvre ---------- */
var chapVu = null;
function entreeChapitre(cr){
  var code = cr.querySelector(".hero-code"), cart = cr.querySelector(".hero-cartouche"), ico = cr.querySelector(".hero-icon"),
      titre = cr.querySelector(".hero-title"), theme = cr.querySelector(".hero-theme");
  anim(cart, [{clipPath:"inset(0 50% 0 50%)", opacity:.3}, {clipPath:"inset(0 0 0 0)", opacity:1}], {duration:750, delay:40, easing:"cubic-bezier(.6,0,.2,1)", fill:"backwards"});
  if(code){
    anim(code, [{opacity:0, transform:"scale(2.8) rotate(-18deg)"}, {opacity:1, transform:"scale(.9) rotate(3deg)", offset:.55}, {opacity:1, transform:"none"}], {duration:600, delay:420, easing:"cubic-bezier(.5,0,.3,1)", fill:"backwards"});
    setTimeout(function(){
      if(!code.isConnected || calme()) return;
      var xy = centre(code), c = code.classList.contains("geo") ? GEO : code.classList.contains("hist") ? HIST : ARDOISE;
      tampon(xy[0], xy[1], 70, c);
      astres(xy[0], xy[1], 12, {force:.7, couleurs:[c, OR, OR_C], taille:.7, gravite:20});
    }, 760);
  }
  anim(theme, [{opacity:0, transform:"translateX(-12px)"}, {opacity:1, transform:"none"}], {duration:600, delay:620, easing:DOUX, fill:"backwards"});
  anim(ico, [{opacity:0, transform:"rotate(-220deg) scale(.3)"}, {opacity:1, transform:"rotate(12deg) scale(1.1)", offset:.75}, {opacity:1, transform:"none"}], {duration:900, delay:380, easing:DOUX, fill:"backwards"});
  anim(titre, [{clipPath:"inset(0 100% 0 0)", transform:"translateX(-10px)"}, {clipPath:"inset(0 0 0 0)", transform:"none"}], {duration:950, delay:450, easing:DOUX, fill:"backwards"});
  [].forEach.call(cr.querySelectorAll(".prem-strip > *"), function(p, i){
    anim(p, [{opacity:0, transform:"translateY(10px) scale(.95)"}, {opacity:1, transform:"none"}], {duration:500, delay:560 + i * 70, easing:RESSORT, fill:"backwards"});
  });
  [].forEach.call(cr.querySelectorAll(".chap-tab"), function(t, i){
    anim(t, [{opacity:0, transform:"translateY(12px) scale(.9)"}, {opacity:1, transform:"none"}], {duration:520, delay:620 + i * 50, easing:RESSORT, fill:"backwards"});
  });
  /* la pastille et la route n'arrivent qu'avec les onglets */
  anim(cr.querySelector(".mo-pastille-onglet"), [{opacity:0}, {opacity:1}], {duration:300, delay:640, fill:"backwards"});
  anim(voyage, [{opacity:0}, {opacity:1}], {duration:500, delay:900, fill:"backwards"});
  cascade(cr.querySelector(".tab-body"), 760);
}
/* les premiers blocs d'un contenu arrivent l'un après l'autre */
function cascade(corps, delai, sens){
  if(!corps) return;
  /* on descend les enveloppes à enfant unique pour animer les vrais blocs, une seule fois chacun */
  var el = corps;
  while(el.children.length === 1 && el.firstElementChild.children.length) el = el.firstElementChild;
  var blocs = [].slice.call(el.children).filter(function(b){ return b.offsetParent !== null; }).slice(0, 10);
  blocs.forEach(function(b, i){
    var a = anim(b, [{opacity:0, transform:sens ? "translateX(" + (sens * 34) + "px)" : "translateY(22px)"}, {opacity:1, transform:"none"}],
      {duration:sens ? 420 : 600, delay:(delai || 0) + i * (sens ? 35 : 70), easing:DOUX, fill:"backwards"});
    differer(b, [a]);
  });
}

/* ---------- E. pastilles : barre latérale et onglets ---------- */
function pastille(conteneur, actif, classe, sansAnim){
  var p = conteneur.querySelector(":scope > ." + classe);
  if(!p){
    p = document.createElement("span"); p.className = classe; p.setAttribute("aria-hidden", "true");
    conteneur.insertBefore(p, conteneur.firstChild);
    conteneur.classList.add("mo-a-pastille");
    sansAnim = true;
  }
  if(!actif){ p.style.opacity = "0"; return; }
  if(sansAnim) p.style.transition = "none";
  p.style.width = actif.offsetWidth + "px";
  p.style.height = actif.offsetHeight + "px";
  p.style.transform = "translate(" + actif.offsetLeft + "px," + actif.offsetTop + "px)";
  p.style.opacity = "1";
  if(sansAnim){ void p.offsetWidth; p.style.transition = ""; }
}
var navActif = null, ongletActif = null;
function pastilles(force){
  var nav = root.querySelector(".nav");
  if(nav){
    var a = nav.querySelector(".chap-btn.active");
    if(a !== navActif || force){ pastille(nav, a, "mo-pastille-nav", force || !navActif); navActif = a; }
  }
  var tabs = root.querySelector(".chap-tabs");
  if(tabs){
    var o = tabs.querySelector(".chap-tab.on");
    if(o !== ongletActif || force){ pastille(tabs, o, "mo-pastille-onglet", force || !ongletActif); ongletActif = o; }
  } else ongletActif = null;
}

/* changer d'onglet : le contenu glisse dans le sens du geste */
var ongletAvant = -1;
document.addEventListener("click", function(ev){
  var t = ev.target.closest ? ev.target.closest(".chap-tab") : null;
  if(!t || !root.contains(t)) return;
  var tous = [].slice.call(root.querySelectorAll(".chap-tab")), i = tous.indexOf(t);
  var av = tous.indexOf(root.querySelector(".chap-tab.on"));
  if(i === av) return;
  requestAnimationFrame(function(){ requestAnimationFrame(function(){
    cascade(root.querySelector(".tab-body"), 0, i > av ? 1 : -1);
    pastilles();
  }); });
});
/* déplier une partie : ses idées tombent en cascade */
document.addEventListener("click", function(ev){
  var h = ev.target.closest ? ev.target.closest(".fold-head") : null;
  if(!h || !root.contains(h)) return;
  var sec = h.closest(".section");
  requestAnimationFrame(function(){ requestAnimationFrame(function(){
    if(!sec || !sec.classList.contains("open")) return;
    var corps = sec.querySelector(".fold-body");
    if(!corps) return;
    [].slice.call(corps.querySelectorAll(".idea")).slice(0, 12).forEach(function(id, i){
      anim(id, [{opacity:0, transform:"translateY(18px)"}, {opacity:1, transform:"none"}], {duration:520, delay:i * 65, easing:DOUX, fill:"backwards"});
      anim(id.querySelector(".idea-marker"), [{opacity:0, transform:"scale(.3) rotate(-40deg)"}, {opacity:1, transform:"scale(1.3)", offset:.6}, {opacity:1, transform:"none"}], {duration:600, delay:i * 65 + 120, easing:DOUX, fill:"backwards"});
    });
  }); });
});
/* changer de matière : la liste se recompose */
document.addEventListener("click", function(ev){
  var t = ev.target.closest ? ev.target.closest(".subj-tab") : null;
  if(!t || !root.contains(t) || t.classList.contains("active")) return;
  requestAnimationFrame(function(){ requestAnimationFrame(function(){
    var nav = root.querySelector(".nav"); if(!nav) return;
    [].slice.call(nav.children).filter(function(e){ return !e.classList.contains("mo-pastille-nav"); }).forEach(function(g, i){
      anim(g, [{opacity:0, transform:"translateX(-18px)"}, {opacity:1, transform:"none"}], {duration:480, delay:i * 60, easing:DOUX, fill:"backwards"});
    });
    pastilles(true);
  }); });
});

/* ---------- F. les figures se dessinent ---------- */
var figures = new WeakSet();
var TRACABLES = "path,line,polyline,polygon,circle,ellipse,rect";
function figure(s){
  if(figures.has(s)) return;
  figures.add(s);
  if(calme() || s.closest(".quiz-tab") || s.querySelector("button, input")) return;
  var corps = s.querySelector(".schema-body") || s;
  var dessin = corps.querySelector("svg");
  var anims = [];
  if(dessin){
    var traits = [].slice.call(dessin.querySelectorAll(TRACABLES));
    if(traits.length && traits.length <= 260){
      traits.forEach(function(t, i){
        var cs = getComputedStyle(t), L = 0;
        try{ L = t.getTotalLength(); }catch(e){}
        var trait = cs.stroke && cs.stroke !== "none" && parseFloat(cs.strokeWidth) > 0;
        var d = 120 + Math.min(i, 120) * 9;
        if(trait && L > 2){
          anims.push(anim(t, [{strokeDasharray:L + " " + L, strokeDashoffset:L, fillOpacity:0}, {strokeDasharray:L + " " + L, strokeDashoffset:0, fillOpacity:0, offset:.7}, {strokeDasharray:L + " " + L, strokeDashoffset:0, fillOpacity:cs.fillOpacity}],
            {duration:Math.min(1600, 500 + L * 2), delay:d, easing:"cubic-bezier(.4,.1,.3,1)", fill:"backwards"}));
        } else {
          anims.push(anim(t, [{opacity:0}, {opacity:cs.opacity}], {duration:600, delay:d + 200, fill:"backwards"}));
        }
      });
      [].forEach.call(dessin.querySelectorAll("text"), function(t, i){
        anims.push(anim(t, [{opacity:0, transform:"translateY(4px)"}, {opacity:1, transform:"none"}], {duration:500, delay:700 + Math.min(i, 30) * 25, fill:"backwards"}));
      });
    } else {
      /* carte trop dense pour être tracée : elle se dévoile depuis le centre */
      anims.push(anim(dessin, [{clipPath:"circle(0% at 50% 50%)"}, {clipPath:"circle(75% at 50% 50%)"}], {duration:1300, delay:100, easing:"cubic-bezier(.4,.05,.2,1)", fill:"backwards"}));
    }
  } else {
    /* schéma en blocs : chaque étape arrive à son tour, les flèches poussent */
    var etapes = corps.querySelectorAll(".flow-step");
    var blocs = etapes.length ? [].slice.call(etapes) : (function(){
      var meilleur = null, n = 2;
      [].forEach.call(corps.querySelectorAll("div"), function(d){ if(d.children.length > n && d.children.length <= 14){ meilleur = d; n = d.children.length; } });
      return meilleur ? [].slice.call(meilleur.children) : [];
    })();
    blocs.forEach(function(b, i){
      anims.push(anim(b, [{opacity:0, transform:"translateY(16px) scale(.96)"}, {opacity:1, transform:"none"}], {duration:560, delay:100 + i * 140, easing:RESSORT, fill:"backwards"}));
      var fl = b.querySelector(".flow-arrow");
      if(fl) anims.push(anim(fl, [{transform:"scaleY(0)", transformOrigin:"50% 0"}, {transform:"scaleY(1)", transformOrigin:"50% 0"}], {duration:400, delay:260 + i * 140, easing:DOUX, fill:"backwards"}));
    });
  }
  anims.push(anim(s.querySelector(".fig"), [{opacity:0, transform:"scale(.5)"}, {opacity:1, transform:"scale(1.25)", offset:.6}, {opacity:1, transform:"none"}], {duration:600, delay:60, fill:"backwards"}));
  differer(s, anims);
}

/* ---------- G. le quiz ---------- */
var serie = 0;
var PALIERS = {3:1, 5:1, 8:1, 12:1, 20:1, 30:1};
function estOption(b){ var f = b.firstElementChild; return f && f.tagName === "B" && /^[ABCD]$/.test(f.textContent.trim()); }
function fondDe(el){ return getComputedStyle(el).backgroundColor.replace(/\s/g, ""); }
document.addEventListener("click", function(ev){
  var b = ev.target.closest ? ev.target.closest(".quiz-tab button") : null;
  if(!b || b.classList.contains("mo-son")) return;
  var qt = b.closest(".quiz-tab"), txt = b.textContent.trim();
  if(estOption(b) && !b.disabled){
    var xy = centre(b);
    requestAnimationFrame(function(){ requestAnimationFrame(function(){ verdict(b, xy, qt); }); });
    return;
  }
  if(/^(Next question|Question suivante)/.test(txt)){
    requestAnimationFrame(function(){ requestAnimationFrame(function(){ nouvelleQuestion(qt); }); });
    return;
  }
  if(/Start again|Recommencer|Tout reprendre|Start the deck|Revoir seulement|Review only/.test(txt) || b.style.borderRadius === "14px"){
    serie = 0;
    requestAnimationFrame(function(){ requestAnimationFrame(function(){ nouvelleQuestion(qt); }); });
  }
  /* cartes : « je savais » / « à revoir » */
  if(/I knew it|Je savais/.test(txt) || /Again|À revoir/.test(txt) && /✗/.test(txt)){
    var ok = /I knew it|Je savais/.test(txt), c = carteDe(qt), xy2 = centre(b);
    if(ok){ astres(xy2[0], xy2[1], 10, {force:.6, couleurs:[GEO, OR, OR_C], taille:.6}); }
    son.carte(ok);
    requestAnimationFrame(function(){ requestAnimationFrame(function(){
      var c2 = carteDe(qt);
      anim(c2, [{opacity:0, transform:"translateX(" + (ok ? 70 : -70) + "px) rotate(" + (ok ? 6 : -6) + "deg)"}, {opacity:1, transform:"none"}], {duration:480, easing:RESSORT});
    }); });
  }
});
function carteDe(qt){
  if(!qt) return null;
  var l = qt.querySelectorAll("div");
  for(var i = 0; i < l.length; i++){ if(l[i].style.minHeight === "150px") return l[i]; }
  return null;
}
/* retourner une carte */
document.addEventListener("click", function(ev){
  var qt = ev.target.closest ? ev.target.closest(".quiz-tab") : null;
  if(!qt) return;
  var c = carteDe(qt);
  if(!c || !c.contains(ev.target)) return;
  requestAnimationFrame(function(){
    anim(c, [{transform:"perspective(900px) rotateY(-90deg)", opacity:.4}, {transform:"perspective(900px) rotateY(8deg)", opacity:1, offset:.7}, {transform:"none", opacity:1}], {duration:520, easing:"cubic-bezier(.3,.7,.3,1.1)"});
  });
});
function verdict(b, xy, qt){
  if(!b.isConnected) return;
  var bon = fondDe(b) === "rgb(228,238,223)";
  var score = scoreDe(qt);
  if(bon){
    serie++;
    anim(b, [{transform:"scale(1)"}, {transform:"scale(1.035)", boxShadow:"0 0 0 4px rgba(62,98,89,.25)"}, {transform:"scale(1)"}], {duration:520, easing:"ease-out"});
    onde(xy[0], xy[1], GEO, 9);
    astres(xy[0], xy[1], 22 + Math.min(serie, 10) * 3, {force:1.15 + Math.min(serie, 8) * .08, couleurs:[OR, OR_C, GEO, ARDOISE, OR]});
    plus(xy[0] + b.offsetWidth * .32, xy[1] - 6, "+1", GEO);
    son.bon(serie - 1);
    if(score) anim(score, [{transform:"scale(1)", color:"inherit"}, {transform:"scale(1.35)", color:GEO}, {transform:"scale(1)", color:"inherit"}], {duration:600, easing:"ease-out"});
    if(PALIERS[serie]){
      var r = qt.getBoundingClientRect();
      setTimeout(function(){
        ruban(r.left + r.width / 2, Math.max(70, r.top + 40), "<b>" + serie + "</b>" + (FR() ? " d’affilée — cap tenu !" : " in a row — steady course!"));
        astres(r.left + r.width / 2, Math.max(70, r.top + 40), 26, {force:1.3});
      }, 260);
    }
  } else {
    serie = 0;
    anim(b, [0, -9, 8, -6, 5, -3, 0].map(function(x){ return {transform:"translateX(" + x + "px)"}; }), {duration:480, easing:"ease-in-out"});
    son.faux();
    var juste = [].filter.call(qt.querySelectorAll("button"), function(o){ return estOption(o) && fondDe(o) === "rgb(228,238,223)"; })[0];
    if(juste) anim(juste, [{boxShadow:"0 0 0 0 rgba(62,98,89,0)"}, {boxShadow:"0 0 0 6px rgba(62,98,89,.28)"}, {boxShadow:"0 0 0 0 rgba(62,98,89,0)"}], {duration:900, delay:250, iterations:2, easing:"ease-in-out"});
  }
}
function scoreDe(qt){
  if(!qt) return null;
  var s = [].filter.call(qt.querySelectorAll("span"), function(x){ return /^(Score|Score :)/.test(x.textContent.trim()); });
  return s[0] || null;
}
function nouvelleQuestion(qt){
  if(!qt) return;
  var opts = [].filter.call(qt.querySelectorAll("button"), estOption);
  if(!opts.length) return;
  var q = opts[0].previousElementSibling;
  anim(q, [{opacity:0, transform:"translateX(30px)"}, {opacity:1, transform:"none"}], {duration:420, easing:DOUX});
  opts.forEach(function(o, i){ anim(o, [{opacity:0, transform:"translateX(40px)"}, {opacity:1, transform:"none"}], {duration:440, delay:60 + i * 55, easing:DOUX, fill:"backwards"}); });
}
var bilans = new WeakSet();
function bilan(qt){
  var cand = [].filter.call(qt.querySelectorAll("div"), function(d){ return /^\s*\d+\s*\/\s*\d+\s*$/.test(d.textContent) && d.children.length === 0 && parseFloat(getComputedStyle(d).fontSize) >= 28; })[0];
  if(!cand || bilans.has(cand)) return;
  bilans.add(cand);
  var m = cand.textContent.match(/(\d+)\s*\/\s*(\d+)/), a = +m[1], n = +m[2], parfait = n > 0 && a === n, bien = n > 0 && a / n >= .7;
  anim(cand, [{opacity:0, transform:"scale(2.6) rotate(-12deg)"}, {opacity:1, transform:"scale(.92) rotate(2deg)", offset:.55}, {opacity:1, transform:"none"}], {duration:700, delay:80, easing:"cubic-bezier(.5,0,.3,1)", fill:"backwards"});
  setTimeout(function(){
    if(!cand.isConnected) return;
    var xy = centre(cand);
    tampon(xy[0], xy[1], parfait ? 140 : 100, parfait ? GEO : bien ? OR : HIST);
    if(parfait){
      astres(xy[0], xy[1], 46, {force:1.8, taille:1.2, gravite:60, duree:1.4});
      setTimeout(function(){ astres(xy[0] - 120, xy[1] + 20, 20, {force:1.2}); astres(xy[0] + 120, xy[1] + 20, 20, {force:1.2}); }, 280);
      ruban(xy[0], xy[1] - 60, "<b>✓</b>" + (FR() ? "Sans faute — l’atlas est à toi." : "Flawless — the atlas is yours."));
    } else if(bien){
      astres(xy[0], xy[1], 22, {force:1.2});
    }
    son.bilan(bien);
  }, 520);
}

/* ---------- H. le voyage de lecture ---------- */
var voyage = document.createElement("div");
voyage.id = "mo-voyage"; voyage.setAttribute("aria-hidden", "true");
voyage.innerHTML = '<i class="v-route"></i><i class="v-fait"></i>'
  + '<svg class="v-port" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="5" r="2"/><path d="M12 7v13M6 12H3a9 9 0 0 0 18 0h-3"/></svg>'
  + '<span class="v-nef"><svg viewBox="0 0 24 24"><path d="M12 3v12" stroke="currentColor" stroke-width="1.4"/><path d="M12 4l6 9h-6z" fill="currentColor" opacity=".85"/><path d="M11 6L6.5 13H11z" fill="#B08D4C"/><path d="M4 16h16l-2.5 3.5h-11z" fill="currentColor"/></svg></span>';
document.body.appendChild(voyage);
var ancre = false, tick = false;
function lecture(){
  tick = false;
  var cr = root.querySelector(".chap-root");
  var h = R.scrollHeight - innerHeight;
  if(!cr || h < 500){ voyage.classList.remove("on"); return; }
  var tabs = root.querySelector(".chap-tabs"), barre = root.querySelector(".mobile-bar");
  var haut = 0;
  if(barre && barre.offsetParent !== null) haut = barre.getBoundingClientRect().bottom;
  if(tabs){ var tb = tabs.getBoundingClientRect().bottom; if(tb > haut) haut = tb; }
  var c = cr.getBoundingClientRect();
  var p = Math.max(0, Math.min(1, scrollY / h));
  voyage.style.setProperty("--g", c.left + "px");
  voyage.style.setProperty("--l", c.width + "px");
  voyage.style.setProperty("--h", haut + "px");
  voyage.style.setProperty("--p", p.toFixed(4));
  voyage.classList.add("on");
  if(!ancre && p > .993){
    ancre = true;
    voyage.classList.remove("fin"); void voyage.offsetWidth; voyage.classList.add("fin");
    var port = voyage.querySelector(".v-port").getBoundingClientRect();
    astres(port.left + 8, port.top + 8, 18, {force:.9, angle:Math.PI / 2, ouverture:2.6});
    son.ancre();
  }
  if(p < .9) ancre = false;
}
addEventListener("scroll", function(){ if(!tick){ tick = true; requestAnimationFrame(lecture); } }, {passive:true});
addEventListener("resize", function(){ pastilles(true); lecture(); });

/* ---------- l'observateur : chaque nouveauté rendue par React ---------- */
var prevu = false;
function balayer(){
  prevu = false;
  /* ce qui attendait d'être vu mais a quitté la page : on libère */
  attente.forEach(function(l, el){ if(!el.isConnected){ l.forEach(function(x){ try{ x.cancel(); }catch(e){} }); attente.delete(el); if(io) io.unobserve(el); } });
  var home = root.querySelector(".home");
  if(home && !home._moVu){ home._moVu = true; entreeAccueil(home); }
  if(!home && voyageAccueil) voyageAccueil();
  /* un chapitre se reconnaît à son code (H1, G2…) : changer de langue ne le rejoue pas */
  var cr = root.querySelector(".chap-root");
  if(cr){
    var cle = cr.querySelector(".hero-code"), cleTxt = cle ? cle.textContent.trim() : (cr.querySelector(".hero-title") || {}).textContent;
    if(cr !== chapVu || cr._moCle !== cleTxt){
      chapVu = cr; cr._moCle = cleTxt;
      pastilles();
      if(!calme()) entreeChapitre(cr);
      ancre = false;
    }
  } else chapVu = null;
  pastilles();
  [].forEach.call(root.querySelectorAll(".schema"), figure);
  [].forEach.call(root.querySelectorAll(".quiz-tab"), function(qt){
    var cap = qt.querySelector(".schema-cap");
    if(cap && !cap.querySelector(".mo-son")) cap.appendChild(boutonSon());
    bilan(qt);
  });
  var panneau = document.querySelector(".srch-panel");
  if(panneau && !panneau._moVu){
    panneau._moVu = true;
    anim(panneau, [{opacity:0, transform:"translateY(-26px) scale(.95)"}, {opacity:1, transform:"translateY(3px) scale(1.005)", offset:.7}, {opacity:1, transform:"none"}], {duration:420, easing:DOUX});
  }
  pastilles();
  lecture();
}
new MutationObserver(function(){ if(!prevu){ prevu = true; requestAnimationFrame(balayer); } })
  .observe(root, {childList:true, subtree:true, attributes:true, attributeFilter:["class"]});
if(document.fonts && document.fonts.ready) document.fonts.ready.then(function(){ pastilles(true); });
balayer();

window.MO = {son:son, astres:astres, onde:onde, ruban:ruban, tampon:tampon, estCalme:calme};
})();
