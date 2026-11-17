/* Vidéo du chapitre 1 de NSI (« Programmation orientée objet ») : illustrations propres au chapitre, dans l'identité
   « flux de données » du moteur (nsi/serie/moteur.js). Chargé par nsi/serie/nsi-ch1.html après moteur.js (generer.py
   l'ajoute s'il existe). Chaque illustration : SERIE_ILLU.nom = function (svg, v) { … return function (t, st) { … }; } ;
   rendu fonction pure du temps (t : temps de la vidéo, st.tl : temps depuis l'apparition). Étapes calées sur la voix
   par les repères {id.k}.
   - memoire : les variables et les objets en mémoire, reliés par leurs références (comme Python Tutor) ;
   - moule : la classe (le plan) et les objets qui en sortent (les instances) ;
   - uml : le diagramme de classe en trois cases. */
(function () {
  "use strict";
  var O, C, sv, P, E, EIO, op, et, lbl, cl;
  function prep() {
    if (O) return;
    O = window.SERIE_OUTILS; C = O.C; sv = O.sv; P = O.P; E = O.E; EIO = O.EIO; op = O.op; et = O.et; lbl = O.lbl; cl = O.cl;
  }
  window.SERIE_ILLU = window.SERIE_ILLU || {};
  var SERIE_ILLU = window.SERIE_ILLU;
  var MONO = "'JetBrains Mono',monospace";
  var DX = 16, DY = -12;   // profondeur des blocs (3D légère)

  function texte(g, x, y, txt, o) {
    o = o || {};
    var e = sv("text", { x: x, y: y, fill: o.c || C.iv, "font-size": o.fs || 20, "font-family": MONO, "font-weight": o.fw || 400,
      "text-anchor": o.ancre || "start", "letter-spacing": o.ls || 0 }, g, txt);
    e.style.whiteSpace = "pre";
    return e;
  }
  function couleurValeur(s) {
    s = String(s);
    if (s === "None" || s === "True" || s === "False") return C.violet;
    if (/^-?\d/.test(s)) return C.ambre;
    if (/^["']/.test(s)) return C.vert;
    return C.iv;
  }
  // bloc en 3D légère : face avant (verre sombre), dessus et côté ; d = { g, avant, dessus, cote, liseré }
  function bloc(g, coul) {
    var b = { g: sv("g", {}, g) };
    b.dessus = sv("path", { fill: "rgba(40,56,120,.85)", stroke: coul, "stroke-width": 1.2 }, b.g);
    b.cote = sv("path", { fill: "rgba(14,20,52,.92)", stroke: coul, "stroke-width": 1.2 }, b.g);
    b.avant = sv("rect", { fill: "rgba(18,28,74,.94)", stroke: coul, "stroke-width": 1.4, rx: 3 }, b.g);
    b.lis = sv("rect", { fill: coul, width: 4 }, b.g);
    b.pose = function (x, y, w, h, lumi) {
      b.dessus.setAttribute("d", "M" + x + " " + y + " l" + DX + " " + DY + " h" + w + " l" + (-DX) + " " + (-DY) + " Z");
      b.cote.setAttribute("d", "M" + (x + w) + " " + y + " l" + DX + " " + DY + " v" + h + " l" + (-DX) + " " + (-DY) + " Z");
      b.avant.setAttribute("x", x); b.avant.setAttribute("y", y); b.avant.setAttribute("width", w); b.avant.setAttribute("height", h);
      b.lis.setAttribute("x", x); b.lis.setAttribute("y", y); b.lis.setAttribute("height", h);
      b.avant.style.filter = lumi > 0 ? "drop-shadow(0 0 " + (4 + 14 * lumi).toFixed(1) + "px " + b.coul + ")" : "";
    };
    b.couleur = function (c) { b.coul = c; [b.dessus, b.cote, b.avant].forEach(function (e) { e.setAttribute("stroke", c); }); b.lis.setAttribute("fill", c); };
    b.couleur(coul);
    return b;
  }
  // flèche (référence) : chemin courbe + pointe ; renvoie { p, tete, pose(x1, y1, x2, y2, u, a) }
  function fleche(g, coul) {
    var f = { p: sv("path", { fill: "none", stroke: coul, "stroke-width": 2.4, "stroke-linecap": "round" }, g),
      tete: sv("path", { fill: coul }, g), parts: [] };
    f.p.style.filter = "drop-shadow(0 0 5px " + coul + ")";
    for (var i = 0; i < 3; i++) { var c0 = sv("circle", { r: 3.2, fill: "#E8F8FF" }, g); c0.style.visibility = "hidden"; f.parts.push(c0); }
    f.p.style.visibility = "hidden"; op(f.tete, 0);
    f.pose = function (x1, y1, x2, y2, u, a, t) {
      var mx = Math.max(40, Math.abs(x2 - x1) * .45);
      var d = "M" + x1.toFixed(1) + " " + y1.toFixed(1) + " C" + (x1 + mx).toFixed(1) + " " + y1.toFixed(1) + " " + (x2 - mx).toFixed(1) + " " + y2.toFixed(1) + " " + x2.toFixed(1) + " " + y2.toFixed(1);
      if (f.d !== d) { f.p.setAttribute("d", d); f.d = d; f.L = f.p.getTotalLength() || 1; f.p.style.strokeDasharray = f.L + " " + (f.L + 2); }
      f.p.style.strokeDashoffset = f.L * (1 - cl(u, 0, 1));
      op(f.p, a); op(f.tete, a * (u >= .98 ? 1 : 0));
      f.p.style.visibility = a <= 0 || u <= 0 ? "hidden" : "";
      // pointe dans la direction d'arrivée (horizontale, la courbe arrive à plat)
      f.tete.setAttribute("d", "M" + x2 + " " + y2 + " l-13 -7 l3 7 l-3 7 Z");
      // particules qui circulent le long de la référence (le flux)
      f.parts.forEach(function (c, i) {
        if (a <= 0 || u < 1) { c.style.visibility = "hidden"; return; }
        var q = ((t * .55 + i / 3) % 1), pt = f.p.getPointAtLength(q * f.L);
        c.style.visibility = ""; c.setAttribute("cx", pt.x.toFixed(1)); c.setAttribute("cy", pt.y.toFixed(1));
        op(c, a * .85 * Math.sin(Math.PI * q));
      });
    };
    return f;
  }

  /* memoire : v.etats = [état 0, état 1, …] ; l'état 0 s'affiche à l'apparition, l'état k au repère {id.k}.
     Un état ne donne que ce qui change par rapport au précédent :
       v : { nom: cible } — cible = identifiant d'un objet (flèche), "=valeur" (valeur écrite dans la variable),
           "None", ou "-" (la variable disparaît) ; « self » est dessinée en rose ;
       o : { id: { c: classe, a: [[attribut, valeur], …], p: [x, y] } } — champs donnés = champs remplacés ; une valeur
           "@id" est une référence vers un autre objet ; "-" à la place de l'objet le retire ;
       note : légende de l'étape (en bas).
     Mise en page : vw (largeur de la colonne des variables, 190), ow (largeur des objets, 300), ordre (ordre des variables). */
  SERIE_ILLU.memoire = function (s, v) {
    prep();
    var VW = v.vw || 190, OW = v.ow || 300, HT = 40, HR = 40, W_ = v.w, H_ = v.h;
    // états complets
    var S = [], cur = { v: {}, o: {} };
    (v.etats || [{}]).forEach(function (e) {
      var n = { v: Object.assign({}, cur.v), o: {} , note: e.note || "" };
      Object.keys(cur.o).forEach(function (k) { n.o[k] = cur.o[k]; });
      Object.keys(e.v || {}).forEach(function (k) { if (e.v[k] === "-") delete n.v[k]; else n.v[k] = e.v[k]; });
      Object.keys(e.o || {}).forEach(function (k) {
        if (e.o[k] === "-") { delete n.o[k]; return; }
        n.o[k] = Object.assign({ c: "", a: [], p: [VW + 60, 60] }, cur.o[k] || {}, e.o[k]);
      });
      S.push(n); cur = n;
    });
    var noms = (v.ordre || []).slice(), ids = [];
    S.forEach(function (e) {
      Object.keys(e.v).forEach(function (k) { if (noms.indexOf(k) < 0) noms.push(k); });
      Object.keys(e.o).forEach(function (k) { if (ids.indexOf(k) < 0) ids.push(k); });
    });
    // cadre : deux zones
    var fond = sv("g", {}, s);
    sv("line", { x1: VW + 18, y1: 0, x2: VW + 18, y2: H_ - 10, stroke: "rgba(79,216,235,.25)", "stroke-width": 1.4, "stroke-dasharray": "4 8" }, fond);
    var t1 = lbl(s, 10, -6, "variables", "titre"), t2 = lbl(s, VW + 44, -6, "objets en mémoire", "titre");
    t1.style.transform = "none"; t2.style.transform = "none"; t1.classList.add("fixe"); t2.classList.add("fixe");
    var gObj = sv("g", {}, s), gFl = sv("g", {}, s), gVar = sv("g", {}, s);
    // objets
    var OB = {};
    ids.forEach(function (id) {
      var rows = [];
      S.forEach(function (e) { if (e.o[id]) e.o[id].a.forEach(function (r) { if (rows.indexOf(r[0]) < 0) rows.push(r[0]); }); });
      var g = sv("g", {}, gObj), b = bloc(g, C.sa);
      var cls = texte(g, 0, 0, "", { c: C.sa, fs: 17, fw: 600, ls: 2 });
      var R = {};
      rows.forEach(function (r) {
        var rg = sv("g", {}, g);
        var hl = sv("rect", { height: HR - 6, rx: 6, fill: "rgba(255,196,107,.22)" }, rg);
        var sep = sv("line", { stroke: "rgba(169,179,218,.16)", "stroke-width": 1 }, rg);
        var nm = texte(rg, 0, 0, r, { c: C.iv2, fs: 19 });
        var va = texte(rg, 0, 0, "", { fs: 20, fw: 600, ancre: "end" }), vb = texte(rg, 0, 0, "", { fs: 20, fw: 600, ancre: "end" });
        var pt = sv("circle", { r: 6, fill: C.sa }, rg);
        R[r] = { g: rg, hl: hl, sep: sep, nm: nm, va: va, vb: vb, pt: pt, f: fleche(gFl, C.violet), f2: fleche(gFl, C.violet) };
      });
      OB[id] = { g: g, b: b, cls: cls, R: R, rows: rows };
    });
    // variables
    var VA = {};
    noms.forEach(function (n, i) {
      var g = sv("g", {}, gVar), y = 34 + i * 70, coul = n === "self" ? C.self : C.sa;
      var r = sv("rect", { x: 8, y: y, width: VW - 16, height: 48, rx: 10, fill: "rgba(16,24,62,.9)", stroke: coul, "stroke-width": 1.5 }, g);
      r.style.filter = "drop-shadow(0 0 6px " + coul + "88)";
      var tn = texte(g, 24, y + 31, n, { c: n === "self" ? C.self : C.iv, fs: 21, fw: 600 });
      var tv = texte(g, VW - 22, y + 31, "", { fs: 20, fw: 600, ancre: "end" });
      var pt = sv("circle", { cx: VW - 24, cy: y + 24, r: 6, fill: coul }, g);
      VA[n] = { g: g, y: y, tv: tv, pt: pt, f: fleche(gFl, coul), f2: fleche(gFl, coul) };
    });
    var note = lbl(s, W_ / 2 + VW / 2, H_ - 50, "", "bulle note"), note2 = lbl(s, W_ / 2 + VW / 2, H_ - 50, "", "bulle note");
    // géométrie d'un objet dans un état
    function hauteur(o) { return HT + Math.max(1, o.a.length) * HR + 6; }
    function geo(id, e) { var o = e.o[id]; return o ? { x: o.p[0], y: o.p[1], h: hauteur(o), o: o } : null; }
    function mix(a, b, u) { return a + (b - a) * u; }
    var VIDE = { v: {}, o: {}, note: "" };
    return function (t, st) {
      op(t1, E(P(st.tl, .1, .5))); op(t2, E(P(st.tl, .3, .5)));
      var T = S.map(function (_, k) { return k ? et(v, String(k), 1e9) : v.t0; });
      var i = 0; T.forEach(function (x, k) { if (t >= x) i = k; });
      var ti = T[i], A = i ? S[i - 1] : VIDE, B = S[i], u = E(P(t, ti, .6)), uo = E(P(t, ti, .3));
      // positions courantes des objets
      var POS = {};
      ids.forEach(function (id) {
        var ga = geo(id, A), gb = geo(id, B), ob = OB[id];
        var al = gb ? (ga ? 1 : u) : (ga ? 1 - uo : 0);
        ob.g.style.display = al > 0 ? "" : "none";
        if (al <= 0) return;
        var g0 = ga || gb, g1 = gb || ga, x = mix(g0.x, g1.x, u), y = mix(g0.y, g1.y, u) + (ga ? 0 : 16 * (1 - u));
        var o = (gb || ga).o, na = ga ? ga.o.a.length : (gb ? 0 : o.a.length), nb = gb ? gb.o.a.length : na;
        var hh = HT + Math.max(1, mix(Math.max(1, na), Math.max(1, nb), u)) * HR + 6;
        POS[id] = { x: x, y: y, h: hh, a: al };
        op(ob.g, al);
        ob.b.pose(x, y, OW, hh, (ga ? 0 : 1 - P(t, ti, 1.2)) + .15);
        ob.cls.setAttribute("x", x + 18); ob.cls.setAttribute("y", y + 27); ob.cls.textContent = (o.c || "").toUpperCase();
        // lignes (attributs)
        ob.rows.forEach(function (r) {
          var x_ = ob.R[r];
          var ka = ga ? ga.o.a.map(function (q) { return q[0]; }).indexOf(r) : -1, kb = gb ? gb.o.a.map(function (q) { return q[0]; }).indexOf(r) : -1;
          var va = ka >= 0 ? ga.o.a[ka][1] : null, vb = kb >= 0 ? gb.o.a[kb][1] : null;
          var ra = ka >= 0 ? 1 : 0, rb = kb >= 0 ? 1 : 0, ral = mix(ra, rb, kb >= 0 ? u : uo);
          if (ral <= 0 || (!gb && !ga)) { x_.g.style.display = "none"; x_.f.pose(0, 0, 0, 0, 0, 0, t); x_.f2.pose(0, 0, 0, 0, 0, 0, t); return; }
          x_.g.style.display = "";
          var k = kb >= 0 ? (ka >= 0 ? mix(ka, kb, u) : kb) : ka, yr = y + HT + k * HR;
          op(x_.g, ral);
          x_.sep.setAttribute("x1", x + 12); x_.sep.setAttribute("x2", x + OW - 12); x_.sep.setAttribute("y1", yr); x_.sep.setAttribute("y2", yr);
          x_.nm.setAttribute("x", x + 18); x_.nm.setAttribute("y", yr + 27);
          var change = vb !== null && va !== vb;
          x_.hl.setAttribute("x", x + 8); x_.hl.setAttribute("y", yr + 3); x_.hl.setAttribute("width", OW - 16);
          op(x_.hl, change ? .9 * (1 - P(t, ti + .3, 1.4)) : 0);
          var refA = va && /^@/.test(va), refB = vb && /^@/.test(vb);
          [[x_.va, vb, refB, change ? u : 1], [x_.vb, change ? va : null, refA, 1 - u]].forEach(function (q) {
            var e = q[0], val = q[1];
            if (val === null || q[2]) { e.style.display = "none"; return; }
            e.style.display = ""; e.textContent = val; e.setAttribute("fill", couleurValeur(val));
            e.setAttribute("x", x + OW - 20); e.setAttribute("y", yr + 28 + (e === x_.va ? 8 * (1 - q[3]) : -8 * (1 - q[3])));
            op(e, q[3]);
          });
          x_.pt.style.display = refB || refA ? "" : "none";
          x_.pt.setAttribute("cx", x + OW - 26); x_.pt.setAttribute("cy", yr + 20);
          x_._ref = [refA ? va.slice(1) : null, refB ? vb.slice(1) : null, x + OW - 20, yr + 20, ral];
        });
      });
      // références entre objets (attribut → objet)
      ids.forEach(function (id) {
        if (!POS[id]) return;
        OB[id].rows.forEach(function (r) {
          var x_ = OB[id].R[r], q = x_._ref;
          if (!q || x_.g.style.display === "none") { x_.f.pose(0, 0, 0, 0, 0, 0, t); x_.f2.pose(0, 0, 0, 0, 0, 0, t); return; }
          var cA = q[0] && POS[q[0]], cB = q[1] && POS[q[1]], meme = q[0] === q[1];
          if (cB) x_.f.pose(q[2], q[3], cB.x - 4, cB.y + 20, meme ? 1 : u, q[4] * cB.a, t); else x_.f.pose(0, 0, 0, 0, 0, 0, t);
          if (cA && !meme) x_.f2.pose(q[2], q[3], cA.x - 4, cA.y + 20, 1, (1 - uo) * cA.a, t); else x_.f2.pose(0, 0, 0, 0, 0, 0, t);
        });
      });
      // variables
      noms.forEach(function (n) {
        var x_ = VA[n], ca = n in A.v ? A.v[n] : undefined, cb = n in B.v ? B.v[n] : undefined;
        var al = cb !== undefined ? (ca !== undefined ? 1 : u) : (ca !== undefined ? 1 - uo : 0);
        x_.g.style.display = al > 0 ? "" : "none"; op(x_.g, al);
        var c = cb !== undefined ? cb : ca, val = /^=/.test(c || "") ? c.slice(1) : c === "None" ? "None" : "";
        x_.tv.textContent = val; x_.tv.setAttribute("fill", couleurValeur(val));
        var estObj = function (q) { return q !== undefined && !/^=/.test(q) && q !== "None"; };
        x_.pt.style.display = estObj(c) ? "" : "none";
        var x1 = VW - 18, y1 = x_.y + 24, meme = ca === cb;
        if (estObj(cb) && POS[cb]) x_.f.pose(x1, y1, POS[cb].x - 4, POS[cb].y + 20, meme ? 1 : u, al * POS[cb].a, t); else x_.f.pose(0, 0, 0, 0, 0, 0, t);
        if (estObj(ca) && !meme && POS[ca]) x_.f2.pose(x1, y1, POS[ca].x - 4, POS[ca].y + 20, 1, (cb === undefined ? al : 1 - uo) * POS[ca].a, t); else x_.f2.pose(0, 0, 0, 0, 0, 0, t);
      });
      // légende de l'étape
      var na = A.note, nb = B.note;
      note.innerHTML = O.esc(nb || ""); note2.innerHTML = O.esc(na || "");
      op(note, nb ? (na === nb ? 1 : u) : 0); op(note2, na && na !== nb ? 1 - uo : 0);
    };
  };

  /* moule : la classe (un plan, à gauche) et les objets fabriqués à partir d'elle (à droite).
     v.classe = { nom, attrs: [...], meths: [...] } ; v.objets = [{ nom: "c1", vals: [...] }, …] (valeurs des attributs).
     Repères : {id.a} les attributs s'allument, {id.m} les méthodes, {id.k} (k = 1, 2…) l'objet k sort du moule :
     un flux de particules part du plan et l'objet s'assemble, avec ses propres valeurs. */
  SERIE_ILLU.moule = function (s, v) {
    prep();
    var K = v.classe, W_ = v.w, H_ = v.h, PX = 20, PY = 80, PW = v.pw || 450;
    var nA = K.attrs.length, nM = K.meths.length, LH = 48;
    var PH = 70 + 34 + nA * LH + 34 + nM * LH + 24;
    var g = sv("g", {}, s);
    var ti1 = lbl(s, PX + PW / 2, 0, "la classe · le plan", "titre"), ti2 = lbl(s, W_ - (v.ow || 330) / 2 - 40, 0, "les objets · les instances", "titre");
    // le plan : panneau en pointillés, quadrillage de plan d'architecte
    var plan = sv("g", {}, g);
    var id = "q" + Math.round(Math.random() * 1e9), defs = sv("defs", {}, s), pat = sv("pattern", { id: id, width: 22, height: 22, patternUnits: "userSpaceOnUse" }, defs);
    sv("path", { d: "M22 0 H0 V22", fill: "none", stroke: "rgba(79,216,235,.10)", "stroke-width": 1 }, pat);
    sv("rect", { x: PX, y: PY, width: PW, height: PH, rx: 16, fill: "rgba(12,22,60,.78)" }, plan);
    sv("rect", { x: PX, y: PY, width: PW, height: PH, rx: 16, fill: "url(#" + id + ")" }, plan);
    var bord = sv("rect", { x: PX, y: PY, width: PW, height: PH, rx: 16, fill: "none", stroke: C.sa, "stroke-width": 1.8, "stroke-dasharray": "9 7" }, plan);
    bord.style.filter = "drop-shadow(0 0 6px rgba(79,216,235,.6))";
    var tc = texte(plan, PX + 26, PY + 46, "", { fs: 29, fw: 600 });
    tc.innerHTML = '<tspan fill="' + C.violet + '">class</tspan> <tspan fill="#9FE9FF">' + K.nom + '</tspan>';
    var y = PY + 70;
    function section(titre, items, coul) {
      var sg = sv("g", {}, plan), hl = sv("rect", { x: PX + 10, y: y + 6, width: PW - 20, height: 30 + items.length * LH, rx: 10, fill: coul, opacity: 0 }, sg);
      sv("line", { x1: PX + 16, x2: PX + PW - 16, y1: y, y2: y, stroke: "rgba(169,179,218,.22)" }, sg);
      texte(sg, PX + 26, y + 28, titre.toUpperCase(), { c: C.iv2, fs: 16, fw: 600, ls: 2 });
      var ts = items.map(function (x, k) { return texte(sg, PX + 40, y + 34 + (k + 1) * LH - 14, x, { fs: 25, c: C.iv }); });
      y += 34 + items.length * LH;
      return { g: sg, hl: hl, ts: ts };
    }
    var sA = section("attributs", K.attrs, "rgba(79,216,235,.16)"), sM = section("méthodes", K.meths, "rgba(154,140,255,.18)");
    // les objets
    var OW = v.ow || 380, OX = W_ - OW - 40, n = v.objets.length, pas = Math.min(250, (H_ - 120) / Math.max(1, n));
    var objs = v.objets.map(function (ob, k) {
      var oy = 120 + k * pas, gg = sv("g", {}, g), fl = sv("path", { fill: "none", stroke: C.sa, "stroke-width": 1.6, "stroke-dasharray": "3 7", opacity: 0 }, gg);
      var x0 = PX + PW, y0 = PY + 50, x1 = OX - 104, y1 = oy + 27, mx = (x1 - x0) * .5;
      var d = "M" + x0 + " " + y0 + " C" + (x0 + mx) + " " + y0 + " " + (x1 - mx) + " " + y1 + " " + x1 + " " + y1;
      fl.setAttribute("d", d);
      var parts = []; for (var i = 0; i < 16; i++) parts.push(sv("rect", { width: 4, height: 4, fill: i % 4 ? C.sa : C.ambre }, gg));
      var bg = sv("g", {}, gg), b = bloc(bg, C.sa), hh = 50 + K.attrs.length * 46;
      b.pose(OX, oy, OW, hh, .4);
      var nom = sv("g", {}, bg);
      var tag = sv("rect", { x: OX - 100, y: oy + 8, width: 80, height: 38, rx: 10, fill: "rgba(16,24,62,.92)", stroke: C.sa, "stroke-width": 1.5 }, nom);
      texte(nom, OX - 60, oy + 34, ob.nom, { fs: 22, fw: 600, ancre: "middle" });
      texte(bg, OX + 18, oy + 32, K.nom.toUpperCase(), { c: C.sa, fs: 17, fw: 600, ls: 2 });
      var vals = K.attrs.map(function (a, j) {
        var yr = oy + 50 + j * 46;
        sv("line", { x1: OX + 12, x2: OX + OW - 12, y1: yr - 4, y2: yr - 4, stroke: "rgba(169,179,218,.16)" }, bg);
        texte(bg, OX + 18, yr + 28, a.replace(/\s*:.*$/, ""), { c: C.iv2, fs: 22 });
        return texte(bg, OX + OW - 20, yr + 28, ob.vals[j], { c: couleurValeur(ob.vals[j]), fs: 23, fw: 600, ancre: "end" });
      });
      return { fl: fl, parts: parts, bg: bg, b: b, oy: oy, hh: hh, vals: vals, L: fl.getTotalLength() || 1 };
    });
    return function (t, st) {
      var tl = st.tl;
      op(plan, E(P(tl, 0, .6))); op(ti1, E(P(tl, .2, .5))); op(ti2, E(P(tl, .4, .5)));
      var ta = et(v, "a", 1e9), tm = et(v, "m", 1e9);
      op(sA.hl, .9 * E(P(t, ta, .4)) * (1 - E(P(t, tm, .4))));
      op(sM.hl, .9 * E(P(t, tm, .4)) * (1 - E(P(t, et(v, "1", 1e9), .4))));
      sA.ts.forEach(function (x, k) { op(x, t >= ta ? E(P(t, ta + k * .25, .4)) : .35); });
      sM.ts.forEach(function (x, k) { op(x, t >= tm ? E(P(t, tm + k * .25, .4)) : .35); });
      objs.forEach(function (o, k) {
        var tk = et(v, String(k + 1), 1e9), q = P(t, tk, .9);
        o.parts.forEach(function (r, i) {
          var f = EIO(cl(q * 1.4 - i * .025, 0, 1));
          if (q <= 0 || f >= 1 || f <= 0) { r.style.visibility = "hidden"; return; }
          var pt = o.fl.getPointAtLength(f * o.L); r.style.visibility = "";
          r.setAttribute("x", (pt.x - 2).toFixed(1)); r.setAttribute("y", (pt.y - 2).toFixed(1)); op(r, .9 - i * .04);
        });
        op(o.fl, .3 * E(P(t, tk + .7, .5)));
        var a = E(P(t, tk + .6, .5));
        op(o.bg, a); o.bg.setAttribute("transform", "translate(" + (24 * (1 - a)).toFixed(1) + ",0)");
        o.b.pose(OX, o.oy, OW, o.hh, .2 + (1 - P(t, tk + .6, 1.4)));
        o.vals.forEach(function (x, j) { op(x, E(P(t, tk + .9 + j * .25, .4))); });
      });
    };
  };

  /* uml : le diagramme de classe en trois cases (nom, attributs avec leur type, méthodes sans self) ; {id.1}, {id.2},
     {id.3} allument la case et sa légende. v.classe_nom, v.attrs, v.meths. */
  SERIE_ILLU.uml = function (s, v) {
    prep();
    var W_ = v.w, BW = v.bw || 470, X = W_ - BW - 60, Y = 50, LH = 44;
    var h1 = 70, h2 = 26 + v.attrs.length * LH, h3 = 26 + v.meths.length * LH, g = sv("g", {}, s);
    var cases = [[Y, h1], [Y + h1, h2], [Y + h1 + h2, h3]];
    var hls = cases.map(function (c) { return sv("rect", { x: X + 4, y: c[0] + 4, width: BW - 8, height: c[1] - 8, rx: 8, fill: "rgba(79,216,235,.16)", opacity: 0 }, g); });
    sv("rect", { x: X, y: Y, width: BW, height: h1 + h2 + h3, rx: 6, fill: "rgba(16,24,62,.88)" }, g);
    var cadre = sv("path", { d: O.dPts(O.ptsBoite(X, Y, BW, h1 + h2 + h3)), fill: "none", stroke: C.sa, "stroke-width": 2 }, g);
    cadre.style.filter = "drop-shadow(0 0 6px rgba(79,216,235,.7))";
    var l1 = sv("line", { x1: X, x2: X + BW, y1: Y + h1, y2: Y + h1, stroke: C.sa, "stroke-width": 1.6 }, g);
    var l2 = sv("line", { x1: X, x2: X + BW, y1: Y + h1 + h2, y2: Y + h1 + h2, stroke: C.sa, "stroke-width": 1.6 }, g);
    hls.forEach(function (r) { g.appendChild(r); });
    var tn = texte(g, X + BW / 2, Y + 45, v.classe_nom || "", { fs: 28, fw: 600, ancre: "middle", c: "#9FE9FF" });
    var ta = v.attrs.map(function (a, k) { return texte(g, X + 28, Y + h1 + 14 + (k + 1) * LH - 12, a, { fs: 23 }); });
    var tm = v.meths.map(function (a, k) { return texte(g, X + 28, Y + h1 + h2 + 14 + (k + 1) * LH - 12, a, { fs: 23 }); });
    var LEG = ["nom de la classe", "attributs, avec leur type", "méthodes, sans self"];
    var legs = cases.map(function (c, k) {
      var d = lbl(s, X - 300, c[0] + c[1] / 2 - 26, LEG[k], "bulle");
      var ln = sv("line", { x1: X - 132, x2: X - 10, y1: c[0] + c[1] / 2, y2: c[0] + c[1] / 2, stroke: C.sa, "stroke-width": 1.6, "stroke-dasharray": "4 5" }, s);
      return { d: d, ln: ln };
    });
    return function (t, st) {
      var tl = st.tl;
      O.trace(cadre, EIO(P(tl, 0, 1))); op(l1, E(P(tl, .7, .4))); op(l2, E(P(tl, .8, .4)));
      op(tn, E(P(tl, .5, .4)));
      ta.forEach(function (x, k) { op(x, E(P(tl, .9 + k * .2, .4))); });
      tm.forEach(function (x, k) { op(x, E(P(tl, 1.2 + k * .2, .4))); });
      var tk = [1, 2, 3].map(function (k) { return et(v, String(k), 1e9); });
      hls.forEach(function (r, k) { var on = t >= tk[k] && (k === 2 || t < tk[k + 1]); op(r, on ? E(P(t, tk[k], .3)) : 0); });
      legs.forEach(function (x, k) { var a = E(P(t, tk[k], .4)); op(x.d, a); op(x.ln, a); });
    };
  };
})();
