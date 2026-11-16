"""Onglet Oral du site DNL : met dans dnl/index.html la liste officielle (syllabus.py), les notes à puces
(<theme>_issues.json, <theme>_terms.json, format de CAHIER_PUCES.md), le composant (composant.js) et le style (style.css).
Usage, depuis la racine : python3 outils/oral-dnl/integrer.py
Rejouable : si l'onglet est déjà dans la page, les blocs existants sont remplacés ; sinon ils sont insérés.
Les versions rédigées en discours (<theme>_issues_redige.json…) sont l'étape intermédiaire de vérification des faits :
elles ne sont pas publiées."""
import json, sys, re, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
sys.path.insert(0, D)
from syllabus import SYLLABUS
P = os.path.join(D, "..", "..", "dnl", "index.html")
s = open(P, encoding="utf-8").read()

INTERDIT = r"(?i)\bros\b|orhan|philip|bellon|\bcourse\b|\bteacher|worksheet|\bslides?\b|professeur|diapo|feuille|11 (december|décembre) 1941"
ORAL = {}
for th in SYLLABUS:
    fi, ft = D + th["id"].replace("-", "_") + "_issues.json", D + th["id"].replace("-", "_") + "_terms.json"
    if not os.path.exists(fi):
        continue
    assert th["fait"], th["id"] + " : réponses présentes mais thème non traité (fait = False)"
    iss = json.load(open(fi, encoding="utf-8")); trm = json.load(open(ft, encoding="utf-8"))
    assert [i["q"] for i in iss] == th["issues"], (th["id"], [i["q"] for i in iss])
    assert [i["q"] for i in trm] == th["terms"], (th["id"], [i["q"] for i in trm])
    for it in iss + trm:
        for L in ("en", "fr"):
            secs = it[L]["sections"]
            assert sum(x["d"] for x in secs) == 270, (it["id"], L, "durées ≠ 270 s")
            assert all(x["t"].strip() and x["pts"] for x in secs) and len(it[L]["jury"]) >= 3, (it["id"], L)
        assert [len(x["pts"]) for x in it["en"]["sections"]] == [len(x["pts"]) for x in it["fr"]["sections"]], it["id"]
        notes = json.dumps([it["en"], it["fr"]], ensure_ascii=False)   # pas q : la question officielle peut contenir « slide »
        assert re.search(INTERDIT, notes) is None, (it["id"], re.search(INTERDIT, notes))
        n = sum(len(x["pts"]) for x in it["en"]["sections"])
        mots = sum(len(p.split()) for x in it["en"]["sections"] for p in x["pts"])
        print(it["id"], n, "puces,", mots, "mots")
    ORAL[th["id"]] = {"issues": iss, "terms": trm}

css = open(D + "style.css", encoding="utf-8").read().strip()
comp = open(D + "composant.js", encoding="utf-8").read().strip()
l_syl = "const ORAL_SYLLABUS = " + json.dumps(SYLLABUS, ensure_ascii=False) + ";"
l_oral = "const ORAL = " + json.dumps(ORAL, ensure_ascii=False) + ";"

def ins(ancre, texte, avant=True):
    global s
    assert s.count(ancre) == 1, ancre[:60]
    s = s.replace(ancre, (texte + ancre) if avant else (ancre + texte))

if '<style id="oral-skin">' in s:                      # mise à jour
    i = s.index('<style id="oral-skin">'); j = s.index("</style>", i) + 8
    s = s[:i] + css + s[j:]
    for debut, ligne in (("const ORAL_SYLLABUS = ", l_syl), ("const ORAL = ", l_oral)):
        assert s.count("\n" + debut) == 1, debut
        i = s.index("\n" + debut) + 1; j = s.index("\n", i)
        s = s[:i] + ligne + s[j:]
    i = s.index("/* ==== ORAL"); j = s.index("function Placeholder({")
    s = s[:i] + comp + "\n" + s[j:]
else:                                                  # première insertion
    ins('<style id="train-skin">', css + "\n")
    ins("function Placeholder({", l_syl + "\n" + l_oral + "\n" + comp + "\n")
    ins('''    .concat([["overview", FR ? "L'essentiel" : "Overview", "🧭"]])''',
        '''    .concat(oralChap(data.code) ? [["oral", "Oral", "🎤"]] : [])\n''')
    ins('''  else if (tab === "video") body = [React.createElement(SerieDNL, { key: "sv", code: data.code, lang: lang })];''',
        '''\n  else if (tab === "oral") body = [React.createElement(OralTab, { key: "or", code: data.code, lang: lang })];''', avant=False)
open(P, "w", encoding="utf-8").write(s)
print("ok", len(s))
