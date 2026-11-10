"""Assemble maths/index.html (site CQFD) à partir des sources de src/.

Usage : python3 outils/specialites/maths/build.py
"""
import os

ICI = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ICI, "src")
SORTIE = os.path.join(ICI, "..", "..", "..", "maths", "index.html")
DEBUT = ["mathml.js", "widgets.js", "anims.js"]
FIN = ["programme.js", "pages.js", "app.js"]


def scripts():
    """Ordre : moteur, autres fichiers d'outils, chapitres ch1.js, ch2.js… (ordre numérique), programme, pages, app.

    Un nouveau chapitre s'enregistre tout seul : fichier src/chN.js qui définit var CHN = {...}, id "chN".
    """
    tous = sorted(f for f in os.listdir(SRC) if f.endswith(".js"))
    chap = sorted((f for f in tous if f[:2] == "ch" and f[2:-3].isdigit()), key=lambda f: int(f[2:-3]))
    autres = [f for f in tous if f not in DEBUT + FIN + chap]
    return [f for f in DEBUT if f in tous] + autres + chap + FIN


def lire(nom):
    with open(os.path.join(SRC, nom), encoding="utf-8") as f:
        return f.read()


def main():
    shell = lire("shell.html")
    js = "\n".join(lire(n) for n in scripts())
    assert "</script" not in js.lower(), "balise </script> dans le JS"
    html = shell.replace("/*STYLE*/", lire("style.css")).replace("/*SCRIPT*/", js)
    with open(SORTIE, "w", encoding="utf-8") as f:
        f.write(html)
    print("maths/index.html :", round(len(html.encode("utf-8")) / 1024), "Ko")


if __name__ == "__main__":
    main()
