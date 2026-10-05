/* =====================================================================
   COUCHE DE MOUVEMENT — « ogni capitolo letto posa una tessera »
   A. le mosaïque du manuel : une tesselle par chapitre, posée quand
      on arrive au bout de sa lecture
   B. un cadre ocre glisse d'un onglet à l'autre
   C. le chapitre qui s'ouvre se compose : badge, titre, filet, blocs
   D. le filet tricolore de l'en-tête suit la lecture ; au bout,
      il projette des tesselles
   E. précédent / suivant : la page se tourne dans le bon sens
   Script maintenu à part de index.html. Il ne réécrit aucune fonction
   du site (elles sont privées) : il observe le DOM et répond aux gestes.
   Il ne cache jamais rien. Aucune persistance : le mosaïque vit le
   temps de la session.
   ===================================================================== */
(function(){
"use strict";
var R = document.documentElement;
var mq = window.matchMedia ? window.matchMedia("(prefers-reduced-motion: reduce)") : null;
function calme(){ return !!(mq && mq.matches); }
if(!calme()) R.classList.add("mo");
if(mq && mq.addEventListener){ mq.addEventListener("change", function(){ R.classList.toggle("mo", !calme()); }); }

var caps = [].slice.call(document.querySelectorAll("section.cap"));
var header = document.querySelector("header");
if(!caps.length || !header) return;

var ORDINE = ["gram", "coniug", "less", "seq"];
var COLORE = {A2:"var(--verde)", B1:"var(--azzurro)", B2:"var(--rosso)"};
var SCHEGGE = ["var(--verde)", "var(--rosso)", "var(--azzurro)", "var(--ocra)", "#fff", "var(--verde-s)"];
var letti = {}, nLetti = 0;
function capAtt(){ return document.querySelector("section.cap.att"); }
function colore(c){ return COLORE[c.getAttribute("data-liv")] || "var(--ocra)"; }
/* rotation stable par chapitre : les tesselles semblent posées à la main */
function rot(id){ var s = 0; for(var i = 0; i < id.length; i++) s = (s * 31 + id.charCodeAt(i)) % 997; return ((s % 9) - 4) * .9; }

/* ---------- couche des tesselles projetées ---------- */
var couche = document.createElement("div");
couche.id = "mo-couche"; couche.setAttribute("aria-hidden", "true");
document.body.appendChild(couche);
function schegge(x, y, n){
  if(calme()) return;
  for(var k = 0; k < n; k++){
    /* elles tombent vers la page, en éventail sous le point d'émission */
    var p = document.createElement("i"), a = Math.PI * .62 + (Math.random() - .5) * Math.PI * .95, d = 50 + Math.random() * 120;
    p.className = "mo-scheggia";
    p.style.left = x + "px"; p.style.top = y + "px";
    p.style.setProperty("--c", SCHEGGE[k % SCHEGGE.length]);
    p.style.setProperty("--s", (6 + Math.random() * 6).toFixed(1) + "px");
    p.style.setProperty("--dx", (Math.cos(a) * d).toFixed(1) + "px");
    p.style.setProperty("--dy", (Math.sin(a) * d).toFixed(1) + "px");
    p.style.setProperty("--r", ((Math.random() - .5) * 540).toFixed(0) + "deg");
    p.style.animationDelay = (Math.random() * 90 | 0) + "ms";
    couche.appendChild(p);
    setTimeout((function(el){ return function(){ el.remove(); }; })(p), 1400);
  }
}

/* ---------- A. le mosaïque du manuel ---------- */
var ordinati = [];
ORDINE.forEach(function(t){ caps.forEach(function(c){ if(c.getAttribute("data-tab") === t) ordinati.push(c); }); });
caps.forEach(function(c){ if(ordinati.indexOf(c) < 0) ordinati.push(c); });
var tessere = {};
var mos = document.createElement("div"), griglia = document.createElement("div"), leg = document.createElement("p");
mos.className = "mo-mosaico";
mos.innerHTML = '<p class="mo-tit">Il mosaico del manuale</p>';
griglia.className = "mo-griglia";
griglia.style.setProperty("--n", ordinati.length);
ordinati.forEach(function(c){
  var b = document.createElement("button"), titolo = c.getAttribute("data-titolo") || c.id;
  b.type = "button"; b.className = "mo-tessera";
  b.style.setProperty("--c", colore(c));
  b.style.setProperty("--rot", rot(c.id).toFixed(1) + "deg");
  b.title = titolo;
  b.setAttribute("aria-label", "Apri il capitolo : " + titolo);
  b.addEventListener("click", function(){ apri(c.id); });
  griglia.appendChild(b);
  tessere[c.id] = b;
});
leg.className = "mo-leg";
mos.appendChild(griglia); mos.appendChild(leg);
var aside = document.querySelector(".corpo > aside");
if(aside){
  var bi = document.getElementById("btn-indice");
  aside.insertBefore(mos, bi ? bi.nextSibling : aside.firstChild);
}
function legenda(){
  var n = ordinati.length;
  leg.innerHTML = nLetti === 0
    ? 'Arriva in fondo a un capitolo per posare la sua tessera. <span class="mo-astuce">Tocca una tessera per aprire il capitolo.</span>'
    : "<b>" + nLetti + (nLetti > 1 ? " tessere posate" : " tessera posata") + "</b> su " + n + " — in questa sessione."
      + (nLetti === n ? " Il mosaico è completo." : "");
}
legenda();
function corrente(){
  var c = capAtt();
  Object.keys(tessere).forEach(function(id){ tessere[id].classList.toggle("corrente", !!c && c.id === id); });
}

/* chapitres lus : une petite tesselle devant leur numéro dans l'index */
var indice = document.getElementById("indice");
function segnaIndice(){
  if(!indice) return;
  [].forEach.call(indice.querySelectorAll("a[data-cap]"), function(a){
    var id = a.getAttribute("data-cap"), c = document.getElementById(id);
    a.classList.toggle("mo-letto", !!letti[id]);
    if(c) a.style.setProperty("--c", colore(c));
  });
}
if(indice) new MutationObserver(segnaIndice).observe(indice, {childList:true});

/* ---------- E. changer de chapitre dans une transition de vue ---------- */
var passa = false;
function senza(fn){ passa = true; try{ fn(); } finally{ passa = false; } }
function transizione(fn, verso){
  if(calme() || !document.startViewTransition){ senza(fn); return; }
  R.setAttribute("data-mo-verso", verso || "salto");
  var vt;
  try{ vt = document.startViewTransition(function(){ senza(fn); }); }
  catch(e){ R.removeAttribute("data-mo-verso"); senza(fn); return; }
  vt.finished.then(fine, fine);
  function fine(){ R.removeAttribute("data-mo-verso"); }
}
/* chaque geste qui change de chapitre est rejoué à l'intérieur de la transition :
   la fonction d'origine du site s'exécute telle quelle */
document.addEventListener("click", function(ev){
  if(passa || calme() || !document.startViewTransition) return;
  var t = ev.target.closest ? ev.target.closest(".nav-cap button, #indice a, nav.tabs button, #risultati a") : null;
  if(!t || t.disabled) return;
  ev.preventDefault(); ev.stopImmediatePropagation();
  var verso = "salto";
  if(t.closest(".nav-cap")) verso = t === t.parentNode.firstElementChild ? "indietro" : "avanti";
  transizione(function(){ t.click(); }, verso);
}, true);
function apri(id){
  var c = document.getElementById(id); if(!c) return;
  transizione(function(){
    var att = capAtt(), tab = c.getAttribute("data-tab");
    if(!att || att.getAttribute("data-tab") !== tab){
      var tb = document.querySelector('nav.tabs button[data-tab="' + tab + '"]');
      if(tb) tb.click();
    }
    var a = indice && indice.querySelector('a[data-cap="' + id + '"]');
    if(a) a.click();
  }, "salto");
}

/* ---------- B. le cadre ocre des onglets ---------- */
var nav = document.querySelector("nav.tabs"), cur = null;
if(nav){
  cur = document.createElement("span");
  cur.className = "mo-cursore"; cur.setAttribute("aria-hidden", "true");
  nav.insertBefore(cur, nav.firstChild);
  nav.classList.add("mo-a-cursore");
}
function cursore(sansAnim){
  if(!cur) return;
  var b = nav.querySelector("button.att");
  if(!b){ cur.style.opacity = "0"; return; }
  if(sansAnim) cur.style.transition = "none";
  cur.style.opacity = "1";
  cur.style.width = b.offsetWidth + "px";
  cur.style.height = (b.offsetHeight + 1) + "px";
  cur.style.transform = "translate(" + b.offsetLeft + "px," + b.offsetTop + "px)";
  if(sansAnim){ void cur.offsetWidth; cur.style.transition = ""; }
}

/* ---------- C. le chapitre qui s'ouvre ---------- */
var ultima = null, finTimer = 0;
function entra(c){
  if(calme()) return;
  c.classList.remove("mo-entra"); void c.offsetWidth; c.classList.add("mo-entra");
  clearTimeout(finTimer);
  finTimer = setTimeout(function(){ c.classList.remove("mo-entra"); }, 1600);
}
function cambio(){
  var c = capAtt();
  if(!c || c === ultima) return;
  if(ultima) ultima.classList.remove("mo-entra");
  ultima = c;
  entra(c);
  corrente();
  cursore(false);
  finita = false;
  avvio = Date.now();
  requestAnimationFrame(lettura);
}
var oc = new MutationObserver(cambio);
caps.forEach(function(c){ oc.observe(c, {attributes:true, attributeFilter:["class"]}); });

/* ---------- D. le filet tricolore suit la lecture ---------- */
var tric = header.querySelector(".tric"), velo = null, perla = null;
if(tric){
  velo = document.createElement("i"); velo.id = "mo-velo"; velo.setAttribute("aria-hidden", "true");
  perla = document.createElement("i"); perla.id = "mo-perla"; perla.setAttribute("aria-hidden", "true");
  tric.appendChild(velo); tric.appendChild(perla);
}
var finita = false, avvio = Date.now(), tick = false, attesa = 0;
function posa(c){
  if(letti[c.id]) return;
  letti[c.id] = true; nLetti++;
  var t = tessere[c.id];
  if(t){
    t.classList.add("posata");
    if(!calme()){ t.classList.remove("nuova"); void t.offsetWidth; t.classList.add("nuova"); }
  }
  segnaIndice();
  legenda();
}
function lettura(){
  tick = false;
  var c = capAtt();
  if(!c || !tric) return;
  var h = document.documentElement.scrollHeight - innerHeight;
  if(h < 260){
    /* chapitre court : il tient à l'écran, on le considère lu après un moment */
    velo.classList.remove("on"); perla.classList.remove("on");
    if(!finita && Date.now() - avvio > 9000){ finita = true; posa(c); }
    else if(!finita){ clearTimeout(attesa); attesa = setTimeout(lettura, 9500); }
    return;
  }
  var p = Math.max(0, Math.min(1, scrollY / h));
  var x = (p * 100).toFixed(2) + "%";
  velo.style.setProperty("--x", x); perla.style.setProperty("--x", x);
  velo.classList.add("on"); perla.classList.add("on");
  if(!finita && p > .985){
    finita = true;
    var dejaLu = !!letti[c.id];
    posa(c);
    if(!calme()){
      perla.classList.remove("fine"); void perla.offsetWidth; perla.classList.add("fine");
      tric.classList.remove("mo-compiuto"); void tric.offsetWidth; tric.classList.add("mo-compiuto");
      var r = tric.getBoundingClientRect();
      schegge(r.right - 6, r.top + r.height / 2, dejaLu ? 10 : 26);
    }
  }
}
addEventListener("scroll", function(){ if(!tick){ tick = true; requestAnimationFrame(lettura); } }, {passive:true});
addEventListener("resize", function(){ cursore(true); lettura(); });
if(document.fonts && document.fonts.ready) document.fonts.ready.then(function(){ cursore(true); });

/* ---------- état initial ---------- */
ultima = capAtt();
cursore(true);
corrente();
if(ultima) entra(ultima);
lettura();

window.MO = {schegge:schegge, estCalme:calme, letti:letti};
})();
