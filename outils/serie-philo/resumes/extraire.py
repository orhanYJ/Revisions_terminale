"""Extrait le texte lu de chaque épisode des séries de philosophie (passages, citations avec auteur, « À retenir »),
une notion par fichier <notion>.txt dans le dossier courant : c'est la source des résumés écrits (<notion>.json).
Usage : python3 outils/serie-philo/resumes/extraire.py   (puis rédiger / mettre à jour <notion>.json, puis integrer.py)
"""
import importlib.util, re, sys, json, os
D = "/home/user/Revisions_terminale/outils/serie-philo"
def clean(s):
    s = re.sub(r"\{[^}]*\}", "", s)
    return re.sub(r"\s+", " ", s).strip()
for notion in ["liberte","devoir","bonheur","conscience","etat"]:
    out = []
    for n in range(1, 8):
        p = f"{D}/{notion}_{n}.py"
        spec = importlib.util.spec_from_file_location(f"m{notion}{n}", p)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        out.append(f"\n\n######## ÉPISODE {n} — {m.TITRE} (code {m.CODE})\n")
        for sc in m.SCENES:
            out.append(f"\n=== Scène « {sc.get('chap')} » (id {sc['id']})" + (f" — notions : {', '.join(sc['notions'])}" if sc.get('notions') else ""))
            txt = []
            for b in sc.get("beats", []):
                if isinstance(b, str): txt.append(clean(b))
                elif isinstance(b, tuple) and b and b[0] == "C":
                    v = sc.get("vis", {}).get(b[2], {}) if len(b) > 2 else {}
                    txt.append("[CITATION LUE] « " + clean(b[1]) + " » (" + v.get("a", "?") + ", " + v.get("o", "?") + ")")
                elif isinstance(b, tuple) and isinstance(b[0], str) and b[0] != "P": txt.append(clean(b[0]))
            out.append(" ".join(t for t in txt if t))
            vis = sc.get("vis", {})
            if sc.get("retenir"): out.append("  [À RETENIR] " + sc["retenir"])
    open(f"{notion}.txt", "w").write("\n".join(out))
    print(notion, sum(len(x.split()) for x in out))
