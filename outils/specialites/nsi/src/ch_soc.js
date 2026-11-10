/* ===================== Architectures matérielles — Système sur puce (SoC) ===================== */
/* Feuille de style commune aux animations des chapitres « architectures, systèmes d'exploitation et réseaux »
   (soc, proc, rout, crypto) : injectée une seule fois, au premier affichage d'une de ces animations. */
var ARCH_CSS = [
  ".ar .scene svg{font-family:var(--mono)}",
  ".ar .scene svg text{font-size:12px;fill:var(--encre)}",
  ".ar .scene svg .pt{font-size:10.5px;fill:var(--encre2)}",
  ".ar .scene svg .gd{font-size:13px;font-weight:700}",
  ".ar-large .scene svg{min-width:540px}",
  ".ar:not(.ar-large) .scene svg{max-width:540px}",
  ".ar-tab th:first-child{width:1%}",
  ".ar .bl rect{fill:var(--bg2);stroke:var(--ligne2);stroke-width:1.4}",
  ".ar .bl.on rect{fill:var(--ambre-f);stroke:var(--ambre);stroke-width:2.6}",
  ".ar .bl.ok rect{fill:var(--vert-f);stroke:var(--vert);stroke-width:2}",
  ".ar .bl.off{opacity:.35}",
  ".ar .bl.ko rect{fill:var(--rouge-f);stroke:var(--rouge);stroke-width:2.4}",
  ".ar .puce{fill:none;stroke:var(--encre3);stroke-width:2;stroke-dasharray:7 4}",
  ".ar .noc{fill:var(--bleu-f);stroke:var(--bleu);stroke-width:1.4}",
  ".ar .noc.on{stroke-width:2.6}",
  ".ar .fil{stroke:var(--ligne2);stroke-width:2;fill:none}",
  ".ar .fil.on{stroke:var(--ambre);stroke-width:3.2}",
  ".ar .fil.ok{stroke:var(--vert);stroke-width:3.4}",
  ".ar .fil.ko{stroke:var(--rouge);stroke-width:2.4;stroke-dasharray:6 5}",
  ".ar .fil.att{stroke:var(--rouge);stroke-width:2.2;stroke-dasharray:6 5}",
  ".ar .fil.tient{stroke:var(--vert);stroke-width:2.6}",
  ".ar .jeton{fill:var(--ambre);stroke:var(--bg2);stroke-width:2}",
  ".ar .jeton.b{fill:var(--bleu)}.ar .jeton.v{fill:var(--vert)}",
  ".ar .tete-f{fill:var(--encre3)}.ar .tete-f.on{fill:var(--ambre)}.ar .tete-f.ok{fill:var(--vert)}.ar .tete-f.ko{fill:var(--rouge)}",
  ".ar .nd circle{fill:var(--bg2);stroke:var(--encre3);stroke-width:1.6}",
  ".ar .nd.on circle{fill:var(--ambre-f);stroke:var(--ambre);stroke-width:2.8}",
  ".ar .nd.ok circle{fill:var(--vert-f);stroke:var(--vert);stroke-width:2.4}",
  ".ar .nd text{font-weight:700;font-size:14px}",
  ".ar .cout{font-size:11px;fill:var(--encre2)}",
  ".ar .cout-f{fill:var(--bg);stroke:none}",
  ".ar .scene .halo{paint-order:stroke;stroke:var(--bleu-f);stroke-width:5px;stroke-linejoin:round}",
  ".ar-tab{overflow-x:auto;margin-top:10px;-webkit-overflow-scrolling:touch}",
  ".ar-tab table{border-collapse:collapse;font-family:var(--mono);font-size:.78rem;margin:0 auto;min-width:100%}",
  ".ar-tab th,.ar-tab td{border:1px solid var(--ligne);padding:4px 6px;text-align:center;white-space:nowrap}",
  ".ar-tab th{background:var(--bg3);color:var(--encre2);font-weight:700}",
  ".ar-tab td.chg{background:var(--ambre-f);color:var(--encre);font-weight:700}",
  ".ar-tab td.fixe{background:var(--vert-f)}",
  ".ar-tab caption{caption-side:top;text-align:left;font-size:.78rem;color:var(--encre2);padding:2px 0 6px}",
  "html.mo .ar .neuf{animation:ar-app .5s cubic-bezier(.2,.8,.2,1) both;transform-box:fill-box;transform-origin:center}",
  "html.mo .ar .trace{stroke-dasharray:var(--l,400);stroke-dashoffset:var(--l,400);animation:ar-trace .7s ease-out forwards}",
  "html.mo .ar td.chg{animation:ar-cell .9s ease-out}",
  "@keyframes ar-app{from{opacity:.15;transform:scale(.85)}}",
  "@keyframes ar-trace{to{stroke-dashoffset:0}}",
  "@keyframes ar-cell{from{background:var(--ambre);color:var(--bg)}}"
].join("\n");
function archStyle() {
  if (document.getElementById("ar-style")) return;
  var s = document.createElement("style"); s.id = "ar-style"; s.textContent = ARCH_CSS; document.head.appendChild(s);
}
/* jeton qui parcourt un chemin SVG (seulement quand l'étape s'anime) */
function archJeton(d, cl, dur, delai) {
  return '<circle class="jeton ' + (cl || "") + '" r="6.5" cx="0" cy="0"><animateMotion dur="' + (dur || 0.9) + 's" begin="' + (delai || 0) + 's" fill="freeze" path="' + d + '"/></circle>';
}

C("soc-cycle", String.raw`
c = 299_792_458          # vitesse de la lumière dans le vide (m/s)
f = 3e9                  # fréquence d'horloge : 3 GHz
periode = 1 / f          # durée d'un cycle (s)
print(round(periode * 1e9, 3), "ns par cycle")
print(round(c * periode * 100, 1), "cm au plus parcourus par un signal pendant un cycle")`, { out: "0.333 ns par cycle\n10.0 cm au plus parcourus par un signal pendant un cycle" });

C("soc-puissance", String.raw`
def puissance_dynamique(c, v, f):
    """Puissance (W) dissipée en commutant : P = C * V**2 * f
    c : capacité commutée (F), v : tension (V), f : fréquence (Hz)."""
    return c * v ** 2 * f

normal = puissance_dynamique(1e-9, 1.0, 3e9)     # valeurs d'ordre de grandeur
econome = puissance_dynamique(1e-9, 0.8, 2e9)    # tension ET fréquence baissées
print(round(normal, 2), "W ->", round(econome, 2), "W")
print("économie :", round(100 * (1 - econome / normal)), "%")`, { out: "3.0 W -> 1.28 W\néconomie : 57 %" });

C("soc-x1", String.raw`
f = 2_000_000_000            # 2 GHz
instructions = 6_000_000_000
ipc = 3                      # instructions exécutées par cycle, en moyenne
print(instructions / (ipc * f), "s")`, { out: "1.0 s" });

C("soc-x2", String.raw`
coeurs = {"performant": (3.0, 2.0), "econome": (1.0, 0.25)}   # (GHz, W), valeurs fictives
travail = 6.0                                                 # milliards de cycles
for nom, (ghz, watts) in coeurs.items():
    duree = travail / ghz
    print(nom, duree, "s", duree * watts, "J")`, { out: "performant 2.0 s 4.0 J\neconome 6.0 s 1.5 J" });

C("soc-x3", String.raw`
transistors, annee = 2300, 1971        # Intel 4004
while transistors < 19_000_000_000:    # ordre de grandeur d'un SoC de 2023
    transistors = transistors * 2
    annee = annee + 2
print(annee, transistors)`, { out: "2017 19293798400" });

C("soc-x4", String.raw`
debit_puce = 100e9      # octets par seconde entre deux blocs de la puce (ordre de grandeur)
debit_carte = 10e9      # octets par seconde entre deux puces d'une carte (ordre de grandeur)
image = 12e6 * 3        # photo de 12 mégapixels, 3 octets par pixel
print(round(image / debit_puce * 1000, 2), "ms", round(image / debit_carte * 1000, 2), "ms")`, { out: "0.36 ms 3.6 ms" });

C("soc-ep-fourni", String.raw`
# Puissance consommée par chaque bloc d'un SoC quand il est actif (mW, valeurs fictives)
BLOCS = {"cpu_perf": 2000, "cpu_eco": 300, "gpu": 1500, "npu": 800,
         "isp": 600, "modem": 900, "affichage": 400}

def puissance(actifs):
    """Renvoie la puissance totale (en mW) des blocs de la liste actifs."""
    ...

def autonomie(energie_wh, actifs):
    """Renvoie l'autonomie en heures d'une batterie de energie_wh wattheures
    quand seuls les blocs actifs fonctionnent."""
    return energie_wh / puissance(actifs)

jeu = ["cpu_perf", "gpu", "affichage", "modem"]
musique = ["cpu_eco", "modem"]`, { fichier: "energie.py", run: false, trous: [7] });

C("soc-ep-bug", String.raw`
def puissance(actifs):
    total = 0
    for b in actifs:
        total = total + BLOCS[b]
    return total

def autonomie(energie_wh, actifs):
    return energie_wh / puissance(actifs)

print(puissance(jeu), autonomie(15, jeu))`, { deps: ["soc-ep-fourni"], fichier: "essai.py", out: "4800 0.003125" });

C("soc-ep-corr", String.raw`
BLOCS = {"cpu_perf": 2000, "cpu_eco": 300, "gpu": 1500, "npu": 800,
         "isp": 600, "modem": 900, "affichage": 400}

def puissance(actifs):
    """Renvoie la puissance totale (en mW) des blocs de la liste actifs."""
    total = 0
    for b in actifs:
        assert b in BLOCS, "bloc inconnu : " + b
        total = total + BLOCS[b]
    return total

def autonomie(energie_wh, actifs):
    """Autonomie en heures : énergie (Wh) divisée par la puissance (W)."""
    assert len(actifs) > 0, "aucun bloc actif"
    return energie_wh / (puissance(actifs) / 1000)       # mW -> W

def bloc_le_plus_gourmand(actifs):
    """Renvoie le nom du bloc actif qui consomme le plus."""
    meilleur = actifs[0]
    for b in actifs:
        if BLOCS[b] > BLOCS[meilleur]:
            meilleur = b
    return meilleur

jeu = ["cpu_perf", "gpu", "affichage", "modem"]
musique = ["cpu_eco", "modem"]
assert puissance(jeu) == 4800 and puissance([]) == 0
assert autonomie(15, jeu) == 3.125
assert round(autonomie(15, musique), 1) == 12.5
assert bloc_le_plus_gourmand(jeu) == "cpu_perf"
print(puissance(jeu), "mW ;", autonomie(15, jeu), "h de jeu ;", round(autonomie(15, musique), 1), "h de musique")`, { fichier: "energie.py", out: "4800 mW ; 3.125 h de jeu ; 12.5 h de musique" });

C("soc-ecrit-calc", String.raw`
f = 1.5e9                 # fréquence du processeur (Hz)
cycles_acces_ram = 150    # cycles perdus à chaque accès à la RAM externe
cycles_acces_cache = 4    # cycles perdus à chaque accès au cache intégré
acces = 10_000_000
print(acces * cycles_acces_ram / f * 1000, "ms")
print(round(acces * cycles_acces_cache / f * 1000, 2), "ms")`, { out: "1000.0 ms\n26.67 ms" });

WIDGETS_EXT["arch-soc"] = function (z, opt, O) {
  archStyle();
  /* blocs : [x, y, largeur, hauteur, libellé (lignes séparées par |)] */
  var B = {
    cpu: [122, 76, 120, 46, "CPU|2 perf. + 4 éco."], gpu: [250, 76, 72, 46, "GPU"], npu: [330, 76, 70, 46, "NPU|(IA)"], sram: [408, 76, 72, 46, "cache|SRAM"],
    isp: [122, 170, 70, 46, "ISP|(image)"], aff: [200, 170, 92, 46, "contrôleur|vidéo"], radio: [300, 170, 86, 46, "modem|radio"], mem: [394, 170, 86, 46, "contrôleur|mémoire"],
    ener: [122, 228, 150, 34, "gestion d’énergie"], es: [280, 228, 200, 34, "interfaces : USB, stockage"],
    capt: [6, 172, 96, 42, "capteur|photo"], ram: [504, 168, 90, 46, "RAM|LPDDR"], flash: [504, 226, 90, 38, "mémoire|flash"],
    ecran: [226, 300, 100, 30, "écran"], ant: [306, 8, 100, 30, "antenne"], batt: [6, 226, 96, 38, "batterie"]
  };
  var YN = 140; /* axe du réseau sur puce */
  var STUB = { capt: "M102 193 L122 193", ram: "M480 193 L504 193", flash: "M480 245 L504 245", ecran: "M276 274 L276 300", ant: "M356 38 L356 52", batt: "M102 245 L122 245" };
  function cx(k) { return B[k][0] + B[k][2] / 2; }
  function bord(k) { var b = B[k]; return b[1] > YN ? b[1] : b[1] + b[3]; }
  function chemin(a, b) { return "M" + cx(a) + " " + bord(a) + " L" + cx(a) + " " + YN + " L" + cx(b) + " " + YN + " L" + cx(b) + " " + bord(b); }
  var SC = {
    photo: [
      { on: [], ext: [], msg: "Le <b>SoC</b> (cadre en pointillés) réunit sur une seule puce de silicium ce qui occupait autrefois toute une carte : processeur (CPU), processeur graphique (GPU), accélérateur d’IA (NPU), processeur d’image (ISP), modem, contrôleurs… Ils communiquent par un <b>réseau sur puce</b> (bande bleue). Autour : ce qui reste en dehors de la puce. Suivons une photo." },
      { on: ["isp"], ext: ["capt"], va: [["capt", "isp"]], msg: "Le <b>capteur</b> envoie des mesures brutes de lumière au <b>processeur d’image (ISP)</b> : un circuit spécialisé qui reconstitue les couleurs et réduit le bruit, bien plus vite et en consommant bien moins qu’un programme sur le CPU." },
      { on: ["isp", "mem"], ext: ["ram"], va: [["isp", "mem"]], msg: "L’image traverse le <b>réseau sur puce</b> jusqu’au <b>contrôleur mémoire</b>, qui l’écrit dans la <b>RAM</b>. Sur un téléphone, la RAM est souvent soudée juste au-dessus du SoC (boîtier empilé) : le trajet hors de la puce reste de quelques millimètres." },
      { on: ["npu", "mem"], va: [["mem", "npu"]], msg: "L’<b>accélérateur d’IA (NPU)</b> relit l’image et repère la scène (un visage, un paysage) pour régler la mise au point et les couleurs. Le CPU n’a rien eu à calculer : chaque tâche va au bloc le plus efficace pour elle." },
      { on: ["gpu", "aff"], ext: ["ecran"], va: [["mem", "gpu"], ["gpu", "aff"]], msg: "Le <b>GPU</b> compose l’aperçu (l’image et les boutons de l’appareil photo) ; le <b>contrôleur vidéo</b> l’envoie à l’<b>écran</b> 60 à 120 fois par seconde." },
      { on: ["cpu", "es"], ext: ["flash"], va: [["mem", "cpu"], ["cpu", "es"]], msg: "Le <b>CPU</b> (un cœur performant) fait compresser la photo puis la confie aux <b>interfaces de stockage</b>, qui l’écrivent dans la <b>mémoire flash</b> : elle est conservée même téléphone éteint." },
      { on: ["radio", "cpu"], ext: ["ant"], va: [["cpu", "radio"]], msg: "Pour l’envoyer, le CPU passe les données au <b>modem radio</b> (4G / 5G, Wi-Fi, Bluetooth), relié à l’<b>antenne</b>. Sur certains téléphones, le modem est une puce voisine plutôt qu’un bloc du SoC." },
      { on: ["cpu", "gpu", "npu", "sram", "isp", "aff", "radio", "mem", "ener", "es"], ext: [], msg: "Bilan : presque tout le trajet a eu lieu <b>dans</b> la puce, sur des distances de quelques millimètres. Moins de distance, c’est un signal plus <b>rapide</b> et moins d’<b>énergie</b> pour charger les fils : c’est tout l’intérêt de l’intégration." }
    ],
    energie: [
      { on: ["cpu", "gpu", "aff", "radio", "mem", "ener"], ext: ["ecran", "batt", "ram", "ant"], msg: "<b>Jeu en ligne</b> : cœurs performants, GPU, contrôleur vidéo et modem tournent à pleine fréquence. Le bloc de <b>gestion d’énergie</b> (avec un circuit voisin relié à la batterie) fournit à chaque bloc sa tension et son horloge." },
      { on: ["cpu", "radio", "mem", "ener"], off: ["gpu", "npu", "isp", "aff"], ext: ["batt", "ant", "ram"], msg: "<b>Musique écran éteint</b> : le GPU, l’ISP, le NPU et le contrôleur vidéo sont <b>coupés</b> (plus aucune alimentation). Seuls les <b>cœurs économes</b> du CPU décodent le son : ils sont plus lents mais consomment beaucoup moins pour une tâche légère." },
      { on: ["ener", "cpu"], off: ["gpu", "npu", "isp", "aff"], ext: ["batt"], msg: "La gestion d’énergie abaisse aussi la <b>tension</b> et la <b>fréquence</b> des cœurs encore actifs. La puissance consommée en commutant suit à peu près P ≈ C·V²·f : baisser la tension de 20 % et la fréquence d’un tiers divise cette puissance par plus de deux." },
      { on: ["ener", "radio"], off: ["cpu", "gpu", "npu", "isp", "aff", "sram", "es"], ext: ["batt", "ant"], msg: "<b>Veille</b> : presque toute la puce est éteinte. Le modem se réveille régulièrement pour écouter le réseau (appels, notifications). Ce découpage fin de l’alimentation n’est possible que parce que tous les blocs sont sur la même puce, pilotés par le même gestionnaire." }
    ]
  };
  function dessine(scene, e, i, etapes, saut) {
    var s = '<svg viewBox="0 0 600 336" role="img" aria-label="Schéma d’un système sur puce de téléphone et de ses composants voisins">';
    s += '<rect class="puce" x="110" y="52" width="382" height="222" rx="14"/><text class="gd" x="118" y="68">SoC (une seule puce)</text>';
    Object.keys(STUB).forEach(function (k) { var on = e.ext && e.ext.indexOf(k) >= 0; s += '<path class="fil' + (on ? " on" : "") + '" d="' + STUB[k] + '"/>'; });
    var nocOn = e.va && e.va.length;
    s += '<rect class="noc' + (nocOn ? " on" : "") + '" x="122" y="' + (YN - 9) + '" width="358" height="18" rx="9"/>';
    (e.va || []).forEach(function (v) { if (B[v[0]][0] > 110 && B[v[0]][0] < 490 && B[v[1]][0] > 110 && B[v[1]][0] < 490) s += '<path class="fil on' + (saut ? "" : " trace") + '" style="--l:500" d="' + chemin(v[0], v[1]) + '"/>'; });
    s += '<text class="pt halo" x="474" y="' + (YN + 4) + '" text-anchor="end">réseau sur puce</text>';
    Object.keys(B).forEach(function (k) {
      var b = B[k], dedans = b[0] > 110 && b[0] < 490 && b[1] > 52 && b[1] < 274;
      var cl = (e.on.indexOf(k) >= 0 || (e.ext || []).indexOf(k) >= 0) ? " on" : (e.off && e.off.indexOf(k) >= 0 ? " off" : "");
      var l = b[4].split("|");
      s += '<g class="bl' + cl + (cl === " on" && !saut ? " neuf" : "") + '"><rect x="' + b[0] + '" y="' + b[1] + '" width="' + b[2] + '" height="' + b[3] + '" rx="' + (dedans ? 7 : 4) + '"' + (dedans ? "" : ' stroke-dasharray="3 3"') + "/>";
      l.forEach(function (t, j) { s += '<text x="' + (b[0] + b[2] / 2) + '" y="' + (b[1] + b[3] / 2 + 4 + (j - (l.length - 1) / 2) * 14) + '" text-anchor="middle"' + (j ? ' class="pt"' : "") + ">" + t + "</text>"; });
      s += "</g>";
    });
    if (!saut) (e.va || []).forEach(function (v, j) {
      var a = v[0], b = v[1], d;
      if (STUB[a] && !(B[a][0] > 110 && B[a][0] < 490)) d = STUB[a].split(" M")[0];
      else d = chemin(a, b);
      s += archJeton(d, "", 0.9, j * 0.9);
    });
    scene.innerHTML = s + "</svg>";
    if (saut && i === 0) scene.scrollLeft = (scene.scrollWidth - scene.clientWidth) / 2;
  }
  O.lecteur(z, { titre: "dans la puce d’un téléphone", sous: "animation", choix: [{ k: "photo", t: "une photo, du capteur au réseau" }, { k: "energie", t: "la gestion d’énergie" }],
    etapes: function (k) { return SC[k]; }, prepare: function (scene) { scene.parentNode.parentNode.classList.add("ar", "ar-large"); }, dessine: dessine, vitesse: 2600 });
};

CH.push({
  id: "soc", n: 15, court: "soc", fichier: "soc.py",
  titre: "Systèmes sur puce (SoC)",
  rubrique: "Rubrique « Architectures matérielles, systèmes d’exploitation et réseaux » : composants intégrés d’un système sur puce",
  accroche: "Du modèle de von Neumann au SoC d’un téléphone : ce qu’il contient, pourquoi tout regrouper sur une puce accélère et économise l’énergie, et ce qu’on y perd.",
  essentiel: [
    "Un <b>système sur puce</b> (SoC, <i>System on Chip</i>) rassemble sur un seul circuit intégré ce qui occupait autrefois une carte entière : processeur, processeur graphique, mémoires locales, contrôleurs, interfaces.",
    "Composants à reconnaître : <b>CPU</b> multicœur, <b>GPU</b> (accélérateur graphique), <b>mémoires locales</b> (caches), <b>contrôleur mémoire</b>, <b>contrôleur vidéo</b>, <b>interfaces radio</b> (modem, Wi-Fi, Bluetooth) et <b>filaires</b> (USB…), <b>gestion d’énergie</b>, <b>réseau sur puce</b> qui relie les blocs.",
    "Avantage <b>vitesse</b> : les blocs sont à quelques millimètres les uns des autres ; les échanges sont plus courts et plus larges qu’entre puces séparées.",
    "Avantage <b>consommation</b> : des fils courts consomment moins, chaque bloc peut être ralenti ou coupé à la demande, et chaque tâche va au circuit spécialisé le plus économe.",
    "Contreparties : rien ne se change ni ne s’ajoute (RAM, processeur), conception très coûteuse, chaleur concentrée sur une petite surface."
  ],
  attendus: [
    "Identifier les principaux composants sur un schéma de circuit et les avantages de leur intégration en termes de vitesse et de consommation (capacité du programme, mot pour mot).",
    "Le programme prend le circuit d’un téléphone comme exemple : microprocesseurs, mémoires locales, interfaces radio et filaires, gestion d’énergie, contrôleurs vidéo, accélérateur graphique, réseaux sur puce.",
    "Faire le lien avec le modèle d’architecture de von Neumann vu en Première."
  ],
  intro: `<div class="boite ex"><div class="lab"># ce chapitre à l’écrit</div><p>Les questions portent sur un <b>schéma</b> (de téléphone, de nano-ordinateur, de console) : nommer les blocs, dire à quoi ils servent, expliquer pourquoi leur intégration rend le système plus rapide et plus économe. On attend des arguments précis (distance, énergie, coupure des blocs), pas un slogan.</p></div>`,
  idees: [
    { id: "i1", t: "Point de départ : le modèle de von Neumann", h: `
<p>En Première, tu as vu le modèle de <b>von Neumann</b> (1945) : une <b>unité arithmétique et logique</b> qui calcule, une <b>unité de contrôle</b> qui enchaîne les instructions, une <b>mémoire</b> qui contient à la fois le programme et les données, des <b>entrées-sorties</b>, le tout relié par des <b>bus</b>.</p>
<p>Dans un ordinateur de bureau, ces fonctions sont réparties sur des composants <b>séparés</b>, assemblés sur une carte mère : le processeur dans son support, des barrettes de RAM qu’on peut changer, une carte graphique enfichée dans un connecteur PCI Express, un disque, une carte réseau. Chaque composant est une puce (ou plusieurs), et ils communiquent par des pistes de cuivre de plusieurs centimètres.</p>
<div class="boite def"><div class="lab">"""définition"""</div><p>Un <b>circuit intégré</b> (une « puce ») est un morceau de silicium sur lequel sont gravés des millions ou des milliards de <b>transistors</b>, les interrupteurs électroniques qui réalisent les portes logiques de Première.</p></div>
<div class="boite histoire"><div class="lab"># git log --histoire</div><p><span class="commit">1971 <b>·</b></span> Intel commercialise le <b>4004</b>, premier microprocesseur sur une seule puce : environ 2 300 transistors. <span class="commit">1965 <b>·</b></span> Gordon Moore avait observé que le nombre de transistors d’une puce doublait à intervalle régulier (il retiendra en 1975 un doublement tous les deux ans) : c’est la « loi de Moore », une observation et non une loi physique. Cette miniaturisation est ce qui a rendu possible le SoC.</p></div>` },

    { id: "i2", t: "Qu’est-ce qu’un système sur puce ?", h: `
<div class="boite def"><div class="lab">"""définition"""</div><p>Un <b>système sur puce</b> (SoC, <i>System on Chip</i>) est un circuit intégré unique qui regroupe <b>tous les composants d’un ordinateur</b> ou presque : un ou plusieurs processeurs, un processeur graphique, des mémoires, des contrôleurs et des interfaces. Le programme le dit ainsi : il regroupe « dans un seul circuit nombre de fonctions autrefois effectuées par des circuits séparés assemblés sur une carte électronique ».</p></div>
<p><b>Exemples</b> (fiches techniques des fabricants) :</p>
<ul><li>l’<b>Apple A17 Pro</b> (2023, iPhone 15 Pro) : gravure en 3 nm, environ 19 milliards de transistors, un CPU de 6 cœurs (2 performants, 4 économes), un GPU de 6 cœurs, un accélérateur d’IA de 16 cœurs ;</li>
<li>le <b>Broadcom BCM2711</b> du Raspberry Pi 4 (2019) : 4 cœurs ARM Cortex-A72 à 1,5 GHz, un GPU, des contrôleurs vidéo, USB, Ethernet ; tout le nano-ordinateur tient autour de cette puce ;</li>
<li>l’<b>Apple M1</b> (2020), SoC d’ordinateurs portables : environ 16 milliards de transistors, avec une mémoire « unifiée » partagée par le CPU et le GPU.</li></ul>
<p>Le programme ajoute une remarque : un SoC est <b>conçu de façon logicielle</b> (on décrit ses circuits dans des langages de description de matériel, on les simule avant de les graver) et ses blocs sont accessibles aux programmes par des <b>API</b>, comme une bibliothèque.</p>
<div class="boite hp"><div class="lab"># microcontrôleur ou SoC ?</div><p>Un <b>microcontrôleur</b> est un petit système sur puce pour les objets simples : la carte micro:bit (version 2) utilise un nRF52833, avec un cœur ARM Cortex-M4 à 64 MHz, 512 Ko de mémoire flash et 128 Ko de RAM, et une radio Bluetooth, tout sur la même puce. Même idée qu’un SoC de téléphone, à une échelle mille fois plus petite.</p></div>` },

    { id: "i3", t: "Les composants d’un SoC de téléphone", h: `
<p>Voici les blocs que cite le programme, avec leur rôle. C’est la liste à savoir reconnaître sur un schéma.</p>
<div class="tab-wrap"><table><tr><th>composant</th><th>rôle</th><th>exemple</th></tr>
<tr><td><b>microprocesseur</b> (CPU), souvent multicœur</td><td>exécute les programmes (système, applications)</td><td>cœurs performants pour les tâches lourdes, cœurs économes pour les tâches légères</td></tr>
<tr><td><b>mémoires locales</b> (caches, SRAM)</td><td>gardent près des cœurs les données et instructions utilisées</td><td>un accès au cache coûte quelques cycles, un accès à la RAM externe plus d’une centaine</td></tr>
<tr><td><b>contrôleur mémoire</b></td><td>fait le lien avec la RAM, à l’extérieur de la puce</td><td>RAM LPDDR souvent soudée sur le SoC</td></tr>
<tr><td><b>accélérateur graphique</b> (GPU)</td><td>calcule les images (jeux, interface), en parallèle sur des centaines d’unités simples</td><td>affichage fluide d’un jeu en 3D</td></tr>
<tr><td><b>contrôleurs vidéo</b></td><td>envoient l’image à l’écran ; décodent ou encodent les vidéos</td><td>lire une vidéo sans faire travailler le CPU</td></tr>
<tr><td><b>interfaces radio</b></td><td>modem 4G / 5G, Wi-Fi, Bluetooth, GPS</td><td>passer un appel, recevoir une notification</td></tr>
<tr><td><b>interfaces filaires</b></td><td>USB, lien vers la mémoire flash, l’appareil photo, l’écran</td><td>brancher le téléphone à un ordinateur</td></tr>
<tr><td><b>gestion d’énergie</b></td><td>règle tension et fréquence de chaque bloc, coupe les blocs inutiles</td><td>écran éteint : GPU coupé</td></tr>
<tr><td><b>réseau sur puce</b> (NoC)</td><td>relie tous les blocs entre eux, comme un petit réseau interne</td><td>l’image va de l’ISP à la RAM puis au GPU</td></tr></table></div>
<p>S’y ajoutent souvent des circuits spécialisés : processeur d’image (<b>ISP</b>) pour l’appareil photo, accélérateur d’intelligence artificielle (<b>NPU</b>), processeur de signal (<b>DSP</b>) pour le son, bloc de sécurité qui garde les clés de chiffrement.</p>
<p>Ce qui reste <b>hors</b> de la puce : la batterie, l’écran, les capteurs, l’antenne, la mémoire flash de stockage, souvent la RAM (soudée juste au-dessus du SoC, dans le même empilement), et une puce de gestion d’alimentation qui fournit les tensions à partir de la batterie.</p>
[[w-arch-soc]]` },

    { id: "i4", t: "Avantage 1 : la vitesse", h: `
<p>Pourquoi est-ce plus rapide quand tout est sur la même puce ? Trois raisons.</p>
<ol><li><b>Les distances sont courtes.</b> Un signal électrique ne va pas plus vite que la lumière. À 3 GHz, un cycle d’horloge dure un tiers de nanoseconde : pendant ce temps, même la lumière ne parcourt que 10 cm.
[[soc-cycle]]
Entre deux puces d’une carte mère, il faut plusieurs cycles pour faire l’aller-retour ; entre deux blocs d’un SoC séparés de quelques millimètres, beaucoup moins.</li>
<li><b>Les liaisons sont plus nombreuses et plus larges.</b> Sur une carte, chaque fil entre deux puces passe par une broche, et le nombre de broches est limité. Dans la puce, on peut tirer des milliers de connexions entre deux blocs : plus de données passent à chaque cycle.</li>
<li><b>Des circuits spécialisés</b> font mieux qu’un programme : décoder une vidéo, corriger une photo ou chiffrer des données avec un bloc dédié est beaucoup plus rapide qu’avec des instructions générales sur le CPU.</li></ol>
<p>Le CPU passe une grande partie de son temps à <b>attendre la mémoire</b>. Les mémoires locales (caches) intégrées à côté des cœurs réduisent ces attentes : l’exercice écrit de ce chapitre le chiffre.</p>` },

    { id: "i5", t: "Avantage 2 : la consommation", h: `
<p>Sur un téléphone, l’énergie est la contrainte principale (batterie, chaleur). L’intégration aide de plusieurs façons.</p>
<ul><li><b>Des fils courts consomment moins</b> : à chaque changement de 0 à 1, il faut charger électriquement le fil ; un fil de quelques millimètres dans la puce demande bien moins d’énergie qu’une piste de carte mère et les circuits d’entrée-sortie qui la pilotent.</li>
<li><b>Couper ce qui ne sert pas</b> : le bloc de gestion d’énergie coupe l’alimentation du GPU quand l’écran est éteint, ou ralentit l’horloge d’un cœur peu occupé. Musique écran éteint : seuls quelques blocs restent alimentés.</li>
<li><b>Le bon cœur pour la bonne tâche</b> : l’architecture « big.LITTLE » (annoncée par ARM en 2011) associe des cœurs performants et des cœurs économes. Un cœur économe met plus de temps, mais dépense moins d’énergie pour une tâche légère : voir l’exercice « prédis » n° 2.</li>
<li><b>Baisser tension et fréquence</b> (DVFS) : la puissance dépensée à commuter les transistors suit approximativement P ≈ C·V²·f (C : capacité commutée, V : tension, f : fréquence). La tension compte au carré.</li></ul>
[[soc-puissance]]
<div class="boite hp"><div class="lab"># pour aller plus loin</div><p>La formule P ≈ C·V²·f n’est pas au programme ; elle explique pourquoi on ne monte plus guère la fréquence des processeurs depuis le milieu des années 2000 (chaleur trop forte) et pourquoi on multiplie plutôt les cœurs et les blocs spécialisés.</p></div>` },

    { id: "i6", t: "Les contreparties de l’intégration", h: `
<p>Tout regrouper a un prix, qu’on te demande parfois à l’écrit :</p>
<ul><li><b>Aucune évolution possible</b> : on ne change pas la RAM ni le processeur d’un téléphone ; une panne d’un bloc rend souvent toute la carte irréparable.</li>
<li><b>Coût de conception très élevé</b> : concevoir et graver une puce de plusieurs milliards de transistors coûte des centaines de millions d’euros ; ce n’est rentable que vendu en très grande série.</li>
<li><b>Chaleur concentrée</b> : toute la puissance est dissipée sur quelques centimètres carrés ; quand la puce chauffe trop, elle baisse sa fréquence (le téléphone ralentit pendant un jeu).</li>
<li><b>Moins de souplesse</b> : un PC de bureau peut recevoir une carte graphique plus puissante ; un SoC est figé à sa fabrication.</li></ul>
<div class="boite ex"><div class="lab"># exemple : où trouve-t-on des SoC ?</div><p>Téléphones et tablettes, montres connectées, consoles portables, nano-ordinateurs (Raspberry Pi), boîtiers TV, voitures, et désormais certains ordinateurs portables (Apple M1 et suivants). Les ordinateurs de bureau et les serveurs gardent souvent des composants séparés, pour la puissance et l’évolutivité.</p></div>` },

    { id: "i7", t: "Lire un schéma de circuit : méthode", h: `
<p>À l’écrit, on te donne un schéma (blocs reliés par des traits) ou une photo annotée de carte. Pour répondre :</p>
<ol><li><b>Repère la limite de la puce</b> : ce qui est dedans est intégré, ce qui est dehors est relié par des broches.</li>
<li><b>Nomme chaque bloc par sa fonction</b> : « calculer » (CPU), « dessiner » (GPU), « stocker temporairement » (cache, RAM), « stocker durablement » (flash), « communiquer sans fil » (modem, Wi-Fi), « communiquer par câble » (USB, Ethernet), « alimenter » (gestion d’énergie), « relier les blocs » (bus, réseau sur puce).</li>
<li><b>Justifie un avantage par un mécanisme</b> : « les blocs sont proches, donc les échanges sont plus rapides » ; « on peut couper l’alimentation des blocs inutilisés, donc on consomme moins ».</li></ol>
<p>Exemple sur le Raspberry Pi 4 : la puce centrale est le SoC (CPU 4 cœurs, GPU, contrôleurs) ; la RAM est une puce à côté ; les ports USB, Ethernet et HDMI sont reliés au SoC (directement ou par une puce contrôleur) ; la carte microSD sert de mémoire de stockage.</p>` }
  ],
  pieges: [
    { t: "Confondre RAM et mémoire de stockage", h: `<p>La <b>RAM</b> est volatile (effacée à l’extinction) et rapide : elle contient les programmes en cours. La <b>mémoire flash</b> (« 128 Go » d’un téléphone) conserve les fichiers. Les <b>caches</b> sont de petites mémoires très rapides <b>dans</b> la puce.</p>` },
    { t: "Dire « c’est plus rapide parce que c’est plus petit » sans mécanisme", h: `<p>Il faut l’argument : distances plus courtes, donc temps de transfert plus courts ; liaisons plus nombreuses, donc plus de données par cycle ; circuits spécialisés plus efficaces que le CPU.</p>` },
    { t: "Croire qu’un SoC n’a qu’un seul processeur", h: `<p>Un SoC contient plusieurs <b>cœurs</b> de CPU, souvent de deux types (performants et économes), plus un GPU et d’autres processeurs spécialisés (NPU, ISP, DSP).</p>` },
    { t: "Oublier les inconvénients", h: `<p>Une question « avantages et inconvénients » attend aussi : pas d’évolution ni de réparation, coût de conception, chaleur concentrée.</p>` }
  ],
  retenir: `
<h2>Définition</h2>
<p><b>SoC</b> (système sur puce) : un seul circuit intégré qui regroupe CPU, GPU, mémoires locales, contrôleurs et interfaces, autrefois répartis sur une carte.</p>
<h2>Les composants (liste du programme)</h2>
<div class="tab-wrap"><table><tr><th>composant</th><th>rôle</th></tr>
<tr><td>microprocesseur (CPU) multicœur</td><td>exécute les programmes</td></tr><tr><td>mémoires locales (caches)</td><td>données proches des cœurs</td></tr><tr><td>accélérateur graphique (GPU)</td><td>calcul des images</td></tr><tr><td>contrôleurs vidéo</td><td>affichage, décodage vidéo</td></tr><tr><td>interfaces radio</td><td>modem 4G / 5G, Wi-Fi, Bluetooth</td></tr><tr><td>interfaces filaires</td><td>USB, stockage, écran, caméra</td></tr><tr><td>gestion d’énergie</td><td>tension, fréquence, coupure des blocs</td></tr><tr><td>réseau sur puce</td><td>relie les blocs</td></tr></table></div>
<h2>Avantages de l’intégration</h2>
<ul><li><b>Vitesse</b> : distances de quelques mm, liaisons larges, circuits spécialisés.</li><li><b>Consommation</b> : fils courts, blocs coupés ou ralentis à la demande, cœurs économes (big.LITTLE).</li><li>Encombrement et coût en grande série.</li></ul>
<h2>Inconvénients</h2>
<ul><li>Pas d’évolution ni de réparation, conception très coûteuse, chaleur concentrée.</li></ul>
<h2>Repères</h2>
<p>Von Neumann (1945) · Intel 4004 (1971, ≈ 2 300 transistors) · loi de Moore (1965, révisée en 1975) · Apple A17 Pro (2023, ≈ 19 milliards de transistors).</p>`,
  predis: [
    { code: "soc-x1", niv: "facile", rep: "6 milliards d’instructions à 3 par cycle font 2 milliards de cycles ; à 2 milliards de cycles par seconde : 1 seconde. La division <code>/</code> donne un flottant : <code>1.0</code>." },
    { code: "soc-x2", niv: "moyen", rep: "Le cœur performant finit en 6 / 3 = 2 s mais dépense 2 × 2 = 4 J ; le cœur économe met 6 s mais ne dépense que 6 × 0,25 = 1,5 J. Plus lent, mais plus économe : c’est l’idée de big.LITTLE pour les tâches qui ne sont pas pressées." },
    { code: "soc-x3", niv: "moyen", rep: "Il faut 23 doublements (2 300 × 2²³ ≈ 1,9 × 10¹⁰) : 1971 + 46 = 2017. La puce réelle de 19 milliards de transistors date de 2023 : la loi de Moore a ralenti." },
    { code: "soc-x4", niv: "facile", rep: "La photo fait 36 millions d’octets. À 100 Go/s : 0,36 ms ; à 10 Go/s : 3,6 ms. Ces débits sont des ordres de grandeur choisis pour l’exercice : l’idée est qu’un débit dix fois plus grand dans la puce divise le temps par dix." }
  ],
  ep: [
    { titre: "Bilan énergétique d’un téléphone", enonce: `<p>On modélise la consommation des blocs d’un SoC (valeurs fictives, en milliwatts) pour estimer l’autonomie d’une batterie de 15 Wh.</p>[[soc-ep-fourni]]`,
      questions: [
        { q: "Compléter <code>puissance(actifs)</code> avec une boucle.", c: `<p>On additionne <code>BLOCS[b]</code> pour chaque bloc <code>b</code> de la liste ; une liste vide donne 0.</p>` },
        { q: "Un élève exécute le code ci-dessous et trouve une autonomie de 0,003 h en jeu. Expliquer et corriger.", code: "[[soc-ep-bug]]", c: `<p>Les puissances sont en <b>milliwatts</b> et l’énergie en <b>wattheures</b> : 15 / 4800 mélange les unités. Il faut convertir : 4800 mW = 4,8 W, et 15 / 4,8 = 3,125 h. C’est un bug d’unités, comme celui de la sonde Mars Climate Orbiter (chapitre « Modularité et mise au point »).</p>` },
        { q: "Écrire <code>bloc_le_plus_gourmand(actifs)</code> et un jeu de tests ; ajouter une assertion qui refuse un bloc inconnu.", c: `[[soc-ep-corr]]` },
        { q: "À l’oral : pourquoi l’autonomie est-elle quatre fois plus grande en écoutant de la musique ?", c: `<p>Écran éteint, le GPU et le contrôleur vidéo sont coupés et le CPU utilise ses cœurs économes : 1 200 mW au lieu de 4 800 mW. Cette coupure fine est possible parce que la gestion d’énergie du SoC pilote chaque bloc séparément.</p>` }
      ] }
  ],
  ecrit: { titre: "Le SoC d’une console portable", points: "≈ 6 points · 40 min", note: "Exercice inventé pour le site, au format de l’épreuve écrite.",
    enonce: `<p>Une console portable est construite autour d’un SoC. Sa fiche technique indique : « CPU 8 cœurs (4 performants, 4 économes) ; GPU ; 6 Mo de cache ; contrôleur LPDDR5 ; décodeur vidéo ; contrôleurs USB-C, Wi-Fi et Bluetooth ; gestion d’énergie intégrée. Hors de la puce : 12 Go de RAM, 256 Go de stockage flash, écran, batterie. »</p>`,
    questions: [
      { q: "Associer à chaque fonction le composant de la fiche qui la réalise : a) afficher un jeu en 3D ; b) lire un film sans solliciter le CPU ; c) jouer en ligne sans câble ; d) garder près des cœurs les données souvent utilisées ; e) conserver les sauvegardes console éteinte.", pts: "1,5 pt", c: `<p>a) le GPU ; b) le décodeur vidéo ; c) le contrôleur Wi-Fi ; d) le cache (mémoire locale) ; e) le stockage flash, hors de la puce.</p>` },
      { q: "Citer deux composants extérieurs au SoC et dire pourquoi l’un d’eux n’est pas intégré.", pts: "1 pt", c: `<p>La RAM, le stockage flash, l’écran, la batterie. Le stockage flash demande une fabrication différente et une grande surface ; l’écran et la batterie sont des objets physiques de grande taille. (La RAM est souvent placée juste au-dessus du SoC, mais reste une puce distincte.)</p>` },
      { q: "On exécute le programme ci-dessous, qui compare le temps perdu pour 10 millions d’accès selon que la donnée est en RAM ou dans le cache. Qu’affiche-t-il ? Que montre-t-il ?", pts: "1,5 pt", code: "[[soc-ecrit-calc|nosortie]]", c: `<p><code>1000.0 ms</code> puis <code>26.67 ms</code>. 10⁷ × 150 cycles = 1,5 × 10⁹ cycles, soit une seconde à 1,5 GHz ; avec le cache, 4 × 10⁷ cycles ≈ 26,67 ms. Les mémoires locales intégrées à côté des cœurs évitent l’essentiel des attentes : c’est un avantage de vitesse de l’intégration.</p>` },
      { q: "Expliquer deux raisons pour lesquelles l’intégration réduit la consommation de la console.", pts: "1 pt", c: `<p>Les liaisons entre blocs sont très courtes, et charger un fil court demande moins d’énergie qu’une piste de carte. La gestion d’énergie intégrée coupe ou ralentit les blocs inutilisés (cœurs performants en veille, GPU coupé dans les menus) et confie les tâches légères aux cœurs économes.</p>` },
      { q: "Donner un inconvénient de ce choix pour le joueur.", pts: "1 pt", c: `<p>Impossible d’ajouter de la RAM ou de changer le processeur : la console ne peut pas évoluer, et la panne d’un bloc oblige à changer toute la carte.</p>` }
    ],
    methode: `<p>Pour chaque avantage, donne la <b>cause</b> (distance, coupure de l’alimentation, circuit spécialisé) et la <b>conséquence</b> (temps, énergie). Pour reconnaître un bloc, pars de sa <b>fonction</b>.</p>` },
  qcm: [
    { q: "Qu’est-ce qu’un SoC ?", c: ["Un logiciel qui gère le système", "Un circuit intégré unique qui regroupe processeur, mémoires locales, contrôleurs et interfaces", "Une carte mère d’ordinateur de bureau", "Un type de mémoire de stockage"], a: 1, e: "System on Chip : tout un système sur une seule puce.", ref: "i2" },
    { q: "Lequel de ces éléments est le plus souvent <b>hors</b> du SoC d’un téléphone ?", c: ["Le GPU", "Les caches", "La batterie", "Le contrôleur mémoire"], a: 2, e: "Batterie, écran, antenne, stockage flash et souvent la RAM sont à l’extérieur.", ref: "i3" },
    { q: "Quel bloc calcule les images d’un jeu en 3D ?", c: ["Le modem", "Le GPU (accélérateur graphique)", "Le contrôleur mémoire", "La gestion d’énergie"], a: 1, e: "Le GPU fait de nombreux calculs simples en parallèle.", ref: "i3" },
    { q: "À quoi sert le réseau sur puce ?", c: ["À se connecter à Internet", "À relier entre eux les blocs du SoC", "À recharger la batterie", "À stocker les fichiers"], a: 1, e: "C’est le réseau interne (bus, routeurs) qui fait circuler les données entre CPU, GPU, mémoire…", ref: "i3" },
    { q: "Pourquoi l’intégration accélère-t-elle les échanges ?", c: ["Parce que le silicium est plus rapide que le cuivre", "Parce que les blocs sont proches et reliés par des liaisons nombreuses", "Parce que le SoC n’a pas d’horloge", "Parce que la RAM devient inutile"], a: 1, e: "Distances de quelques millimètres et milliers de connexions entre blocs.", ref: "i4" },
    { q: "À 3 GHz, pendant un cycle d’horloge, un signal parcourt au plus environ…", c: ["10 m", "1 m", "10 cm", "1 mm"], a: 2, e: "Un tiers de nanoseconde à la vitesse de la lumière : 10 cm. D’où l’intérêt des courtes distances.", ref: "i4" },
    { q: "Comment un SoC économise-t-il l’énergie écran éteint ?", c: ["Il augmente la fréquence", "Il coupe l’alimentation des blocs inutiles (GPU, contrôleur vidéo)", "Il éteint la RAM définitivement", "Il ne peut pas économiser"], a: 1, e: "La gestion d’énergie coupe ou ralentit chaque bloc séparément.", ref: "i5" },
    { q: "Dans une architecture big.LITTLE, un cœur économe…", c: ["est plus rapide et consomme plus", "est plus lent mais dépense moins d’énergie pour une tâche légère", "ne sert qu’au démarrage", "remplace le GPU"], a: 1, e: "Les tâches légères ou non pressées vont aux cœurs économes.", ref: "i5" },
    { q: "D’après P ≈ C·V²·f, baisser la tension de moitié (à fréquence égale) divise la puissance par…", c: ["2", "4", "8", "Elle ne change pas"], a: 1, e: "La tension compte au carré : (1/2)² = 1/4.", ref: "i5" },
    { q: "Quel est un inconvénient d’un SoC ?", c: ["Il consomme plus qu’une carte", "On ne peut ni changer ni ajouter un composant intégré", "Il est plus encombrant", "Il ne peut pas avoir plusieurs cœurs"], a: 1, e: "Pas d’évolution ni de réparation d’un bloc.", ref: "i6" },
    { q: "Le modèle de von Neumann place dans la même mémoire…", c: ["le programme et les données", "le processeur et le GPU", "le cache et le disque", "les seules instructions"], a: 0, e: "C’est sa caractéristique principale (Première).", ref: "i1" },
    { q: "Le premier microprocesseur sur une seule puce, l’Intel 4004 (1971), comptait environ…", c: ["23 transistors", "2 300 transistors", "2,3 millions de transistors", "2,3 milliards de transistors"], a: 1, e: "Environ 2 300 ; un SoC de téléphone de 2023 en compte de l’ordre de 19 milliards.", ref: "i1" },
    { q: "Sur un schéma, un bloc relié à l’antenne qui gère la 5G est…", c: ["le contrôleur vidéo", "une interface radio (modem)", "la mémoire cache", "l’ISP"], a: 1, e: "Les interfaces radio : modem cellulaire, Wi-Fi, Bluetooth.", ref: "i7" }
  ],
  cartes: [
    { r: "SoC", v: "System on Chip : un seul circuit intégré qui regroupe CPU, GPU, mémoires locales, contrôleurs, interfaces." },
    { r: "Circuit intégré", v: "Puce de silicium portant des millions ou milliards de transistors." },
    { r: "CPU multicœur", v: "Plusieurs processeurs (cœurs) sur la puce ; souvent performants + économes (big.LITTLE)." },
    { r: "GPU", v: "Accélérateur graphique : calcul des images, très parallèle." },
    { r: "Mémoires locales (caches)", v: "Petites mémoires très rapides près des cœurs ; évitent d’attendre la RAM." },
    { r: "Contrôleur mémoire", v: "Fait le lien entre le SoC et la RAM extérieure." },
    { r: "Interfaces radio / filaires", v: "Radio : modem 4G / 5G, Wi-Fi, Bluetooth. Filaires : USB, stockage, écran, caméra." },
    { r: "Gestion d’énergie", v: "Règle tension et fréquence de chaque bloc, coupe les blocs inutiles." },
    { r: "Réseau sur puce (NoC)", v: "Réseau interne qui relie les blocs du SoC." },
    { r: "Avantage vitesse", v: "Distances de quelques mm, liaisons nombreuses, circuits spécialisés." },
    { r: "Avantage consommation", v: "Fils courts, blocs coupés ou ralentis, cœurs économes." },
    { r: "Inconvénients du SoC", v: "Pas d’évolution ni de réparation, conception coûteuse, chaleur concentrée." },
    { r: "P ≈ C·V²·f (pour aller plus loin)", v: "Puissance de commutation : la tension compte au carré." },
    { r: "Intel 4004 (1971)", v: "Premier microprocesseur sur une puce, ≈ 2 300 transistors." },
    { r: "Loi de Moore", v: "1965 (révisée en 1975) : doublement du nombre de transistors d’une puce environ tous les deux ans." }
  ]
});
