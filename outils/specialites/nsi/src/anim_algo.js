/* Animations pas à pas des chapitres Diviser pour régner, Programmation dynamique, Recherche textuelle,
   Calculabilité, Paradigmes et Histoire. Chaque animation utilise le lecteur commun (outils.lecteur).
   Les éléments qui se déplacent (lettres, fenêtre, tête de lecture) gardent leur nœud d'une étape à l'autre :
   leur transition CSS (sous html.mo) montre le mouvement ; « saut » rend le dessin instantané. */
(function () {
  if (typeof document === "undefined") return;
  var css = [
    ".aa svg{font-family:var(--mono);font-size:13px}",
    ".aa text{fill:var(--encre);dominant-baseline:central;text-anchor:middle}",
    ".aa text.g{text-anchor:start}.aa text.p{font-size:10.5px;fill:var(--encre3)}.aa text.t{font-size:11.5px;fill:var(--encre2)}",
    ".aa .c{fill:var(--bg2);stroke:var(--ligne2);stroke-width:1.2}",
    ".aa .vide .c{fill:none;stroke-dasharray:3 3;stroke:var(--ligne)}.aa .vide text{opacity:0}",
    ".aa .on .c,.aa .c.on{fill:var(--ambre-f);stroke:var(--ambre);stroke-width:2}",
    ".aa .ok .c,.aa .c.ok{fill:var(--vert-f);stroke:var(--vert);stroke-width:2}",
    ".aa .ko .c,.aa .c.ko{fill:var(--rouge-f);stroke:var(--rouge);stroke-width:2}",
    ".aa .bl .c,.aa .c.bl{fill:var(--bleu-f);stroke:var(--bleu);stroke-width:2}",
    ".aa .q0 .c{fill:var(--bleu-f);stroke:var(--bleu)}.aa .q1 .c{fill:var(--vert-f);stroke:var(--vert)}.aa .q2 .c{fill:var(--ambre-f);stroke:var(--ambre)}.aa .q3 .c{fill:var(--rouge-f);stroke:var(--rouge)}",
    ".aa .muet{opacity:.38}.aa .trait{stroke:var(--ligne2);stroke-width:1.2;fill:none}.aa .fl{stroke:var(--ambre);stroke-width:2;fill:none}.aa .fl.v{stroke:var(--vert)}",
    ".aa .tete-l{fill:var(--ambre)}.aa .fen{fill:none;stroke:var(--bleu);stroke-width:2;stroke-dasharray:5 3}",
    ".aa .legende{display:flex;flex-wrap:wrap;gap:6px 14px;font-family:var(--mono);font-size:.76rem;color:var(--encre2);margin-top:8px}",
    ".aa .legende i{display:inline-block;width:12px;height:12px;border-radius:3px;vertical-align:-2px;margin-right:5px;border:1.5px solid}",
    ".aa .code-l{font-family:var(--mono);font-size:.82rem;white-space:pre;line-height:1.55;padding:8px 10px;border:1px solid var(--ligne);border-radius:8px;background:var(--code-bg);overflow-x:auto}",
    ".aa .code-l .l{display:block;padding:0 4px;border-radius:4px}.aa .code-l .l.vise{background:var(--ambre-f);box-shadow:inset 3px 0 0 var(--ambre)}",
    ".aa .vars{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px;font-family:var(--mono);font-size:.82rem}.aa .vars span{border:1px solid var(--ligne2);border-radius:7px;padding:3px 8px;background:var(--bg2)}.aa .vars span.chg{border-color:var(--ambre);background:var(--ambre-f)}",
    ".aa .reecr{font-family:var(--mono);font-size:.84rem;display:flex;flex-direction:column;gap:4px}.aa .reecr div{padding:3px 8px;border-radius:6px;border-left:3px solid var(--ligne2);overflow-wrap:anywhere}.aa .reecr div.der{border-left-color:var(--vert);background:var(--vert-f)}",
    ".aa .deux{display:grid;gap:10px}@media (min-width:720px){.aa .deux{grid-template-columns:1.1fr 1fr}}",
    ".aa table{font-family:var(--mono);font-size:.78rem}.aa table td,.aa table th{padding:4px 7px;white-space:nowrap}",
    ".aa .jauge{font-family:var(--mono);font-size:.76rem;color:var(--encre2)}",
    "html.mo .aa .mv{transition:transform .55s cubic-bezier(.3,.7,.2,1)}",
    "html.mo .aa .jg{transition:width .7s cubic-bezier(.3,.7,.2,1)}",
    "html.mo .aa .neuf{animation:aa-pop .45s cubic-bezier(.2,.8,.2,1)}",
    "html.mo .aa .instant .mv,html.mo .aa .instant .jg{transition:none}",
    "@keyframes aa-pop{from{opacity:.2;transform:translateY(-6px)}}"
  ].join("\n");
  var st = document.createElement("style");
  st.id = "anim-algo-css";
  st.textContent = css;
  (document.head || document.documentElement).appendChild(st);
})();

function aaPos(el, x, y) { el.style.transform = "translate(" + x + "px," + y + "px)"; }
function aaInstant(scene, saut) {
  if (!saut) { scene.classList.remove("instant"); return function () {}; }
  scene.classList.add("instant");
  return function () { void scene.getBoundingClientRect(); scene.classList.remove("instant"); };
}
function aaCase(cls, x, y, w, h, txt, extra) {
  return '<g class="' + cls + '"' + (extra || "") + '><rect class="c" x="' + x + '" y="' + y + '" width="' + w + '" height="' + h + '" rx="5"/><text x="' + (x + w / 2) + '" y="' + (y + h / 2) + '">' + txt + "</text></g>";
}

/* ===================== 1. Tri fusion ===================== */
WIDGETS_EXT["algo-tri-fusion"] = function (z, opt, O) {
  var T = [38, 27, 43, 3, 9, 82, 10, 15], CW = 34, CH = 26, RH = 40;
  function fusion(a, b) { var r = [], i = 0, j = 0; while (i < a.length && j < b.length) r.push(a[i] <= b[j] ? a[i++] : b[j++]); return r.concat(a.slice(i), b.slice(j)); }
  function groupes(taille) { var g = []; for (var k = 0; k < 8; k += taille) g.push(T.slice(k, k + taille)); return g; }
  var TAILLES = [8, 4, 2, 1, 2, 4, 8];
  function rangees() {
    var R = [0, 1, 2, 3].map(function (r) { return groupes(TAILLES[r]); });
    var prec = R[3];
    for (var r = 4; r < 7; r++) { var nv = []; for (var k = 0; k < prec.length; k += 2) nv.push(fusion(prec[k], prec[k + 1])); R.push(nv); prec = nv; }
    return R;
  }
  var RG = rangees();
  function x(i, taille) { var larg = 8 * CW + (8 / taille - 1) * 9; return (340 - larg) / 2 + i * CW + Math.floor(i / taille) * 9; }
  function etapesTout() {
    var E = [];
    function snap(vis, cour, src, msg) { E.push({ vis: vis, cour: cour, src: src, msg: msg }); }
    snap({ 0: 8 }, [0, 0], null, "La liste de 8 éléments à trier. Première phase : on <b>divise</b> jusqu’à n’avoir que des listes d’un élément.");
    snap({ 0: 8, 1: 8 }, [1, -1], null, "<b>Diviser</b> : on coupe en deux moitiés de 4. Elles sont <b>indépendantes</b> : chacune sera triée sans regarder l’autre.");
    snap({ 0: 8, 1: 8, 2: 8 }, [2, -1], null, "Encore une division : quatre listes de 2.");
    snap({ 0: 8, 1: 8, 2: 8, 3: 8 }, [3, -1], null, "Huit listes d’<b>un</b> élément : c’est le <b>cas de base</b>, elles sont déjà triées. Il y a eu log₂ 8 = 3 niveaux de division.");
    var vis = { 0: 8, 1: 8, 2: 8, 3: 8 };
    for (var r = 4; r < 7; r++) {
      var n = RG[r].length, taille = TAILLES[r];
      for (var g = 0; g < n; g++) {
        vis = JSON.parse(JSON.stringify(vis)); vis[r] = (g + 1) * taille;
        var a = RG[r - 1][2 * g], b = RG[r - 1][2 * g + 1];
        snap(vis, [r, g], [r - 1, 2 * g, 2 * g + 1], "<b>Fusionner</b> [" + a.join(", ") + "] et [" + b.join(", ") + "] : on compare les têtes, on prend la plus petite → <b>[" + RG[r][g].join(", ") + "]</b>." + (r === 6 ? " La liste est triée. Chaque niveau de fusion a traité les 8 éléments : 3 niveaux × 8 = au plus 24 comparaisons, soit n log₂ n." : ""));
      }
    }
    return E;
  }
  function etapesFusion() {
    var a = [3, 27, 38, 43], b = [9, 10, 15, 82], i = 0, j = 0, res = [], E = [], src;
    E.push({ a: a, b: b, i: 0, j: 0, res: [], src: null, msg: "Deux listes <b>déjà triées</b>. On regarde leurs <b>têtes</b> (flèches) : le plus petit élément de tout l’ensemble est forcément l’une des deux." });
    while (i < a.length && j < b.length) {
      if (a[i] <= b[j]) { src = ["a", i]; res.push(a[i]); E.push({ a: a, b: b, i: i + 1, j: j, res: res.slice(), src: src, msg: "Comparer " + a[i] + " et " + b[j] + " : <b>" + a[i] + "</b> est le plus petit, il descend dans le résultat ; la flèche de la liste du haut avance." }); i++; }
      else { src = ["b", j]; res.push(b[j]); E.push({ a: a, b: b, i: i, j: j + 1, res: res.slice(), src: src, msg: "Comparer " + a[i] + " et " + b[j] + " : <b>" + b[j] + "</b> est le plus petit, il descend ; la flèche de la liste du bas avance." }); j++; }
    }
    var reste = a.slice(i).concat(b.slice(j));
    res = res.concat(reste);
    E.push({ a: a, b: b, i: i, j: j + (i < a.length ? 0 : reste.length), res: res, src: null, msg: "Une liste est épuisée : on <b>recopie le reste</b> de l’autre (" + reste.join(", ") + ") sans comparer. Bilan : " + (E.length - 1) + " comparaisons pour 8 éléments, au plus p + q − 1 = 7. La fusion est <b>linéaire</b>." });
    return E;
  }
  function prepare(sc, k) {
    if (k === "tout") {
      var s = '<svg viewBox="0 0 340 ' + (7 * RH + 14) + '" role="img" aria-label="Arbre du tri fusion">';
      for (var r = 0; r < 7; r++) {
        if (r === 4) s += '<line class="trait" x1="6" x2="334" y1="' + (r * RH + 4) + '" y2="' + (r * RH + 4) + '" stroke-dasharray="4 4"/>';
        for (var i = 0; i < 8; i++) {
          var v = RG[r][Math.floor(i / TAILLES[r])][i % TAILLES[r]];
          s += aaCase("vide", x(i, TAILLES[r]), r * RH + 10, CW - 4, CH, v, ' id="tf-' + r + "-" + i + '"');
        }
      }
      s += '<text class="p g" x="4" y="6">diviser ↓</text><text class="p g" x="4" y="' + (4 * RH + 2) + '">fusionner ↓</text></svg>';
      sc.innerHTML = '<div class="aa">' + s + '<div class="legende"><span><i style="background:var(--ambre-f);border-color:var(--ambre)"></i>en cours</span><span><i style="background:var(--bleu-f);border-color:var(--bleu)"></i>listes fusionnées</span></div></div>';
    } else {
      var t = '<svg viewBox="0 0 340 250" role="img" aria-label="Fusion de deux listes triées">';
      t += '<text class="t g" x="6" y="22">a</text><text class="t g" x="6" y="92">b</text><text class="t g" x="6" y="192">résultat</text>';
      for (var k2 = 0; k2 < 4; k2++) { t += aaCase("", 40 + k2 * 44, 10, 38, 26, [3, 27, 38, 43][k2], ' id="fa-' + k2 + '"'); t += aaCase("", 40 + k2 * 44, 80, 38, 26, [9, 10, 15, 82][k2], ' id="fb-' + k2 + '"'); }
      for (var m = 0; m < 8; m++) t += aaCase("vide", 6 + m * 41, 205, 36, 26, "", ' id="fr-' + m + '"');
      t += '<g id="pa" class="mv"><path class="tete-l" d="M0 0 L-7 10 L7 10z"/></g><g id="pb" class="mv"><path class="tete-l" d="M0 0 L-7 10 L7 10z"/></g><g id="vol" class="mv" style="opacity:0"><rect class="c on" x="-19" y="-13" width="38" height="26" rx="5"/><text x="0" y="0"></text></g></svg>';
      sc.innerHTML = '<div class="aa">' + t + "</div>";
    }
  }
  function dessine(sc, e, i, E, saut) {
    var aa = sc.querySelector(".aa");
    if (e.vis) {
      for (var r = 0; r < 7; r++) for (var c = 0; c < 8; c++) {
        var el = sc.querySelector("#tf-" + r + "-" + c), vu = e.vis[r] !== undefined && c < e.vis[r];
        var cl = vu ? "" : "vide";
        var taille = TAILLES[r];
        if (vu && e.cour[0] === r && (e.cour[1] === -1 || Math.floor(c / taille) === e.cour[1])) cl = "on" + (!saut && (r >= 4 || e.cour[1] === -1) ? " neuf" : "");
        else if (vu && e.src && e.src[0] === r && (Math.floor(c / TAILLES[r]) === e.src[1] || Math.floor(c / TAILLES[r]) === e.src[2])) cl = "bl";
        else if (vu && r < 4 && e.cour[0] >= 4) cl = "muet";
        el.setAttribute("class", cl);
      }
      return;
    }
    var fin = aaInstant(aa, saut);
    for (var k = 0; k < 4; k++) { sc.querySelector("#fa-" + k).setAttribute("class", k < e.i ? "muet" : k === e.i ? "on" : ""); sc.querySelector("#fb-" + k).setAttribute("class", k < e.j ? "muet" : k === e.j ? "on" : ""); }
    for (var m = 0; m < 8; m++) { var rc = sc.querySelector("#fr-" + m); rc.setAttribute("class", m < e.res.length ? (m === e.res.length - 1 && e.src ? "ok" : "bl") : "vide"); rc.querySelector("text").textContent = m < e.res.length ? e.res[m] : ""; }
    aaPos(sc.querySelector("#pa"), 59 + Math.min(e.i, 3.6) * 44, 40);
    aaPos(sc.querySelector("#pb"), 59 + Math.min(e.j, 3.6) * 44, 110);
    sc.querySelector("#pa").style.opacity = e.i < 4 ? 1 : 0;
    sc.querySelector("#pb").style.opacity = e.j < 4 ? 1 : 0;
    var vol = sc.querySelector("#vol");
    if (e.src && !saut && O.MO()) {
      var x0 = 59 + e.src[1] * 44, y0 = e.src[0] === "a" ? 23 : 93, d = e.res.length - 1;
      vol.querySelector("text").textContent = e.res[d];
      vol.style.transition = "none"; vol.style.opacity = 1; aaPos(vol, x0, y0); void vol.getBoundingClientRect();
      vol.style.transition = ""; aaPos(vol, 24 + d * 41, 218);
      setTimeout(function () { vol.style.opacity = 0; }, 560);
    } else vol.style.opacity = 0;
    fin();
  }
  var L = O.lecteur(z, { titre: "tri fusion pas à pas", sous: "diviser, puis fusionner", choix: [{ k: "tout", t: "vue d’ensemble" }, { k: "fusion", t: "une fusion pas à pas" }],
    etapes: function (k) { return k === "tout" ? etapesTout() : etapesFusion(); }, prepare: prepare, dessine: dessine, vitesse: 1700 });
  if (opt === "fusion") L.charger("fusion");
};

/* ===================== 2. Rotation d'image sur place ===================== */
WIDGETS_EXT["algo-rotation"] = function (z, opt, O) {
  var N = 4, C = 46, X0 = 60, Y0 = 14;
  var L0 = "ABCDEFGHIJKLMNOP".split("");
  function quart(lettre) { var k = L0.indexOf(lettre), i = Math.floor(k / N), j = k % N; return (i < 2 ? 0 : 2) + (j < 2 ? 0 : 1); }
  function etapes() {
    var img = [], E = [];
    for (var i = 0; i < N; i++) img.push(L0.slice(i * N, i * N + N));
    function snap(msg, vise) { E.push({ img: img.map(function (l) { return l.slice(); }), vise: vise || [], msg: msg }); }
    function cycle(x, y, h, i, j) {
      var hg = img[y + i][x + j];
      img[y + i][x + j] = img[y + h + i][x + j];
      img[y + h + i][x + j] = img[y + h + i][x + h + j];
      img[y + h + i][x + h + j] = img[y + i][x + h + j];
      img[y + i][x + h + j] = hg;
      return [[y + i, x + j], [y + h + i, x + j], [y + h + i, x + h + j], [y + i, x + h + j]];
    }
    snap("Une image de 4 × 4 pixels (une lettre par pixel). Les couleurs repèrent les <b>quatre quarts</b> de départ. But : un quart de tour dans le sens horaire, <b>sans seconde image</b>.");
    var Q = [[0, 0, "haut gauche"], [2, 0, "haut droit"], [0, 2, "bas gauche"], [2, 2, "bas droit"]];
    Q.forEach(function (q) {
      var v = cycle(q[0], q[1], 1, 0, 0);
      snap("<b>Régner</b> : appel récursif sur le quart " + q[2] + " (2 × 2). Il tourne d’un quart de tour sur lui-même : ses 4 pixels font un échange circulaire.", v);
    });
    for (var i2 = 0; i2 < 2; i2++) for (var j2 = 0; j2 < 2; j2++) {
      var v2 = cycle(0, 0, 2, i2, j2);
      snap("<b>Combiner</b> : on fait tourner les quarts. Échange circulaire de 4 pixels, un par quart (haut gauche → haut droit → bas droit → bas gauche → haut gauche), avec une seule variable auxiliaire. (" + (2 * i2 + j2 + 1) + "/4)", v2);
    }
    snap("Terminé : chaque couleur a changé de quart et chaque quart a tourné. Le pixel en haut à gauche est M, l’ancien coin bas gauche. Aucune copie de l’image : la mémoire utilisée ne dépend pas de la taille.");
    return E;
  }
  function prepare(sc) {
    var s = '<svg viewBox="0 0 310 ' + (N * C + 30) + '" role="img" aria-label="Rotation d’une image 4 × 4">';
    s += '<rect x="' + (X0 - 4) + '" y="' + (Y0 - 4) + '" width="' + (N * C + 8) + '" height="' + (N * C + 8) + '" rx="8" class="trait"/>';
    s += '<line class="trait" x1="' + (X0 + 2 * C) + '" x2="' + (X0 + 2 * C) + '" y1="' + (Y0 - 4) + '" y2="' + (Y0 + N * C + 4) + '" stroke-dasharray="4 4"/><line class="trait" y1="' + (Y0 + 2 * C) + '" y2="' + (Y0 + 2 * C) + '" x1="' + (X0 - 4) + '" x2="' + (X0 + N * C + 4) + '" stroke-dasharray="4 4"/>';
    L0.forEach(function (l) { s += '<g id="rot-' + l + '" class="mv q' + quart(l) + '"><rect class="c" x="3" y="3" width="' + (C - 6) + '" height="' + (C - 6) + '" rx="7"/><text x="' + C / 2 + '" y="' + C / 2 + '" style="font-size:17px;font-weight:700">' + l + "</text></g>"; });
    s += "</svg>";
    sc.innerHTML = '<div class="aa">' + s + "</div>";
  }
  function dessine(sc, e, i, E, saut) {
    var fin = aaInstant(sc.querySelector(".aa"), saut);
    var vise = {}; e.vise.forEach(function (p) { vise[p[0] + "-" + p[1]] = 1; });
    for (var r = 0; r < N; r++) for (var c = 0; c < N; c++) {
      var g = sc.querySelector("#rot-" + e.img[r][c]);
      aaPos(g, X0 + c * C, Y0 + r * C);
      g.querySelector("rect").style.strokeWidth = vise[r + "-" + c] ? "3.5" : "";
    }
    fin();
  }
  O.lecteur(z, { titre: "rotation d’un quart de tour, sur place", sous: "diviser pour régner", etapes: etapes, prepare: prepare, dessine: dessine, vitesse: 1800 });
};

/* ===================== 3. Tables de programmation dynamique ===================== */
WIDGETS_EXT["algo-table-dyn"] = function (z, opt, O) {
  var P = [1, 3, 4], S = 10, A = "PYTHON", B = "PHOTON";
  function etapesMonnaie() {
    var nb = [0], ch = [0], E = [];
    E.push({ nb: nb.slice(), ch: ch.slice(), s: 0, cand: [], msg: "Pièces 1, 3 et 4. <b>nb[s]</b> = nombre minimal de pièces pour rendre s. Cas de base : nb[0] = 0. On remplit de gauche à droite." });
    for (var s = 1; s <= S; s++) {
      var best = s + 1, bp = 0, cand = [];
      P.forEach(function (p) { if (p <= s) { cand.push(s - p); if (nb[s - p] + 1 < best) { best = nb[s - p] + 1; bp = p; } } });
      nb.push(best); ch.push(bp);
      var det = P.filter(function (p) { return p <= s; }).map(function (p) { return "1 + nb[" + (s - p) + "] = " + (nb[s - p] + 1); }).join(" ; ");
      E.push({ nb: nb.slice(), ch: ch.slice(), s: s, cand: cand, choisi: s - bp, msg: "<b>s = " + s + "</b> : on essaie chaque première pièce possible : " + det + ". Minimum <b>" + best + "</b> (première pièce " + bp + "). Les cases utilisées sont déjà remplies." });
    }
    var reste = S, chemin = [];
    while (reste > 0) { chemin.push(reste); reste -= ch[reste]; }
    E.push({ nb: nb, ch: ch, s: -1, cand: [], chemin: chemin, msg: "<b>Reconstruction</b> pour 10 : choix[10] = 3, il reste 7 ; choix[7] = 3, il reste 4 ; choix[4] = 4, il reste 0. Réponse : <b>3 + 3 + 4</b>, 3 pièces. (Le glouton aurait donné 4 + 4 + 1 + 1.)" });
    return E;
  }
  function etapesLcs() {
    var n = A.length, m = B.length, L = [], E = [], i, j;
    for (i = 0; i <= n; i++) { L.push([]); for (j = 0; j <= m; j++) L[i].push(i && j ? null : 0); }
    function cp() { return L.map(function (l) { return l.slice(); }); }
    E.push({ L: cp(), cur: null, dep: [], msg: "Table L de 7 × 7 : L[i][j] = longueur de la plus longue sous-séquence commune aux i premières lettres de PYTHON et aux j premières de PHOTON. Ligne 0 et colonne 0 : mot vide, 0." });
    for (i = 1; i <= n; i++) for (j = 1; j <= m; j++) {
      var eg = A[i - 1] === B[j - 1];
      L[i][j] = eg ? L[i - 1][j - 1] + 1 : Math.max(L[i - 1][j], L[i][j - 1]);
      E.push({ L: cp(), cur: [i, j], dep: eg ? [[i - 1, j - 1]] : [[i - 1, j], [i, j - 1]], eg: eg,
        msg: "L[" + i + "][" + j + "] : " + A[i - 1] + (eg ? " = " : " ≠ ") + B[j - 1] + (eg ? " → diagonale + 1 = <b>" + L[i][j] + "</b>." : " → max(haut, gauche) = <b>" + L[i][j] + "</b>.") });
    }
    i = n; j = m; var ch = [], res = "";
    while (i > 0 && j > 0) {
      ch.push([i, j]);
      if (A[i - 1] === B[j - 1]) { res = A[i - 1] + res; i--; j--; }
      else if (L[i - 1][j] >= L[i][j - 1]) i--; else j--;
      E.push({ L: cp(), cur: null, dep: [], chemin: ch.slice(), lu: res, msg: "<b>Remontée</b> depuis la case en bas à droite : diagonale quand les lettres sont égales (on note la lettre), sinon vers la plus grande voisine. Lettres notées : <b>" + (res || "…") + "</b>" + (i === 0 || j === 0 ? ". Fin : PLSC de longueur " + L[n][m] + "." : "") });
    }
    return E;
  }
  function svgMonnaie(e, saut) {
    var W = 29, X = 10, s = '<svg viewBox="0 0 340 162" role="img" aria-label="Tableau nb du rendu de monnaie">';
    for (var k = 0; k <= S; k++) {
      var vu = k < e.nb.length, cl = !vu ? "vide" : k === e.s ? "on" + (saut ? "" : " neuf") : e.cand.indexOf(k) >= 0 ? (k === e.choisi ? "ok" : "bl") : e.chemin && e.chemin.indexOf(k) >= 0 ? "ok" : "";
      s += '<text class="p" x="' + (X + k * W + 13) + '" y="20">' + k + "</text>" + aaCase(cl, X + k * W, 30, 26, 28, vu ? e.nb[k] : "");
      if (vu && k > 0) s += '<text class="p" x="' + (X + k * W + 13) + '" y="132">' + e.ch[k] + "</text>";
    }
    s += '<text class="p g" x="10" y="152">en haut : s · cases : nb[s] · en bas : choix[s]</text>';
    if (e.s > 0) e.cand.forEach(function (c) { var x1 = X + c * W + 13, x2 = X + e.s * W + 13; s += '<path class="fl' + (c === e.choisi ? " v" : "") + '" d="M' + x1 + " 60 Q" + (x1 + x2) / 2 + " " + (88 + (x2 - x1) / 4) + " " + x2 + ' 60"/>'; });
    if (e.chemin) { for (var q = 0; q < e.chemin.length; q++) { var a = e.chemin[q], b = a - e.ch[a]; var xa = X + a * W + 13, xb = X + b * W + 13; s += '<path class="fl v" d="M' + xa + " 30 Q" + (xa + xb) / 2 + " " + (6 - (xa - xb) / 6) + " " + xb + ' 30"/><text class="t" x="' + (xa + xb) / 2 + '" y="' + (12 - (xa - xb) / 12) + '">' + e.ch[a] + "</text>"; } }
    return s + "</svg>";
  }
  function svgLcs(e, saut) {
    var W = 34, X = 40, Y = 34, s = '<svg viewBox="0 0 300 290" role="img" aria-label="Table de la plus longue sous-séquence commune">';
    for (var j = 0; j <= 6; j++) s += '<text class="t" x="' + (X + j * W + 16) + '" y="12">' + (j ? B[j - 1] : "·") + "</text>";
    for (var i = 0; i <= 6; i++) {
      s += '<text class="t" x="20" y="' + (Y + i * W + 15) + '">' + (i ? A[i - 1] : "·") + "</text>";
      for (var k = 0; k <= 6; k++) {
        var v = e.L[i][k], cl = v === null ? "vide" : "";
        if (e.cur && e.cur[0] === i && e.cur[1] === k) cl = "on" + (saut ? "" : " neuf");
        else if (e.dep.some(function (d) { return d[0] === i && d[1] === k; })) cl = "bl";
        else if (e.chemin && e.chemin.some(function (d) { return d[0] === i && d[1] === k; })) cl = A[i - 1] === B[k - 1] ? "ok" : "bl";
        s += aaCase(cl, X + k * W, Y + i * W, 30, 30, v === null ? "" : v);
      }
    }
    if (e.lu !== undefined) s += '<text x="150" y="282" style="font-weight:700">PLSC : ' + (e.lu || "…") + "</text>";
    return s + "</svg>";
  }
  var L = O.lecteur(z, { titre: "une table qui se remplit", sous: "programmation dynamique", choix: [{ k: "monnaie", t: "rendu de monnaie" }, { k: "lcs", t: "PLSC PYTHON / PHOTON" }],
    etapes: function (k) { return k === "lcs" ? etapesLcs() : etapesMonnaie(); },
    dessine: function (sc, e, i, E, saut) { sc.innerHTML = '<div class="aa">' + (e.L ? svgLcs(e, saut) : svgMonnaie(e, saut)) + '<div class="legende"><span><i style="background:var(--ambre-f);border-color:var(--ambre)"></i>case calculée</span><span><i style="background:var(--bleu-f);border-color:var(--bleu)"></i>cases utilisées</span><span><i style="background:var(--vert-f);border-color:var(--vert)"></i>choix retenu</span></div></div>'; },
    vitesse: 1200 });
  if (opt === "lcs") L.charger("lcs");
};

/* ===================== 4. Recherche textuelle : naïf et Horspool ===================== */
WIDGETS_EXT["algo-boyer-moore"] = function (z, opt, O) {
  var T = "LES BANANES ET LES ANANAS", M = "ANANAS", n = T.length, m = M.length, W = 13.4, X = 6;
  var D = {}; for (var k = 0; k < m - 1; k++) D[M[k]] = m - 1 - k;
  function etapes(mode) {
    var E = [], i = 0, cmp = 0, trouve = [];
    function snap(o) { o.cmp = cmp; o.trouve = trouve.slice(); E.push(o); }
    snap({ i: 0, j: null, msg: mode === "naif" ? "Algorithme <b>naïf</b> : on compare de <b>gauche à droite</b> ; à chaque échec, la fenêtre avance d’<b>une</b> case." : "Boyer-Moore-Horspool : table de décalage (prétraitement du motif) : <b>A → 1, N → 2</b>, tout autre caractère → 6. On compare de <b>droite à gauche</b>." });
    while (i <= n - m) {
      var j = mode === "naif" ? 0 : m - 1, ok = true, res = {};
      while (mode === "naif" ? j < m : j >= 0) {
        cmp++;
        var eg = T[i + j] === M[j]; res[j] = eg ? "ok" : "ko";
        snap({ i: i, j: j, res: JSON.parse(JSON.stringify(res)), msg: "Fenêtre en " + i + " : texte[" + (i + j) + "] = " + (T[i + j] === " " ? "espace" : T[i + j]) + (eg ? " = " : " ≠ ") + M[j] + " (motif[" + j + "])." + (eg ? "" : " <b>Échec.</b>") });
        if (!eg) { ok = false; break; }
        j = mode === "naif" ? j + 1 : j - 1;
      }
      if (ok) trouve.push(i);
      var saut = mode === "naif" ? 1 : (D[T[i + m - 1]] || m), c = T[i + m - 1];
      var txt = (ok ? "<b>Occurrence trouvée en " + i + "</b>. " : "") + (mode === "naif" ? "On avance d’une case." : "Sous la dernière case de la fenêtre : « " + (c === " " ? "espace" : c) + " » → saut de <b>" + saut + "</b>" + (saut === m ? " (absent de la table : on saute tout le motif)." : "."));
      i += saut;
      if (i <= n - m) snap({ i: i, j: null, res: {}, msg: txt });
      else snap({ i: i - saut, j: null, res: res, fin: true, msg: txt + " La fenêtre dépasserait le texte : fin. <b>" + cmp + " comparaisons</b> " + (mode === "naif" ? "(Horspool en fait 13 sur cet exemple)." : "(le naïf en fait 31 sur cet exemple).") });
    }
    return E;
  }
  function prepare(sc) {
    var s = '<svg viewBox="0 0 345 120" role="img" aria-label="Fenêtre de recherche glissant sur le texte">';
    for (var k = 0; k < n; k++) { s += '<text class="p" x="' + (X + k * W + W / 2) + '" y="10">' + (k % 5 === 0 ? k : "") + "</text>"; s += aaCase("", X + k * W, 18, W - 1.5, 24, T[k] === " " ? "␣" : T[k], ' id="bt-' + k + '"'); }
    s += '<g id="bmot" class="mv">';
    for (k = 0; k < m; k++) s += aaCase("", k * W, 0, W - 1.5, 24, M[k], ' id="bm-' + k + '"');
    s += '<rect class="fen" x="-2" y="-48" width="' + (m * W + 2.5) + '" height="76" rx="6"/></g>';
    s += '<text id="bcpt" class="t g" x="6" y="108"></text><text id="btrouve" class="t" x="300" y="108"></text></svg>';
    sc.innerHTML = '<div class="aa">' + s + "</div>";
  }
  function dessine(sc, e, i, E, saut) {
    var fin = aaInstant(sc.querySelector(".aa"), saut);
    aaPos(sc.querySelector("#bmot"), X + e.i * W, 62);
    for (var k = 0; k < m; k++) sc.querySelector("#bm-" + k).setAttribute("class", e.res && e.res[k] ? e.res[k] : (e.j === null && !e.fin && k === m - 1 && E[0].msg.indexOf("Horspool") >= 0 ? "on" : ""));
    for (k = 0; k < n; k++) {
      var cl = "";
      e.trouve.forEach(function (t) { if (k >= t && k < t + m) cl = "ok"; });
      if (e.j !== null && e.j !== undefined && k === e.i + e.j) cl = e.res[e.j];
      sc.querySelector("#bt-" + k).setAttribute("class", cl);
    }
    sc.querySelector("#bcpt").textContent = "comparaisons : " + e.cmp;
    sc.querySelector("#btrouve").textContent = e.trouve.length ? "trouvé en " + e.trouve.join(", ") : "";
    fin();
  }
  var L = O.lecteur(z, { titre: "la fenêtre glisse sur le texte", sous: "ANANAS dans « LES BANANES ET LES ANANAS »", choix: [{ k: "horspool", t: "Boyer-Moore-Horspool" }, { k: "naif", t: "naïf" }],
    etapes: etapes, prepare: prepare, dessine: dessine, vitesse: 1100 });
  if (opt === "naif") L.charger("naif");
};

/* ===================== 5. Machine de Turing ===================== */
WIDGETS_EXT["algo-turing"] = function (z, opt, O) {
  var TR = [["debut", "0", "0", "D", "debut"], ["debut", "1", "1", "D", "debut"], ["debut", "_", "_", "G", "retenue"], ["retenue", "1", "0", "G", "retenue"], ["retenue", "0", "1", "-", "fin"], ["retenue", "_", "1", "-", "fin"]];
  var CW = 34, X0 = 14, NC = 9;
  function etapes(mot) {
    var ruban = {}, E = [], pos = 0, etat = "debut", k;
    for (k = 0; k < mot.length; k++) ruban[k] = mot[k];
    function vue() { var t = []; for (var c = -2; c < NC - 2; c++) t.push(ruban[c] || "_"); return t; }
    E.push({ r: vue(), pos: 0, etat: etat, ligne: -1, ecrit: null, msg: "Ruban : le nombre binaire <b>" + mot + "</b> (" + parseInt(mot, 2) + " en décimal). Tête sur le premier chiffre, état <b>debut</b>. Les cases vides contiennent le blanc _." });
    var garde = 0;
    while (etat !== "fin" && garde++ < 50) {
      var lu = ruban[pos] || "_", li = -1;
      TR.forEach(function (t, q) { if (t[0] === etat && t[1] === lu) li = q; });
      var t = TR[li];
      ruban[pos] = t[2];
      var avant = pos;
      pos += t[3] === "G" ? -1 : t[3] === "D" ? 1 : 0;
      var ancien = etat; etat = t[4];
      E.push({ r: vue(), pos: pos, etat: etat, ligne: li, ecrit: avant, msg: "État <b>" + ancien + "</b>, lu <b>" + lu + "</b> → écrire <b>" + t[2] + "</b>, " + (t[3] === "G" ? "aller à gauche" : t[3] === "D" ? "aller à droite" : "ne pas bouger") + ", état <b>" + etat + "</b>." + (etat === "fin" ? " La machine s’arrête : le ruban contient <b>" + vue().join("").replace(/_/g, "") + "</b> (" + (parseInt(mot, 2) + 1) + ")." : "") });
    }
    return E;
  }
  function prepare(sc) {
    var s = '<svg viewBox="0 0 340 112" role="img" aria-label="Ruban et tête d’une machine de Turing">';
    for (var c = 0; c < NC; c++) s += aaCase("", X0 + c * CW, 46, CW - 3, 32, "", ' id="tu-' + c + '"') + '<text class="p" x="' + (X0 + c * CW + 15.5) + '" y="90">' + (c - 2) + "</text>";
    s += '<text class="p g" x="' + X0 + '" y="104">…ruban infini des deux côtés…</text>';
    s += '<g id="tete" class="mv"><path class="tete-l" d="M0 40 L-9 26 L9 26z"/><rect x="-32" y="0" width="64" height="22" rx="11" style="fill:var(--ambre-f);stroke:var(--ambre)"/><text id="tetat" x="0" y="11" style="font-size:11.5px"></text></g></svg>';
    var tab = '<div class="tab-wrap" style="margin-top:8px"><table class="petit"><tr><th>état</th><th>lu</th><th>écrit</th><th>dépl.</th><th>nouvel état</th></tr>' + TR.map(function (t, q) { return '<tr id="tl-' + q + '"><td>' + t.join("</td><td>") + "</td></tr>"; }).join("") + "</table></div>";
    sc.innerHTML = '<div class="aa">' + s + tab + "</div>";
  }
  function dessine(sc, e, i, E, saut) {
    var fin = aaInstant(sc.querySelector(".aa"), saut);
    for (var c = 0; c < NC; c++) { var g = sc.querySelector("#tu-" + c); g.querySelector("text").textContent = e.r[c]; g.setAttribute("class", e.ecrit !== null && c === e.ecrit + 2 ? "ok" + (saut ? "" : " neuf") : e.r[c] === "_" ? "muet" : ""); }
    aaPos(sc.querySelector("#tete"), X0 + (e.pos + 2) * CW + 15.5, 2);
    sc.querySelector("#tetat").textContent = e.etat;
    for (var q = 0; q < TR.length; q++) { var tr = sc.querySelector("#tl-" + q); tr.style.background = q === e.ligne ? "var(--ambre-f)" : ""; tr.style.fontWeight = q === e.ligne ? "700" : ""; }
    fin();
  }
  O.lecteur(z, { titre: "machine de Turing : ajouter 1 en binaire", choix: [{ k: "1011", t: "ruban 1011" }, { k: "111", t: "ruban 111" }], etapes: etapes, prepare: prepare, dessine: dessine, vitesse: 1300 });
};

/* ===================== 6. Trois paradigmes en action ===================== */
WIDGETS_EXT["algo-paradigmes"] = function (z, opt, O) {
  var CODE_IMP = ["s = 0", "for x in t:", "    if x % 2 == 0:", "        s = s + x * x", "print(s)"];
  function etapes(k) {
    var E = [];
    if (k === "imp") {
      var t = [1, 2, 3, 4], s = 0;
      E.push({ l: 1, v: { t: "[1, 2, 3, 4]" }, chg: "", msg: "Impératif : on exécute des <b>instructions</b> qui modifient un <b>état</b> (la mémoire, à droite). Pour savoir ce que vaut s, il faut savoir où on en est." });
      E.push({ l: 1, v: { t: "[1, 2, 3, 4]", s: 0 }, chg: "s", msg: "Affectation : s reçoit 0." });
      t.forEach(function (x) {
        E.push({ l: 2, v: { t: "[1, 2, 3, 4]", s: s, x: x }, chg: "x", msg: "La boucle donne à x la valeur " + x + "." });
        E.push({ l: 3, v: { t: "[1, 2, 3, 4]", s: s, x: x }, chg: "", msg: x + " % 2 == 0 : " + (x % 2 === 0 ? "vrai." : "faux, on passe.") });
        if (x % 2 === 0) { s += x * x; E.push({ l: 4, v: { t: "[1, 2, 3, 4]", s: s, x: x }, chg: "s", msg: "s est <b>modifiée</b> : elle vaut maintenant " + s + ". L’ancienne valeur est perdue." }); }
      });
      E.push({ l: 5, v: { t: "[1, 2, 3, 4]", s: s, x: 4 }, chg: "", msg: "Affichage de <b>20</b>. Le résultat est le dernier état de la variable s." });
      return E;
    }
    if (k === "fonc") {
      var R = ["somme(carres(pairs([1, 2, 3, 4])))", "somme(carres([2, 4]))", "somme([4, 16])", "20"];
      var M = ["Fonctionnel : le programme est une <b>expression</b>. On l’évalue en remplaçant chaque appel de fonction par son résultat, de l’intérieur vers l’extérieur. Aucune variable n’est modifiée.", "pairs([1, 2, 3, 4]) vaut [2, 4] : on <b>remplace</b> l’appel par sa valeur (c’est ce que fait filter).", "carres([2, 4]) vaut [4, 16] (map). La liste [2, 4] n’a pas été modifiée : une nouvelle liste est créée.", "somme([4, 16]) vaut <b>20</b>. Une fonction pure peut toujours être remplacée par sa valeur : c’est la <b>transparence référentielle</b>."];
      R.forEach(function (r, q) { E.push({ reecr: R.slice(0, q + 1), msg: M[q] }); });
      var R2 = ["f([1, 2, 3, 4])", "f([2, 3, 4])", "4 + f([3, 4])", "4 + f([4])", "4 + (16 + f([]))", "4 + (16 + 0)", "20"];
      R2.forEach(function (r, q) { E.push({ reecr: R2.slice(0, q + 1), msg: q === 0 ? "Même calcul en <b>récursif</b> (f renvoie 0 pour la liste vide, et ajoute le carré du premier élément s’il est pair) : la boucle est remplacée par la récursion." : q === R2.length - 1 ? "Résultat <b>20</b>, sans jamais modifier de variable." : "On remplace f(…) par sa définition." }); });
      return E;
    }
    var vals = [];
    E.push({ obj: [], appel: "s = Serie()", msg: "Objet : on crée un <b>objet</b> de la classe Serie. Il contient son propre état (l’attribut valeurs), vide pour l’instant." });
    [1, 2, 3, 4].forEach(function (x) { vals.push(x); E.push({ obj: vals.slice(), appel: "s.ajouter(" + x + ")", msg: "On <b>envoie un message</b> à l’objet : la méthode ajouter modifie <b>son</b> attribut valeurs. Personne d’autre n’y touche directement (encapsulation)." }); });
    E.push({ obj: vals.slice(), appel: "s.somme_carres_pairs()  →  20", msg: "La méthode lit l’état de l’objet et renvoie <b>20</b>. Les données et les traitements qui les concernent sont regroupés au même endroit." });
    return E;
  }
  function dessine(sc, e, i, E, saut) {
    var h = '<div class="aa">';
    if (e.l) {
      h += '<div class="deux"><div class="code-l">' + CODE_IMP.map(function (l, q) { return '<span class="l' + (q + 1 === e.l ? " vise" : "") + '">' + O.hlPy(l) + "</span>"; }).join("") + '</div><div><div class="titre-pile">état (variables)</div><div class="vars">' + Object.keys(e.v).map(function (k) { return '<span class="' + (k === e.chg ? "chg" + (saut ? "" : " neuf") : "") + '">' + k + " = " + e.v[k] + "</span>"; }).join("") + "</div></div></div>";
    } else if (e.reecr) {
      h += '<div class="titre-pile">évaluation par réécriture</div><div class="reecr">' + e.reecr.map(function (r, q) { return '<div class="' + (q === e.reecr.length - 1 ? "der" + (saut ? "" : " neuf") : "") + '">' + (q ? "= " : "") + O.esc(r) + "</div>"; }).join("") + "</div>";
    } else {
      h += '<svg viewBox="0 0 330 130" role="img" aria-label="Un objet et son état"><rect x="150" y="12" width="172" height="104" rx="10" style="fill:var(--bleu-f);stroke:var(--bleu);stroke-width:1.5"/><text x="236" y="30" style="font-weight:700">objet Serie</text><text class="t" x="236" y="54">valeurs =</text>';
      e.obj.forEach(function (v, q) { h += aaCase(q === e.obj.length - 1 && /ajouter/.test(e.appel) ? "on" + (saut ? "" : " neuf") : "", 164 + q * 38, 66, 32, 30, v); });
      if (!e.obj.length) h += '<text class="t" x="236" y="81">[ ]</text>';
      h += '<text class="g" x="4" y="64" style="font-size:12px">s</text><path class="fl" d="M18 64 L146 64"/><path class="tete-l" d="M146 59 L154 64 L146 69z"/></svg><div class="code-l"><span class="l vise">' + O.esc(e.appel) + "</span></div>";
    }
    sc.innerHTML = h + "</div>";
  }
  O.lecteur(z, { titre: "un même calcul, trois paradigmes", sous: "somme des carrés des nombres pairs de [1, 2, 3, 4]", choix: [{ k: "imp", t: "impératif" }, { k: "fonc", t: "fonctionnel" }, { k: "obj", t: "objet" }], etapes: etapes, dessine: dessine, vitesse: 1500 });
};

/* ===================== 7. Frise de l'histoire ===================== */
WIDGETS_EXT["algo-frise"] = function (z, opt, O) {
  var ERES = [
    { t: "Antiquité → XVIIe", m: 90, ev: [["−300", "Euclide", "i"], ["825", "al-Khwarizmi", "i"], ["1642", "Pascaline", "m"]], msg: "Des <b>algorithmes</b> sans machines (Euclide, al-Khwarizmi), puis des <b>machines à calculer</b> sans programme (la Pascaline ne sait qu’additionner et soustraire)." },
    { t: "XIXe siècle", m: 85, ev: [["1801", "Jacquard", "m"], ["1843", "Lovelace", "l"], ["1854", "Boole", "i"]], msg: "Les <b>cartes perforées</b> séparent le « programme » du métier à tisser. Ada Lovelace publie un programme pour une machine qui n’existe pas encore : le logiciel naît sur le papier." },
    { t: "1936-1945", m: 80, ev: [["1936", "Turing", "i"], ["1941", "Z3", "m"], ["1945", "von Neumann", "i"]], msg: "<b>1936</b> : la machine universelle (théorie). 1941-1945 : des calculateurs réels, programmés en <b>recâblant</b> ou par film perforé. Le matériel domine." },
    { t: "1946-1949", m: 70, ev: [["1946", "ENIAC", "m"], ["1947", "transistor", "m"], ["1948", "Baby", "l"]], msg: "<b>21 juin 1948</b> : premier programme <b>enregistré en mémoire</b>. Changer de calcul ne demande plus de modifier la machine : le logiciel devient une donnée." },
    { t: "1950-1968", m: 55, ev: [["1952", "A-0", "l"], ["1957", "Fortran", "l"], ["1958", "circuit intégré", "m"]], msg: "Compilateurs et <b>langages de haut niveau</b> : un même programme tourne sur plusieurs machines. Le circuit intégré miniaturise le matériel." },
    { t: "1969-1980", m: 40, ev: [["1969", "ARPANET, Unix", "r"], ["1971", "Intel 4004", "m"], ["1973", "Micral N", "m"]], msg: "<b>1969</b> : ARPANET, Unix, et IBM qui vend ses logiciels à part. Le microprocesseur rend le matériel bon marché ; le logiciel devient un produit." },
    { t: "1981-1999", m: 28, ev: [["1983", "TCP/IP", "r"], ["1991", "Web, Linux, Python", "l"]], msg: "Micro-ordinateurs dans les foyers, <b>Internet</b> (TCP/IP, 1983) et le <b>Web</b> (1989-1991). La valeur et le coût sont désormais surtout dans le logiciel." },
    { t: "depuis 2000", m: 22, ev: [["2007", "smartphone", "m"], ["2016", "AlphaGo", "l"]], msg: "Smartphones (SoC), informatique en nuage et <b>virtualisation</b> : une machine peut être un logiciel. Retour de matériels spécialisés (GPU) pour l’intelligence artificielle." }
  ];
  function etapes() { return ERES.map(function (e, k) { return { k: k, msg: "<b>" + e.t + "</b> — " + e.msg }; }); }
  var COUL = { m: ["var(--bleu)", "var(--bleu-f)", "matériel"], l: ["var(--vert)", "var(--vert-f)", "logiciel"], i: ["var(--ambre)", "var(--ambre-f)", "idée"], r: ["var(--violet)", "var(--bg2)", "réseau"] };
  function prepare(sc) {
    var h = '<div class="aa"><div class="frise-v" style="position:relative;padding-left:18px;border-left:3px solid var(--ligne2);margin-left:8px">';
    ERES.forEach(function (e, k) {
      h += '<div id="fe-' + k + '" style="position:relative;padding:5px 0 7px;transition:opacity .4s">' +
        '<span id="fp-' + k + '" style="position:absolute;left:-26px;top:9px;width:13px;height:13px;border-radius:50%;border:2px solid var(--encre3);background:var(--bg2)"></span>' +
        '<div style="font-family:var(--mono);font-size:.78rem;font-weight:700;color:var(--encre2)">' + e.t + '</div><div style="display:flex;flex-wrap:wrap;gap:5px;margin-top:3px">' +
        e.ev.map(function (v) { var c = COUL[v[2]]; return '<span style="font-family:var(--mono);font-size:.76rem;border:1.5px solid ' + c[0] + ';background:' + c[1] + ';border-radius:7px;padding:2px 7px"><b>' + v[0] + "</b> " + O.esc(v[1]) + "</span>"; }).join("") + "</div></div>";
    });
    h += '</div><div class="jauge" style="margin-top:8px">part du matériel (bleu) et du logiciel (vert) dans l’effort et la valeur — ordre de grandeur illustratif<div style="display:flex;height:14px;border-radius:7px;overflow:hidden;border:1px solid var(--ligne2);margin-top:4px"><div id="jm" class="jg" style="background:var(--bleu)"></div><div style="flex:1;background:var(--vert)"></div></div></div>';
    h += '<div class="legende">' + ["m", "l", "i", "r"].map(function (k) { return '<span><i style="background:' + COUL[k][1] + ";border-color:" + COUL[k][0] + '"></i>' + COUL[k][2] + "</span>"; }).join("") + "</div></div>";
    sc.innerHTML = h;
  }
  function dessine(sc, e, i, E, saut) {
    var fin = aaInstant(sc.querySelector(".aa"), saut);
    ERES.forEach(function (er, k) {
      var g = sc.querySelector("#fe-" + k), p = sc.querySelector("#fp-" + k);
      g.style.opacity = k > e.k ? 0.22 : 1;
      g.classList.toggle("neuf", k === e.k && !saut);
      g.style.background = k === e.k ? "var(--bg3)" : "";
      p.style.background = k <= e.k ? "var(--vert)" : "var(--bg2)";
      p.style.borderColor = k <= e.k ? "var(--vert)" : "var(--encre3)";
    });
    sc.querySelector("#jm").style.width = ERES[e.k].m + "%";
    fin();
  }
  O.lecteur(z, { titre: "la frise qui se déroule", sous: "matériel et logiciel", etapes: etapes, prepare: prepare, dessine: dessine, vitesse: 2600 });
};
