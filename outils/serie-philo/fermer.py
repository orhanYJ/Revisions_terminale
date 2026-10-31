"""Ferme automatiquement un visuel de texte quand le suivant apparaît (ajoute {-A} devant {B} dans le script).

Usage : python3 outils/serie-philo/fermer.py liberte_2      (après generer.py, qui a écrit le .data.js)
Ne touche que des repères : le texte lu ne change pas, la voix en cache reste valable. Relancer generer.py ensuite.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chevauchements import chevauchements

ICI = os.path.dirname(os.path.abspath(__file__))


def fermer(module):
    code = module.replace("_", "-")
    P = os.path.join(ICI, module + ".py")
    s = open(P, encoding="utf-8").read()
    n = 0
    for _, _, a, ta, b, tb in chevauchements(code):
        # A est apparu avant B : on ferme A à l'apparition de B
        if "{" + b + "}" in s:
            s = s.replace("{" + b + "}", "{-" + a + "}{" + b + "}", 1)
            n += 1
            continue
        m = re.search(r'"' + re.escape(b) + r'"\s*[,)]', s)           # l'identifiant à la fin du tuple ("C", texte, id)
        k = s.rfind('("C",', 0, m.start()) if m else -1
        if k >= 0 and "dict(" not in s[k:m.start()]:
            ligne = s.rfind("\n", 0, k) + 1
            indent = s[ligne:k]
            s = s[:ligne] + indent + '"{-' + a + '}",\n' + s[ligne:]
            n += 1
        else:
            print("  introuvable :", b)
    open(P, "w", encoding="utf-8").write(s)
    print(f"{module} : {n} fermeture(s) ajoutée(s)")


if __name__ == "__main__":
    for m in sys.argv[1:]:
        fermer(m)
