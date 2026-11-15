"""Onglet Oral du site DNL : injecte la liste officielle (syllabus.py), les réponses rédigées (h_t1_*.json),
le composant (composant.js) et le style (style.css) dans dnl/index.html.
Usage, depuis la racine : python3 outils/oral-dnl/integrer.py H3 [H2 H1]   (chapitres dont l'onglet est publié)
Attention : à lancer sur un index.html qui n'a pas encore l'onglet ; pour publier un chapitre de plus,
remplacer seulement la constante ORAL (voir CLAUDE.md)."""
import json, sys, re
import os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
sys.path.insert(0, D)
from syllabus import SYLLABUS
P = os.path.join(D, "..", "..", "dnl", "index.html")
s = open(P, encoding="utf-8").read()

mots = lambda it: sum(len(b["p"].split()) for b in it["en"]["blocs"])
ORAL = {}
CHAPS = sys.argv[1:] or ["H1", "H2", "H3"]   # tout le thème : l'onglet Oral porte le thème entier
PAR_CHAP = {"H1": {"h-t1-ki-1", "h-t1-ki-2", "h-t1-kt-1", "h-t1-kt-2"}, "H2": {"h-t1-ki-3", "h-t1-kt-2", "h-t1-kt-3"}, "H3": {"h-t1-ki-4", "h-t1-kt-4", "h-t1-kt-5"}}
GARDER = set().union(*[PAR_CHAP[c] for c in CHAPS])
for tid, fi, ft in [("h-t1", "h_t1_issues.json", "h_t1_terms.json")]:
    th = next(t for t in SYLLABUS if t["id"] == tid)
    iss = json.load(open(D + fi)); trm = json.load(open(D + ft))
    assert [i["q"] for i in iss] == th["issues"], (tid, [i["q"] for i in iss])
    assert [i["q"] for i in trm] == th["terms"], (tid, [i["q"] for i in trm])
    iss = [i for i in iss if i["id"] in GARDER]; trm = [i for i in trm if i["id"] in GARDER]
    for it in iss + trm:
        for L in ("en", "fr"):
            assert it[L]["plan"] and it[L]["blocs"] and len(it[L]["jury"]) >= 3, (it["id"], L)
            for b in it[L]["blocs"]:
                assert b["k"] in ("intro", "definition", "partie", "conclusion") and b["p"].strip(), (it["id"], b)
        assert len(it["en"]["blocs"]) == len(it["fr"]["blocs"]), it["id"]
        assert re.search(r"(?i)\bros\b|orhan|philip|bellon", json.dumps(it, ensure_ascii=False)) is None, it["id"]
        print(it["id"], mots(it), "mots")
    ORAL[tid] = {"issues": iss, "terms": trm}

def ins(ancre, texte, avant=True):
    global s
    assert s.count(ancre) == 1, ancre[:60]
    s = s.replace(ancre, (texte + ancre) if avant else (ancre + texte))

css = open(D + "style.css", encoding="utf-8").read()
ins('<style id="train-skin">', css)
comp = open(D + "composant.js", encoding="utf-8").read()
donnees = ("const ORAL_SYLLABUS = " + json.dumps(SYLLABUS, ensure_ascii=False) + ";\n" +
           "const ORAL = " + json.dumps(ORAL, ensure_ascii=False) + ";\n")
ins("function Placeholder({", donnees + comp + "\n")
ins('''    .concat([["overview", FR ? "L'essentiel" : "Overview", "🧭"]])''',
    '''    .concat(oralChap(data.code) ? [["oral", "Oral", "🎤"]] : [])\n''')
ins('''  else if (tab === "video") body = [React.createElement(SerieDNL, { key: "sv", code: data.code, lang: lang })];''',
    '''\n  else if (tab === "oral") body = [React.createElement(OralTab, { key: "or", code: data.code, lang: lang })];''', avant=False)
open(P, "w", encoding="utf-8").write(s)
print("ok", len(s))
