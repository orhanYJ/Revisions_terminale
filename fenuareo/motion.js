/* =====================================================================
   COUCHE DE MOUVEMENT — « chaque leçon vue, la pirogue avance d'un coup de pagaie »
   A. une pirogue (va'a) navigue sur la barre de progression : elle avance
      quand une nouvelle leçon est vue, et donne un coup de pagaie à
      chaque bonne réponse
   B. ouvrir une leçon : l'en-tête se lève, le macron du titre se trace ;
      les blocs du dessous arrivent quand on les atteint
   C. exercices : une bonne réponse fait des ronds dans le lagon, une
      mauvaise tangue dans la houle
   D. revenir au sommaire : la carte de la leçon lue salue ; filtrer fait
      se relever les cartes restantes
   Script maintenu à part de index.html. Il ne réécrit aucune fonction du
   site : il écoute les gestes et observe le DOM. Il ne cache jamais ce qui
   est déjà à l'écran. Il ne pose rien sur le body. Aucune persistance.
   ===================================================================== */
(function(){
"use strict";
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

/* ---------- A. la pirogue ---------- */
var barre = $(".progbar-in"), piste = $(".pb-track"), plein = $("#pb-fill"), vaa = null;
if(barre && piste && plein){
  vaa = document.createElement("span");
  vaa.className = "mo-vaa"; vaa.setAttribute("aria-hidden", "true");
  vaa.innerHTML = '<svg viewBox="0 0 26 15">'
    + '<path class="ama" d="M4 3.5 H20 M8 3.5 V8 M16 3.5 V8"/>'
    + '<path class="pagaie" d="M15 6 L19 13"/>'
    + '<circle class="rameur" cx="13" cy="6.2" r="2"/>'
    + '<path class="coque" d="M1 9 H25 C23 12.5 19 14 13 14 C7 14 3 12.5 1 9 Z"/></svg>';
  barre.appendChild(vaa);
}
var dernierPct = null;
function naviguer(){
  if(!vaa) return;
  var pct = parseFloat(plein.style.width) || 0;
  var x = piste.offsetLeft + piste.clientWidth * pct / 100 - 13;
  x = Math.max(piste.offsetLeft - 13, Math.min(x, piste.offsetLeft + piste.clientWidth - 13));
  var y = piste.offsetTop + piste.offsetHeight / 2 - 12;
  vaa.style.setProperty("--x", x.toFixed(1) + "px");
  vaa.style.setProperty("--y", y.toFixed(1) + "px");
  vaa.style.display = piste.offsetWidth < 40 ? "none" : "";
  if(dernierPct !== null && pct > dernierPct) ramer();
  dernierPct = pct;
}
function ramer(){ if(vaa && !calme()) rejouer(vaa, "mo-rame", 1000); }
if(plein) new MutationObserver(naviguer).observe(plein, {attributes:true, attributeFilter:["style"]});
addEventListener("resize", naviguer);

/* ---------- B. ouvrir une leçon ---------- */
var BLOCS = ".l-corps > *,.l-exos > *,.recap,.l-nav";
function vu(el, n){
  el.style.setProperty("--k", n);
  el.classList.add("mo-vu");
  el.classList.remove("mo-attente");
  setTimeout(function(){ el.classList.remove("mo-vu"); el.style.removeProperty("--k"); }, 1500);
}
var io = ("IntersectionObserver" in window) ? new IntersectionObserver(function(entrees){
  var n = 0;
  entrees.forEach(function(en){ if(en.isIntersecting){ vu(en.target, n++); io.unobserve(en.target); } });
}, {rootMargin:"0px 0px -8% 0px"}) : null;
function preparer(vue){
  if(!io) return;
  $$(".mo-attente").forEach(function(el){ el.classList.remove("mo-attente"); io.unobserve(el); });
  if(!vue || calme()) return;
  var bas = innerHeight;
  $$(BLOCS, vue).forEach(function(el){
    var parent = el.parentElement && el.parentElement.closest(BLOCS);
    if(parent && vue.contains(parent) && parent !== el) return;
    if(!el.offsetHeight || el.getBoundingClientRect().top < bas) return;   /* déjà à l'écran : on n'y touche pas */
    el.classList.add("mo-attente");
    io.observe(el);
  });
}
var lue = null;
function ouvrir(l){
  lue = l;
  if(!calme()) rejouer(l, "mo-ouvre", 1400);
  /* le site remonte en douceur en haut : on mesure une fois revenu */
  setTimeout(function(){ if(!l.hidden) preparer(l); }, 450);
}
$$(".lecon").forEach(function(l){
  new MutationObserver(function(){ if(!l.hidden && l !== lue) ouvrir(l); })
    .observe(l, {attributes:true, attributeFilter:["hidden"]});
});
/* tout en bas, la marge de l'observateur ne peut plus être franchie : on montre ce qui reste */
addEventListener("scroll", function(){
  if(scrollY < R.scrollHeight - innerHeight - 2) return;
  var n = 0;
  $$(".mo-attente").forEach(function(el){ if(el.getBoundingClientRect().top < innerHeight){ vu(el, n++); if(io) io.unobserve(el); } });
}, {passive:true});

/* ---------- C. les exercices ---------- */
function ronds(el, x, y, couleur){
  if(calme()) return;
  var r = el.getBoundingClientRect();
  var grand = Math.max(r.width, r.height) * 1.6;
  for(var i = 0; i < 3; i++){
    var o = document.createElement("i");
    o.className = "mo-rond"; o.setAttribute("aria-hidden", "true");
    o.style.setProperty("--x", (x - r.left) + "px");
    o.style.setProperty("--y", (y - r.top) + "px");
    o.style.setProperty("--r", (grand * (1 - i * .22)).toFixed(0) + "px");
    o.style.setProperty("--d", (i * .16) + "s");
    if(couleur) o.style.borderColor = couleur;
    el.appendChild(o);
    setTimeout(function(n){ return function(){ n.remove(); }; }(o), 1500);
  }
}
document.addEventListener("click", function(ev){
  if(!ev.target.closest) return;
  var b = ev.target.closest(".exo-opt"), x = ev.clientX, y = ev.clientY;
  if(b){
    /* le site a déjà corrigé dans son propre écouteur : on lit le verdict qu'il a posé */
    requestAnimationFrame(function(){
      if(b.classList.contains("faux")){
        if(!calme()) rejouer(b, "mo-houle", 600);
        var juste = b.parentNode && b.parentNode.querySelector(".exo-opt.juste");
        if(juste){ var r = juste.getBoundingClientRect(); ronds(juste, r.left + 24, r.top + r.height / 2, "var(--vert)"); }
      } else if(b.classList.contains("juste")){
        if(!x && !y){ var q = b.getBoundingClientRect(); x = q.left + q.width / 2; y = q.top + q.height / 2; }
        ronds(b, x, y);
        ramer();
      }
    });
    return;
  }
  var a = ev.target.closest(".exo-actions button");
  if(a) requestAnimationFrame(function(){ verdict(a.closest(".exo")); });
});
document.addEventListener("keydown", function(ev){
  if(ev.key !== "Enter" || !ev.target.classList || !ev.target.classList.contains("exo-in")) return;
  var exo = ev.target.closest(".exo");
  requestAnimationFrame(function(){ verdict(exo); });
});
function verdict(exo){
  if(!exo || calme()) return;
  var fb = $(".exo-fb", exo), inp = $(".exo-in", exo);
  if(!fb || !inp) return;
  if(fb.classList.contains("fb-ok")){
    var r = inp.getBoundingClientRect();
    ronds(exo, r.left + r.width / 2, r.top + r.height / 2);
    ramer();
  } else if(fb.classList.contains("fb-no")) rejouer(inp, "mo-houle", 600);
}

/* ---------- D. le sommaire ---------- */
var hub = $("#hub");
var aSaluer = null;
var ioSalut = ("IntersectionObserver" in window) ? new IntersectionObserver(function(entrees){
  entrees.forEach(function(en){
    if(!en.isIntersecting) return;
    ioSalut.unobserve(en.target);
    saluer(en.target);
  });
}, {rootMargin:"0px 0px -15% 0px"}) : null;
function saluer(c){
  if(calme()) return;
  rejouer(c, "mo-salue", 1100);
  if(c.animate) c.animate([{transform:"none"}, {transform:"translateY(-5px) scale(1.02)", offset:.35}, {transform:"none"}],
    {duration:900, easing:"cubic-bezier(.3,1.4,.5,1)", composite:"add"});
}
if(hub) new MutationObserver(function(){
  if(hub.style.display === "none" || !lue) return;
  var c = $('.hcard[data-goto="' + lue.getAttribute("data-lecon-idx") + '"]');
  lue = null;
  if(!c || c.classList.contains("hidden")) return;
  /* le site remonte en haut : la carte salue quand on la retrouve */
  setTimeout(function(){ if(ioSalut){ ioSalut.observe(c); } else saluer(c); }, 500);
}).observe(hub, {attributes:true, attributeFilter:["style"]});

$$("[data-fcat],[data-fniv]").forEach(function(f){
  f.addEventListener("click", function(){
    if(calme()) return;
    requestAnimationFrame(function(){
      var k = 0, bas = innerHeight;
      $$(".hcard:not(.hidden)").forEach(function(c){
        var r = c.getBoundingClientRect();
        if(r.bottom < 0 || r.top > bas || !c.animate) return;
        c.animate([{opacity:0, transform:"translateY(12px)"}, {opacity:1, transform:"none"}],
          {duration:450, delay:Math.min(k++, 14) * 30, easing:"cubic-bezier(.2,.7,.2,1)", fill:"backwards"});
      });
    });
  });
});

/* ---------- démarrage ---------- */
naviguer();
if(document.fonts && document.fonts.ready) document.fonts.ready.then(naviguer);
var ouverte = $$(".lecon").filter(function(l){ return !l.hidden; })[0];
if(ouverte){ lue = ouverte; preparer(ouverte); }
window.MO = {estCalme:calme};
})();
