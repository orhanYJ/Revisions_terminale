// Vérifie un short sans navigateur : chaque repère [passage, mot] du plan existe dans le texte lu,
// les plans sont dans l'ordre, aucun plan ne dure moins de 0,5 s, les types existent (modèle A + types du short).
// Usage : SHORT_MUET=1 python3 outils/shorts/voix.py <code> && node outils/shorts/verifier.js <code>
// (utilise sortie/<code>.data.js : brouillon muet ou voix définitive)
const fs = require('fs'), path = require('path'), vm = require('vm');
const code = process.argv[2], ICI = __dirname;
const ctx = { window: {}, console };
ctx.window.window = ctx.window;
vm.createContext(ctx);
const lire = f => vm.runInContext(fs.readFileSync(path.join(ICI, f), 'utf8'), ctx, { filename: f });
lire(`sortie/${code}.data.js`);
const D = ctx.window.SHORT;
const norm = s => s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]/g, '');
const seg = id => { const s = D.segs.find(s => s.id === id); if (!s) throw new Error('passage absent : ' + id); return s; };
function T(id, k) {
  const s = seg(id);
  if (k === undefined) return s.t0;
  if (typeof k === 'number') return s.mots[(k + s.mots.length) % s.mots.length][0];
  const n = norm(k), m = s.mots.find(w => norm(w[2]).startsWith(n));
  if (!m) throw new Error(`mot « ${k} » absent de ${id} (mots : ${s.mots.map(w => w[2]).join(' ')})`);
  return m[0];
}
let erreurs = 0, PLANS = [];
const S = { T, plans: l => (PLANS = l) };
ctx.S = S;
lire(`${code}.plan.js`);
ctx.window.PLAN(S);
const typesA = ['photo', 'collage', 'mot', 'cerveau', 'tampon', 'date', 'perso', 'poignet', 'horloge', 'eeg', 'frise', 'portrait', 'pierre', 'causes', 'stop', 'bac', 'chaine'];
let typesShort = [];
if (fs.existsSync(path.join(ICI, `${code}.types-a.js`))) {
  ctx.S = Object.assign({}, S, { g: {}, W: 1080, H: 1920, cl: x => x, lerp: x => x, pr: x => x, eo: x => x, back: x => x, rnd: x => x });
  lire(`${code}.types-a.js`);
  typesShort = Object.keys(ctx.window.TYPES_A({ C: {} }));
}
ctx.S = Object.assign({}, S, { g: {}, W: 1080, H: 1920 });
lire('formats-a.js');
typesShort = typesShort.concat(ctx.window.TYPES_FORMATS);
const tps = a => Array.isArray(a) ? T(...a) : a;
const res = PLANS.map((p, i) => {
  let a;
  try { a = Array.isArray(p.a) ? T(...p.a) - (p.av ?? .06) : p.a; } catch (e) { console.log(`plan ${i} (${p.type}) : ${e.message}`); erreurs++; return null; }
  for (const k of ['a2', 'cercle', 'rouges', 'pct', 'tampon', 'zero', 'rep', 'chrono']) if (Array.isArray(p[k])) { try { tps(p[k]); } catch (e) { console.log(`plan ${i} champ ${k} : ${e.message}`); erreurs++; } }
  [...(p.lignes || []), ...(p.items || []), ...(p.souligne ? [p.souligne] : [])].forEach(([x]) => { if (Array.isArray(x)) try { tps(x); } catch (e) { console.log(`plan ${i} ligne : ${e.message}`); erreurs++; } });
  (p.indices || []).forEach(([x]) => { if (Array.isArray(x)) try { tps(x); } catch (e) { console.log(`plan ${i} indice : ${e.message}`); erreurs++; } });
  (p.etapes || []).forEach(([x]) => { if (Array.isArray(x)) try { tps(x); } catch (e) { console.log(`plan ${i} étape : ${e.message}`); erreurs++; } });
  if (!typesA.includes(p.type) && !typesShort.includes(p.type)) { console.log(`plan ${i} : type inconnu « ${p.type} »`); erreurs++; }
  return { i, a, type: p.type };
}).filter(Boolean).sort((x, y) => x.a - y.a);
// même règle que core.js : le plan qui suit un verdict est retardé pour que le verdict reste 1,3 s
(function () { const L = res.map(x => Object.assign({}, PLANS[x.i], { a: x.a }));
  L.forEach((p, i) => { if (!Array.isArray(p.rep) || i + 1 >= L.length) return; let r; try { r = T(...p.rep) - .04; } catch (e) { return; }
    const q = L[i + 1], apres = i + 2 < L.length ? L[i + 2].a : D.dur; if (q.a >= r - .05 && q.a < r + 1.3) q.a = Math.max(q.a, Math.min(r + 1.3, apres - .6)); });
  L.forEach((p, i) => { res[i].a = p.a; }); })();
res.forEach((p, k) => { const b = k + 1 < res.length ? res[k + 1].a : D.dur; if (b - p.a < .5) { console.log(`plan ${p.i} (${p.type}) trop court : ${(b - p.a).toFixed(2)} s`); erreurs++; } });
// un verdict (champ rep) doit rester au moins 1,2 s à l'écran avant le plan suivant
PLANS.forEach((p, i) => { if (!p.rep || !Array.isArray(p.rep)) return; let r; try { r = tps(p.rep); } catch (e) { return; }
  const pa = Array.isArray(p.a) ? T(...p.a) - (p.av ?? .06) : p.a;
  const moi = res.find(x => x.i === i), suiv = res.filter(x => x.a > (moi ? moi.a : pa) + .01).map(x => x.a).sort((x, y) => x - y)[0] ?? D.dur;
  if (r > suiv) return;
  if (suiv - r < 1.2) { console.log(`plan ${i} (${p.type}) : verdict tenu ${(suiv - r).toFixed(2)} s seulement (au moins 1,2 s : av négatif sur le plan suivant)`); erreurs++; } });
const n = res.length, moy = D.dur / Math.max(1, n);
console.log(`${code} : ${n} plans, ${D.dur.toFixed(1)} s, un plan toutes les ${moy.toFixed(1)} s, chapitres : ${PLANS.filter(p => p.ch !== undefined).length}, chocs : ${PLANS.filter(p => p.choc).length}, chaîne : ${PLANS.some(p => p.type === 'chaine') ? 'oui' : 'NON'}`);
if (erreurs) { console.log(erreurs + ' erreur(s)'); process.exit(1); } else console.log('OK');
