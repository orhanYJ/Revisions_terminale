#!/usr/bin/env python3
"""Ajoute un fichier de chapitre à build.py (DONNEES) et relie des items « bientôt » du programme à ce chapitre.

Usage : python3 outils/specialites/nsi/lier.py ch5_dictionnaires.js ch5 dico [autre_item …]
Modification ponctuelle (les fichiers partagés ne sont jamais réécrits en entier).
"""
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
fichier, chapitre, items = sys.argv[1], sys.argv[2], sys.argv[3:]

b = ICI / "build.py"
s = b.read_text(encoding="utf-8")
m = re.search(r'^DONNEES = \[(.*)\]$', s, re.M)
liste = [x.strip().strip('"') for x in m.group(1).split(",")]
if fichier not in liste:
    liste.insert(liste.index("programme.js"), fichier)
    s = s[:m.start()] + "DONNEES = [" + ", ".join('"%s"' % x for x in liste) + "]" + s[m.end():]
    b.write_text(s, encoding="utf-8")

p = ICI / "src" / "programme.js"
s = p.read_text(encoding="utf-8")
for it in items:
    m = re.search(r'\{ id: "%s", t: "([^"]*)",.*?\n?(?=\s*\{ (?:id|ch):|\s*\]\s*\})' % re.escape(it), s, re.S)
    assert m, it
    bloc = m.group(0)
    fin = bloc.rstrip()
    virgule = "," if fin.endswith(",") else ""
    blanc = bloc[len(bloc.rstrip()):]
    s = s.replace(bloc, '{ ch: "%s", t: "%s" }%s%s' % (chapitre, m.group(1), virgule, blanc), 1)
p.write_text(s, encoding="utf-8")
print("ok", fichier, chapitre, items)
