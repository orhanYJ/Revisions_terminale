"""Données du site SES (« Faits & Courbes ») pour les vidéos : mêmes chiffres, mêmes sources, mêmes chaînes causales.

Les vidéos de SES ne recopient aucun chiffre à la main : un script de vidéo (outils/serie-ses/ses_<chap>.py) lit les
graphiques (GRAPHES), les chaînes causales (CHAINES), les animations (ANIMS : titre et légendes des étapes) et le
chapitre (CH) directement dans les sources du site, outils/specialites/ses/src/, évaluées par node.

    import site_ses
    D = site_ses.donnees()          # {"graphes": {...}, "chaines": {...}, "anims": {...}, "ch": {...}}
    D["graphes"]["e1-pib"]["y"]      # taux de croissance du PIB, comme dans le site

Le lecteur vidéo rejoue aussi les animations du site (type sanim de ses/serie/moteur.js) : leurs fonctions de rendu
(rendu(A, étape, avancement), fonctions pures) sont copiées telles quelles dans ses/serie/site-ses.js, avec la boîte
à outils A de anim-moteur.js et les graphiques qu'elles lisent. Ce fichier est régénéré à chaque generer.py d'une vidéo
SES (fonction ecrire_js) ; à la main : python3 outils/serie-ses/site_ses.py
"""
import json, os, subprocess

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
SRC = os.path.join(RACINE, "outils", "specialites", "ses", "src")
SORTIE_JS = os.path.join(RACINE, "ses", "serie", "site-ses.js")

_EXTRAIT = r"""
const fs = require('fs'), vm = require('vm'), path = require('path');
const S = process.argv[1];
const ctx = {}; vm.createContext(ctx);
let code = fs.readFileSync(path.join(S, 'data-commun.js'), 'utf8') + '\n';
for (const f of fs.readdirSync(S).sort()) if (/^data-.*\.js$/.test(f) && f !== 'data-commun.js' && f !== 'data-pages.js') code += fs.readFileSync(path.join(S, f), 'utf8') + '\n';
code += 'this.__R = JSON.stringify({graphes: GRAPHES, chaines: CHAINES, ch: CH, auteurs: AUTEURS,' +
  ' anims: Object.fromEntries(Object.entries(ANIMS).map(([k, a]) => [k, {t: a.t, h: a.h, src: a.src, etapes: a.etapes}]))});';
vm.runInContext(code, ctx);
process.stdout.write(ctx.__R);
"""

_cache = None


def donnees():
    global _cache
    if _cache is None:
        r = subprocess.run(["node", "-e", _EXTRAIT, SRC], capture_output=True, text=True, check=True)
        _cache = json.loads(r.stdout)
    return _cache


def ecrire_js():
    """ses/serie/site-ses.js : boîte à outils des animations du site, graphiques et animations (rendu compris)."""
    lire = lambda n: open(os.path.join(SRC, n), encoding="utf-8").read()
    anims = sorted(f for f in os.listdir(SRC) if f.startswith("data-anim-") and f.endswith(".js"))
    js = ("// Généré par outils/serie-ses/site_ses.py depuis outils/specialites/ses/src/ : ne pas modifier à la main.\n"
          "// Animations du site (anim-moteur.js, " + ", ".join(anims) + ") rejouées dans les vidéos (type sanim).\n"
          "var CH = {}, CHAINES = {}, ANIMS = {};\nvar GRAPHES = " +
          json.dumps(donnees()["graphes"], ensure_ascii=False, separators=(",", ":")) + ";\n" +
          lire("anim-moteur.js") + "\n" + "\n".join(lire(f) for f in anims) + "\n")
    os.makedirs(os.path.dirname(SORTIE_JS), exist_ok=True)
    ancien = open(SORTIE_JS, encoding="utf-8").read() if os.path.exists(SORTIE_JS) else None
    if ancien != js:
        with open(SORTIE_JS, "w", encoding="utf-8") as f:
            f.write(js)
    return SORTIE_JS


if __name__ == "__main__":
    print(ecrire_js())
