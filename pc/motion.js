/* =====================================================================
   COMPLÉMENT DE MOUVEMENT — « chaque réussite émet de la lumière »
   S'ajoute à la couche écrite dans la page, dont il réutilise les outils
   (window.MO : son, émission de photons, couleurs spectrales) :
   A. l'accueil devient un laboratoire : des ions flottent, fuient la main,
      émettent de la lumière en se heurtant ; toucher envoie une onde
   B. un chapitre s'ouvre : son titre s'allume, la réaction se propage le
      long de l'équation, le filigrane tourbillonne
   C. définitions, pièges, méthodes, exercices, figures s'éclairent en
      arrivant ; chaque formule est traversée d'un éclat
   D. toucher une formule la fait briller
   E. le QCM fête les séries : flash à 5 d'affilée, arc-en-ciel à 10,
      feu d'artifice de photons pour une série maîtrisée
   Rien n'est réécrit : les fonctions du site sont appelées telles quelles,
   l'animation vient après. Ce qui attend son apparition n'est figé qu'en
   pause par ce script. Aucune persistance.
   ===================================================================== */
(function(){
"use strict";
var R = document.documentElement;
var mq = window.matchMedia ? window.matchMedia("(prefers-reduced-motion: reduce)") : null;
function calme(){ return !!(mq && mq.matches); }
var MO = window.MO || {};
function emission(x, y, n, f, t){ if(MO.emission && !calme()) MO.emission(x, y, n, f, t); }
function couleur(l, a){ return MO.couleurLambda ? MO.couleurLambda(l, a) : "rgba(228,92,16," + (a == null ? 1 : a) + ")"; }
function anim(el, kf, o){ if(!el || !el.animate || calme()) return null; try{ return el.animate(kf, o); }catch(e){ return null; } }
var DOUX = "cubic-bezier(.2,.8,.2,1)";

var couche = document.createElement("div");
couche.id = "mo2-couche"; couche.setAttribute("aria-hidden", "true");
document.body.appendChild(couche);

/* ---------- A. le laboratoire de l'accueil ---------- */
var IONS = [["H₃O⁺", 640], ["HO⁻", 470], ["Cl⁻", 520], ["Na⁺", 600], ["H₂O", 455], ["NH₄⁺", 560], ["CO₂", 430], ["e⁻", 680],
  ["H⁺", 610], ["Cu²⁺", 480], ["MnO₄⁻", 420], ["Fe³⁺", 590], ["SO₄²⁻", 500], ["OH⁻", 465]];
function labo(){
  var hero = document.querySelector("#page-accueil .hero");
  if(!hero || calme() || hero.querySelector("canvas.mo-labo")) return;
  var cv = document.createElement("canvas"), c = cv.getContext("2d");
  if(!c) return;
  cv.className = "mo-labo"; cv.setAttribute("aria-hidden", "true");
  hero.insertBefore(cv, hero.firstChild);
  var W = 0, H = 0, dpr = 1, parts = [], ondes = [], px = -999, py = -999, actif = true, visible = true;
  function placer(){
    dpr = Math.min(2, window.devicePixelRatio || 1);
    W = hero.offsetWidth; H = hero.offsetHeight;
    /* on mesure l'origine réelle du bloc conteneur du canevas, quel qu'il soit */
    cv.style.left = "0px"; cv.style.top = "0px";
    var o = cv.getBoundingClientRect(), hr = hero.getBoundingClientRect();
    cv.style.left = (hr.left - o.left) + "px"; cv.style.top = (hr.top - o.top) + "px";
    cv.style.width = W + "px"; cv.style.height = H + "px";
    cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr);
    c.setTransform(dpr, 0, 0, dpr, 0, 0);
  }
  placer();
  var n = W < 520 ? 9 : 14;
  for(var i = 0; i < n; i++){
    var a = Math.random() * Math.PI * 2, v = .18 + Math.random() * .3;
    parts.push({x:Math.random() * W, y:Math.random() * H, vx:Math.cos(a) * v, vy:Math.sin(a) * v,
      r:15 + Math.random() * 7, t:IONS[i % IONS.length][0], l:IONS[i % IONS.length][1], eclat:0, rep:0});
  }
  function sombre(){ return R.getAttribute("data-theme") === "sombre"; }
  hero.addEventListener("pointermove", function(e){ var r = hero.getBoundingClientRect(); px = e.clientX - r.left; py = e.clientY - r.top; });
  hero.addEventListener("pointerleave", function(){ px = py = -999; });
  hero.addEventListener("pointerdown", function(e){
    if(e.target.closest("button, a, .mo-raie")) return;
    var r = hero.getBoundingClientRect(), x = e.clientX - r.left, y = e.clientY - r.top;
    ondes.push({x:x, y:y, r:0});
    parts.forEach(function(p){
      var dx = p.x - x, dy = p.y - y, d = Math.max(30, Math.hypot(dx, dy));
      p.vx += dx / d * 260 / d; p.vy += dy / d * 260 / d; p.eclat = Math.max(p.eclat, 160 / d);
    });
    emission(e.clientX, e.clientY, 12, .9);
  });
  addEventListener("resize", placer);
  if("IntersectionObserver" in window) new IntersectionObserver(function(es){ visible = es[0].isIntersecting; if(visible) boucle(); }).observe(hero);
  var enCours = false;
  function boucle(){ if(!enCours){ enCours = true; requestAnimationFrame(image); } }
  function image(){
    enCours = false;
    if(!cv.isConnected || calme()) return;
    if(!visible || document.hidden || !hero.offsetParent){ setTimeout(boucle, 400); return; }
    if(hero.offsetWidth !== W || hero.offsetHeight !== H) placer();
    c.clearRect(0, 0, W, H);
    var nuit = sombre();
    /* les liaisons faibles entre ions proches */
    for(var i = 0; i < parts.length; i++) for(var j = i + 1; j < parts.length; j++){
      var a = parts[i], b = parts[j], dx = b.x - a.x, dy = b.y - a.y, d = Math.hypot(dx, dy);
      if(d < 120){
        c.strokeStyle = couleur((a.l + b.l) / 2, (1 - d / 120) * (nuit ? .35 : .22));
        c.lineWidth = 1; c.beginPath(); c.moveTo(a.x, a.y); c.lineTo(b.x, b.y); c.stroke();
      }
      var mind = a.r + b.r;
      if(d < mind && d > 0){
        /* choc élastique, avec un éclat de lumière si le choc est franc */
        var nx = dx / d, ny = dy / d, rv = (a.vx - b.vx) * nx + (a.vy - b.vy) * ny;
        if(rv > 0){
          a.vx -= rv * nx; a.vy -= rv * ny; b.vx += rv * nx; b.vy += rv * ny;
          if(rv > .35){ a.eclat = b.eclat = 1; ondes.push({x:(a.x + b.x) / 2, y:(a.y + b.y) / 2, r:0, l:(a.l + b.l) / 2}); }
        }
        var rec = (mind - d) / 2; a.x -= nx * rec; a.y -= ny * rec; b.x += nx * rec; b.y += ny * rec;
      }
    }
    parts.forEach(function(p){
      /* la main repousse les ions */
      var dx = p.x - px, dy = p.y - py, d = Math.hypot(dx, dy);
      if(d < 110 && d > 0){ p.vx += dx / d * .22 * (1 - d / 110); p.vy += dy / d * .22 * (1 - d / 110); p.eclat = Math.max(p.eclat, .5); }
      /* agitation thermique et frottement : ils ne s'arrêtent jamais tout à fait */
      p.vx += (Math.random() - .5) * .02; p.vy += (Math.random() - .5) * .02;
      var sp = Math.hypot(p.vx, p.vy), cible = .32;
      if(sp > 2.4){ p.vx *= 2.4 / sp; p.vy *= 2.4 / sp; }
      p.vx += (p.vx / (sp || 1)) * (cible - sp) * .01; p.vy += (p.vy / (sp || 1)) * (cible - sp) * .01;
      p.x += p.vx; p.y += p.vy;
      if(p.x < p.r){ p.x = p.r; p.vx = Math.abs(p.vx); } if(p.x > W - p.r){ p.x = W - p.r; p.vx = -Math.abs(p.vx); }
      if(p.y < p.r){ p.y = p.r; p.vy = Math.abs(p.vy); } if(p.y > H - p.r){ p.y = H - p.r; p.vy = -Math.abs(p.vy); }
      var e = p.eclat; p.eclat *= .94;
      var g = c.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.r * (1.6 + e));
      g.addColorStop(0, couleur(p.l, (nuit ? .28 : .16) + e * .4));
      g.addColorStop(1, couleur(p.l, 0));
      c.fillStyle = g; c.beginPath(); c.arc(p.x, p.y, p.r * (1.6 + e), 0, Math.PI * 2); c.fill();
      c.strokeStyle = couleur(p.l, (nuit ? .55 : .38) + e * .5); c.lineWidth = 1.2;
      c.beginPath(); c.arc(p.x, p.y, p.r * .72, 0, Math.PI * 2); c.stroke();
      c.fillStyle = couleur(p.l, (nuit ? .72 : .5) + e * .45);
      c.font = "600 " + Math.round(p.r * .62) + "px Charter, Cambria, Georgia, serif";
      c.textAlign = "center"; c.textBaseline = "middle";
      c.fillText(p.t, p.x, p.y + 1);
    });
    ondes = ondes.filter(function(o){
      o.r += 3.2;
      var al = Math.max(0, 1 - o.r / 90);
      c.strokeStyle = couleur(o.l || 560, al * .7); c.lineWidth = 2;
      c.beginPath(); c.arc(o.x, o.y, o.r, 0, Math.PI * 2); c.stroke();
      return al > 0;
    });
    boucle();
  }
  anim(cv, [{opacity:0}, {opacity:1}], {duration:1400, delay:300, fill:"backwards"});
  boucle();
}

/* ---------- C. ce qui s'éclaire en arrivant ---------- */
var prepares = new WeakSet(), attente = new Map();
var io = ("IntersectionObserver" in window) ? new IntersectionObserver(function(es){
  es.forEach(function(e){
    if(!e.isIntersecting) return;
    var f = attente.get(e.target);
    attente.delete(e.target); io.unobserve(e.target);
    if(f) f();
  });
}, {rootMargin:"0px 0px -8% 0px"}) : null;
var BLOCS = ".def, .piege, .methode, .exo, .fbloc, .tb-wrap, .fig, .qcm-serie, details.rap, .exo-comp, .dmaison, h3";
var TEINTE = {def:600, piege:625, methode:470, exo:540, fbloc:580, rap:600, fig:500, "exo-comp":520, dmaison:560};
function teinteDe(el){ for(var k in TEINTE) if(el.classList.contains(k)) return TEINTE[k]; return 590; }
function preparer(page){
  if(!page || calme() || !io) return;
  [].forEach.call(page.querySelectorAll(".part.vu, .part.vu details[open]"), function(part){
    [].forEach.call(part.querySelectorAll(BLOCS + ", .eqc"), function(el){
      if(prepares.has(el) || el.offsetParent === null) return;
      prepares.add(el);
      if(el.getBoundingClientRect().top < innerHeight * .92) return;   /* déjà à l'écran : la couche de la page s'en charge */
      if(el.classList.contains("eqc")){ attente.set(el, function(){ eclat(el); }); io.observe(el); return; }
      var l = teinteDe(el);
      var a = anim(el, [{opacity:0, transform:"translateY(28px) scale(.985)"}, {opacity:1, transform:"none"}], {duration:620, easing:DOUX, fill:"backwards"});
      var b = el.tagName === "H3" ? null : anim(el, [{boxShadow:"inset 5px 0 0 " + couleur(l) + ", 0 0 30px " + couleur(l, .35)}, {boxShadow:"inset 0 0 0 transparent, 0 0 0 transparent"}], {duration:1300, delay:200, easing:"ease-out"});
      [a, b].forEach(function(x){ if(x) x.pause(); });
      attente.set(el, function(){ [a, b].forEach(function(x){ if(x) x.play(); }); });
      io.observe(el);
    });
  });
}
function eclat(el){
  if(calme() || !el.isConnected) return;
  /* un seul éclat à la fois sur une même formule */
  if(el._mo2 && Date.now() - el._mo2 < 900) return;
  el._mo2 = Date.now();
  var r = el.getBoundingClientRect();
  if(r.width < 4) return;
  var e = document.createElement("i");
  e.className = "mo2-eclat";
  e.style.cssText = "position:absolute;left:" + (r.left + scrollX) + "px;top:" + (r.top + scrollY) + "px;width:" + r.width + "px;height:" + r.height + "px";
  document.body.appendChild(e);
  setTimeout(function(){ e.remove(); }, 1000);
}
addEventListener("beforeprint", function(){ attente.forEach(function(f){ try{ f(); }catch(e){} }); attente.clear(); });

/* ---------- D. toucher une formule ---------- */
document.addEventListener("click", function(ev){
  var f = ev.target.closest ? ev.target.closest(".eqc") : null;
  if(!f || calme() || ev.target.closest("a, button")) return;
  f.classList.remove("mo2-frappe"); void f.offsetWidth; f.classList.add("mo2-frappe");
  emission(ev.clientX, ev.clientY, 14, .9);
  eclat(f);
});
/* un anneau de lumière sous le doigt, sur les onglets et les fiches */
document.addEventListener("pointerdown", function(ev){
  if(calme()) return;
  var t = ev.target.closest ? ev.target.closest(".pills a, details.rap > summary, .btn-reset, .tabnav a") : null;
  if(!t) return;
  var o = document.createElement("i"); o.className = "mo2-anneau";
  o.style.left = ev.clientX + "px"; o.style.top = ev.clientY + "px";
  o.style.setProperty("--c", couleur(420 + Math.random() * 260));
  couche.appendChild(o); setTimeout(function(){ o.remove(); }, 600);
}, {passive:true});

/* ---------- B. un chapitre qui s'ouvre ---------- */
function allumer(page){
  if(!page || calme()) return;
  var h = page.querySelector(".chap-hero");
  if(!h) return;
  h.classList.remove("mo2-allume"); void h.offsetWidth; h.classList.add("mo2-allume");
  clearTimeout(h._mo2); h._mo2 = setTimeout(function(){ h.classList.remove("mo2-allume"); }, 2800);
  var eq = h.querySelector(".grand-eq");
  if(eq) setTimeout(function(){
    if(!eq.isConnected || calme()) return;
    var r = eq.getBoundingClientRect();
    emission(r.right - 8, r.top + r.height / 2, 16, 1);
  }, 2300);
}
var go0 = window.go;
if(typeof go0 === "function"){
  window.go = function(id){
    var r = go0.apply(this, arguments);
    /* la couche de la page change de page dans une transition de vue, donc en différé :
       on relit la page affichée une fois le changement fait */
    setTimeout(function(){
      var page = document.querySelector(".page.on");
      allumer(page); preparer(page);
      if(page && page.id === "page-accueil") labo();
    }, 140);
    return r;
  };
}
var onglet0 = window.onglet;
if(typeof onglet0 === "function"){
  window.onglet = function(){
    var r = onglet0.apply(this, arguments);
    requestAnimationFrame(function(){ preparer(document.querySelector(".page.on")); });
    return r;
  };
}
/* une fiche dépliée révèle de nouveaux blocs */
document.addEventListener("toggle", function(ev){
  if(ev.target && ev.target.tagName === "DETAILS" && ev.target.open) requestAnimationFrame(function(){ preparer(document.querySelector(".page.on")); });
}, true);

/* ---------- E. le QCM fête les séries ---------- */
function flash(x, y){
  if(calme()) return;
  var f = document.createElement("i"); f.className = "mo2-flash";
  f.style.setProperty("--x", x + "px"); f.style.setProperty("--y", y + "px");
  document.body.appendChild(f);
  var a = anim(f, [{opacity:0}, {opacity:1, offset:.18}, {opacity:0}], {duration:900, easing:"ease-out"});
  setTimeout(function(){ f.remove(); }, 950);
}
function arcenciel(){
  if(calme()) return;
  var b = document.createElement("i"); b.className = "mo2-arcenciel";
  document.body.appendChild(b);
  anim(b, [{transform:"translateY(0)"}, {transform:"translateY(" + (innerHeight * 1.46 + 20) + "px)"}], {duration:1300, easing:"cubic-bezier(.45,0,.3,1)"});
  setTimeout(function(){ b.remove(); }, 1350);
}
function feuDArtifice(){
  if(calme()) return;
  for(var k = 0; k < 7; k++) setTimeout(function(){
    var x = innerWidth * (.15 + Math.random() * .7), y = innerHeight * (.18 + Math.random() * .45);
    emission(x, y, 26, 1.5);
  }, k * 190);
}
var dernier = new WeakMap(), fete = 0;
new MutationObserver(function(muts){
  var bilan = false;
  muts.forEach(function(m){
    var b = m.target.nodeType === 1 && m.target.classList.contains("mo-bilan") ? m.target : null;
    [].forEach.call(m.addedNodes, function(n){ if(n.nodeType === 1 && n.classList.contains("mo-bilan")) b = n; });
    if(b && /maîtrisée/.test(b.textContent)) bilan = true;
    var cible = m.target.nodeType === 1 ? m.target : m.target.parentNode;
    var badge = cible && cible.closest ? (cible.closest(".mo-badge") || (cible.querySelector && cible.querySelector(".mo-badge"))) : null;
    if(badge){
      var nb = parseInt(badge.textContent, 10);
      if(nb && dernier.get(badge) !== nb){
        dernier.set(badge, nb);
        var r = badge.getBoundingClientRect();
        if(nb === 5 || nb === 15 || nb === 25) flash(r.left + r.width / 2, r.top + r.height / 2);
        if(nb === 10 || nb === 20 || nb === 30){ arcenciel(); flash(r.left + r.width / 2, r.top + r.height / 2); }
      }
    }
  });
  /* un seul feu d'artifice par bilan, même si le message change en plusieurs mutations */
  if(bilan && Date.now() - fete > 1500){ fete = Date.now(); setTimeout(feuDArtifice, 250); }
}).observe(document.body, {childList:true, subtree:true, characterData:true});

/* ---------- départ ---------- */
var page0 = document.querySelector(".page.on");
if(page0 && page0.id === "page-accueil") labo();
preparer(page0);
if(page0 && page0.id !== "page-accueil") allumer(page0);
})();
