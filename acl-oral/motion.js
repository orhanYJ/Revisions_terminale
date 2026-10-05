/* =====================================================================
   COUCHE DE MOUVEMENT — « une braise veille sur chaque page »
   Script commun aux trois sites ACL oral ; seule la ligne MOTIF change.
   A. entrer dans une page : le filigrane se trace à la braise, puis
      s'anime selon l'œuvre (flamme qui s'attise, télécran qui grésille et
      dont l'œil suit la main, pousse qui déplie ses feuilles) ; la main
      sur l'en-tête le ranime
   B. un tison glisse dans le rail jusqu'à la page en cours
   C. « révisé » : des étincelles montent du bouton, le point du rail
      prend feu, la jauge s'embrase
   D. le fil de braise de la lecture, en haut de l'écran
   E. les blocs du dessous arrivent quand on les atteint ; les vers d'un
      poème s'éclairent à mesure ; chez Butler, la scène atteinte par
      l'index rougeoie et le changement de mode fond le texte
   Script maintenu à part de index.html. Il ne réécrit aucune fonction du
   site : il écoute les gestes et observe le DOM. Il ne cache jamais ce qui
   est déjà à l'écran. Aucune persistance.
   ===================================================================== */
(function(){
"use strict";
var MOTIF = "lanterne";   /* lanterne (corpus Dystopie) · telecran (1984) · graine (Butler) */

var R = document.documentElement;
var mq = window.matchMedia ? window.matchMedia("(prefers-reduced-motion: reduce)") : null;
function calme(){ return !!(mq && mq.matches); }
R.classList.toggle("mo", !calme());
if(mq && mq.addEventListener){ mq.addEventListener("change", function(){ R.classList.toggle("mo", !calme()); }); }
var $ = function(s, r){ return (r || document).querySelector(s); };
var $$ = function(s, r){ return [].slice.call((r || document).querySelectorAll(s)); };

function rejouer(el, classe, ms){
  el.classList.remove(classe); void el.offsetWidth; el.classList.add(classe);
  clearTimeout(el["_mo" + classe]);
  el["_mo" + classe] = setTimeout(function(){ el.classList.remove(classe); }, ms);
}

var sections = $$("section");
var rail = $("nav.rail");

/* ---------- A. les filigranes ---------- */
/* on repère les pièces du dessin par leur tracé, sans toucher au balisage */
function preparerFiligrane(wm){
  if(!wm || wm._mo) return;
  wm._mo = true;
  var k = 0;
  $$("path,circle,rect", wm).forEach(function(el){
    var d = el.getAttribute("d") || "";
    if(el.getAttribute("stroke-dasharray")){ el.classList.add("mo-halo"); return; }
    if(d.indexOf("M200 236c") === 0){ el.classList.add("mo-flamme"); return; }
    if(el.tagName.toLowerCase() === "circle" && el.getAttribute("r") === "19"){ el.classList.add("mo-iris"); return; }
    if(d.indexOf("M90 128h220") === 0){ el.classList.add("mo-trame"); return; }
    /* la flamme et les feuilles ont leur propre geste : on ne les trace pas */
    if(d.indexOf("M200 210c") === 0){ el.classList.add("mo-feuille", "g"); return; }
    if(d.indexOf("M200 180c") === 0){ el.classList.add("mo-feuille", "d"); return; }
    if(d.indexOf("M104 74v26") === 0){ el.classList.add("mo-etoiles"); return; }
    try{
      var L = el.getTotalLength();
      if(L > 0){ el.style.setProperty("--l", Math.ceil(L) + 2); el.style.setProperty("--k", k++); el.classList.add("mo-l"); }
    }catch(e){}
  });
}
function attiser(hero, ms){ if(hero && !calme()) rejouer(hero, "mo-attise", ms || 2500); }

/* 1984 : l'œil du télécran suit la main (ou le doigt qui touche) */
var regard = null;
function suivreRegard(x, y){
  var s = $$("section.on .hero .wm .mo-iris")[0];
  if(!s || calme()) return;
  var svg = s.ownerSVGElement, r = svg.getBoundingClientRect();
  if(r.bottom < 0 || r.top > innerHeight || !r.width) return;
  var k = r.width / 400, cx = r.left + 200 * k, cy = r.top + 194 * k;
  var dx = x - cx, dy = y - cy, n = Math.hypot(dx, dy) || 1;
  var m = Math.min(22, n / k / 14);
  s.style.transform = "translate(" + (dx / n * m).toFixed(1) + "px," + (dy / n * m).toFixed(1) + "px)";
}
if(MOTIF === "telecran"){
  document.addEventListener("pointermove", function(ev){
    if(ev.pointerType !== "mouse") return;
    var x = ev.clientX, y = ev.clientY;
    if(!regard) regard = requestAnimationFrame(function(){ regard = null; suivreRegard(x, y); });
  }, {passive:true});
  document.addEventListener("pointerdown", function(ev){ suivreRegard(ev.clientX, ev.clientY); }, {passive:true});
}

/* la main sur l'en-tête ranime le filigrane (pas plus d'une fois toutes les trois secondes) */
$$(".hero").forEach(function(h){
  var dernier = 0;
  h.addEventListener("pointerenter", function(){
    if(Date.now() - dernier < 3000) return;
    dernier = Date.now();
    preparerFiligrane($(".wm", h));
    attiser(h);
  });
});

/* ---------- B. le tison du rail ---------- */
var tison = null, tisonY = null;
if(rail){
  tison = document.createElement("i");
  tison.className = "mo-tison"; tison.setAttribute("aria-hidden", "true");
  rail.appendChild(tison);
}
function placerTison(sansAnim){
  if(!tison) return;
  var a = $(".navlink.active", rail);
  if(!a || !a.offsetHeight){ rail.classList.remove("mo-glisse"); tison.style.height = "0"; return; }
  var rr = rail.getBoundingClientRect(), ra = a.getBoundingClientRect();
  var y = ra.top - rr.top + rail.scrollTop, h = ra.height;
  tison.style.height = h + "px";
  tison.style.transform = "translateY(" + y + "px)";
  if(!sansAnim && tisonY !== null && tisonY !== y && !calme() && tison.animate){
    tison.animate([{transform:"translateY(" + tisonY + "px)", height:tison._h + "px"}, {transform:"translateY(" + y + "px)", height:h + "px"}],
      {duration:420, easing:"cubic-bezier(.3,1.15,.4,1)"});
  }
  tisonY = y; tison._h = h;
  rail.classList.add("mo-glisse");
}

/* ---------- C. « révisé » ---------- */
function etincelles(btn){
  for(var i = 0; i < 9; i++){
    var e = document.createElement("i");
    e.className = "mo-etincelle"; e.setAttribute("aria-hidden", "true");
    var a = -Math.PI / 2 + (Math.random() - .5) * 1.9, d = 30 + Math.random() * 46;
    e.style.left = (12 + Math.random() * 76) + "%";
    e.style.setProperty("--x", (Math.cos(a) * d).toFixed(0) + "px");
    e.style.setProperty("--y", (Math.sin(a) * d - 10).toFixed(0) + "px");
    e.style.setProperty("--d", (Math.random() * .18).toFixed(2) + "s");
    btn.appendChild(e);
    setTimeout(function(n){ return function(){ n.remove(); }; }(e), 1300);
  }
}
document.addEventListener("click", function(ev){
  var b = ev.target.closest ? ev.target.closest(".reviewed button") : null;
  if(!b || calme()) return;
  /* le site a déjà basculé l'état dans son propre écouteur : on lit le résultat */
  requestAnimationFrame(function(){
    if(!b.classList.contains("on")) return;
    etincelles(b);
    rejouer(b, "mo-allume", 1100);
    var l = $('.navlink[data-s="' + b.dataset.id + '"]');
    if(l) rejouer(l, "mo-allume", 1300);
    var bar = $(".rail .prog .bar");
    if(bar) rejouer(bar, "mo-allume", 1300);
  });
});

/* ---------- D. le fil de braise ---------- */
var braise = document.createElement("div");
braise.id = "mo-braise"; braise.setAttribute("aria-hidden", "true");
braise.innerHTML = '<i class="b-fil"></i><i class="b-tete"></i>';
document.body.appendChild(braise);
var tick = false;
function lecture(){
  tick = false;
  var h = R.scrollHeight - innerHeight;
  if(h < 400){ braise.classList.remove("on"); return; }
  /* sur grand écran le fil part du bord du rail ; sur téléphone le rail est replié */
  var g = rail ? Math.max(0, Math.round(rail.getBoundingClientRect().right)) : 0;
  if(g > innerWidth * .5) g = 0;
  braise.style.setProperty("--g", g + "px");
  braise.style.setProperty("--p", Math.max(0, Math.min(1, scrollY / h)).toFixed(4));
  braise.classList.add("on");
  if(scrollY >= h - 2) auBout();
}
/* tout en bas de la page, la marge de l'observateur ne peut plus être franchie : on montre ce qui reste */
function auBout(){
  var n = 0;
  $$(".mo-attente").forEach(function(el){ if(el.getBoundingClientRect().top < innerHeight){ vu(el, n++); if(io) io.unobserve(el); } });
  $$(".mo-sombre").forEach(function(v){ if(v.getBoundingClientRect().top < innerHeight){ v.classList.remove("mo-sombre"); if(ioVers) ioVers.unobserve(v); } });
}
addEventListener("scroll", function(){ if(!tick){ tick = true; requestAnimationFrame(lecture); } }, {passive:true});
addEventListener("resize", function(){ lecture(); placerTison(true); });

/* ---------- E. ce qui arrive quand on l'atteint ---------- */
var BLOCS = ".panel,.qcard,.ki,.bridge,.thesis,.memq,.plan > .step,.compare-wrap,.triwrap,blockquote,.seealso,.tbl";
function vu(el, n){
  el.style.setProperty("--k", n);
  el.classList.add("mo-vu");
  el.classList.remove("mo-attente");
  setTimeout(function(){ el.classList.remove("mo-vu"); el.style.removeProperty("--k"); }, 1600);
}
var io = ("IntersectionObserver" in window) ? new IntersectionObserver(function(entrees){
  var n = 0;
  entrees.forEach(function(en){ if(en.isIntersecting){ vu(en.target, n++); io.unobserve(en.target); } });
}, {rootMargin:"0px 0px -8% 0px"}) : null;
var ioVers = ("IntersectionObserver" in window) ? new IntersectionObserver(function(entrees){
  var n = 0;
  entrees.forEach(function(en){
    if(!en.isIntersecting) return;
    var v = en.target;
    v.style.setProperty("--k", Math.min(n++, 12));
    v.classList.add("mo-lueur");
    v.classList.remove("mo-sombre");
    ioVers.unobserve(v);
    setTimeout(function(){ v.classList.remove("mo-lueur"); v.style.removeProperty("--k"); }, 2200);
  });
}, {rootMargin:"0px 0px -12% 0px"}) : null;

function preparer(sec){
  if(!io) return;
  $$(".mo-attente").forEach(function(el){ el.classList.remove("mo-attente"); io.unobserve(el); });
  $$(".mo-sombre").forEach(function(el){ el.classList.remove("mo-sombre"); ioVers.unobserve(el); });
  if(!sec || calme()) return;
  var bas = innerHeight;
  $$(BLOCS, sec).forEach(function(el){
    var parent = el.parentElement && el.parentElement.closest(BLOCS);
    if(parent && sec.contains(parent)) return;   /* un bloc dans un bloc arrive avec lui */
    if(!el.offsetHeight || el.getBoundingClientRect().top < bas) return;   /* déjà à l'écran : on n'y touche pas */
    el.classList.add("mo-attente");
    io.observe(el);
  });
  $$(".poem .vln", sec).forEach(function(v){
    if(!v.offsetHeight || v.getBoundingClientRect().top < bas) return;
    v.classList.add("mo-sombre");
    ioVers.observe(v);
  });
}

/* Butler : la scène atteinte par l'index rougeoie */
document.addEventListener("click", function(ev){
  var c = ev.target.closest ? ev.target.closest(".sceneidx .chip") : null;
  if(!c || calme()) return;
  var anc = $(c.getAttribute("href"));
  if(!anc) return;
  var cible = anc.nextElementSibling;
  while(cible && !cible.offsetHeight) cible = cible.nextElementSibling;
  if(!cible) return;
  cible.classList.remove("mo-attente");
  var fait = false;
  function marquer(){ if(fait) return; fait = true; removeEventListener("scrollend", marquer); rejouer(cible, "mo-repere", 1900); }
  addEventListener("scrollend", marquer);
  setTimeout(marquer, 900);
});
/* Butler : changer de mode fond le texte de la page */
$$("#modetoggle button").forEach(function(b){
  b.addEventListener("click", function(){
    var sec = $("section.on .body") || $("section.on");
    if(sec && sec.animate && !calme()) sec.animate([{opacity:.25}, {opacity:1}], {duration:380, easing:"ease-out"});
    requestAnimationFrame(function(){ preparer($("section.on")); lecture(); });
  });
});

/* ---------- changer de page ---------- */
function entrer(sec){
  var wm = $(".hero .wm", sec);
  preparerFiligrane(wm);
  if(!calme()){
    rejouer(sec, "mo-entre", 2600);
    var hero = $(".hero", sec);
    setTimeout(function(){ if(sec.classList.contains("on")) attiser(hero); }, 1200);
  }
  placerTison(false);
  /* le site remonte en douceur en haut de page : on mesure les blocs une fois revenu */
  setTimeout(function(){ preparer(sec); lecture(); }, 60);
}
var mo = new MutationObserver(function(ms){
  ms.forEach(function(m){
    var s = m.target;
    if(s.classList.contains("on") && (m.oldValue || "").split(/\s+/).indexOf("on") < 0) entrer(s);
  });
});
sections.forEach(function(s){ mo.observe(s, {attributes:true, attributeFilter:["class"], attributeOldValue:true}); });

/* ---------- démarrage ---------- */
var ici = $("section.on");
if(ici){
  preparerFiligrane($(".hero .wm", ici));
  if(!calme()){ rejouer(ici, "mo-entre", 2600); setTimeout(function(){ attiser($(".hero", ici)); }, 1200); }
}
placerTison(true);
preparer(ici);
lecture();
if(document.fonts && document.fonts.ready) document.fonts.ready.then(function(){ placerTison(true); });
window.MO = {estCalme:calme};
})();
