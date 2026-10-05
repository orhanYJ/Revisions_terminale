/* =====================================================================
   COUCHE DE MOUVEMENT — « la reliure s'ouvre, la dorure prend la lumière »
   Script commun aux trois sites ACL écrit ; seule la ligne MOTIF change.
   A. la couverture s'ouvre : un éclat court le long du filet doré, le titre
      prend la lumière ; le motif de l'œuvre se dessine sur le plat et
      répond à la main (fleuron, lotus brodé, onde de la radio)
   B. la tranche de lecture : sous la barre, la dorure (ou le fil, ou
      l'onde) avance avec la lecture
   C. changer de page : la feuille tourne, le filet du titre se dore ; un
      guide doré glisse d'un onglet et d'une entrée du rail à l'autre
   D. les blocs du dessous arrivent quand on les atteint ; une citation
      retrouvée s'écrit ; un paquet mélangé se redistribue
   Script maintenu à part de index.html. Il ne réécrit aucune fonction du
   site : il écoute les gestes et observe le DOM. Il ne cache jamais ce qui
   est déjà à l'écran. Aucune persistance.
   ===================================================================== */
(function(){
"use strict";
var MOTIF = "fleuron";   /* fleuron (l'épreuve) · kantha (Brick Lane) · marconi (Lughnasa) */

var R = document.documentElement;
var mq = window.matchMedia ? window.matchMedia("(prefers-reduced-motion: reduce)") : null;
function calme(){ return !!(mq && mq.matches); }
R.classList.toggle("mo", !calme());
if(mq && mq.addEventListener){ mq.addEventListener("change", function(){ R.classList.toggle("mo", !calme()); }); }
var NS = "http://www.w3.org/2000/svg";
var $ = function(s, r){ return (r || document).querySelector(s); };
var $$ = function(s, r){ return [].slice.call((r || document).querySelectorAll(s)); };
var ajouts = [];   /* tout ce que cette couche insère dans la page */

function rejouer(el, classe, ms){
  el.classList.remove(classe); void el.offsetWidth; el.classList.add(classe);
  clearTimeout(el["_mo" + classe]);
  el["_mo" + classe] = setTimeout(function(){ el.classList.remove(classe); }, ms);
}

/* ---------- A. la couverture ---------- */
var board = $(".board"), boardIn = $(".board-in");
var decor = null, onde = null;

function svg(vb){ var s = document.createElementNS(NS, "svg"); s.setAttribute("viewBox", vb); s.setAttribute("aria-hidden", "true"); return s; }
function trait(parent, d, k, cls){
  var p = document.createElementNS(NS, "path");
  p.setAttribute("d", d); p.setAttribute("class", cls || "d");
  if(k != null) p.style.setProperty("--k", k);
  parent.appendChild(p);
  try{ p.style.setProperty("--l", Math.ceil(p.getTotalLength()) + 2); }catch(e){}
  return p;
}
function point(parent, x, y, r, k){
  var c = document.createElementNS(NS, "circle");
  c.setAttribute("cx", x); c.setAttribute("cy", y); c.setAttribute("r", r); c.setAttribute("class", "pt");
  c.style.setProperty("--k", k); c.style.transformOrigin = x + "px " + y + "px";
  parent.appendChild(c);
}

/* l'épreuve : un fleuron de relieur, poussé au fer doré */
function fleuron(s){
  var g = document.createElementNS(NS, "g"); s.appendChild(g);
  trait(g, "M40 40 H260 V260 H40 Z", 0, "d fin");
  trait(g, "M50 50 H250 V250 H50 Z", 0, "d fin");
  trait(g, "M150 70 V230", 1);
  trait(g, "M150 112 L188 150 L150 188 L112 150 Z", 2);
  trait(g, "M150 112 C150 84 186 74 196 96 C202 111 184 119 176 107", 3);
  trait(g, "M150 112 C150 84 114 74 104 96 C98 111 116 119 124 107", 3);
  trait(g, "M150 188 C150 216 186 226 196 204 C202 189 184 181 176 193", 4);
  trait(g, "M150 188 C150 216 114 226 104 204 C98 189 116 181 124 193", 4);
  trait(g, "M188 150 C206 136 226 138 236 150 C226 162 206 164 188 150 Z", 5);
  trait(g, "M112 150 C94 136 74 138 64 150 C74 162 94 164 112 150 Z", 5);
  trait(g, "M50 50 C70 52 80 62 82 82 M250 50 C230 52 220 62 218 82 M50 250 C70 248 80 238 82 218 M250 250 C230 248 220 238 218 218", 6, "d fin");
  point(g, 150, 150, 5, 6); point(g, 150, 62, 3, 7); point(g, 150, 238, 3, 7);
  point(g, 244, 150, 3, 8); point(g, 56, 150, 3, 8);
}

/* Brick Lane : un lotus de nakshi kantha, brodé point après point */
function kantha(s){
  var fils = ["#D06A7E", "#C4A052", "#5FA79C"];
  var dessin = [
    [0, "M150 92 C176 126 176 164 150 194 C124 164 124 126 150 92 Z"],
    [2, "M150 194 C121 180 98 150 102 118 C126 128 145 158 150 194"],
    [2, "M150 194 C179 180 202 150 198 118 C174 128 155 158 150 194"],
    [1, "M150 194 C112 196 78 178 66 150 C98 146 132 166 150 194"],
    [1, "M150 194 C188 196 222 178 234 150 C202 146 168 166 150 194"],
    [2, "M78 222 C102 210 124 232 150 220 C176 208 198 230 222 218"],
    [1, "M64 240 C96 230 120 250 150 240 C180 230 204 250 236 240"],
    [0, "M150 34 A116 116 0 1 1 149.9 34"]
  ];
  var g = document.createElementNS(NS, "g"); s.appendChild(g);
  var k = 0;
  dessin.forEach(function(t){
    var guide = document.createElementNS(NS, "path");
    guide.setAttribute("d", t[1]);
    var L = 0;
    try{ L = guide.getTotalLength(); }catch(e){}
    if(!L) return;
    /* points avant : 6 de fil, 4 de toile */
    for(var x = 0; x + 6 <= L; x += 10){
      var a = guide.getPointAtLength(x), b = guide.getPointAtLength(x + 6);
      var l = document.createElementNS(NS, "line");
      l.setAttribute("x1", a.x.toFixed(1)); l.setAttribute("y1", a.y.toFixed(1));
      l.setAttribute("x2", b.x.toFixed(1)); l.setAttribute("y2", b.y.toFixed(1));
      l.setAttribute("class", "point"); l.setAttribute("stroke", fils[t[0]]);
      l.style.setProperty("--k", k++);
      g.appendChild(l);
    }
  });
  point(g, 150, 150, 3.5, 20);
}

/* Lughnasa : l'onde de la Marconi, et cinq sœurs qui y dansent */
function marconi(s){
  var g = document.createElementNS(NS, "g"); s.appendChild(g);
  var arcs = [];
  [14, 28, 42].forEach(function(r, i){
    var a = document.createElementNS(NS, "path");
    a.setAttribute("d", "M" + (150 - r * .8) + " " + (84 - r * .6) + " A" + r + " " + r + " 0 0 1 " + (150 + r * .8) + " " + (84 - r * .6));
    a.setAttribute("class", "arc"); g.appendChild(a); arcs.push(a);
  });
  var mat = document.createElementNS(NS, "path");
  mat.setAttribute("d", "M150 84 V112 M140 112 H160");
  mat.setAttribute("class", "arc"); mat.style.opacity = ".7"; g.appendChild(mat);
  var ligne = document.createElementNS(NS, "path");
  ligne.setAttribute("class", "onde"); g.appendChild(ligne);
  var soeurs = [];
  for(var i = 0; i < 5; i++){
    var c = document.createElementNS(NS, "circle");
    c.setAttribute("r", "4.2"); c.setAttribute("class", "soeur"); g.appendChild(c); soeurs.push(c);
  }
  var energie = 0, phase = 0, fil = 0;
  function y(x, A){ return 170 + A * Math.sin(x * .055 - phase) * Math.sin(Math.PI * (x - 20) / 260); }
  function dessiner(){
    var A = 3 + energie * 34, d = "";
    for(var x = 20; x <= 280; x += 4) d += (x === 20 ? "M" : " L") + x + " " + y(x, A).toFixed(1);
    ligne.setAttribute("d", d);
    soeurs.forEach(function(c, i){
      var x = 70 + i * 40;
      c.setAttribute("cx", x);
      c.setAttribute("cy", (y(x, A) - 7 - energie * 6 * Math.abs(Math.sin(phase * 1.5 + i))).toFixed(1));
    });
    arcs.forEach(function(a, i){ a.style.opacity = (.35 + .6 * Math.max(0, energie - i * .18)).toFixed(2); });
  }
  function boucle(){
    fil = 0;
    if(document.hidden || calme()){ energie = 0; dessiner(); return; }
    phase += .05 + energie * .22;
    energie *= .975;
    if(energie < .01) energie = 0;
    dessiner();
    if(energie > 0) fil = requestAnimationFrame(boucle);
  }
  dessiner();
  return { relance: function(e){ if(calme() || !s.parentNode.offsetWidth) return; energie = Math.min(1, energie + e); if(!fil) fil = requestAnimationFrame(boucle); } };
}

if(board && boardIn){
  decor = document.createElement("div");
  decor.className = "mo-decor"; decor.setAttribute("aria-hidden", "true");
  var s = svg("0 0 300 300");
  decor.appendChild(s);
  boardIn.appendChild(decor);
  ajouts.push(decor);
  if(MOTIF === "kantha") kantha(s);
  else if(MOTIF === "marconi") onde = marconi(s);
  else fleuron(s);
  if(!calme()){
    if(MOTIF !== "marconi") decor.classList.add("mo-trace");
    $$(".rubric li", board).forEach(function(li, i){ li.style.setProperty("--k", Math.floor(i / 2)); });
    rejouer(board, "mo-ouvre", 1600);
    rejouer(board, "mo-eclat", 1800);
    if(onde) setTimeout(function(){ onde.relance(1); }, 300);
  }
  /* la main sur la couverture : la dorure reprend la lumière (pas plus d'une fois toutes les quatre secondes) */
  var dernier = Date.now();
  board.addEventListener("pointerenter", function(){
    if(calme() || Date.now() - dernier < 4000) return;
    dernier = Date.now();
    rejouer(board, "mo-eclat", 1800);
    if(MOTIF !== "marconi") rejouer(decor, "mo-luit", 1500);
  });
  /* la radio : la main qui passe relance la musique */
  if(onde){
    var px = null, py = null;
    board.addEventListener("pointermove", function(ev){
      if(px !== null) onde.relance(Math.min(.2, Math.hypot(ev.clientX - px, ev.clientY - py) / 400));
      px = ev.clientX; py = ev.clientY;
    });
    board.addEventListener("pointerleave", function(){ px = py = null; });
    board.addEventListener("pointerdown", function(){ onde.relance(.6); });
  }
}

/* ---------- B. la tranche de lecture ---------- */
var topbar = $(".topbar");
var tranche = document.createElement("div");
tranche.id = "mo-tranche"; tranche.setAttribute("aria-hidden", "true");
var toile = null, ctx = null, vibre = 0, vfil = 0, vphase = 0, pLu = 0;
if(MOTIF === "marconi"){
  toile = document.createElement("canvas");
  tranche.appendChild(toile);
  ctx = toile.getContext && toile.getContext("2d");
} else {
  tranche.className = MOTIF === "kantha" ? "t-fil" : "";
  tranche.innerHTML = '<i class="t-trait"></i><i class="t-tete"></i>';
}
document.body.appendChild(tranche);
ajouts.push(tranche);

function ondeTranche(){
  if(!ctx) return;
  var dpr = Math.min(2, window.devicePixelRatio || 1), W = innerWidth, H = 12;
  if(toile.width !== Math.round(W * dpr)){ toile.width = Math.round(W * dpr); toile.height = H * dpr; }
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  ctx.clearRect(0, 0, W, H);
  var fin = pLu * W;
  if(fin < 1) return;
  var A = .4 + vibre * 4;
  var grad = ctx.createLinearGradient(0, 0, W, 0);
  grad.addColorStop(0, "#C4A052"); grad.addColorStop(1, "#E6CB8B");
  ctx.strokeStyle = grad; ctx.lineWidth = 2; ctx.lineCap = "round"; ctx.lineJoin = "round";
  ctx.beginPath();
  for(var x = 0; x <= fin; x += 3){
    var amort = Math.min(1, (fin - x) / 160);   /* l'onde vit surtout près de la tête */
    var yy = 6 + A * amort * Math.sin(x * .09 - vphase);
    if(x === 0) ctx.moveTo(x, yy); else ctx.lineTo(x, yy);
  }
  ctx.stroke();
  ctx.fillStyle = "rgba(255,243,210,.95)";
  ctx.beginPath(); ctx.arc(fin, 6, 2.4, 0, Math.PI * 2); ctx.fill();
}
function vibrer(){
  vfil = 0;
  vphase += .25 + vibre * .3;
  vibre *= .92;
  if(vibre < .02 || calme()) vibre = 0;
  ondeTranche();
  if(vibre > 0) vfil = requestAnimationFrame(vibrer);
}

var tick = false, arret = 0, yAvant = scrollY;
function lecture(){
  tick = false;
  var h = R.scrollHeight - innerHeight;
  if(h < 400){ tranche.classList.remove("on"); return; }
  var hb = topbar ? Math.max(0, Math.round(topbar.getBoundingClientRect().bottom)) : 0;
  tranche.style.setProperty("--haut", hb + "px");
  pLu = Math.max(0, Math.min(1, scrollY / h));
  tranche.style.setProperty("--p", pLu.toFixed(4));
  tranche.classList.add("on");
  if(ctx){
    if(!calme()){ vibre = Math.min(1, vibre + Math.min(Math.abs(scrollY - yAvant), 80) / 160); if(!vfil) vfil = requestAnimationFrame(vibrer); }
    ondeTranche();
  } else {
    /* l'aiguille pique tant qu'on défile, puis se pose */
    tranche.classList.add("ecrit");
    clearTimeout(arret); arret = setTimeout(function(){ tranche.classList.remove("ecrit"); }, 260);
  }
  yAvant = scrollY;
  if(scrollY >= h - 2) auBout();
}
/* tout en bas de la page, la marge de l'observateur ne peut plus être franchie : on montre ce qui reste */
function auBout(){
  $$(".mo-attente").forEach(function(el){
    if(el.getBoundingClientRect().top >= innerHeight) return;
    el.classList.remove("mo-attente");
    if(io) io.unobserve(el);
  });
}
addEventListener("scroll", function(){ if(!tick){ tick = true; requestAnimationFrame(lecture); } }, {passive:true});
addEventListener("resize", function(){ lecture(); guides(true); });

/* ---------- C. changer de page ---------- */
function vue(){
  var a = $(".area.on");
  var p = a && $(":scope > .pane.on", a);
  if(!p) return a;
  if(p.classList.contains("showall")) return p;
  return $(":scope > .leaf.on", p) || p;
}

/* l'onglet en cours : un souligné doré glisse d'un onglet à l'autre */
var areas = $(".areas"), souligne = null;
if(areas){
  souligne = document.createElement("i");
  souligne.className = "mo-souligne"; souligne.setAttribute("aria-hidden", "true");
  areas.appendChild(souligne);
  ajouts.push(souligne);
}
function placeSouligne(sansAnim){
  if(!souligne) return;
  var b = $('button[aria-current="true"]', areas);
  if(!b || !b.offsetWidth){ areas.classList.remove("mo-glisse"); return; }
  var x = b.offsetLeft + 4, w = b.offsetWidth - 8;
  if(sansAnim || calme() || !souligne._x){
    souligne.style.transform = "translateX(" + x + "px)"; souligne.style.width = w + "px";
  } else if(souligne.animate){
    souligne.animate([
      {transform:"translateX(" + souligne._x + "px)", width:souligne._w + "px"},
      {transform:"translateX(" + x + "px)", width:w + "px"}
    ], {duration:420, easing:"cubic-bezier(.3,1.2,.4,1)"});
    souligne.style.transform = "translateX(" + x + "px)"; souligne.style.width = w + "px";
  }
  souligne._x = x; souligne._w = w;
  areas.classList.add("mo-glisse");
}

/* le rail : son signet doré glisse jusqu'à l'entrée en cours. Le rail est
   réécrit à chaque affichage : on le suit plutôt que de toucher à son rendu */
var edge = $("#edge"), signet = null, signetY = null;
function placeSignet(){
  if(!edge || !edge.offsetWidth) return;
  var a = $('a[aria-current="true"]', edge);
  if(!a){ edge.classList.remove("mo-glisse"); return; }
  if(!signet){
    signet = document.createElement("i");
    signet.className = "mo-signet"; signet.setAttribute("aria-hidden", "true");
  }
  if(signet.parentNode !== edge) edge.appendChild(signet);
  var y = a.offsetTop, h = a.offsetHeight, x = a.offsetLeft;
  signet.style.left = x + "px";
  signet.style.height = h + "px";
  signet.style.transform = "translateY(" + y + "px)";
  if(signetY !== null && signetY !== y && !calme() && signet.animate){
    signet.animate([{transform:"translateY(" + signetY + "px)"}, {transform:"translateY(" + y + "px)"}],
      {duration:380, easing:"cubic-bezier(.3,1.15,.4,1)"});
  }
  signetY = y;
  edge.classList.add("mo-glisse");
}
if(edge) new MutationObserver(function(){
  if(signet && signet.parentNode !== edge) placeSignet();
}).observe(edge, {childList:true});

function guides(sansAnim){ placeSouligne(sansAnim); placeSignet(); }

/* la feuille tourne */
function tourner(v){
  if(!v || calme()) return;
  if(v.animate) v.animate([
    {opacity:0, transform:"perspective(1400px) rotateY(-7deg) translateX(16px)", transformOrigin:"0 50%"},
    {opacity:1, transform:"none", transformOrigin:"0 50%"}
  ], {duration:520, easing:"cubic-bezier(.2,.8,.2,1)"});
  rejouer(v, "mo-tourne", 1400);
}

/* ---------- D. les blocs qui arrivent ---------- */
var BLOCS = ".card,.cit-entry,.panel,.essay,.rewrite,.tbl-wrap,.verdict,.margin-note,.method-note,.gloss,.fiche-ref,.placeholder,.two-col,ol.steps > li,ul.dash,.scene,.check";
var io = ("IntersectionObserver" in window) ? new IntersectionObserver(function(entrees){
  var n = 0;
  entrees.forEach(function(en){
    if(!en.isIntersecting) return;
    var el = en.target;
    el.style.setProperty("--k", n++);
    el.classList.add("mo-vu");
    el.classList.remove("mo-attente");
    io.unobserve(el);
    setTimeout(function(){ el.classList.remove("mo-vu"); el.style.removeProperty("--k"); }, 1400);
  });
}, {rootMargin:"0px 0px -8% 0px"}) : null;

function preparer(v){
  if(!io) return;
  $$(".mo-attente").forEach(function(el){ el.classList.remove("mo-attente"); io.unobserve(el); });
  if(!v || calme()) return;
  var bas = innerHeight;
  $$(BLOCS, v).forEach(function(el){
    var parent = el.parentElement && el.parentElement.closest(BLOCS);
    if(parent && v.contains(parent)) return;   /* un bloc dans un bloc arrive avec lui */
    if(!el.offsetHeight || el.getBoundingClientRect().top < bas) return;   /* déjà à l'écran : on n'y touche pas */
    el.classList.add("mo-attente");
    io.observe(el);
  });
}

function nouvellePage(){
  var v = vue();
  guides(false);
  tourner(v);
  /* le site remonte en haut de page juste avant : on mesure après */
  requestAnimationFrame(function(){ preparer(v); lecture(); });
}
addEventListener("hashchange", nouvellePage);
/* la langue change la largeur des onglets */
$$("#btn-fr,#btn-en").forEach(function(b){ b.addEventListener("click", function(){ requestAnimationFrame(function(){ guides(true); }); }); });
document.addEventListener("click", function(ev){
  if(!ev.target.closest) return;
  if(ev.target.closest("[data-showall]")) requestAnimationFrame(function(){ preparer(vue()); lecture(); });
  var b;
  /* une citation retrouvée */
  if((b = ev.target.closest("[data-reveal]")) && !calme()){
    var carte = b.closest(".cit-entry"), hote = carte && carte.closest("[data-bank]");
    if(carte) rejouer(carte, "mo-revele", 1300);
    if(hote){
      var toutes = $$(":scope > .cit-entry", hote);
      if(toutes.length && toutes.every(function(c){ return c.classList.contains("shown"); })){
        var sc = $(".score", hote);
        if(sc) rejouer(sc, "mo-complet", 900);
      }
    }
  }
  /* un paquet mélangé ou un changement de mode : les fiches se redistribuent */
  if((b = ev.target.closest("[data-shuffle],[data-mode]")) && !calme()){
    var h = b.closest("[data-bank]");
    if(!h) return;
    requestAnimationFrame(function(){
      var bas = innerHeight, k = 0;
      $$(":scope > .cit-entry", h).forEach(function(c){
        c.classList.remove("mo-attente");
        var r = c.getBoundingClientRect();
        c.style.setProperty("--k", (r.top < bas && r.bottom > 0) ? k++ : 0);
      });
      rejouer(h, "mo-donne", 1200);
    });
  }
});

/* ---------- l'enregistrement du fichier ne doit rien emporter de cette couche ---------- */
if(typeof window.citSaveFile === "function"){
  var enregistrer = window.citSaveFile;
  window.citSaveFile = function(){
    var places = ajouts.concat(signet ? [signet] : []).filter(function(n){ return n.parentNode; })
      .map(function(n){ return {n:n, p:n.parentNode, s:n.nextSibling}; });
    places.forEach(function(o){ o.p.removeChild(o.n); });
    var marques = $$('[class*="mo-"]').map(function(el){
      var c = [].filter.call(el.classList, function(x){ return x.indexOf("mo-") === 0; });
      c.forEach(function(x){ el.classList.remove(x); });
      return {el:el, c:c};
    });
    var avait = R.classList.contains("mo");
    R.classList.remove("mo");
    try{ return enregistrer.apply(this, arguments); }
    finally{
      places.forEach(function(o){ o.p.insertBefore(o.n, o.s && o.s.parentNode === o.p ? o.s : null); });
      marques.forEach(function(m){ m.c.forEach(function(x){ if(x !== "mo-attente") m.el.classList.add(x); }); });
      if(avait) R.classList.add("mo");
    }
  };
}

/* ---------- démarrage ---------- */
guides(true);
placeSignet();
preparer(vue());
lecture();
if(document.fonts && document.fonts.ready) document.fonts.ready.then(function(){ guides(true); lecture(); });
window.MO = {estCalme:calme};
})();
