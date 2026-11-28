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
        cles = {norm(f) for f in [m["w"]] + m["formes"] if len(norm(f)) > 2 and norm(f) not in ("the", "and", "for")}
        if any(re.search(r"(^|[^a-z])" + re.escape(c) + r"([^a-z]|$)", norm(m["def"])) for c in cles):
            avert.append(f"{q} : la définition contient le mot à trouver")
        for tr in m["trous"]:
            reste = norm(tr.get("s", "").replace("___", " "))
            vus = [c for c in cles if re.search(r"(^|[^a-z])" + re.escape(c) + r"([^a-z]|$)", reste)]
            if vus: avert.append(f"{q} : la phrase à trous laisse voir « {vus[0]} »")
        for e in m["ex"]:
            dedans = norm(re.search(r"\[\[(.+?)\]\]", e).group(1)) if "[[" in e else ""
            if dedans and not any(norm(f).split()[0] in dedans for f in m["formes"] + [m["w"]]):
                avert.append(f"{q} : exemple surligné « {dedans} » sans forme connue")
    return err, avert

def elargir_trous(m):
    """Pour une expression de plusieurs mots, le trou doit porter sur l'expression,
    pas sur un morceau : si une forme de l'expression se lit dans la phrase,
    (1) collée au trou ou le recouvrant, le trou est élargi à l'ensemble
    (« cope ___ » → « ___ », réponse « cope with ») ;
    (2) ailleurs dans la phrase, le trou passe sur l'expression et le mot
    d'origine est remis en clair (« feel like ___ out » → « ___ going out »)."""
    if len(m["w"].split()) < 2:
        return 0
    mots_w = m["w"].lower().replace("’", "'").split()
    sujets = {"i'd", "i", "we", "you", "it's", "it", "he", "she", "they", "there's", "if", "as", "when", "in", "to", "on", "at", "by", "for", "all", "no"}
    def plausible(f):
        p0 = f.lower().split()[0]
        return p0 in mots_w or p0 in sujets or p0[0] == mots_w[0][0]
    formes = sorted({f for f in m["formes"] if len(f.split()) >= 2 and plausible(f)}, key=len, reverse=True)
    petits = {w for w in mots_w}
    n = 0
    for tr in m["trous"]:
        i = tr["s"].index("___")
        complet = tr["s"][:i] + tr["a"] + tr["s"][i + 3:]
        bas = complet.lower()
        j = i + len(tr["a"])                       # fin de la réponse dans la phrase complète
        trouve = None
        for f in formes:
            fl = f.lower()
            k = bas.find(fl)
            while k >= 0:
                fin = k + len(fl)
                if (k == 0 or not bas[k - 1].isalpha()) and (fin == len(bas) or not bas[fin].isalpha()):
                    trouve = (k, fin); break
                k = bas.find(fl, k + 1)
            if trouve: break
        if not trouve:
            continue
        k, fin = trouve
        if k <= i and fin >= j:                    # l'expression recouvre déjà la réponse
            d, e = k, fin
        elif fin <= i and complet[fin:i].strip() == "":                     # expression juste avant
            d, e = (k, j) if tr["a"].lower() in petits else (k, fin)
        elif k >= j and complet[j:k].strip() == "":                         # expression juste après
            d, e = (i, fin) if tr["a"].lower() in petits else (k, fin)
        elif k < i or k > j:                       # ailleurs : le trou passe sur l'expression
            d, e = k, fin
        else:
            continue
        alts = []
        if d <= i and e >= j:                      # les variantes suivent l'élargissement
            for x in tr.get("alt", []):
                cx = tr["s"][:i] + x + tr["s"][i + 3:]
                alts.append(cx[d:e + len(x) - len(tr["a"])])
        tr["s"] = complet[:d] + "___" + complet[e:]
        tr["a"] = complet[d:e]
        tr.pop("alt", None)
        if alts: tr["alt"] = alts
        n += 1
    return n

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
        elargis = sum(elargir_trous(m) for m in mots)
        if elargis: print(f"  {lid} : {elargis} trous élargis à l'expression entière")
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
