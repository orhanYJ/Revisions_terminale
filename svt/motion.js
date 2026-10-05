/* =====================================================================
   COMPLÉMENT DE MOUVEMENT — « tout ce qu'on fait fait pousser quelque chose »
   S'ajoute aux couches écrites dans la page, dont il réutilise les outils
   (window.MO : son, gerbe, centre) :
   A. l'accueil devient un jardin : pollen qui monte, feuilles qui
      tombent, la main fait du vent et la plante du programme s'y penche
   B. chaque chapitre porte une double hélice d'ADN qui tourne, se tord
      au défilement et, touchée, se désapparie puis se réapparie
   C. encadrés, définitions, pièges, schémas poussent en arrivant
   D. les schémas invitent au toucher ; chaque étape fait éclore une lueur
   E. le QCM : éclat de soleil à 5 d'affilée, pluie de feuilles à 10,
      pluie de pétales pour un sans-faute
   Le script observe la vue que la page reconstruit à chaque navigation :
   aucune fonction du site n'est réécrite. Aucune persistance.
   ===================================================================== */
(function(){
"use strict";
var R = document.documentElement;
var mq = window.matchMedia ? window.matchMedia("(prefers-reduced-motion: reduce)") : null;
function calme(){ return !!(mq && mq.matches); }
var MO = window.MO || {};
var vue = document.getElementById("view");
if(!vue) return;
function anim(el, kf, o){ if(!el || !el.animate || calme()) return null; try{ return el.animate(kf, o); }catch(e){ return null; } }
function gerbe(x, y, n, o){ if(MO.gerbe && !calme()) MO.gerbe(x, y, n, o); }
var DOUX = "cubic-bezier(.2,.8,.2,1)";

/* la palette du site, relue quand le thème change */
var PAL = {};
function palette(){
  var cs = getComputedStyle(R);
  ["--leaf", "--leaf-2", "--leaf-3", "--lime", "--water", "--clay", "--plum", "--bark", "--ink", "--paper", "--rose", "--amber", "--violet"].forEach(function(k){
    PAL[k] = (cs.getPropertyValue(k) || "").trim();
  });
  PAL.sombre = R.getAttribute("data-theme") === "dark";
}
palette();
new MutationObserver(palette).observe(R, {attributes:true, attributeFilter:["data-theme"]});
function rgba(hex, a){
  var h = (hex || "#2F7D52").replace("#", "");
  if(h.length === 3) h = h.replace(/./g, "$&$&");
  var n = parseInt(h, 16);
  return "rgba(" + (n >> 16 & 255) + "," + (n >> 8 & 255) + "," + (n & 255) + "," + a + ")";
}

/* place un canevas exactement sur un élément, quel que soit son bloc conteneur */
function poser(cv, cible, debord){
  debord = debord || 0;
  var dpr = Math.min(2, window.devicePixelRatio || 1);
  var W = cible.offsetWidth + 2 * debord, H = cible.offsetHeight + 2 * debord;
  cv.style.left = "0px"; cv.style.top = "0px";
  var o = cv.getBoundingClientRect(), r = cible.getBoundingClientRect();
  cv.style.left = (r.left - o.left - debord) + "px"; cv.style.top = (r.top - o.top - debord) + "px";
  cv.style.width = W + "px"; cv.style.height = H + "px";
  cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr);
  cv.getContext("2d").setTransform(dpr, 0, 0, dpr, 0, 0);
  return {W:W, H:H};
}
/* une boucle d'image par canevas, suspendue hors écran ou onglet caché */
function boucle(cv, dessin){
  var visible = true, prevu = false;
  if("IntersectionObserver" in window) new IntersectionObserver(function(es){ visible = es[0].isIntersecting; if(visible) relance(); }).observe(cv);
  function relance(){ if(!prevu){ prevu = true; requestAnimationFrame(image); } }
  function image(t){
    prevu = false;
    if(!cv.isConnected || calme()) return;
    if(!visible || document.hidden){ setTimeout(relance, 400); return; }
    dessin(t);
    relance();
  }
  relance();
}

/* ---------- A. le jardin de l'accueil ---------- */
var vent = 0, ventCible = 0;
function jardin(hero){
  if(calme() || hero.querySelector("canvas.mo3-jardin")) return;
  var cv = document.createElement("canvas"), c = cv.getContext("2d");
  if(!c) return;
  cv.className = "mo3-jardin"; cv.setAttribute("aria-hidden", "true");
  hero.insertBefore(cv, hero.firstChild);
  var dim = poser(cv, hero), px = -999, py = -999, plante = hero.querySelector(".mo-plante");
  var pollen = [], feuilles = [];
  for(var i = 0; i < 24; i++) pollen.push({x:Math.random() * dim.W, y:Math.random() * dim.H, r:.8 + Math.random() * 2.2, v:.15 + Math.random() * .35, p:Math.random() * 6});
  function feuille(){
    return {x:Math.random() * dim.W, y:-20 - Math.random() * 80, s:9 + Math.random() * 9, vy:.4 + Math.random() * .5, rot:Math.random() * 6, vr:(Math.random() - .5) * .05,
      p:Math.random() * 6, c:[PAL["--lime"], PAL["--leaf-3"], "#F3E9C6", PAL["--clay"], PAL["--amber"] || "#E6A93A"][Math.random() * 5 | 0]};
  }
  for(var k = 0; k < 9; k++){ var f = feuille(); f.y = Math.random() * dim.H; feuilles.push(f); }
  hero.addEventListener("pointermove", function(e){
    var r = hero.getBoundingClientRect(), x = e.clientX - r.left;
    if(px > -999) ventCible = Math.max(-3, Math.min(3, ventCible + (x - px) * .05));
    px = x; py = e.clientY - r.top;
  });
  hero.addEventListener("pointerleave", function(){ px = py = -999; });
  hero.addEventListener("pointerdown", function(e){
    if(e.target.closest("a, button")) return;
    ventCible += (Math.random() < .5 ? -1 : 1) * 2.5;
    gerbe(e.clientX, e.clientY, 14, {force:.9, spread:Math.PI * 1.6});
  });
  addEventListener("resize", function(){ if(cv.isConnected) dim = poser(cv, hero); });
  boucle(cv, function(t){
    if(hero.offsetWidth + 0 !== dim.W) dim = poser(cv, hero);
    vent += (ventCible - vent) * .05; ventCible *= .97;
    if(plante) plante.style.setProperty("--mo3-vent", (vent * 2.2).toFixed(2) + "deg");
    c.clearRect(0, 0, dim.W, dim.H);
    var s = t / 1000;
    /* le pollen monte en dansant */
    pollen.forEach(function(p){
      p.y -= p.v; p.x += Math.sin(s * 1.3 + p.p) * .3 + vent * .6;
      var dx = p.x - px, dy = p.y - py, d = Math.hypot(dx, dy);
      if(d < 70 && d > 0){ p.x += dx / d * 1.6; p.y += dy / d * 1.6; }
      if(p.y < -6){ p.y = dim.H + 6; p.x = Math.random() * dim.W; }
      if(p.x < -6) p.x = dim.W + 6; if(p.x > dim.W + 6) p.x = -6;
      /* une luciole : un halo large et pâle, un cœur vif qui palpite */
      var pal = .5 + .5 * Math.sin(s * 2.4 + p.p);
      c.fillStyle = rgba(PAL["--lime"] || "#B7D94C", .1 + pal * .1);
      c.beginPath(); c.arc(p.x, p.y, p.r * 3.4, 0, Math.PI * 2); c.fill();
      c.fillStyle = rgba("#F0F7D8", .55 + pal * .4);
      c.beginPath(); c.arc(p.x, p.y, p.r, 0, Math.PI * 2); c.fill();
    });
    /* les feuilles tombent en se balançant */
    feuilles.forEach(function(f, i){
      f.y += f.vy; f.x += Math.sin(s * 1.1 + f.p) * .7 + vent * 1.4; f.rot += f.vr + vent * .01;
      if(f.y > dim.H + 20 || f.x < -40 || f.x > dim.W + 40) feuilles[i] = feuille();
      c.save(); c.translate(f.x, f.y); c.rotate(f.rot + Math.sin(s * 2 + f.p) * .5);
      c.fillStyle = rgba(f.c, .78);
      c.beginPath(); c.moveTo(0, -f.s); c.quadraticCurveTo(f.s * .75, 0, 0, f.s); c.quadraticCurveTo(-f.s * .75, 0, 0, -f.s); c.fill();
      c.strokeStyle = rgba(PAL["--leaf-2"] || "#1F5C3B", .35); c.lineWidth = .7;
      c.beginPath(); c.moveTo(0, -f.s * .8); c.lineTo(0, f.s * .8); c.stroke();
      c.restore();
    });
  });
  anim(cv, [{opacity:0}, {opacity:1}], {duration:1500, delay:400, fill:"backwards"});
}

/* ---------- B. la double hélice du chapitre ---------- */
var BASES = ["--leaf", "--water", "--clay", "--plum"];
function helice(tete){
  if(calme() || tete.querySelector("canvas.mo3-helice")) return;
  var cv = document.createElement("canvas"), c = cv.getContext("2d");
  if(!c) return;
  cv.className = "mo3-helice"; cv.setAttribute("aria-hidden", "true");
  tete.insertBefore(cv, tete.firstChild);
  var dim = poser(cv, tete, 6);
  var ouvert = 0, ouvertCible = 0, vitesse = 1, phaseScroll = 0, apparition = 0;
  /* toucher l'en-tête (hors liens) désapparie l'hélice, puis elle se referme */
  tete.addEventListener("pointerdown", function(e){
    if(e.target.closest("a, button")) return;
    ouvertCible = 1; vitesse = 2.6;
    var r = tete.getBoundingClientRect();
    gerbe(e.clientX, e.clientY, 10, {force:.7, spread:Math.PI * 2});
    setTimeout(function(){ ouvertCible = 0; }, 1300);
  });
  tete.addEventListener("pointerenter", function(){ vitesse = 1.8; });
  tete.addEventListener("pointerleave", function(){ vitesse = 1; });
  addEventListener("resize", function(){ if(cv.isConnected) dim = poser(cv, tete, 6); });
  var dernierY = scrollY;
  boucle(cv, function(t){
    if(tete.offsetWidth + 12 !== dim.W) dim = poser(cv, tete, 6);
    phaseScroll += (scrollY - dernierY) * .012; dernierY = scrollY;
    ouvert += (ouvertCible - ouvert) * .07;
    vitesse += (1 - vitesse) * .01;
    apparition = Math.min(1, apparition + .02);
    c.clearRect(0, 0, dim.W, dim.H);
    /* l'hélice est centrée sur la médaille : à sa gauche sur ordinateur, à sa droite sur
       téléphone (le titre passe alors dessous) ; elle s'efface vers le texte */
    var med = tete.querySelector(".medal"), tr = tete.getBoundingClientRect(), mr = med ? med.getBoundingClientRect() : null;
    var colonne = mr && mr.bottom <= tr.top + mr.height + 8 && getComputedStyle(tete).flexDirection.indexOf("column") === 0;
    var mx = mr ? mr.left - tr.left + mr.width / 2 + 6 : dim.W * .85, my = mr ? mr.top - tr.top + mr.height / 2 + 6 : dim.H / 2;
    var x0, x1, cy = my;
    if(colonne){ x0 = mr.right - tr.left + 14; x1 = dim.W - 4; }
    else { x0 = Math.max(dim.W * .58, mx - 250); x1 = dim.W - 4; }
    var A = (colonne ? 18 : 24) * (1 + ouvert * .7), pas = 26, n = Math.max(4, Math.floor((x1 - x0) / pas * 2));
    var ph = t / 1000 * .9 * vitesse + phaseScroll;
    for(var i = 0; i <= n; i++){
      var x = x0 + i * (x1 - x0) / n, a = i * .42 + ph;
      var y1 = cy + Math.sin(a) * A, y2 = cy + Math.sin(a + Math.PI) * A, z = Math.cos(a);
      var fondu = Math.min(1, (x - x0) / ((x1 - x0) * .35)) * apparition;
      var al = (PAL.sombre ? .5 : .38) * fondu;
      /* les barreaux : une paire de bases, colorée, qui s'écarte à l'ouverture */
      if(i % 2 === 0){
        var col = PAL[BASES[(i / 2) % 4]] || "#2F7D52", m = (y1 + y2) / 2, ec = ouvert * 10;
        c.strokeStyle = rgba(col, al * .9); c.lineWidth = 2.4;
        c.beginPath(); c.moveTo(x, y1); c.lineTo(x, m - ec * Math.sign(y2 - y1 || 1)); c.stroke();
        c.strokeStyle = rgba(PAL[BASES[((i / 2) + 2) % 4]] || col, al * .9);
        c.beginPath(); c.moveTo(x, y2); c.lineTo(x, m + ec * Math.sign(y2 - y1 || 1)); c.stroke();
      }
      /* les deux brins : les nucléotides grossissent au premier plan */
      c.fillStyle = rgba(PAL["--leaf-2"] || "#1F5C3B", al * (z > 0 ? 1 : .55));
      c.beginPath(); c.arc(x, y1, 2.2 + z * 1.2, 0, Math.PI * 2); c.fill();
      c.fillStyle = rgba(PAL["--water"] || "#5D9AA8", al * (z < 0 ? 1 : .55));
      c.beginPath(); c.arc(x, y2, 2.2 - z * 1.2, 0, Math.PI * 2); c.fill();
    }
  });
}

/* ---------- C. ce qui pousse en arrivant ---------- */
var attente = new Map();
var io = ("IntersectionObserver" in window) ? new IntersectionObserver(function(es){
  es.forEach(function(e){
    if(!e.isIntersecting) return;
    var f = attente.get(e.target); attente.delete(e.target); io.unobserve(e.target);
    if(f) f();
  });
}, {rootMargin:"0px 0px -8% 0px"}) : null;
var BLOCS = "article .box, article .def, article .piege, article .retenir, article .schema, article table, article .methode, article figure, .notions";
function pousser(racine){
  if(calme() || !io) return;
  [].forEach.call(racine.querySelectorAll(BLOCS), function(el){
    if(el._mo3 || el.offsetParent === null) return;
    el._mo3 = true;
    if(el.getBoundingClientRect().top < innerHeight * .92) return;
    var a = anim(el, [{opacity:0, transform:"translateY(34px) scaleY(.92)", transformOrigin:"50% 100%"}, {opacity:1, transform:"translateY(-3px) scaleY(1.01)", transformOrigin:"50% 100%", offset:.7}, {opacity:1, transform:"none", transformOrigin:"50% 100%"}],
      {duration:720, easing:DOUX, fill:"backwards"});
    var b = anim(el, [{boxShadow:"inset 4px 0 0 " + rgba(PAL["--lime"], .9) + ", 0 0 26px " + rgba(PAL["--leaf"], .25)}, {boxShadow:"inset 0 0 0 transparent, 0 0 0 transparent"}], {duration:1300, delay:250, easing:"ease-out"});
    [a, b].forEach(function(x){ if(x) x.pause(); });
    attente.set(el, function(){
      [a, b].forEach(function(x){ if(x) x.play(); });
      if(el.classList.contains("schema")) inviter(el);
    });
    io.observe(el);
  });
}
addEventListener("beforeprint", function(){ attente.forEach(function(f){ try{ f(); }catch(e){} }); attente.clear(); });

/* ---------- D. les schémas invitent au toucher ---------- */
function inviter(s){
  var b = s.querySelector(".ctrls button:not(.on)") || s.querySelector(".ctrls button");
  if(!b || calme()) return;
  setTimeout(function(){ b.classList.remove("mo3-invite"); void b.offsetWidth; b.classList.add("mo3-invite"); }, 500);
}
document.addEventListener("click", function(ev){
  var b = ev.target.closest ? ev.target.closest(".schema .ctrls button, .schema [data-spot]") : null;
  if(!b || calme()) return;
  var s = b.closest(".schema"), box = s && s.querySelector(".svgbox");
  if(!box) return;
  b.classList.remove("mo3-invite");
  var e = document.createElement("i"); e.className = "mo3-eclosion"; e.setAttribute("aria-hidden", "true");
  var r = box.getBoundingClientRect();
  e.style.setProperty("--x", (b.closest(".svgbox") ? ev.clientX - r.left : r.width / 2) + "px");
  e.style.setProperty("--y", (b.closest(".svgbox") ? ev.clientY - r.top : r.height / 2) + "px");
  if(getComputedStyle(box).position === "static") box.style.position = "relative";
  box.appendChild(e);
  anim(e, [{opacity:0, transform:"scale(.6)"}, {opacity:1, transform:"scale(1)", offset:.3}, {opacity:0, transform:"scale(1.15)"}], {duration:900, easing:"ease-out"});
  setTimeout(function(){ e.remove(); }, 950);
  var c = MO.centre ? MO.centre(b) : null;
  if(c) gerbe(c[0], c[1], 8, {force:.6});
});

/* ---------- E. le QCM : soleil, feuilles, pétales ---------- */
function soleil(x, y){
  if(calme()) return;
  var f = document.createElement("i"); f.className = "mo3-soleil";
  f.style.setProperty("--x", x + "px"); f.style.setProperty("--y", y + "px");
  document.body.appendChild(f);
  anim(f, [{opacity:0}, {opacity:1, offset:.2}, {opacity:0}], {duration:1000, easing:"ease-out"});
  setTimeout(function(){ f.remove(); }, 1050);
}
/* une pluie plein écran : feuilles (série de 10) ou pétales (sans-faute) */
function pluie(petales){
  if(calme()) return;
  var cv = document.createElement("canvas"), c = cv.getContext("2d");
  if(!c) return;
  cv.className = "mo3-pluie"; cv.setAttribute("aria-hidden", "true");
  document.body.appendChild(cv);
  var dpr = Math.min(2, window.devicePixelRatio || 1), W = innerWidth, H = innerHeight;
  cv.width = W * dpr; cv.height = H * dpr; c.setTransform(dpr, 0, 0, dpr, 0, 0);
  var cols = petales ? [PAL["--rose"] || "#E58BA5", PAL["--amber"] || "#E6A93A", PAL["--lime"], PAL["--violet"] || "#9B7BD0", "#FFFFFF"]
    : [PAL["--leaf"], PAL["--leaf-3"], PAL["--lime"], PAL["--leaf-2"]];
  var n = petales ? 110 : 70, items = [];
  for(var i = 0; i < n; i++) items.push({x:Math.random() * W, y:-20 - Math.random() * H * .9, s:(petales ? 6 : 7) + Math.random() * 8,
    vy:2 + Math.random() * 2.8, vx:(Math.random() - .5) * 1.2, rot:Math.random() * 6, vr:(Math.random() - .5) * .2, p:Math.random() * 6, c:cols[i % cols.length]});
  var debut = 0, DUREE = petales ? 4200 : 3200;
  function image(t){
    if(!debut) debut = t;
    var u = (t - debut) / DUREE;
    c.clearRect(0, 0, W, H);
    var al = u < .8 ? 1 : Math.max(0, (1 - u) / .2);
    items.forEach(function(it){
      it.y += it.vy; it.x += it.vx + Math.sin(t / 400 + it.p) * .9; it.rot += it.vr;
      c.save(); c.translate(it.x, it.y); c.rotate(it.rot); c.scale(1, .55 + .45 * Math.abs(Math.sin(t / 300 + it.p)));
      c.fillStyle = rgba(it.c, .9 * al);
      c.beginPath();
      if(petales){ c.ellipse(0, 0, it.s * .55, it.s, 0, 0, Math.PI * 2); }
      else { c.moveTo(0, -it.s); c.quadraticCurveTo(it.s * .7, 0, 0, it.s); c.quadraticCurveTo(-it.s * .7, 0, 0, -it.s); }
      c.fill(); c.restore();
    });
    if(u < 1) requestAnimationFrame(image); else cv.remove();
  }
  requestAnimationFrame(image);
}
/* la couche de la page recrée son badge à chaque question : on suit donc la série
   elle-même, pas l'élément, pour ne fêter chaque palier qu'une fois */
var serieVue = 0, vuBilan = new WeakSet();
function qcm(){
  var b = vue.querySelector(".mo-serie");
  var n0 = b ? parseInt(b.textContent, 10) || 0 : 0;
  if(n0 < serieVue) serieVue = n0;
  if(b){
    var n = n0;
    if(n && n > serieVue){
      serieVue = n;
      var r = b.getBoundingClientRect();
      if(n % 5 === 0) soleil(r.left + r.width / 2, r.top + r.height / 2);
      if(n % 10 === 0) pluie(false);
    }
  }
  var bi = vue.querySelector(".qbilan");
  if(bi && !vuBilan.has(bi)){
    vuBilan.add(bi);
    serieVue = 0;
    /* le score affiché défile depuis zéro : on lit le résultat dans l'état du quiz */
    var parfait = false;
    try{ parfait = typeof QS !== "undefined" && QS && QS.liste && QS.liste.length > 0 && QS.score === QS.liste.length; }catch(e){}
    if(parfait) setTimeout(function(){ pluie(true); }, 1100);
    else setTimeout(function(){
      var m = ((bi.querySelector(".qscore") || {}).textContent || "").match(/(\d+)\s*\/\s*(\d+)/);
      if(m && +m[1] === +m[2] && +m[2] > 0 && bi.isConnected) pluie(true);
    }, 2400);
  }
}

/* ---------- l'observateur de la vue ---------- */
var prevu = false;
function balayer(){
  prevu = false;
  var hero = vue.querySelector(".hero.mo-hero");
  if(hero) jardin(hero);
  var tete = vue.querySelector(".chaphead");
  if(tete && !tete._mo3){
    tete._mo3 = true;
    helice(tete);
    anim(tete.querySelector(".medal"), [{opacity:0, transform:"perspective(500px) rotateY(-160deg) scale(.5)"}, {opacity:1, transform:"perspective(500px) rotateY(18deg) scale(1.08)", offset:.7}, {opacity:1, transform:"none"}],
      {duration:1000, delay:150, easing:DOUX, fill:"backwards"});
  }
  pousser(vue);
  qcm();
}
new MutationObserver(function(){ if(!prevu){ prevu = true; requestAnimationFrame(balayer); } })
  .observe(vue, {childList:true, subtree:true, characterData:true});
addEventListener("load", balayer);
balayer();
})();
