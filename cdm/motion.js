/* =====================================================================
   COUCHE DE MOUVEMENT — « l'écran s'éteint, la lampe s'allume »
   A. la lumière froide de l'écran, en bas, se retire à mesure qu'on lit
   B. la veillée : sous la barre, un filet passe du bleu écran à l'ambre
   C. la barre suit la section en cours : une pastille ambrée glisse
   D. la chronologie australienne se dessine au fil de la lecture
   E. ondes, notions, chiffres, plan : chacun s'éclaire quand on l'atteint
   F. au bout du dossier, le ciel du pied de page s'étoile
   Script maintenu à part de index.html. Il ne touche pas au seul moment
   orchestré du chargement (la lueur de lampe) et ne cache jamais ce qui
   est déjà à l'écran. Aucune persistance.
   ===================================================================== */
(function(){
"use strict";
var R = document.documentElement;
var mq = window.matchMedia ? window.matchMedia("(prefers-reduced-motion: reduce)") : null;
function calme(){ return !!(mq && mq.matches); }
if(!calme()) R.classList.add("mo");
if(mq && mq.addEventListener){ mq.addEventListener("change", function(){ R.classList.toggle("mo", !calme()); }); }

var barre = document.querySelector(".barre"), nav = barre && barre.querySelector("nav");
var sections = [].slice.call(document.querySelectorAll("main section[id]"));
var enveloppe = document.querySelector(".enveloppe");
if(!sections.length) return;

/* ---------- A. la lumière de l'écran ---------- */
var ecran = document.createElement("div");
ecran.id = "mo-ecran"; ecran.setAttribute("aria-hidden", "true");
document.body.insertBefore(ecran, enveloppe || document.body.firstChild);

/* ---------- B. la veillée ---------- */
var veillee = document.createElement("div");
veillee.id = "mo-veillee"; veillee.setAttribute("aria-hidden", "true");
veillee.innerHTML = '<i class="v-trait"></i><i class="v-tete"></i>';
document.body.appendChild(veillee);

/* ---------- C. la pastille de la section en cours ---------- */
var liens = nav ? [].slice.call(nav.querySelectorAll('a[href^="#"]')) : [];
var pastille = null;
if(nav && liens.length){
  pastille = document.createElement("span");
  pastille.className = "mo-pastille"; pastille.setAttribute("aria-hidden", "true");
  nav.insertBefore(pastille, nav.firstChild);
}
var ici = null;
function placer(lien, sansAnim){
  if(!pastille || !lien) return;
  if(sansAnim) pastille.style.transition = "none";
  pastille.style.width = lien.offsetWidth + "px";
  pastille.style.height = lien.offsetHeight + "px";
  pastille.style.transform = "translate(" + lien.offsetLeft + "px," + lien.offsetTop + "px)";
  pastille.style.opacity = "1";
  if(sansAnim){ void pastille.offsetWidth; pastille.style.transition = ""; }
}
function suivre(id, sansAnim){
  var lien = null;
  liens.forEach(function(a){ var on = a.getAttribute("href") === "#" + id; a.classList.toggle("mo-ici", on); if(on) lien = a; });
  if(!lien){ if(pastille) pastille.style.opacity = "0"; return; }
  placer(lien, sansAnim);
  /* sur téléphone la barre défile : on garde la section en cours en vue */
  var g = lien.offsetLeft, d = g + lien.offsetWidth;
  if(g < nav.scrollLeft + 12 || d > nav.scrollLeft + nav.clientWidth - 12){
    var cible = Math.max(0, g - (nav.clientWidth - lien.offsetWidth) / 2);
    try{ nav.scrollTo({left:cible, behavior:(calme() || sansAnim) ? "auto" : "smooth"}); }catch(e){ nav.scrollLeft = cible; }
  }
}

/* ---------- D. la chronologie ---------- */
var chrono = document.querySelector(".chrono"), fil = null, dates = [];
if(chrono){
  fil = document.createElement("i");
  fil.className = "mo-fil"; fil.setAttribute("aria-hidden", "true");
  chrono.appendChild(fil);
  chrono.classList.add("mo-suivi");
  dates = [].slice.call(chrono.children).filter(function(e){ return e.tagName === "LI"; });
}

/* ---------- F. le ciel ---------- */
var footer = document.querySelector("footer"), ciel = null;
if(footer) footer.classList.add("mo-avec-ciel");
function etoiler(){
  if(ciel || !footer) return;
  ciel = document.createElement("div");
  ciel.className = "mo-ciel"; ciel.setAttribute("aria-hidden", "true");
  var g = 7;   /* tirage fixe : le même ciel à chaque lecture */
  function hasard(){ g = (g * 9301 + 49297) % 233280; return g / 233280; }
  for(var k = 0; k < 18; k++){
    var e = document.createElement("i");
    e.className = "mo-etoile";
    e.style.left = (3 + hasard() * 94).toFixed(1) + "%";
    e.style.top = (8 + hasard() * 80).toFixed(1) + "%";
    e.style.setProperty("--t", (1.6 + hasard() * 1.8).toFixed(1) + "px");
    e.style.setProperty("--a", (.35 + hasard() * .5).toFixed(2));
    e.style.setProperty("--d", (k * .17 + hasard() * .25).toFixed(2) + "s");
    ciel.appendChild(e);
  }
  var lune = document.createElement("i");
  lune.className = "mo-lune";
  ciel.appendChild(lune);
  footer.insertBefore(ciel, footer.firstChild);
}

/* ---------- lecture : un seul calcul par image ---------- */
var tick = false;
function lecture(){
  tick = false;
  var hb = barre ? Math.round(barre.getBoundingClientRect().bottom) : 0;
  veillee.style.setProperty("--haut", hb + "px");
  var h = R.scrollHeight - innerHeight;
  var p = h > 0 ? Math.max(0, Math.min(1, scrollY / h)) : 1;
  veillee.style.setProperty("--p", p.toFixed(4));
  /* la lumière froide se retire d'abord vite, puis s'éteint tout à fait */
  ecran.style.setProperty("--o", Math.pow(1 - p, 1.6).toFixed(3));

  /* section en cours */
  var ligne = hb + innerHeight * .3, id = sections[0].id;
  if(scrollY >= h - 4) id = sections[sections.length - 1].id;
  else sections.forEach(function(s){ if(s.getBoundingClientRect().top <= ligne) id = s.id; });
  if(id !== ici){ suivre(id, ici === null); ici = id; }

  /* chronologie : le fil descend avec la lecture */
  if(fil){
    var r = chrono.getBoundingClientRect(), pointe = innerHeight * .62;
    var f = Math.max(0, Math.min(1, (pointe - r.top) / Math.max(1, r.height)));
    fil.style.setProperty("--f", f.toFixed(4));
    dates.forEach(function(li){
      li.classList.toggle("mo-allume", li.getBoundingClientRect().top + 12 <= pointe);
    });
  }

  if(footer && footer.getBoundingClientRect().top < innerHeight * .85) etoiler();
}
addEventListener("scroll", function(){ if(!tick){ tick = true; requestAnimationFrame(lecture); } }, {passive:true});
addEventListener("resize", function(){ if(ici) suivre(ici, true); lecture(); });
if(document.fonts && document.fonts.ready) document.fonts.ready.then(function(){ if(ici) suivre(ici, true); });

/* ---------- E. ce qui s'éclaire quand on l'atteint ---------- */
var attente = [];
[].forEach.call(document.querySelectorAll(".onde"), function(svg){
  [].forEach.call(svg.querySelectorAll("path"), function(p){
    try{ p.style.setProperty("--len", Math.ceil(p.getTotalLength()) + 1); }catch(e){}
  });
  attente.push(svg);
});
[".notions", ".chiffres", ".plan"].forEach(function(sel){
  [].forEach.call(document.querySelectorAll(sel), function(el){
    [].forEach.call(el.children, function(li, k){ li.style.setProperty("--k", k); });
    attente.push(el);
  });
});
if("IntersectionObserver" in window && !calme()){
  var io = new IntersectionObserver(function(entrees){
    entrees.forEach(function(en){
      if(!en.isIntersecting) return;
      en.target.classList.remove("mo-attente");
      en.target.classList.add("mo-vu");
      io.unobserve(en.target);
    });
  }, {rootMargin:"0px 0px -10% 0px"});
  attente.forEach(function(el){
    /* ce qui est déjà à l'écran au chargement ne bouge pas : la lampe a la scène */
    if(el.getBoundingClientRect().top < innerHeight) return;
    el.classList.add("mo-attente");
    io.observe(el);
  });
}

lecture();
window.MO = {estCalme:calme, etoiler:etoiler};
})();
