/* Vidéo SES É3 (ses-e3, « Comment lutter contre le chômage ? ») — illustrations propres à la vidéo, chargées après le moteur.
   1. Les deux animations du chapitre É3 du site (ANIMS["e3-spirale"], ANIMS["e3-appariement"]) : elles sont écrites dans
      outils/specialites/ses/src/data-e3.js et non dans un fichier data-anim-*.js, donc site-ses.js (généré par site_ses.py)
      ne les contient pas. Elles sont recopiées ici telles quelles (même texte, même rendu) pour le type sanim.
   2. SERIE_ILLU.chomage : la courbe du taux de chômage en France, 1975-2025 (GRAPHES["e3-chomage"], données du site,
      Insee), tracée année après année par périodes : phases=[[de, a, "étiquette"], …], la phase k au repère {id.k} ;
      {id.fh} : courbes des femmes et des hommes ; points=[[année, "texte", dx, dy], …] : valeurs pointées quand la courbe
      les atteint. Rendu fonction pure du temps. */
(function () {
  "use strict";
  window.ANIMS = window.ANIMS || {};
window.ANIMS["e3-spirale"] = {
    t: "Le cercle vicieux du chômage conjoncturel… et la relance",
    h: 330,
    src: "Schéma de principe (mécanisme keynésien de la demande effective). La jauge est illustrative ; repère réel : en France, 7,4 % de chômage en 2008, 9,1 % en 2009 (Insee).",
    etapes: [
      { l: "Un choc frappe l’économie : la demande de biens et de services baisse (en 2009, crise financière mondiale).", d: 3 },
      { l: "Les entreprises vendent moins : elles produisent moins, réduisent l’intérim et les heures, puis l’emploi.", d: 3 },
      { l: "Le chômage augmente : des ménages perdent leurs revenus, les autres s’inquiètent et épargnent par précaution.", d: 3 },
      { l: "La consommation recule encore, donc la demande baisse de nouveau : le cercle vicieux s’auto-entretient.", d: 3.5 },
      { l: "La relance : l’État dépense plus ou baisse les impôts, la banque centrale baisse ses taux. La demande repart.", d: 3.5 },
      { l: "Le cercle tourne dans l’autre sens : production, embauches, revenus et consommation se renforcent. Le chômage conjoncturel recule.", d: 4 }
    ],
    rendu: function (A, i, p) {
      var cx = 180, cy = 150, R = 100, RX = 128, s = "";
      var noeuds = [{ a: -90, t: "Demande" }, { a: 0, t: "Production" }, { a: 90, t: "Emploi" }, { a: 180, t: "Revenus et consommation" }];
      var sens = i >= 4 ? 1 : -1, actif = i <= 3 ? i : (i === 4 ? 0 : 3);
      function pos(a) { return [cx + RX * Math.cos(a * Math.PI / 180), cy + R * Math.sin(a * Math.PI / 180)]; }
      for (var k = 0; k < 4; k++) {
        var a1 = noeuds[k].a + (k % 2 ? 28 : 34), a2 = noeuds[(k + 1) % 4].a - (k % 2 ? 34 : 28), pts = [];
        for (var t = 0; t <= 1.0001; t += 0.04) { var aa = (a1 + (a2 - a1) * t) * Math.PI / 180; pts.push([cx + RX * Math.cos(aa), cy + R * Math.sin(aa)]); }
        var montre = i >= 3 ? 1 : (k < i ? 1 : (k === i ? A.s(p, 0.3, 1) : 0));
        var coul = i >= 4 ? "vert" : "corail";
        if (i === 5) montre = 1;
        if (montre > 0) {
          s += A.pl(pts, i === 4 ? A.s(p, 0.3, 1) : montre, { c: i === 4 ? "gris" : coul, sw: 2.4, tir: i === 4 });
          var fin = pts[pts.length - 1], av = pts[pts.length - 3];
          if ((i === 4 ? A.s(p, 0.3, 1) : montre) >= 1) s += A.fl(av[0], av[1], fin[0], fin[1], { c: i === 4 ? "gris" : coul, sw: 0.1 });
        }
      }
      noeuds.forEach(function (n, k) {
        var q = pos(n.a), act = (i <= 3 && k <= i) || i >= 4;
        var lg = k === 3; s += A.boite(lg ? 0 : q[0] - 50, q[1] - (lg ? 22 : 19), lg ? 110 : 100, lg ? 44 : 38, n.t + (act ? (sens < 0 ? " ↓" : (i === 5 || k === 0 ? " ↑" : "")) : ""), { k: act ? (sens < 0 ? "effet" : "cause") : "neutre", t: lg ? 11.5 : 12.5, g: true });
      });
      var ch = i <= 1 ? 7.4 : i === 2 ? A.l(7.4, 9.1, A.s(p, 0, 1)) : i === 3 ? A.l(9.1, 9.8, A.s(p, 0, 1)) : i === 4 ? 9.8 : A.l(9.8, 8.4, A.s(p, 0, 1));
      s += A.jauge(110, 300, 140, ch, 12, { c: i >= 5 ? "vert" : "corail", l: "chômage (illustratif)", val: A.fr(ch, 1) + " %" });
      if (i === 0) s += A.t(cx, cy - 4, "choc de demande", { t: 12.5, g: true, a: "middle", c: "corail", op: A.s(p, 0, 0.5), w: 90 });
      if (i === 3) s += A.t(cx, cy - 4, "cercle vicieux", { t: 13, g: true, a: "middle", c: "corail", op: A.s(p, 0.3, 0.8), w: 90 });
      if (i >= 4) {
        s += A.t(cx, cy - 4, "relance", { t: 14, g: true, a: "middle", c: "vert", op: i === 4 ? A.s(p, 0, 0.4) : 1 });
        s += A.t(cx, cy + 13, "budgétaire et monétaire", { t: 10.5, a: "middle", c: "gris", op: i === 4 ? A.s(p, 0.2, 0.6) : 1, w: 90 });
        if (i === 4) s += A.fl(cx, 10, cx, cy - R - 22, { c: "vert", sw: 3, p: A.s(p, 0, 0.5) });
      }
      return s;
    }
  };
  
  window.ANIMS["e3-appariement"] = {
    t: "Des chômeurs et des emplois vacants en même temps",
    h: 310,
    src: "Schéma de principe. Repère : en 2025, 14,7 % de chômage pour les actifs sans diplôme ou avec le brevet, 5,3 % pour les diplômés du supérieur (Insee).",
    etapes: [
      { l: "Sur le marché du travail, des personnes cherchent un emploi (à gauche) et des entreprises ont des postes vacants (à droite).", d: 3 },
      { l: "Une partie se rencontre vite : ces postes sont pourvus.", d: 3 },
      { l: "Frictions : d’autres mettent du temps à se trouver (recherche, candidatures, entretiens). C’est le chômage frictionnel.", d: 3.5 },
      { l: "Inadéquation de qualification : un poste de technicien informatique ne convient pas à un ancien ouvrier du textile sans formation.", d: 3.5 },
      { l: "Inadéquation spatiale : l’emploi est à Lyon, le chômeur à 400 km et ne peut pas déménager facilement (logement, conjoint).", d: 3.5 },
      { l: "Résultat : chômeurs et emplois vacants coexistent durablement. C’est du chômage structurel ; la formation et la mobilité peuvent le réduire.", d: 3.5 }
    ],
    rendu: function (A, i, p) {
      var s = A.t(70, 22, "Demandeurs d’emploi", { t: 13, g: true, a: "middle", f: true }) + A.t(290, 22, "Postes vacants", { t: 13, g: true, a: "middle", f: true });
      var cand = [["vendeur", "", 0], ["comptable", "", 0], ["cariste", "", 0], ["infirmière", "", 1], ["ouvrier textile", "qualif", 2], ["soudeur (Lille)", "lieu", 3]];
      var postes = [["vendeur", 0], ["comptable", 0], ["cariste", 0], ["infirmière", 1], ["technicien informatique", 2], ["soudeur (Lyon)", 3]];
      cand.forEach(function (c, k) {
        var y = 40 + k * 40, x = 12, op = 1;
        var apparie = (k < 3 && i >= 1) || (k === 3 && i >= 2);
        var tx = 0;
        if (k < 3 && i === 1) tx = A.s(p, 0.1 + k * 0.15, 0.6 + k * 0.15);
        else if (k < 3 && i > 1) tx = 1;
        if (k === 3 && i === 2) tx = A.s(p, 0.4, 1);
        else if (k === 3 && i > 2) tx = 1;
        var x2 = A.l(x, 234, tx);
        if (apparie && tx >= 1) op = 0.35;
        s += A.boite(x2, y, 116, 30, c[0], { k: tx >= 1 ? "cause" : "neutre", op: op, t: 12 });
      });
      postes.forEach(function (c, k) {
        var y = 40 + k * 40, pris = (k < 3 && i >= 1 && (i > 1 || A.s(p, 0.1 + k * 0.15, 0.6 + k * 0.15) >= 1)) || (k === 3 && (i > 2 || (i === 2 && A.s(p, 0.4, 1) >= 1)));
        s += A.boite(234, y, 116, 30, c[0], { k: pris ? "cause" : "meca", t: 12, op: pris ? 0.35 : 1 });
      });
      if (i === 2) s += A.t(180, 296, "frictions : le temps de se trouver", { t: 12, a: "middle", c: "moutarde", g: true, op: A.s(p, 0, 0.4), h: true });
      if (i >= 3) {
        var q = i === 3 ? A.s(p, 0, 0.6) : 1;
        s += A.fl(130, 215, 230, 215, { c: "corail", sw: 2, p: q, tir: true }) + A.t(180, 208, "qualification ≠", { t: 11.5, a: "middle", c: "corail", g: true, op: q, h: true });
        s += A.t(180, 232, "✕", { t: 16, a: "middle", c: "corail", g: true, op: q });
      }
      if (i >= 4) {
        var q2 = i === 4 ? A.s(p, 0, 0.6) : 1;
        s += A.fl(130, 255, 230, 255, { c: "corail", sw: 2, p: q2, tir: true }) + A.t(180, 248, "distance ≠", { t: 11.5, a: "middle", c: "corail", g: true, op: q2, h: true });
        s += A.t(180, 272, "✕", { t: 16, a: "middle", c: "corail", g: true, op: q2 });
      }
      if (i === 5) s += A.r(6, 196, 348, 88, { f: "none", s: "moutarde", sw: 2.5, op: A.s(p, 0, 0.5), r: 10 }) + A.t(180, 302, "chômage structurel", { t: 12.5, g: true, a: "middle", c: "moutarde", op: A.s(p, 0.3, 0.8), h: true });
      return s;
    }
  };

  var O = window.SERIE_OUTILS, sv = O.sv, C = O.C, E = O.E, EIO = O.EIO, P = O.P, op = O.op, et = O.et, lab = O.etiquette;
  window.SERIE_ILLU = window.SERIE_ILLU || {};
  function fr(n) { return n.toFixed(1).replace(".", ","); }

  SERIE_ILLU.chomage = function (s, v) {
    var g = window.GRAPHES["e3-chomage"], W_ = v.w, H_ = v.h, xs = g.x;
    var ml = 78, mr = 150, mt = 124, mb = 78, pw = W_ - ml - mr, ph = H_ - mt - mb, ymax = 12;
    function X(a) { return ml + (a - xs[0]) / (xs[xs.length - 1] - xs[0]) * pw; }
    function Y(y) { return mt + (1 - y / ymax) * ph; }
    var gg = sv("g", {}, s), fond = sv("g", {}, gg);
    var ti = lab(gg, 0, 34, g.t, { ancre: "start", fs: 34, c: C.iv, fw: 700 });
    var st_ = lab(gg, 0, 66, "Taux de chômage au sens du BIT, en % de la population active", { ancre: "start", fs: 21, c: C.iv2, fw: 500 });
    var src = lab(gg, 0, H_ - 8, "Source : Insee, enquête Emploi 2025, séries longues (juillet 2026)", { ancre: "start", fs: 18, c: C.iv2, fw: 500 });
    var grille = [];
    for (var y = 0; y <= ymax; y += 2) {
      grille.push(sv("line", { x1: ml, x2: ml + pw, y1: Y(y), y2: Y(y), stroke: y ? "rgba(22,24,26,.12)" : C.iv, "stroke-width": y ? 1.2 : 2.2 }, fond));
      grille.push(lab(fond, ml - 14, Y(y) + 8, y + " %", { ancre: "end", fs: 20, c: C.iv2, fw: 500 }));
    }
    for (var a = 1975; a <= 2025; a += 10) grille.push(lab(fond, X(a), Y(0) + 34, String(a), { fs: 20, c: C.iv2, fw: 500 }));
    function serie(k) { return g.series[k].v; }
    function chemin(vals, a1) {   // la courbe jusqu'à l'année a1 (fractionnaire)
      var d = "";
      for (var i = 0; i < xs.length; i++) {
        if (xs[i] > a1) {
          if (i > 0) { var u = a1 - xs[i - 1]; d += " L" + X(a1).toFixed(1) + " " + Y(vals[i - 1] + (vals[i] - vals[i - 1]) * u).toFixed(1); }
          break;
        }
        d += (d ? " L" : "M") + X(xs[i]).toFixed(1) + " " + Y(vals[i]).toFixed(1);
      }
      return d || "M0 0";
    }
    var lF = sv("path", { d: "", fill: "none", stroke: C.corail, "stroke-width": 3, "stroke-linejoin": "round", opacity: 0 }, gg);
    var lH = sv("path", { d: "", fill: "none", stroke: C.canard, "stroke-width": 3, "stroke-linejoin": "round", opacity: 0 }, gg);
    var lE = sv("path", { d: "", fill: "none", stroke: C.iv, "stroke-width": 5, "stroke-linejoin": "round", "stroke-linecap": "round" }, gg);
    var tF = lab(gg, X(2025) + 12, Y(serie(1)[50]) + 30, "femmes", { ancre: "start", fs: 22, c: C.corail, fw: 700 });
    var tH = lab(gg, X(2025) + 12, Y(serie(2)[50]) - 22, "hommes", { ancre: "start", fs: 22, c: C.canard, fw: 700 });
    var tE = lab(gg, X(2025) + 12, Y(serie(0)[50]) + 8, "ensemble", { ancre: "start", fs: 22, c: C.iv, fw: 700 });
    var bout = sv("circle", { r: 7, fill: C.corail, stroke: C.papier, "stroke-width": 2.5 }, gg);
    var phases = (v.phases || [[1975, 2025, ""]]).map(function (p, k) {
      var b = sv("rect", { x: X(p[0]), y: mt, width: Math.max(2, X(p[1]) - X(p[0])), height: ph, fill: C.moutarde, opacity: 0 }, fond);
      var l = lab(fond, (X(p[0]) + X(p[1])) / 2, mt - 10, p[2] || "", { fs: 20, c: C.mo, fw: 700 });
      return { de: p[0], a: p[1], b: b, l: l, k: k, dur: p[3] || Math.max(1.2, (p[1] - p[0]) * .14) };
    });
    var pts = (v.points || []).map(function (q) {
      var i = xs.indexOf(q[0]), yv = serie(0)[i], gq = sv("g", { opacity: 0 }, gg);
      sv("circle", { cx: X(q[0]), cy: Y(yv), r: 7.5, fill: C.iv, stroke: C.papier, "stroke-width": 2.5 }, gq);
      lab(gq, X(q[0]) + (q[2] || 0), Y(yv) + (q[3] != null ? q[3] : -20), q[1] || (fr(yv) + " %"), { fs: 23, c: C.iv, fw: 700 });
      return { a: q[0], g: gq };
    });
    return function (t, st) {
      var tl = st.tl, a0 = E(P(tl, 0, .6));
      op(ti, a0); op(st_, E(P(tl, .2, .6))); op(src, E(P(tl, .4, .6)) * .9);
      grille.forEach(function (e, i) { op(e, E(P(tl, .2 + i * .02, .5))); });
      var acur = xs[0] - 1e-6, k0 = -1;
      phases.forEach(function (p) {
        var tk = et(v, String(p.k + 1), 1 + p.k * 4);
        if (t >= tk) { k0 = p.k; acur = Math.max(acur, p.de + (p.a - p.de) * EIO(P(t, tk, p.dur))); }
      });
      phases.forEach(function (p) {
        var on = p.k === k0 ? E(P(t, et(v, String(p.k + 1), 1 + p.k * 4), .5)) : 0;
        op(p.b, on * .13); op(p.l, on);
      });
      var vis = acur >= xs[0];
      lE.setAttribute("d", vis ? chemin(serie(0), acur) : "M0 0"); op(lE, vis ? 1 : 0);
      if (vis) {
        var i = Math.min(xs.length - 1, Math.floor(acur - xs[0])), u = acur - xs[i], yv = i < xs.length - 1 ? serie(0)[i] + (serie(0)[i + 1] - serie(0)[i]) * u : serie(0)[i];
        bout.setAttribute("cx", X(Math.min(acur, 2025)).toFixed(1)); bout.setAttribute("cy", Y(yv).toFixed(1));
      }
      op(bout, vis && acur < 2025 - 1e-3 ? 1 : 0);
      pts.forEach(function (q) { op(q.g, acur >= q.a - 1e-6 ? 1 : 0); });
      var tf = v.et && v.et.fh != null ? v.et.fh : null, qf = tf == null ? 0 : EIO(P(t, tf, 2.2));
      lF.setAttribute("d", qf > 0 ? chemin(serie(1), 1975 + 50 * qf) : "M0 0"); lH.setAttribute("d", qf > 0 ? chemin(serie(2), 1975 + 50 * qf) : "M0 0");
      op(lF, qf > 0 ? .9 : 0); op(lH, qf > 0 ? .9 : 0);
      op(tF, qf >= 1 ? E(P(t, tf + 2.2, .5)) : 0); op(tH, qf >= 1 ? E(P(t, tf + 2.2, .5)) : 0);
      op(tE, acur >= 2025 - 1e-3 ? 1 : 0);
    };
  };
})();
