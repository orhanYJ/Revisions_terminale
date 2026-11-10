#!/usr/bin/env python3
"""Assemble nsi/index.html à partir de src/ (feuille de style, données des chapitres, moteur).

Usage : python3 outils/specialites/nsi/build.py
"""
import pathlib

ICI = pathlib.Path(__file__).resolve().parent
SRC = ICI / "src"
SORTIE = ICI.parent.parent.parent / "nsi" / "index.html"
DONNEES = ["base.js", "ch1_poo.js", "ch2_recursivite.js", "ch3_lineaires.js", "ch4_mise_au_point.js", "ch5_dictionnaires.js", "ch_dpr.js", "ch6_bases_de_donnees.js", "ch_soc.js", "programme.js", "pages.js"]


def lire(nom):
    return (SRC / nom).read_text(encoding="utf-8")


def main():
    shell = lire("shell.html")
    donnees = "\n".join(lire(n) for n in DONNEES)
    for marque, contenu in (("/*STYLE*/", lire("style.css")), ("/*DATA*/", donnees), ("/*APP*/", lire("app.js"))):
        assert shell.count(marque) == 1, marque
        assert "</script" not in contenu.lower() or marque == "/*STYLE*/", "balise </script> dans " + marque
        shell = shell.replace(marque, contenu)
    SORTIE.write_text(shell, encoding="utf-8")
    print(SORTIE, round(len(shell.encode("utf-8")) / 1024), "Ko")


if __name__ == "__main__":
    main()
