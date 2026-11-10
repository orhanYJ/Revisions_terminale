#!/usr/bin/env python3
"""Assemble nsi/index.html à partir de src/ (feuille de style, données des chapitres, moteur).

Usage : python3 outils/specialites/nsi/build.py
"""
import json
import pathlib

import traces

ICI = pathlib.Path(__file__).resolve().parent
SRC = ICI / "src"
SORTIE = ICI.parent.parent.parent / "nsi" / "index.html"
DONNEES = ["base.js", "ch1_poo.js", "ch2_recursivite.js", "ch3_lineaires.js", "ch4_mise_au_point.js", "ch5_dictionnaires.js", "ch_dpr.js", "ch_dyn.js", "ch_texte.js", "ch_calc.js", "ch_para.js", "ch6_bases_de_donnees.js", "ch_soc.js", "ch_proc.js", "ch_rout.js", "ch7_arbres.js", "ch8_graphes.js", "programme.js", "pages.js"]


def lire(nom):
    return (SRC / nom).read_text(encoding="utf-8")


def main():
    shell = lire("shell.html")
    donnees = "\n".join(lire(n) for n in DONNEES)
    # traces d'exécution réelles (sys.settrace) des extraits marqués trace: true
    donnees += "\nvar TRACES = " + json.dumps(traces.calculer([SRC / n for n in DONNEES]), ensure_ascii=False).replace("</", "<\\/") + ";\n"
    for marque, contenu in (("/*STYLE*/", lire("style.css")), ("/*DATA*/", donnees), ("/*APP*/", lire("app.js"))):
        assert shell.count(marque) == 1, marque
        assert "</script" not in contenu.lower() or marque == "/*STYLE*/", "balise </script> dans " + marque
        shell = shell.replace(marque, contenu)
    SORTIE.write_text(shell, encoding="utf-8")
    print(SORTIE, round(len(shell.encode("utf-8")) / 1024), "Ko")


if __name__ == "__main__":
    main()
