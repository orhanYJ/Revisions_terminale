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
        sous="pH · couples · Brønsted", img="c1-citron.jpg",
        accroche="Un citron, du vinaigre, un détartrant : qu'ont-ils en commun, et que mesure vraiment le pH ?",
        exos=["Exercice 1 (pour démarrer) : l'acide lactique, son couple, [H₃O⁺] et réaction totale ou non.",
              "Exercice 2 (plus difficile) : deux flacons de même concentration, acide fort ou acide faible ?",
              "Exercice 3 (type bac) : l'acidité des pluies, à partir de documents."],
        tags=["acide base", "pH", "Brønsted", "couple acide base", "acide fort acide faible", "dilution pH",
              "transformations acides-bases", "physique chimie terminale", "spécialité physique chimie", "bac physique chimie",
              "cours terminale", "exercices corrigés"]),
    "ch2": dict(
        sous="absorbance · conductivité · infrarouge", img="c2-cuves.jpg",
        accroche="Comment doser un colorant sans en détruire une goutte ? En faisant passer de la lumière ou du courant.",
        exos=["Exercice 1 (pour démarrer) : un colorant alimentaire, loi de Beer-Lambert et étalonnage.",
              "Exercice 2 (plus difficile) : la conductivité d'une solution de chlorure de calcium, loi de Kohlrausch.",
              "Exercice 3 (type bac) : un sirop de menthe à deux colorants, à partir de documents."],
        tags=["loi de Beer-Lambert", "absorbance", "spectrophotométrie", "dosage par étalonnage", "conductivité",
              "loi de Kohlrausch", "spectroscopie infrarouge", "méthodes physiques d'analyse", "physique chimie terminale",
              "spécialité physique chimie", "bac physique chimie", "exercices corrigés"]),
    "ch3": dict(
        sous="équivalence · pH-métrie · conductimétrie", img="c3-chou.jpg",
        accroche="« 7 % » sur l'étiquette d'un vinaigre : comment le vérifier quand on ne peut pas compter les molécules ?",
        exos=["Exercice 1 (pour démarrer) : le titrage d'un comprimé d'aspirine par la soude.",
              "Exercice 2 (plus difficile) : l'acide sulfurique d'un électrolyte de batterie, de l'étiquette au titrage.",
              "Exercice 3 (type bac) : un détartrant à l'acide chlorhydrique, l'étiquette dit-elle vrai ?"],
        tags=["titrage", "dosage par titrage", "équivalence", "titrage pH-métrique", "titrage conductimétrique",
              "méthode des tangentes", "indicateur coloré", "méthodes chimiques d'analyse", "physique chimie terminale",
              "spécialité physique chimie", "bac physique chimie", "exercices corrigés"]),
    "ch4": dict(
        sous="E = hν · effet photoélectrique · cellules", img="c4-panneaux.jpg",
        accroche="Une calculatrice sans pile marche à la lumière : comment la lumière fabrique-t-elle un courant ?",
        exos=["Exercice 1 (pour démarrer) : l'énergie des photons d'une lampe germicide.",
              "Exercice 2 (plus difficile) : un pointeur laser vert et une cellule photoélectrique au césium.",
              "Exercice 3 (type bac) : un module photovoltaïque, une batterie et une DEL, rendement et bilan."],
        tags=["photon", "effet photoélectrique", "Einstein", "E = hν", "travail d'extraction", "niveaux d'énergie",
              "cellule photovoltaïque", "rendement", "physique chimie terminale", "spécialité physique chimie",
              "bac physique chimie", "exercices corrigés"]),
    "ch5": dict(
        sous="conjugaison · afocale · grossissement", img="c5-lune.jpg",
        accroche="Une lunette rapproche-t-elle vraiment la Lune ? Deux lentilles dans un tube, et tout s'explique.",
        exos=["Exercice 1 (pour démarrer) : vergence, focale et grossissement d'une lunette.",
              "Exercice 2 (plus difficile) : refaire le raisonnement du grossissement sur un astre de 0,50°.",
              "Exercice 3 (type bac) : une lunette 90/900 et le cratère Copernic, quel oculaire choisir ?"],
        tags=["lunette astronomique", "lentille convergente", "relation de conjugaison", "lunette afocale",
              "grossissement", "optique terminale", "physique chimie terminale", "spécialité physique chimie",
              "bac physique chimie", "exercices corrigés"]),
    "svt-ch4": dict(
        sous="symbiose · phénotype étendu · comportements", img="ch4-baleine.jpg",
        accroche="Un ver qui vit de la lumière, un gammare qui se jette dans le bec d'un oiseau, des baleines qui changent de chant : "
                 "des différences entre individus qui ne viennent pas de leurs gènes.",
        pill2="+ 2 exercices corrigés", exos_txt="deux exercices corrigés pas à pas : l'exploitation d'un graphique et une rédaction type bac",
        exos=["Exercice 1 : exploiter le graphique d'apprentissage d'un jeune chimpanzé (cassage de noix).",
              "Exercice 2 (type bac) : rédiger une synthèse sur la diversité non génétique du vivant."],
        tags=["hérédité non génétique", "symbiose", "mutualisme", "parasitisme", "phénotype étendu", "microbiote",
              "ver de Roscoff", "gammare", "chant des oiseaux", "baleine à bosse", "culture animale", "comportement inné acquis",
              "SVT terminale", "spécialité SVT", "bac SVT", "génétique et évolution"]),
    "maths-ch1": dict(
        sous="initialisation · hérédité · Bernoulli", img="m1-dominos.jpg", gros="La récurrence",
        accroche="n² + n + 41 est premier quarante fois de suite… puis plus du tout. Comment prouver qu'une propriété est vraie "
                 "pour tous les entiers, sans les vérifier un par un ?",
        pill2="+ 2 exercices corrigés", exos_txt="deux exercices corrigés pas à pas : une formule à démontrer et un sujet type bac",
        exos=["Exercice 1 (pour démarrer) : démontrer une formule explicite, u(n) = (n + 1)² + 1.",
              "Exercice 2 (type bac) : les abonnés d'une chaîne, encadrement par récurrence, suite auxiliaire et algorithme de seuil en Python."],
        tags=["raisonnement par récurrence", "récurrence", "initialisation hérédité", "démonstration par récurrence",
              "inégalité de Bernoulli", "suites", "toile d'araignée", "algorithme de seuil", "maths terminale",
              "spécialité maths", "bac maths", "exercices corrigés"]),
    "hggsp-t1-intro": dict(
        sous="mer · espace · dernières frontières", img="t1-rice.jpg", gros="Océans et espace",
        accroche="Le 2 août 2007, un drapeau russe est planté au fond de l'océan, sous le pôle Nord. Il n'a aucune valeur "
                 "juridique : pourquoi ? Océan et espace, deux espaces de conquête aux règles opposées.",
        pill2="+ dissertation et étude critique",
        exos_txt="une dissertation (« Les océans et l'espace sont-ils encore des dernières frontières ? ») et une étude critique "
                 "(le discours de Kennedy à l'université Rice, 1962), corrigées pas à pas",
        exos=["Dissertation : « Les océans et l'espace sont-ils encore des dernières frontières ? » (problématique et plan détaillé).",
              "Étude critique : le discours de J. F. Kennedy à l'université Rice, 12 septembre 1962 (présenter, analyser, critiquer)."],
        tags=["HGGSP", "HGGSP terminale", "spécialité HGGSP", "bac HGGSP", "nouveaux espaces de conquête", "océan et espace",
              "Montego Bay", "ZEE", "haute mer", "traité de l'espace 1967", "dernières frontières", "New Space",
              "syndrome de Kessler", "orbites", "mer de Chine méridionale", "dissertation HGGSP", "étude critique"]),
    "ses-e1": dict(
        titre_yt="La croissance économique : sources et défis · Cours complet + sujets corrigés | SES Terminale",
        sous="PGF · progrès endogène · destruction créatrice · soutenabilité", img="e1-pib.jpg", gros="La croissance",
        accroche="La France produit 8,6 fois plus qu'en 1950. D'où vient cette croissance, à qui profite-t-elle, "
                 "et peut-elle durer sur une planète finie ?",
        pill2="+ 5 sujets corrigés",
        exos_txt="cinq sujets corrigés pas à pas : un calcul sur le PIB, les trois parties de l'épreuve composée et une dissertation",
        exos=["Savoir-faire : calculer avec le PIB (coefficients multiplicateurs, taux de croissance, phrase de lecture) — données Insee.",
              "Partie 1 : « Montrez que les institutions peuvent favoriser la croissance économique » — sujet inventé pour le site.",
              "Partie 2 : la croissance française depuis 1950, document Insee — exercice du site.",
              "Partie 3 : « Montrez que l'innovation est une source de croissance économique » — sujet inventé pour le site.",
              "Dissertation : « Le progrès technique suffit-il à rendre la croissance soutenable ? » — sujet inventé pour le site."],
        tags=["croissance économique", "SES terminale", "spécialité SES", "bac SES", "productivité globale des facteurs",
              "résidu de Solow", "croissance endogène", "progrès technique", "destruction créatrice", "Schumpeter",
              "institutions", "droits de propriété", "inégalités", "croissance soutenable", "effet rebond",
              "épreuve composée", "dissertation SES"]),
}

# matière : libellés et couleurs de la miniature
MATIERE = {
    # identité « paillasse » des vidéos PC (11/2026) : fond clair, bleu-vert de labo, trait rose de phénolphtaléine
    "pc": dict(nom="Physique-chimie", court="PC", desc="physique-chimie", fond="#eef4f8", fond_rgb="238,244,248",
               acc="#0e8a8c", pill="#0e8a8c", pill_c="#fff", txt="#17323d", txt2="#4f6873", ombre="255,255,255",
               police="'Space Grotesk',sans-serif", sous_police="'Space Grotesk',sans-serif", sous_style="normal",
               pill2="background:#fff;color:#17323d;border:2px solid #d3e0e8", trait="#e0457b"),
    "svt": dict(nom="SVT", court="SVT", desc="SVT", fond="#0b120e", fond_rgb="11,18,14",
                acc="#B7D94C", pill="#B7D94C", pill_c="#0b120e", txt="#F1EFE3", txt2="#b8c9a8", ombre="0,0,0"),
    "maths": dict(nom="Maths", court="Maths", desc="maths", fond="#1b2422", fond_rgb="27,36,34",
                  acc="#F4D35E", pill="#F4D35E", pill_c="#1b2422", txt="#ECEBE4", txt2="#BFC4BB", ombre="0,0,0"),
    "ses": dict(nom="SES", court="SES", desc="SES", fond="#0D181C", fond_rgb="13,24,28",
                acc="#F0BE4F", pill="#FF7B65", pill_c="#14232A", txt="#ECE6DA", txt2="#A5B0B3", ombre="0,0,0"),
    "hggsp": dict(nom="HGGSP", court="HGGSP", desc="HGGSP", fond="#07090b", fond_rgb="7,9,11",
                  acc="#FF5B49", pill="#B3241B", pill_c="#FFF8F0", txt="#DCE3E8", txt2="#93A3AF", ombre="0,0,0"),
}


def episode(code):
    for site in ("pc", "svt", "philo", "maths", "ses", "hggsp"):
        f = os.path.join(RACINE, site, "serie", code + ".data.js")
        if os.path.exists(f):
            d = open(f, encoding="utf-8").read()
            return site, json.loads(d[d.index("=") + 1:].strip().rstrip(";"))
    sys.exit("épisode introuvable : " + code)


SUP = str.maketrans("0123456789-+−n", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺⁻ⁿ")
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


def plat(t):
    """Texte enrichi du moteur (10^-19, x^{2}, E_c, P_{reçue}, [[a|b]]) → texte simple pour YouTube."""
    t = re.sub(r"‾\{([^}]*)\}", "\\1", t)   # mesure algébrique : la barre ne passe pas en texte simple
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
    mt = MATIERE[site]
    titre = "%s · Cours complet + exercices corrigés | %s Terminale" % (ep["titre"], mt["nom"])
    if len(titre) > 100:
        titre = "%s · Cours + exercices corrigés | %s Terminale" % (ep["titre"], mt["court"])
    titre = m.get("titre_yt", titre)          # titre propre à la vidéo quand l'intitulé du chapitre est trop long (SES)
    assert len(titre) <= 100, titre
    duree = round(ep["dur"] / 60)
    desc = [
        m["accroche"],
        "",
        "Chapitre %d de %s de Terminale (spécialité) : « %s ». Tout le cours, en partant de zéro, "
        "avec les exemples, les méthodes et les pièges, puis %s. Environ %d minutes." % (
            ep["num"], mt["desc"], ep["titre"], m.get("exos_txt", "trois exercices corrigés pas à pas : un simple, "
                                                       "un plus difficile, un type bac"), duree),
        "",
        "Avant chaque correction, l'écran « À toi » t'invite à mettre la vidéo en pause et à chercher seul.",
        "",
        "CHAPITRES",
    ] + chapitres(ep) + [
        "",
        "LES EXERCICES" + ("" if site in ("svt", "ses", "maths", "hggsp") else " (inventés pour la vidéo)"),   # spécialités : exercices du site
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
    mt = MATIERE[site]
    return """<!doctype html><html lang="fr"><head><meta charset="utf-8">
<link rel="stylesheet" href="%(base)sfonts.css">
<style>
html,body{margin:0;width:1280px;height:720px;overflow:hidden;background:%(fond)s}
.img{position:absolute;right:0;top:0;width:760px;height:720px;background:url(%(base)simg/%(img)s) center/cover}
.img:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,%(fond)s 0%%,rgba(%(rgb)s,.85) 22%%,rgba(%(rgb)s,.15) 60%%,rgba(%(rgb)s,0) 100%%)}
.txt{position:absolute;left:70px;top:0;bottom:0;width:780px;display:flex;flex-direction:column;justify-content:center;color:%(txt)s;font-family:%(police)s}
.sur{font-weight:700;font-size:34px;letter-spacing:.08em;text-transform:uppercase;color:%(acc)s}
.gros{overflow:hidden;font-weight:700;font-size:132px;line-height:.95;padding-bottom:.14em;margin:22px 0 8px;letter-spacing:-.02em;text-shadow:0 4px 30px rgba(%(ombre)s,.6)}
.trait{width:260px;height:9px;border-radius:5px;background:%(trait)s;margin:4px 0 22px}
.sous{font-family:%(spol)s;font-style:%(sstyle)s;font-size:40px;color:%(txt2)s}
.bas{display:flex;gap:16px;margin-top:44px}
.pill{font-weight:700;font-size:30px;padding:12px 24px;border-radius:999px;background:%(pill)s;color:%(pillc)s}
.pill.c{%(pill2s)s}
.num{position:absolute;right:36px;bottom:24px;font-family:%(police)s;font-weight:700;font-size:30px;color:%(txt)s;background:rgba(%(rgb)s,.75);padding:8px 18px;border-radius:12px}
</style></head><body>
<div class="img"></div>
<div class="txt">
  <div class="sur">Terminale · %(mat)s · Ch. %(num)d</div>
  <div class="gros">%(gros)s</div>
%(trait_div)s  <div class="sous">%(sous)s</div>
  <div class="bas"><span class="pill">Cours complet</span><span class="pill c">%(pill2)s</span></div>
</div>
<div class="num">%(min)d min</div>
<script>/* titre trop large ou trop haut : on réduit la taille */var g=document.querySelector(".gros"),t=document.querySelector(".txt"),f=120;g.style.fontSize=f+"px";function trop(){var a=t.firstElementChild.getBoundingClientRect(),b=t.lastElementChild.getBoundingClientRect();return g.scrollWidth>g.clientWidth||a.top<40||b.bottom>650}while(trop()&&f>48){f-=4;g.style.fontSize=f+"px"}</script>
</body></html>""" % dict(base=base, img=m["img"], num=ep["num"], gros=e(m.get("gros", ep["titre"])).replace("-", "\u2011"), sous=e(m["sous"]),
                         min=round(ep["dur"] / 60), fond=mt["fond"], rgb=mt["fond_rgb"], txt=mt["txt"], txt2=mt["txt2"],
                         acc=mt["acc"], pill=mt["pill"], pillc=mt["pill_c"], mat=mt["nom"], pill2=e(m.get("pill2", "+ 3 exercices corrigés")),
                         police=mt.get("police", "Archivo,sans-serif"), spol=mt.get("sous_police", "Spectral,serif"), sstyle=mt.get("sous_style", "italic"),
                         ombre=mt.get("ombre", "0,0,0"), trait=mt.get("trait", "transparent"),
                         trait_div='  <div class="trait"></div>\n' if mt.get("trait") else "",
                         pill2s=mt.get("pill2", "background:rgba(242,231,218,.12);color:#f2e7da;border:2px solid rgba(242,231,218,.35)"))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    dossier = sys.argv[-1]
    for c in sys.argv[1:-1]:
        kit(c, dossier)
