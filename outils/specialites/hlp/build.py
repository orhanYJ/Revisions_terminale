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
donnees = "\n".join(lire(n) for n in ["data-commun.js", "data-e1.js", "data-e2.js", "data-e3.js", "data-atelier.js", "data-pages.js"])
for ancre, contenu in [("/*STYLE*/", lire("style.css")), ("/*DATA*/", donnees), ("/*APP*/", lire("app.js"))]:
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
