"""Assemble maths/index.html (site CQFD) à partir des sources de src/.

Usage : python3 outils/specialites/maths/build.py
"""
import os

ICI = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ICI, "src")
SORTIE = os.path.join(ICI, "..", "..", "..", "maths", "index.html")
SCRIPTS = ["mathml.js", "widgets.js", "ch1.js", "ch2.js", "ch3.js", "ch4.js", "ch5.js", "programme.js", "pages.js", "app.js"]


def lire(nom):
    with open(os.path.join(SRC, nom), encoding="utf-8") as f:
        return f.read()


def main():
    shell = lire("shell.html")
    js = "\n".join(lire(n) for n in SCRIPTS if os.path.exists(os.path.join(SRC, n)))
    assert "</script" not in js.lower(), "balise </script> dans le JS"
    html = shell.replace("/*STYLE*/", lire("style.css")).replace("/*SCRIPT*/", js)
    with open(SORTIE, "w", encoding="utf-8") as f:
        f.write(html)
    print("maths/index.html :", round(len(html.encode("utf-8")) / 1024), "Ko")


if __name__ == "__main__":
    main()
