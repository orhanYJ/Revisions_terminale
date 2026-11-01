"""Vérifie un script d'épisode sans enregistrer la voix.

Usage : python3 outils/serie-philo/verifier.py liberte_2
Contrôles : chaque repère {id} / {-id} / {id.k} renvoie à un visuel de sa scène ; chaque visuel est appelé ;
chaque citation ("C", texte, id) a son visuel de type cit ; images présentes dans philo/serie/img ; illustrations
connues du moteur ; types connus ; quiz ; durée estimée (débit mesuré sur l'épisode 1).
"""
import importlib, os, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, ICI)
MARQUE = re.compile(r"\{([-!]?)([^{}]+)\}")
TYPES = {"titre", "chapitre", "mot", "question", "nuage", "def", "note", "tag", "cit", "portrait", "cols", "cartes", "liste",
         "dialogue", "frise", "tableau", "illu", "carte", "frappe", "flash", "generique"}
MOTS_PAR_S = 2.9       # débit du narrateur (calé sur l'épisode 1 : 13,6 min réelles)


def illus_connues():
    js = open(os.path.join(RACINE, "philo", "serie", "moteur.js"), encoding="utf-8").read()
    return set(re.findall(r"ILLU\.(\w+) = function", js))


def verifier(nom):
    ep = importlib.import_module(nom)
    err, mots, secondes = [], 0, 0.0
    ill = illus_connues()
    for attr in ("CODE", "NOTION", "NUM", "TITRE", "SUIVANT", "SCENES", "QUIZ"):
        if not hasattr(ep, attr):
            err.append(f"attribut manquant : {attr}")
    tous = set()
    for sc in ep.SCENES:
        vis = sc.get("vis", {})
        appel, fin, etapes = set(), set(), set()
        etapes_k = {}
        for b in sc["beats"]:
            if isinstance(b, str):
                txt = b
            elif b[0] == "P":
                secondes += b[1]
                continue
            elif b[0] == "C":
                txt = b[1]
                appel.add(b[2])
                if b[2] not in vis:
                    err.append(f"[{sc['id']}] citation sans visuel : {b[2]}")
                elif vis[b[2]].get("type") != "cit":
                    err.append(f"[{sc['id']}] le visuel {b[2]} d'une citation n'est pas de type cit")
                secondes += 1.4
            else:
                txt = b[0]
            for m in MARQUE.finditer(txt):
                k, ident = m.group(1), m.group(2)
                if k == "!":
                    continue
                base = ident.split(".")[0]
                if base not in vis:
                    err.append(f"[{sc['id']}] repère vers un visuel inconnu : {{{k}{ident}}}")
                if k == "-":
                    fin.add(base)
                elif "." in ident:
                    etapes.add(base)
                    etapes_k.setdefault(base, set()).add(ident.split(".", 1)[1])
                else:
                    appel.add(base)
            lu = MARQUE.sub("", txt)
            n = len(lu.split())
            mots += n
            secondes += n / MOTS_PAR_S + 0.4
        for ident, spec in vis.items():
            if ident in tous:
                err.append(f"[{sc['id']}] identifiant de visuel déjà utilisé dans une autre scène : {ident} (les repères sont globaux)")
            tous.add(ident)
            if ident not in appel:
                err.append(f"[{sc['id']}] visuel jamais appelé : {ident}")
            for e in etapes:
                if e not in appel:
                    err.append(f"[{sc['id']}] étapes d'un visuel jamais appelé : {e}")
            t = spec.get("type")
            nb = len(spec.get("items", [])) if t in ("liste", "cartes") else 0
            if nb and any(x.isdigit() for x in etapes_k.get(ident, ())):
                manque = [k for k in range(1, nb + 1) if str(k) not in etapes_k[ident]]
                hors = sorted(x for x in etapes_k[ident] if x.isdigit() and not 1 <= int(x) <= nb)
                if manque or hors:
                    err.append(f"[{sc['id']}] liste {ident} : chaque ligne k s'affiche au repère {{{ident}.k}} (k de 1 à {nb}) ; "
                               f"manquent {manque}, en trop {hors}")
            if t not in TYPES:
                err.append(f"[{sc['id']}] type inconnu {t} ({ident})")
            if t == "illu" and spec.get("nom") not in ill:
                err.append(f"[{sc['id']}] illustration inconnue du moteur : {spec.get('nom')} ({ident})")
            for cle in ("img",):
                if spec.get(cle) and not os.path.exists(os.path.join(RACINE, "philo", "serie", "img", spec[cle] + ".jpg")):
                    err.append(f"[{sc['id']}] image absente : img/{spec[cle]}.jpg ({ident})")
            if t == "frise":
                for it in spec.get("items", []):
                    if it.get("img") and not os.path.exists(os.path.join(RACINE, "philo", "serie", "img", it["img"] + ".jpg")):
                        err.append(f"[{sc['id']}] image de frise absente : {it['img']}")
            if t == "tableau" and not spec.get("legende"):
                err.append(f"[{sc['id']}] tableau sans légende (auteur, licence) : {ident}")
        if sc.get("carton", True):
            secondes += 2.9
        if sc.get("retenir"):
            secondes += 3.8
    for q in ep.QUIZ:
        if q.get("voir") and q["voir"] not in tous:
            err.append(f"quiz : « voir » renvoie à un visuel inconnu : {q['voir']}")
        if not (0 <= q.get("ok", -1) < len(q.get("r", []))):
            err.append(f"quiz : réponse « ok » hors des choix : {q.get('q', '')[:40]}")
    print(f"{nom} : {len(ep.SCENES)} scènes, {mots} mots, durée estimée {(secondes + 6.2) / 60:.1f} min, "
          f"{sum(1 for sc in ep.SCENES for v in sc['vis'].values() if v.get('type') == 'tableau')} tableaux")
    for e in err:
        print("  ERREUR", e)
    return not err


if __name__ == "__main__":
    ok = all([verifier(m) for m in sys.argv[1:]])
    sys.exit(0 if ok else 1)
