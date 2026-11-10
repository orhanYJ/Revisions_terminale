#!/usr/bin/env python3
"""Assemble hlp/index.html à partir des sources de src/ (CSS, données, application)."""
import os
ICI = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ICI, "src")
RACINE = os.path.normpath(os.path.join(ICI, "..", "..", ".."))
def lire(n):
    with open(os.path.join(SRC, n), encoding="utf-8") as f:
        return f.read()
shell = lire("shell.html")
# Données : le tronc commun d'abord, puis toutes les entrées (data-e*.js, dans l'ordre des noms),
# puis l'atelier, les animations et les pages transversales. Un nouveau fichier data-e<N>.js est pris d'office.
ENTREES = sorted(n for n in os.listdir(SRC) if n.startswith("data-e") and n.endswith(".js"))
ORDRE = ["data-commun.js"] + ENTREES + ["data-atelier.js", "data-anims.js", "data-pages.js"]
ORDRE = [n for n in ORDRE if os.path.exists(os.path.join(SRC, n))]
donnees = "\n".join(lire(n) for n in ORDRE)
STYLE = lire("style.css") + ("\n" + lire("theme-ancien.css") if os.path.exists(os.path.join(SRC, "theme-ancien.css")) else "")
APP = (lire("animations.js") + "\n" if os.path.exists(os.path.join(SRC, "animations.js")) else "") + lire("app.js")
for ancre, contenu in [("/*STYLE*/", STYLE), ("/*DATA*/", donnees), ("/*APP*/", APP)]:
    assert shell.count(ancre) == 1, ancre
    shell = shell.replace(ancre, contenu)
logo = "<!--LOGO-->"
assert shell.count(logo) == 1
deb = donnees.index("H.LOGO = '") + len("H.LOGO = '")
fin = donnees.index("';\n", deb)
shell = shell.replace(logo, donnees[deb:fin].replace("' +\n    '", ""))
sortie = os.path.join(RACINE, "hlp", "index.html")
with open(sortie, "w", encoding="utf-8") as f:
    f.write(shell)
print(sortie, len(shell.encode("utf-8")), "octets")
