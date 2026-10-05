/* =====================================================================
   COUCHE DE MOUVEMENT — « le stylo rouge corrige sous tes yeux »
   A. ouvrir une fiche : chaque faute se fait barrer à la main, puis la
      correction s'écrit, paire après paire
   B. le quiz : une coche se trace sur la bonne réponse, la mauvaise est
      entourée à l'encre rouge ; en fin de série, la note est entourée
   C. la lecture : un trait d'encre s'écrit sous la barre d'onglets
   D. changer d'onglet fait arriver les fiches ; le filet du titre se trace
   Script maintenu à part de index.html. Il ne réécrit aucune fonction du
   site : il écoute les gestes et observe le DOM. Il ne cache jamais rien.
   Aucune persistance.
   ===================================================================== */
(function(){
"use strict";
var R = document.documentElement;
var mq = window.matchMedia ? window.matchMedia("(prefers-reduced-motion: reduce)") : null;
function calme(){ return !!(mq && mq.matches); }
if(!calme()) R.classList.add("mo");
if(mq && mq.addEventListener){ mq.addEventListener("change", function(){ R.classList.toggle("mo", !calme()); }); }
var NS = "http://www.w3.org/2000/svg";

function rejouer(el, classe, ms){
  el.classList.remove(classe); void el.offsetWidth; el.classList.add(classe);
  clearTimeout(el["_mo" + classe]);
  el["_mo" + classe] = setTimeout(function(){ el.classList.remove(classe); }, ms);
}

/* ---------- A. une fiche s'ouvre ---------- */
function corriger(card){
  if(calme()) return;
  var n = 0;
  [].forEach.call(card.querySelectorAll(".pairs"), function(ul){
    [].forEach.call(ul.children, function(li, i){ li.style.setProperty("--k", n + Math.floor(i / 2)); });
    n += Math.ceil(ul.children.length / 2);
  });
  rejouer(card, "mo-ouvre", 900);
  if(n) rejouer(card, "mo-corrige", 600 + Math.min(n, 14) * 320 + 700);
}
/* l'ouverture passe par la classe collapsed retirée : on l'observe plutôt que de réécrire le geste */
var cartes = document.querySelectorAll("section.card");
var oc = new MutationObserver(function(ms){
  var ouvertes = [];
  ms.forEach(function(m){
    var c = m.target;
    var avant = (m.oldValue || "").indexOf("collapsed") >= 0, apres = c.classList.contains("collapsed");
    if(avant && !apres && !c.classList.contains("hidden-by-search") && !recherche) ouvertes.push(c);
  });
  /* « tout déplier » ouvre tout d'un coup : on ne rejoue la correction que sur les fiches à l'écran */
  if(ouvertes.length > 1) ouvertes = ouvertes.filter(function(c){ var r = c.getBoundingClientRect(); return r.bottom > 0 && r.top < innerHeight; });
  ouvertes.forEach(corriger);
});
[].forEach.call(cartes, function(c){ oc.observe(c, {attributes:true, attributeFilter:["class"], attributeOldValue:true}); });
/* une recherche déplie les fiches trouvées : ce n'est pas un geste d'ouverture */
var recherche = false;
var si = document.getElementById("searchInput");
if(si) si.addEventListener("input", function(){ recherche = si.value.trim().length >= 2; });

/* ---------- B. le quiz ---------- */
function marque(btn, type){
  var s = document.createElementNS(NS, "svg");
  s.setAttribute("class", "mo-marque " + type);
  s.setAttribute("aria-hidden", "true");
  var forme;
  if(type === "mo-coche"){
    s.setAttribute("viewBox", "0 0 26 22");
    forme = document.createElementNS(NS, "path");
    forme.setAttribute("d", "M3 12.5 C5.5 14 7.5 16.5 9.5 19.5 C12.5 12 17.5 6 23.5 2.5");
  } else {
    /* l'ellipse est construite aux dimensions réelles, en pixels : sa longueur mesurée
       est bien celle qui se trace */
    var W = btn.offsetWidth + (type === "mo-note" ? 32 : 24), H = btn.offsetHeight + (type === "mo-note" ? 22 : 14);
    s.setAttribute("viewBox", "0 0 " + W + " " + H);
    /* une boucle de stylo : bords arrondis qui épousent tout le bouton, et un trait qui
       dépasse son point de départ, comme quand on entoure à la main */
    var r = Math.max(4, H / 2 - 2.5), g = 2.5, d = W - 2.5;
    forme = document.createElementNS(NS, "path");
    forme.setAttribute("d", "M" + (g + r + 8) + "," + (g + 1.2) + " L" + (d - r) + "," + g
      + " A" + r + "," + r + " 0 0 1 " + d + "," + (H / 2) + " A" + r + "," + r + " 0 0 1 " + (d - r) + "," + (H - g)
      + " L" + (g + r) + "," + (H - g - .8) + " A" + r + "," + r + " 0 0 1 " + g + "," + (H / 2 + .6) + " A" + r + "," + r + " 0 0 1 " + (g + r + 2) + "," + (g + .4)
      + " L" + (g + r + Math.min(60, W * .18)) + "," + (g + 2.6));
    forme.setAttribute("transform", "rotate(-.5 " + W / 2 + " " + H / 2 + ")");
  }
  s.appendChild(forme);
  btn.appendChild(s);
  try{ forme.style.setProperty("--l", Math.ceil(forme.getTotalLength()) + 2); }catch(e){}
  return s;
}
document.addEventListener("click", function(ev){
  var b = ev.target.closest ? ev.target.closest(".opts button") : null;
  if(!b) return;
  /* le site a déjà corrigé dans son propre écouteur : on lit le verdict qu'il a posé */
  requestAnimationFrame(function(){
    var opts = b.closest(".opts");
    if(!opts || opts._mo) return;
    opts._mo = true;
    var juste = opts.querySelector("button.good");
    if(juste && !juste.querySelector(".mo-coche")) marque(juste, "mo-coche");
    if(b.classList.contains("bad")){
      marque(b, "mo-cercle");
      if(!calme()) rejouer(b, "mo-secoue", 450);
    }
    note();
  });
});
var score = document.getElementById("quizScore");
function note(){
  if(!score) return;
  var vieille = score.querySelector(".mo-note");
  if(/terminée/.test(score.textContent)){
    if(!vieille) marque(score, "mo-note");
  } else if(vieille) vieille.remove();
}
/* une nouvelle série recrée les questions et réécrit le score : l'ellipse partirait avec */
if(score) new MutationObserver(function(){
  if(score.querySelector(".mo-note") || !/terminée/.test(score.textContent)) return;
  marque(score, "mo-note");
}).observe(score, {childList:true, characterData:true, subtree:true});

/* ---------- C. le trait d'encre de la lecture ---------- */
var encre = document.createElement("div");
encre.id = "mo-encre"; encre.setAttribute("aria-hidden", "true");
encre.innerHTML = '<i class="e-trait"></i><span class="e-plume"><svg viewBox="0 0 16 16" fill="currentColor"><path d="M1.5 14.5 L3 10 L11.5 1.5 L14.5 4.5 L6 13 Z" opacity=".9"/><path d="M1.5 14.5 L3 10 L6 13 Z" fill="#fff" opacity=".55"/></svg></span>';
document.body.appendChild(encre);
var barre = document.querySelector(".bar"), tick = false, arret = 0;
function lecture(){
  tick = false;
  var h = R.scrollHeight - innerHeight;
  if(h < 400){ encre.classList.remove("on"); return; }
  var hb = barre ? Math.max(0, Math.round(barre.getBoundingClientRect().bottom)) : 0;
  encre.style.setProperty("--haut", (hb - 1) + "px");
  encre.style.setProperty("--p", Math.max(0, Math.min(1, scrollY / h)).toFixed(4));
  encre.classList.add("on");
  /* la plume s'agite tant qu'on défile, puis se pose */
  encre.classList.add("ecrit");
  clearTimeout(arret); arret = setTimeout(function(){ encre.classList.remove("ecrit"); }, 260);
}
addEventListener("scroll", function(){ if(!tick){ tick = true; requestAnimationFrame(lecture); } }, {passive:true});
addEventListener("resize", lecture);

/* ---------- D. onglets et titre ---------- */
var tabbar = document.getElementById("tabbar");
if(tabbar) tabbar.addEventListener("click", function(ev){
  var t = ev.target.closest ? ev.target.closest("button[data-tab]") : null;
  if(!t || calme()) return;
  requestAnimationFrame(function(){
    var p = document.getElementById(t.dataset.tab);
    if(p) rejouer(p, "mo-arrive", 900);
    lecture();
  });
});
var filet = document.querySelector(".filet-titre");
if(filet && !calme()) rejouer(filet, "mo-trace", 1600);

lecture();
window.MO = {estCalme:calme};
})();
