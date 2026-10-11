/* Moteur des animations SVT (svt/anim/).
   Chaque page déclare ANIM.lancer({ END, SCENES, CALL, CUES, QUIZ, draw, bascule }).
   draw(c) reçoit l'instant c.t et l'option c.opt, et renvoie les couches SVG :
   { tf, cp, cells, nuc, sp, chr, let, fx, lab, st }.
   Intégration dans le cours : ?embed=1 (lecteur, puis quiz sous le lecteur à la demande), ?theme=dark|light, ?t0=secondes. */
window.ANIM = (() => {
'use strict';
const $ = s => document.querySelector(s);
const clamp = (x,a,b) => Math.max(a, Math.min(b, x));
const ease = x => x < .5 ? 4*x*x*x : 1 - Math.pow(-2*x+2, 3)/2;
const sm = x => { x = clamp(x,0,1); return x*x*(3-2*x); };
const lerp = (a,b,x) => a + (b-a)*x;
const f = n => Math.round(n*10)/10;
const op = n => Math.round(clamp(n,0,1)*100)/100;
const reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
const PARAMS = new URLSearchParams(location.search);
const EMBED = PARAMS.has('embed');
if(PARAMS.get('theme')) document.documentElement.setAttribute('data-theme', PARAMS.get('theme'));
if(EMBED) document.documentElement.classList.add('embed');

const AMB = '#F5C451', MAG = '#FF5CA8', CYA = '#3FD9C8';
let C = null, t = 0, playing = false, lastNow = 0, opt = 0, stepMode = false, muted = false, curIdx = -1, started = false;
const kAt = (tt,a,b) => ease(clamp((tt-a)/(b-a), 0, 1));
const k = (a,b) => kAt(t,a,b);
const vel = (a,b) => (kAt(t+.04,a,b) - kAt(t-.04,a,b)) / .08 * (b-a) / 4;

/* ---------- son ---------- */
let ac = null, master = null;
function audio(){
  if(!ac){ const A = window.AudioContext || window.webkitAudioContext; if(!A) return null; ac = new A(); master = ac.createGain(); master.gain.value = .5; master.connect(ac.destination); }
  if(ac.state === 'suspended') ac.resume();
  return ac;
}
function tone(fr, dur, o={}){
  if(muted || !ac) return;
  const {type='sine', g=.1, at=0, to=null, lp=null} = o, t0 = ac.currentTime + at;
  const osc = ac.createOscillator(), v = ac.createGain();
  osc.type = type; osc.frequency.setValueAtTime(fr, t0);
  if(to) osc.frequency.exponentialRampToValueAtTime(to, t0+dur);
  v.gain.setValueAtTime(.0001, t0); v.gain.exponentialRampToValueAtTime(g, t0+.02); v.gain.exponentialRampToValueAtTime(.0001, t0+dur);
  if(lp){ const fl = ac.createBiquadFilter(); fl.type = 'lowpass'; fl.frequency.value = lp; osc.connect(fl); fl.connect(v); } else osc.connect(v);
  v.connect(master); osc.start(t0); osc.stop(t0+dur+.05);
}
const SFX = {
  step:()=>{ tone(740,.4,{g:.06}); tone(988,.5,{g:.045,at:.09}); },
  pair:()=>{ tone(196,.5,{type:'triangle',g:.1,to:262}); tone(294,.45,{type:'triangle',g:.07,at:.18,to:392}); },
  chiasma:()=>{ [1175,1397,1568,1760,2093].forEach((fr,i)=>tone(fr,.6,{g:.04,at:i*.08})); },
  spark:()=>{ [2637,3136,2349,3520].forEach((fr,i)=>tone(fr,.18,{g:.05,at:i*.03})); tone(160,.5,{type:'triangle',g:.12,to:90}); },
  swap:()=>{ tone(260,1.2,{type:'sawtooth',g:.04,to:520,lp:1000}); tone(520,1.2,{type:'sawtooth',g:.035,to:260,lp:1000}); },
  error:()=>{ tone(311,.5,{type:'sawtooth',g:.05,lp:900}); tone(294,.6,{type:'sawtooth',g:.05,at:.18,lp:900,to:233}); },
  split:()=>{ tone(392,.5,{type:'triangle',g:.1,to:262}); tone(588,.5,{type:'triangle',g:.05,to:392,at:.05}); },
  pinch:()=>{ tone(523,.25,{g:.07}); tone(784,.3,{g:.06,at:.12}); },
  pop:()=>{ tone(880,.15,{type:'triangle',g:.08,to:1320}); },
  dup:()=>{ tone(330,.5,{type:'triangle',g:.1,to:660}); tone(495,.5,{type:'triangle',g:.05,to:990,at:.06}); },
  flip:()=>{ tone(440,.45,{type:'triangle',g:.1,to:660}); },
  whoosh:()=>{ tone(300,.7,{type:'sawtooth',g:.03,to:900,lp:1400}); },
  mut:()=>{ tone(1568,.12,{g:.05}); tone(2093,.16,{g:.04,at:.05}); },
  fuse:()=>{ tone(262,.9,{type:'triangle',g:.09,to:392}); tone(392,.9,{type:'triangle',g:.06,at:.1,to:523}); },
  final:()=>{ [523,659,784,1047].forEach((fr,i)=>tone(fr,.8,{g:.08,at:i*.12,type:'triangle'})); },
  good:()=>{ tone(659,.25,{g:.12,type:'triangle'}); tone(988,.45,{g:.1,at:.1,type:'triangle'}); },
  bad:()=>{ tone(233,.38,{g:.12,type:'triangle',to:185}); },
  win:()=>{ [523,659,784,1047,1319].forEach((fr,i)=>tone(fr,.6,{g:.08,at:i*.1,type:'triangle'})); }
};
function fire(a,b){ for(const c of (C.CUES || [])) if(c[0] > a && c[0] <= b && (!c[2] || c[2](opt))) (SFX[c[1]] || (()=>{}))(); }

/* ---------- géométrie ---------- */
function smooth(p){
  let d = `M${f(p[0][0])} ${f(p[0][1])}`;
  for(let i=0; i<p.length-1; i++){
    const p0 = p[i-1] || p[i], p1 = p[i], p2 = p[i+1], p3 = p[i+2] || p2;
    d += ` C${f(p1[0]+(p2[0]-p0[0])/6)} ${f(p1[1]+(p2[1]-p0[1])/6)} ${f(p2[0]-(p3[0]-p1[0])/6)} ${f(p2[1]-(p3[1]-p1[1])/6)} ${f(p2[0])} ${f(p2[1])}`;
  }
  return d;
}
const ys = (a,b,n) => Array.from({length:n+1}, (_,i) => a + (b-a)*i/n);
/* un brin épais à reflet : chromatide, fragment d'ADN */
function strand(d, col, w=12, o=1){
  return `<g opacity="${op(o)}"><path d="${d}" stroke="${col}" stroke-width="${w}" stroke-linecap="round" fill="none"/><path d="${d}" stroke="#FFFFFF" stroke-opacity=".28" stroke-width="${f(w*.25)}" stroke-linecap="round" fill="none" transform="translate(${f(-w*.2)} 0)"/></g>`;
}
function wobblyEllipse(cx,cy,rx,ry,ph=0,amp=1){
  let d = '';
  for(let i=0; i<=56; i++){ const a = i/56*6.2832, w = 1 + amp*(.016*Math.sin(4*a + t*.9 + ph) + .01*Math.sin(7*a - t*.7 + ph));
    d += (i ? 'L' : 'M') + f(cx + Math.cos(a)*rx*w) + ' ' + f(cy + Math.sin(a)*ry*w); }
  return d + 'Z';
}
/* contour organique de cellules qui se divisent : métaballes + marching squares */
const GX0 = -45, GY0 = -5, GS = 5, GNX = 98, GNY = 88, GV = new Float32Array((GNX+1)*(GNY+1));
const TAB = [[],[[3,0]],[[0,1]],[[3,1]],[[1,2]],[[3,0],[1,2]],[[0,2]],[[3,2]],[[2,3]],[[0,2]],[[0,1],[2,3]],[[1,2]],[[1,3]],[[0,1]],[[3,0]],[]];
function cellPath(bl){
  if(!bl.length) return '';
  const idx = (i,j) => j*(GNX+1) + i;
  for(let j=0; j<=GNY; j++){ const y = GY0 + j*GS; for(let i=0; i<=GNX; i++){ const x = GX0 + i*GS; let F = 0;
    for(let n=0; n<bl.length; n++){ const b = bl[n], dx = (x-b[0])/b[2], dy = (y-b[1])/b[3]; let d2 = dx*dx + dy*dy; const th = Math.atan2(dy,dx);
      d2 *= 1 + .03*Math.sin(3*th + t*.8 + n*1.7) + .018*Math.sin(5*th - t*1.1 + n); F += 1/(d2*d2 + 1e-6); }
    GV[idx(i,j)] = F - 1; } }
  const adj = new Map(), P = new Map();
  const vtx = (key,x1,y1,v1,x2,y2,v2) => { if(!P.has(key)){ const s = v1/(v1-v2); P.set(key,[x1+(x2-x1)*s, y1+(y2-y1)*s]); } return key; };
  const link = (a,b) => { if(!adj.has(a)) adj.set(a,[]); if(!adj.has(b)) adj.set(b,[]); adj.get(a).push(b); adj.get(b).push(a); };
  for(let j=0; j<GNY; j++) for(let i=0; i<GNX; i++){
    const a = GV[idx(i,j)], b = GV[idx(i+1,j)], c = GV[idx(i+1,j+1)], d = GV[idx(i,j+1)];
    const code = (a>0?1:0)|(b>0?2:0)|(c>0?4:0)|(d>0?8:0); if(code===0 || code===15) continue;
    const x = GX0 + i*GS, y = GY0 + j*GS;
    const E = e => e===0 ? vtx(idx(i,j)*2, x,y,a, x+GS,y,b) : e===1 ? vtx(idx(i+1,j)*2+1, x+GS,y,b, x+GS,y+GS,c) : e===2 ? vtx(idx(i,j+1)*2, x,y+GS,d, x+GS,y+GS,c) : vtx(idx(i,j)*2+1, x,y,a, x,y+GS,d);
    for(const [e1,e2] of TAB[code]) link(E(e1), E(e2));
  }
  let out = ''; const seen = new Set();
  for(const start of adj.keys()){
    if(seen.has(start)) continue;
    const loop = []; let prev = null, cur = start;
    while(cur !== undefined && !seen.has(cur)){ seen.add(cur); loop.push(P.get(cur)); const nb = adj.get(cur); const nx = nb[0] !== prev ? nb[0] : nb[1]; prev = cur; cur = nx; }
    if(loop.length > 4){
      const m = (p,q) => [(p[0]+q[0])/2, (p[1]+q[1])/2];
      const s0 = m(loop[0], loop[1]); out += `M${f(s0[0])} ${f(s0[1])}`;
      for(let i=1; i<=loop.length; i++){ const p = loop[i % loop.length], q = loop[(i+1) % loop.length], mm = m(p,q); out += `Q${f(p[0])} ${f(p[1])} ${f(mm[0])} ${f(mm[1])}`; }
      out += 'Z';
    }
  }
  return out;
}
/* fuseau de division */
function fiber(P0,P2,off,g,o){
  const mx = (P0[0]+P2[0])/2, my = (P0[1]+P2[1])/2 + off;
  const c1 = [lerp(P0[0],mx,g), lerp(P0[1],my,g)];
  const ex = (1-g)*(1-g)*P0[0] + 2*(1-g)*g*mx + g*g*P2[0], ey = (1-g)*(1-g)*P0[1] + 2*(1-g)*g*my + g*g*P2[1];
  return `<path d="M${f(P0[0])} ${f(P0[1])} Q${f(c1[0])} ${f(c1[1])} ${f(ex)} ${f(ey)}" fill="none" stroke="${AMB}" stroke-opacity="${op(o)}" stroke-width="1.1" stroke-linecap="round"/>`;
}
function pole(x,y,o){
  if(o <= 0) return '';
  let s = `<g opacity="${op(o)}"><circle cx="${f(x)}" cy="${f(y)}" r="18" fill="url(#halo)"/>`;
  for(let a=0; a<12; a++){ const r = a*Math.PI/6 + .2, L = 9 + 5*Math.sin(a*2.3 + t); s += `<path d="M${f(x)} ${f(y)} q${f(Math.cos(r+.3)*L*.5)} ${f(Math.sin(r+.3)*L*.5)} ${f(Math.cos(r)*L)} ${f(Math.sin(r)*L)}" stroke="${AMB}" stroke-opacity=".55" fill="none"/>`; }
  return s + `<circle cx="${f(x)}" cy="${f(y)}" r="3.6" fill="${AMB}"/></g>`;
}
/* éclair (flash) et halo pulsant à un endroit précis */
function flash(x,y,t0,dur=1.5){
  if(t < t0 - .3 || t > t0 + dur) return '';
  const p = clamp((t-(t0-.3))/dur, 0, 1);
  return `<circle cx="${f(x)}" cy="${f(y)}" r="${f(6+42*p)}" fill="url(#flash)" opacity="${op(1-p)}"/><circle cx="${f(x)}" cy="${f(y)}" r="${f(4+30*p)}" fill="none" stroke="#FFFFFF" stroke-width="1.2" opacity="${op((1-p)*.9)}"/>`;
}
function halo(x,y,o,r0=10){
  if(o <= 0) return '';
  const r = r0 + 2.5*Math.sin(t*7);
  return `<circle cx="${f(x)}" cy="${f(y)}" r="${f(r+10)}" fill="url(#halo)" opacity="${op(o)}"/><circle cx="${f(x)}" cy="${f(y)}" r="${f(r)}" fill="none" stroke="${AMB}" stroke-width="1.4" opacity="${op(o)}"/>`;
}
/* trajectoire en arc entre deux points */
function arc(A,B,h,u){ const x = lerp(A[0],B[0],u), y = lerp(A[1],B[1],u) - h*4*u*(1-u); return [x,y]; }
/* mélange de deux couleurs #rrggbb */
function mix(c1,c2,u){
  u = clamp(u,0,1);
  const a = parseInt(c1.slice(1),16), b = parseInt(c2.slice(1),16);
  const r = Math.round(lerp(a>>16, b>>16, u)), g = Math.round(lerp((a>>8)&255, (b>>8)&255, u)), bl = Math.round(lerp(a&255, b&255, u));
  return '#' + ((1<<24) + (r<<16) + (g<<8) + bl).toString(16).slice(1);
}
function label(x,y,txt,col='#F2F5FA',size=11,o=1){
  if(o <= 0) return '';
  const w = txt.length*size*.52 + 18;
  return `<g opacity="${op(o)}"><rect x="${f(x-w/2)}" y="${f(y-size)}" width="${f(w)}" height="${f(size*2)}" rx="${f(size)}" fill="#0A1222" fill-opacity=".85"/><text x="${f(x)}" y="${f(y)}" dy=".36em" font-size="${size}" font-weight="700" fill="${col}" text-anchor="middle">${txt}</text></g>`;
}

/* ---------- légendes pointées ---------- */
function callouts(st){
  let s = '';
  for(const c of (C.CALL || [])){
    if(c.si && !c.si(opt)) continue;
    const o = k(c.a, c.a+.45) * (1 - k(c.b-.45, c.b)); if(o <= 0) continue;
    const g = k(c.a+.15, c.a+1), [lx,ly] = c.lab, w = c.text.length*5.7 + 20, oo = op(o);
    for(const A of (c.anc ? c.anc(st) : [])){
      const ex = lerp(lx,A[0],g), ey = lerp(ly,A[1],g);
      s += `<line x1="${lx}" y1="${ly}" x2="${f(ex)}" y2="${f(ey)}" stroke="#E9EEF7" stroke-opacity="${op(.7*o)}" stroke-width=".9"/>`;
      if(g > .9) s += `<circle cx="${f(A[0])}" cy="${f(A[1])}" r="5.5" fill="none" stroke="${AMB}" stroke-opacity="${op(.6*o)}"/><circle cx="${f(A[0])}" cy="${f(A[1])}" r="2.2" fill="${AMB}" opacity="${oo}"/>`;
    }
    s += `<g opacity="${oo}"><rect x="${f(lx-w/2)}" y="${ly-10.5}" width="${f(w)}" height="21" rx="10.5" fill="#0A1222" fill-opacity=".88" stroke="${c.col || AMB}" stroke-opacity=".6"/><text x="${lx}" y="${ly}" dy=".36em" font-size="11" font-weight="700" fill="#F2F5FA">${c.text}</text></g>`;
  }
  return s;
}

/* ---------- rendu ---------- */
let E = {}, VES = [];
function render(){
  const out = C.draw({t, opt, k, vel, kAt}) || {};
  E.world.setAttribute('transform', out.tf || '');
  const cp = out.cp || '';
  E.cells.innerHTML = (cp ? `<path d="${cp}" fill="url(#cyto)"/><path d="${cp}" fill="none" stroke="#7FA3D6" stroke-opacity=".16" stroke-width="9"/><path d="${cp}" fill="none" stroke="#86A9DB" stroke-width="2"/>` : '') + (out.cells || '');
  E.clip.setAttribute('d', cp || 'M0 0Z');
  let v = '';
  if(cp) for(const p of VES){ const x = p.x + 6*Math.sin(t*p.sp + p.ph), y = p.y + 5*Math.cos(t*p.sp*.8 + p.ph); v += `<circle cx="${f(x)}" cy="${f(y)}" r="${p.s}" fill="#7FA3D6" fill-opacity=".16"/>`; }
  E.ves.innerHTML = v;
  E.nuc.innerHTML = out.nuc || '';
  E.sp.innerHTML = out.sp || '';
  E.chr.innerHTML = out.chr || '';
  E.let.innerHTML = out.let || '';
  E.fx.innerHTML = out.fx || '';
  E.call.innerHTML = callouts(out.st || {});
  E.lab.innerHTML = out.lab || '';
  updateUI();
}

/* ---------- interface ---------- */
const fmt = s => `${Math.floor(s/60)}:${String(Math.floor(s%60)).padStart(2,'0')}`;
const sceneIdx = () => { for(let i=C.SCENES.length-1; i>=0; i--) if(t >= C.SCENES[i].t) return i; return 0; };
function postH(){
  if(!EMBED || window.parent === window) return;
  const w = document.querySelector('.wrap'), h = w ? w.getBoundingClientRect().bottom + window.scrollY : document.body.scrollHeight;
  window.parent.postMessage({type:'anim-h', id:C.id, h:Math.ceil(h) + 2}, '*');
}
function updateUI(){
  E.scrub.value = Math.round(t*10);
  E.scrub.style.setProperty('--p', (t/C.END*100).toFixed(2) + '%');
  E.time.textContent = `${fmt(t)} / ${fmt(C.END)}`;
  const i = sceneIdx();
  if(i !== curIdx){
    curIdx = i; const s = C.SCENES[i];
    E.stepNo.textContent = `Étape ${i+1} sur ${C.SCENES.length}`;
    E.capTitle.textContent = typeof s.title === 'function' ? s.title(opt) : s.title;
    E.capText.innerHTML = typeof s.text === 'function' ? s.text(opt) : s.text;
    E.capState.textContent = typeof s.state === 'function' ? s.state(opt) : s.state;
    E.cap.classList.remove('in'); void E.cap.offsetWidth; if(!reduce) E.cap.classList.add('in');
    postH();
  }
  if(E.optBtn) E.optBtn.hidden = !C.bascule || t < C.bascule.des;
  E.toQuiz.hidden = !C.QUIZ || i < C.SCENES.length - 1 || (EMBED && document.documentElement.classList.contains('quizon'));
}
function setPlayIcon(){
  E.playIc.innerHTML = playing ? '<rect x="3" y="2" width="5" height="18" rx="1.5" fill="currentColor"/><rect x="12" y="2" width="5" height="18" rx="1.5" fill="currentColor"/>' : '<path d="M3 2v18l15-9z" fill="currentColor"/>';
  E.play.setAttribute('aria-label', playing ? 'Pause' : 'Lecture');
}
function play(){
  audio(); started = true; E.big.hidden = true; if(t >= C.END - .01) t = 0;
  if(playing) return;                 /* une seule boucle d'animation à la fois */
  playing = true; lastNow = performance.now(); setPlayIcon(); requestAnimationFrame(loop);
}
function pause(){ playing = false; setPlayIcon(); }
function loop(now){
  if(!playing) return;
  const dt = Math.min(.1, (now - lastNow)/1000); lastNow = now;
  const nt = t + dt;
  if(stepMode){ const e = C.SCENES[sceneIdx()].e - .02; if(t < e && nt >= e){ fire(t,e); t = e; pause(); render(); return; } }
  if(nt >= C.END){ fire(t,C.END); t = C.END; pause(); E.bigLabel.textContent = "Revoir l'animation"; E.big.hidden = false; render(); return; }
  fire(t,nt); t = nt; render(); requestAnimationFrame(loop);
}
/* aller à un instant : la lecture continue si elle était en cours, la pause est respectée
   (sauf au tout premier appui, ou si 'lire' est demandé, par exemple pour la bascule) */
function jump(nt, lire){
  const go = lire || playing || !started;
  t = clamp(nt, 0, C.END); curIdx = -1; started = true;
  if(t < C.END - .01){ E.big.hidden = true; E.bigLabel.textContent = "Lancer l'animation"; }
  render();
  if(go) play();
}
function nextStep(){ const i = sceneIdx(); if(i < C.SCENES.length-1) jump(C.SCENES[i+1].t); }
function prevStep(){ const i = sceneIdx(); jump(t - C.SCENES[i].t > 1.2 || i === 0 ? C.SCENES[i].t : C.SCENES[i-1].t); }
function setMute(){
  E.muteIc.innerHTML = '<path d="M3 7h3l5-4v14l-5-4H3z" fill="currentColor"/>' + (muted ? '<path d="M14 7l5 6M19 7l-5 6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>' : '<path d="M14 6.5a5 5 0 0 1 0 7M16.5 4a8.5 8.5 0 0 1 0 12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>');
  E.mute.setAttribute('aria-pressed', String(muted)); E.mute.setAttribute('aria-label', muted ? 'Activer le son' : 'Couper le son');
}

/* ---------- quiz ---------- */
function quiz(){
  const Q = C.QUIZ; if(!Q || !Q.length){ const z = $('#quiz'); if(z) z.hidden = true; return; }
  let qi = 0, score = 0, answered = false, results = [];
  const qNum = $('#qNum'), qDots = $('#qDots'), qText = $('#qText'), qOpts = $('#qOpts'), qEx = $('#qEx'), qNext = $('#qNext'), qMain = $('#qMain'), qEnd = $('#qEnd'), qcard = $('#qcard');
  const dots = () => { qDots.innerHTML = Q.map((_,i) => `<i class="${results[i]===true?'ok':results[i]===false?'ko':''}${i===qi?' cur':''}"></i>`).join(''); };
  function burst(el){
    if(reduce) return;
    const r = el.getBoundingClientRect(), rc = qcard.getBoundingClientRect(), b = document.createElement('div'); b.className = 'burst';
    b.style.left = (r.left - rc.left + r.width*.5) + 'px'; b.style.top = (r.top - rc.top + r.height*.5) + 'px';
    for(let i=0; i<18; i++){ const p = document.createElement('i'), a = Math.random()*Math.PI*2, d = 40 + Math.random()*70;
      p.style.setProperty('--dx', (Math.cos(a)*d).toFixed(1)+'px'); p.style.setProperty('--dy', (Math.sin(a)*d).toFixed(1)+'px');
      p.style.background = [MAG,CYA,'#B7D94C'][i%3]; p.style.animationDelay = (Math.random()*.08).toFixed(2)+'s'; b.appendChild(p); }
    qcard.appendChild(b); setTimeout(() => b.remove(), 900);
  }
  function showQ(){
    answered = false; const q = Q[qi];
    qNum.textContent = `Question ${qi+1} sur ${Q.length}`; qText.textContent = q.q; qOpts.innerHTML = '';
    q.o.forEach((o,i) => { const b = document.createElement('button'); b.type = 'button'; b.className = 'opt'; b.textContent = o; b.addEventListener('click', () => answer(i,b)); qOpts.appendChild(b); });
    qEx.hidden = true; qNext.hidden = true; dots();
  }
  function answer(i,b){
    if(answered) return; answered = true; audio();
    const q = Q[qi], ok = i === q.a;
    [...qOpts.children].forEach((el,n) => { el.disabled = true; if(n === q.a) el.classList.add('good'); });
    if(ok){ score++; SFX.good(); burst(b); } else { b.classList.add('bad'); SFX.bad(); }
    results[qi] = ok; dots();
    qEx.innerHTML = `<strong>${ok ? 'Exact.' : 'Pas tout à fait.'}</strong> ${q.ex}`; qEx.hidden = false;
    qNext.textContent = qi < Q.length-1 ? 'Question suivante' : 'Voir mon score'; qNext.hidden = false; qNext.focus();
  }
  qNext.addEventListener('click', () => {
    if(qi < Q.length-1){ qi++; showQ(); return; }
    qMain.hidden = true; qEnd.hidden = false;
    $('#qScore').textContent = `${score} sur ${Q.length}`;
    $('#qMsg').textContent = score === Q.length ? "Parfait." : score >= Q.length-1 ? "Presque parfait. Relis l'explication de la question manquée, puis refais le quiz." : "Relance l'animation sur les étapes qui t'ont posé problème, puis réessaie.";
    if(score >= Q.length-1){ SFX.win(); burst($('#qScore')); }
  });
  $('#qAgain').addEventListener('click', () => { qi = 0; score = 0; results = []; qEnd.hidden = true; qMain.hidden = false; showQ(); });
  showQ();
}

/* ---------- démarrage ---------- */
function lancer(cfg){
  C = cfg;
  let seed = cfg.graine || 11; const rnd = () => (seed = (seed*16807) % 2147483647, (seed-1)/2147483646);
  VES = Array.from({length:42}, () => { const a = rnd()*6.283, r = Math.sqrt(rnd())*200; return {x:200+Math.cos(a)*r, y:205+Math.sin(a)*r, s:1+rnd()*2.4, ph:rnd()*6.28, sp:.25+rnd()*.5}; });
  E = {world:$('#world'), cells:$('#cells'), ves:$('#ves'), clip:$('#clipP'), nuc:$('#nucleus'), sp:$('#spindle'), chr:$('#chromo'), let:$('#letters'), fx:$('#fx'), call:$('#callouts'), lab:$('#labels'),
       scrub:$('#scrub'), time:$('#time'), play:$('#play'), playIc:$('#playIc'), big:$('#bigplay'), bigLabel:$('#bigplayLabel'), optBtn:$('#optBtn'), toQuiz:$('#toQuiz'),
       cap:$('#cap'), stepNo:$('#stepNo'), capTitle:$('#capTitle'), capText:$('#capText'), capState:$('#capState'), mute:$('#mute'), muteIc:$('#muteIc')};
  E.scrub.max = Math.round(C.END*10);
  $('#ticks').innerHTML = C.SCENES.slice(1).map(s => `<i style="left:${(s.t/C.END*100).toFixed(2)}%"></i>`).join('');
  E.big.addEventListener('click', play);
  E.play.addEventListener('click', () => playing ? pause() : play());
  $('#next').addEventListener('click', nextStep);
  $('#prev').addEventListener('click', prevStep);
  E.scrub.addEventListener('input', () => { t = E.scrub.value/10; if(started && t < C.END) E.big.hidden = true; render(); });
  $('#stepMode').addEventListener('change', e => { stepMode = e.target.checked; });
  if(C.bascule && E.optBtn){
    E.optBtn.textContent = C.bascule.off;
    E.optBtn.addEventListener('click', () => { opt ^= 1; E.optBtn.textContent = opt ? C.bascule.on : C.bascule.off; jump(C.bascule.saut, true); });
  }
  E.mute.addEventListener('click', () => { muted = !muted; audio(); setMute(); });
  document.addEventListener('keydown', e => {
    const tag = (e.target.tagName || '').toLowerCase();
    if(['input','button','a','textarea'].includes(tag)) return;
    if(e.code === 'Space'){ e.preventDefault(); playing ? pause() : play(); }
    else if(e.key === 'ArrowRight') nextStep();
    else if(e.key === 'ArrowLeft') prevStep();
  });
  window.addEventListener('message', e => {
    const d = e.data || {};
    if(d.type === 'anim-theme') document.documentElement.setAttribute('data-theme', d.theme);
    if(d.type === 'anim-pause') pause();
  });
  window.addEventListener('resize', postH);
  if(window.ResizeObserver) new ResizeObserver(postH).observe(document.body);
  const t0 = parseFloat(PARAMS.get('t0'));
  if(t0 > 0 && t0 < C.END) t = t0;
  /* intégré au cours : le quiz s'ouvre sous le lecteur, dans la même page */
  if(EMBED) E.toQuiz.addEventListener('click', ev => {
    ev.preventDefault();
    document.documentElement.classList.add('quizon'); E.toQuiz.hidden = true; postH();
    const z = $('#quiz');
    if(z && window.parent !== window) window.parent.postMessage({type:'anim-goto', id:C.id, y:z.getBoundingClientRect().top + window.scrollY}, '*');
  });
  setPlayIcon(); setMute(); quiz(); render(); postH();
}

return {lancer, H:{clamp, ease, sm, lerp, f, op, smooth, ys, strand, wobblyEllipse, cellPath, fiber, pole, flash, halo, arc, mix, label, AMB, MAG, CYA}};
})();
