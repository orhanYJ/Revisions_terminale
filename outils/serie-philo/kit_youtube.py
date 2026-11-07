#!/usr/bin/env python3
"""Kit de publication YouTube d'une vidéo de la série (à côté du MP4 fait par video.js).

Usage (depuis la racine du dépôt) :
    python3 outils/serie-philo/kit_youtube.py ch1 DOSSIER [ch2 ...]

Écrit dans DOSSIER, pour chaque code :
  <code>-youtube.txt  titre, description (chapitres horodatés, exercices, crédits), tags, commentaire épinglé (quiz)
  <code>.fr.srt       sous-titres français (repris de la piste `sous` du lecteur, lignes longues découpées)
  <code>-miniature.html  page 1280 × 720 de la miniature (la capture PNG est faite par miniature.js)
Les métadonnées propres à chaque vidéo (titre court, accroche, exercices, tags, image) sont dans META.
"""
import json, os, re, sys, html

RACINE = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))

META = {
    "ch1": dict(
        gros="Acides & bases", sous="pH · couples · Brønsted", img="c1-citron.jpg",
        accroche="Un citron, du vinaigre, un détartrant : qu'ont-ils en commun, et que mesure vraiment le pH ?",
        exos=["Exercice 1 (pour démarrer) : l'acide lactique, son couple et le pH de sa solution.",
              "Exercice 2 (plus difficile) : deux flacons de même concentration, acide fort ou acide faible ?",
              "Exercice 3 (type bac) : l'acidité des pluies, à partir de documents."],
        tags=["acide base", "pH", "Brønsted", "couple acide base", "acide fort acide faible", "dilution pH",
              "transformations acides-bases", "physique chimie terminale", "spécialité physique chimie", "bac physique chimie",
              "cours terminale", "exercices corrigés"]),
    "ch2": dict(
        gros="Beer-Lambert", sous="absorbance · conductivité · infrarouge", img="c2-cuves.jpg",
        accroche="Comment doser un colorant sans en détruire une goutte ? En faisant passer de la lumière ou du courant.",
        exos=["Exercice 1 (pour démarrer) : un colorant alimentaire, loi de Beer-Lambert et étalonnage.",
              "Exercice 2 (plus difficile) : la conductivité d'une solution de chlorure de calcium, loi de Kohlrausch.",
              "Exercice 3 (type bac) : un sirop de menthe à deux colorants, à partir de documents."],
        tags=["loi de Beer-Lambert", "absorbance", "spectrophotométrie", "dosage par étalonnage", "conductivité",
              "loi de Kohlrausch", "spectroscopie infrarouge", "méthodes physiques d'analyse", "physique chimie terminale",
              "spécialité physique chimie", "bac physique chimie", "exercices corrigés"]),
    "ch3": dict(
        gros="Le titrage", sous="équivalence · pH-métrie · conductimétrie", img="c3-chou.jpg",
        accroche="« 7 % » sur l'étiquette d'un vinaigre : comment le vérifier quand on ne peut pas compter les molécules ?",
        exos=["Exercice 1 (pour démarrer) : le titrage d'un comprimé d'aspirine par la soude.",
              "Exercice 2 (plus difficile) : l'acide sulfurique d'un électrolyte de batterie, de l'étiquette au titrage.",
              "Exercice 3 (type bac) : un détartrant à l'acide chlorhydrique, l'étiquette dit-elle vrai ?"],
        tags=["titrage", "dosage par titrage", "équivalence", "titrage pH-métrique", "titrage conductimétrique",
              "méthode des tangentes", "indicateur coloré", "méthodes chimiques d'analyse", "physique chimie terminale",
              "spécialité physique chimie", "bac physique chimie", "exercices corrigés"]),
    "ch4": dict(
        gros="Le photon", sous="E = hν · effet photoélectrique · cellules", img="c4-panneaux.jpg",
        accroche="Une calculatrice sans pile marche à la lumière : comment la lumière fabrique-t-elle un courant ?",
        exos=["Exercice 1 (pour démarrer) : l'énergie des photons d'une lampe germicide.",
              "Exercice 2 (plus difficile) : un pointeur laser vert et une cellule photoélectrique au césium.",
              "Exercice 3 (type bac) : un module photovoltaïque, une batterie et une DEL, rendement et bilan."],
        tags=["photon", "effet photoélectrique", "Einstein", "E = hν", "travail d'extraction", "niveaux d'énergie",
              "cellule photovoltaïque", "rendement", "physique chimie terminale", "spécialité physique chimie",
              "bac physique chimie", "exercices corrigés"]),
    "ch5": dict(
        gros="La lunette", sous="conjugaison · afocale · grossissement", img="c5-lune.jpg",
        accroche="Une lunette rapproche-t-elle vraiment la Lune ? Deux lentilles dans un tube, et tout s'explique.",
        exos=["Exercice 1 (pour démarrer) : vergence, focale et grossissement d'une lunette.",
              "Exercice 2 (plus difficile) : refaire le raisonnement du grossissement sur un astre de 0,50°.",
              "Exercice 3 (type bac) : une lunette 90/900 et le cratère Copernic, quel oculaire choisir ?"],
        tags=["lunette astronomique", "lentille convergente", "relation de conjugaison", "lunette afocale",
              "grossissement", "optique terminale", "physique chimie terminale", "spécialité physique chimie",
              "bac physique chimie", "exercices corrigés"]),
}


def episode(code):
    for site in ("pc", "philo"):
        f = os.path.join(RACINE, site, "serie", code + ".data.js")
        if os.path.exists(f):
            d = open(f, encoding="utf-8").read()
            return site, json.loads(d[d.index("=") + 1:].strip().rstrip(";"))
    sys.exit("épisode introuvable : " + code)


SUP = str.maketrans("0123456789-+−n", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺⁻ⁿ")
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


def plat(t):
    """Texte enrichi du moteur (10^-19, x^{2}, E_c, P_{reçue}, [[a|b]]) → texte simple pour YouTube."""
    t = re.sub(r"\[\[(.+?)\|(.+?)\]\]", lambda m: "%s/%s" % tuple(x if re.fullmatch(r"[\w,.]+", x) else "(%s)" % x for x in m.groups()), t)
    def sup(m):
        x = m.group(1) or m.group(2)
        return x.translate(SUP) if all(c in "0123456789-+−n" for c in x) else "^" + x
    t = re.sub(r"\^\{([^}]*)\}|\^([-+−]?\d+|n)", sup, t)
    def sub(m):
        x = m.group(1) or m.group(2)
        return x.translate(SUB) if x.isdigit() else "_" + x
    t = re.sub(r"_\{([^}]*)\}|_(\w+)", sub, t)
    return t


def hms(t, srt=False):
    t = max(0.0, t)
    h, r = divmod(t, 3600)
    m, s = divmod(r, 60)
    if srt:
        ms = int(round((s - int(s)) * 1000))
        if ms == 1000:
            s, ms = int(s) + 1, 0
        return "%02d:%02d:%02d,%03d" % (h, m, int(s), ms)
    return ("%d:%02d:%02d" % (h, m, int(s))) if h else ("%d:%02d" % (m, int(s)))


def decouper(t0, t1, txt, maxc=90):
    """Découpe une ligne trop longue en phrases (puis en morceaux), le temps au prorata des caractères."""
    if len(txt) <= maxc:
        return [(t0, t1, txt)]
    morceaux = re.split(r"(?<=[.!?…:;»])\s+", txt)
    out = []
    for m in morceaux:
        while len(m) > maxc:
            i = m.rfind(" ", 0, maxc)
            i = i if i > 20 else maxc
            out.append(m[:i].strip()); m = m[i:].strip()
        if m:
            out.append(m)
    # regroupe les morceaux trop courts
    res = []
    for m in out:
        if res and len(res[-1]) + len(m) + 1 <= maxc:
            res[-1] += " " + m
        else:
            res.append(m)
    tot = sum(len(m) for m in res)
    t, lignes = t0, []
    for m in res:
        d = (t1 - t0) * len(m) / tot
        lignes.append((t, t + d, m)); t += d
    return lignes


def srt(ep):
    lignes = []
    for t0, t1, txt in ep["sous"]:
        lignes += decouper(t0, t1, re.sub(r"\s+", " ", txt).strip())
    out = []
    for i, (a, b, txt) in enumerate(lignes, 1):
        out.append("%d\n%s --> %s\n%s\n" % (i, hms(a, True), hms(b, True), txt))
    return "\n".join(out)


def chapitres(ep):
    vus, out = set(), []
    for s in ep["scenes"]:
        c = s.get("chap")
        if not c or c in vus:
            continue
        vus.add(c)
        out.append([s["t0"], c])
    out[0][0] = 0  # YouTube exige un premier chapitre à 0:00
    return ["%s %s" % (hms(t), c) for t, c in out]


def kit(code, dossier):
    site, ep = episode(code)
    m = META[code]
    titre = "%s · Cours complet + exercices corrigés | Physique-chimie Terminale" % ep["titre"]
    if len(titre) > 100:
        titre = "%s · Cours + exercices corrigés | PC Terminale" % ep["titre"]
    assert len(titre) <= 100, titre
    duree = round(ep["dur"] / 60)
    desc = [
        m["accroche"],
        "",
        "Chapitre %d de physique-chimie de Terminale (spécialité) : « %s ». Tout le cours, en partant de zéro, "
        "avec les exemples, les méthodes et les pièges, puis trois exercices corrigés pas à pas : un simple, "
        "un plus difficile, un type bac. Environ %d minutes." % (ep["num"], ep["titre"], duree),
        "",
        "Avant chaque correction, l'écran « À toi » t'invite à mettre la vidéo en pause et à chercher seul.",
        "",
        "CHAPITRES",
    ] + chapitres(ep) + [
        "",
        "LES EXERCICES (inventés pour la vidéo)",
    ] + m["exos"] + [
        "",
        "Le quiz de fin est dans le commentaire épinglé.",
        "",
        "CRÉDITS",
    ] + ep.get("credits", []) + [
        "Voix de synthèse ; musique originale composée pour la série.",
    ]
    desc_txt = "\n".join(desc)
    assert len(desc_txt) < 5000, len(desc_txt)
    tags = m["tags"]
    assert len(", ".join(tags)) < 500
    # commentaire épinglé : le quiz (questions puis réponses, pour chercher avant de lire)
    q, r = ["QUIZ · %d questions pour vérifier que tu as tout compris" % len(ep["quiz"]), ""], ["", "RÉPONSES"]
    for i, x in enumerate(ep["quiz"], 1):
        q.append("%d. %s" % (i, plat(x["q"])))
        for j, rep in enumerate(x["r"]):
            q.append("   %s) %s" % ("abcd"[j], plat(rep)))
        r.append(plat("%d. %s) %s. %s Revoir : %s" % (i, "abcd"[x["ok"]], x["r"][x["ok"]], x.get("ex", ""), hms(x["voir"]))))
    comm = "\n".join(q + r)
    blocs = [
        "TITRE (%d caractères)" % len(titre), titre, "",
        "DESCRIPTION (%d caractères)" % len(desc_txt), desc_txt, "",
        "TAGS", ", ".join(tags), "",
        "COMMENTAIRE ÉPINGLÉ (%d caractères)" % len(comm), comm, "",
        "RÉGLAGES CONSEILLÉS",
        "Catégorie : Éducation. Langue de la vidéo : français. Public : « Non, elle n'est pas conçue pour les enfants ».",
        "Sous-titres : importer %s.fr.srt (français)." % code,
        "Miniature : %s-miniature.png (1280 × 720)." % code,
        "Contenu synthétique : la voix est une voix de synthèse qui n'imite aucune personne réelle ; "
        "à déclarer si YouTube le demande (case « contenu modifié ou synthétique »).",
    ]
    os.makedirs(dossier, exist_ok=True)
    open(os.path.join(dossier, code + "-youtube.txt"), "w", encoding="utf-8").write("\n".join(blocs) + "\n")
    open(os.path.join(dossier, code + ".fr.srt"), "w", encoding="utf-8").write(srt(ep))
    open(os.path.join(dossier, code + "-miniature.html"), "w", encoding="utf-8").write(miniature(site, ep, m))
    print("%s : %s · %d chapitres · %d sous-titres" % (code, titre, len(chapitres(ep)), srt(ep).count("-->")))


def miniature(site, ep, m):
    base = "http://localhost:8765/%s/serie/" % site
    e = html.escape
    return """<!doctype html><html lang="fr"><head><meta charset="utf-8">
<link rel="stylesheet" href="%(base)sfonts.css">
<style>
html,body{margin:0;width:1280px;height:720px;overflow:hidden;background:#17100a}
.img{position:absolute;right:0;top:0;width:760px;height:720px;background:url(%(base)simg/%(img)s) center/cover}
.img:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,#17100a 0%%,rgba(23,16,10,.85) 22%%,rgba(23,16,10,.15) 60%%,rgba(23,16,10,0) 100%%)}
.txt{position:absolute;left:70px;top:0;bottom:0;width:780px;display:flex;flex-direction:column;justify-content:center;color:#f2e7da;font-family:Archivo,sans-serif}
.sur{font-weight:700;font-size:34px;letter-spacing:.08em;text-transform:uppercase;color:#ff8b3e}
.gros{overflow:hidden;font-weight:700;font-size:132px;line-height:.95;margin:22px 0 22px;letter-spacing:-.02em;text-shadow:0 4px 30px rgba(0,0,0,.6)}
.sous{font-family:Spectral,serif;font-style:italic;font-size:40px;color:#cbb49c}
.bas{display:flex;gap:16px;margin-top:44px}
.pill{font-weight:700;font-size:30px;padding:12px 24px;border-radius:999px;background:#e45c10;color:#fff}
.pill.c{background:rgba(242,231,218,.12);color:#f2e7da;border:2px solid rgba(242,231,218,.35)}
.num{position:absolute;right:36px;bottom:24px;font-family:'Archivo',sans-serif;font-weight:700;font-size:30px;color:#f2e7da;background:rgba(23,16,10,.75);padding:8px 18px;border-radius:12px}
</style></head><body>
<div class="img"></div>
<div class="txt">
  <div class="sur">Terminale · Physique-chimie · Ch. %(num)d</div>
  <div class="gros">%(gros)s</div>
  <div class="sous">%(sous)s</div>
  <div class="bas"><span class="pill">Cours complet</span><span class="pill c">+ 3 exercices corrigés</span></div>
</div>
<div class="num">%(min)d min</div>
<script>/* titre trop large : on réduit la taille */var g=document.querySelector(".gros"),f=132;while(g.scrollWidth>g.clientWidth&&f>60){f-=4;g.style.fontSize=f+"px"}</script>
</body></html>""" % dict(base=base, img=m["img"], num=ep["num"], gros=e(m["gros"]).replace("-", "\u2011"), sous=e(m["sous"]),
                         min=round(ep["dur"] / 60))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    dossier = sys.argv[-1]
    for c in sys.argv[1:-1]:
        kit(c, dossier)
