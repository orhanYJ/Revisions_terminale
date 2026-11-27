#!/usr/bin/env python3
"""Injecte les listes de vocabulaire (outils/vocab/listes/<id>.json) dans vocab/index.html.

Chaque liste est placée entre les marqueurs /*mots:<id>*/ … /*fin*/ de la constante LISTES.
Rejouable. Contrôle le format de chaque mot (voir CAHIER.md) et refuse en cas d'erreur.
Usage : python3 outils/vocab/integrer.py
"""
import json, re, sys, pathlib

RACINE = pathlib.Path(__file__).resolve().parents[2]
PAGE = RACINE / "vocab" / "index.html"
LISTES = RACINE / "outils" / "vocab" / "listes"
CHAMPS = ["id", "w", "pos", "ipa", "reg", "fr", "def", "col", "ex", "piege", "fam", "trous", "ecris", "formes"]
INTERDITS = re.compile(r"orhan|cengiz|philip|bellon|\bM\. Ros\b|ton cours|ta prof|ton prof|en classe|\bclaude\b", re.I)

def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[.,;:!?\"]", " ", s.lower().replace("’", "'"))).strip()

def controler(mots, prefixe, deja):
    err, avert = [], []
    for m in mots:
        q = m.get("id", "?")
        manque = [c for c in CHAMPS if c not in m]
        if manque: err.append(f"{q} : champs manquants {manque}"); continue
        if not q.startswith(prefixe): err.append(f"{q} : préfixe attendu {prefixe}")
        cle = norm(m["w"])
        if cle in deja: err.append(f"{q} : « {m['w']} » déjà présent ({deja[cle]})")
        deja[cle] = q
        if m["reg"] not in ("courant", "formel", "familier"): err.append(f"{q} : registre {m['reg']}")
        if not (m["ipa"].startswith("/") and m["ipa"].endswith("/")): err.append(f"{q} : ipa")
        if len(m["ex"]) != 2 or any("[[" not in e or "]]" not in e for e in m["ex"]): err.append(f"{q} : exemples")
        if len(m["trous"]) != 2: err.append(f"{q} : il faut 2 phrases à trous")
        for tr in m["trous"]:
            if tr.get("s", "").count("___") != 1: err.append(f"{q} : trou « {tr.get('s')} »")
            if not tr.get("a") or not tr.get("fr"): err.append(f"{q} : réponse ou traduction manquante")
        if re.search(r"<(?!/?(b|i)>)", m["piege"]): err.append(f"{q} : balise interdite dans piege")
        if not m["formes"]: err.append(f"{q} : formes vides")
        tout = json.dumps(m, ensure_ascii=False)
        if INTERDITS.search(tout): err.append(f"{q} : mention interdite ({INTERDITS.search(tout).group(0)})")
        for e in m["ex"]:
            dedans = norm(re.search(r"\[\[(.+?)\]\]", e).group(1)) if "[[" in e else ""
            if dedans and not any(norm(f).split()[0] in dedans for f in m["formes"] + [m["w"]]):
                avert.append(f"{q} : exemple surligné « {dedans} » sans forme connue")
    return err, avert

def main():
    page = PAGE.read_text(encoding="utf-8")
    deja = {norm(w): "argu" for w in re.findall(r'^\{ id: "[a-z]+", w: "([^"]+)"', page, re.M)}
    erreurs, n = [], 0
    lots = {}
    for f in sorted(LISTES.glob("*.json")):
        lots.setdefault(f.stem.split("-")[0], []).append(json.loads(f.read_text(encoding="utf-8")))
    for lid, paquets in lots.items():
        # les lots d'une même liste sont entrelacés (chacun est trié du plus utile au moins utile)
        mots, vus = [], set()
        for i in range(max(len(x) for x in paquets)):
            for x in paquets:
                if i < len(x):
                    cle = norm(x[i].get("w", ""))
                    if cle in vus or cle in deja:
                        print(f"  doublon ignoré [{lid}] {x[i].get('w')}"); continue
                    vus.add(cle); mots.append(x[i])
        mots = [{c: m[c] for c in CHAMPS + ["alt"] if c in m} for m in mots]
        ids = set()
        for m in mots:
            while m["id"] in ids: m["id"] += "-2"
            ids.add(m["id"])
        e, a = controler(mots, lid[0] + "-", deja)
        erreurs += [f"[{lid}] {x}" for x in e]
        for x in a: print(f"  avertissement [{lid}] {x}")
        marque = re.compile(r"/\*mots:" + lid + r"\*/.*?/\*fin\*/", re.S)
        if len(marque.findall(page)) != 1:
            erreurs.append(f"[{lid}] marqueur absent ou multiple"); continue
        bloc = "/*mots:" + lid + "*/" + json.dumps(mots, ensure_ascii=False, separators=(",", ":")).replace("},{", "},\n{") + "/*fin*/"
        page = marque.sub(lambda _: bloc, page)
        n += len(mots)
        print(f"{lid} : {len(mots)} mots")
    if erreurs:
        print("\n".join(erreurs)); sys.exit(1)
    PAGE.write_text(page, encoding="utf-8")
    print(f"OK : {n} mots injectés dans {PAGE.relative_to(RACINE)}")

if __name__ == "__main__":
    main()
