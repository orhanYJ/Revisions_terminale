#!/usr/bin/env python3
"""Kit de publication YouTube des séries d'histoire (un MP4 par chapitre, épisodes bout à bout).

Usage (depuis la racine du dépôt) :
    python3 outils/serie-dnl/kit_youtube_dnl.py DOSSIER H3-en [H1-en H2-en-1 …]

Pour chaque vidéo (clé de KITS), écrit dans DOSSIER :
  <clé>-youtube.txt      titre, description (chapitres horodatés, crédits), tags, commentaire épinglé (quiz du récap)
  <clé>.<langue>.srt     sous-titres (pistes `sous` des épisodes, décalées comme dans le MP4)
  <clé>-miniature.html   miniature 1280 × 720 (capture PNG : outils/serie-philo/miniature.js DOSSIER <clé>)
Le MP4 est fait à part (video.js par épisode, puis assemblage sans le générique de 5,6 s de chaque épisode) :
les horodatages supposent ce montage.

Miniature propre à l'histoire-géographie (distincte de SVT, PC, philo, ACL) : photo d'archive virée sépia sous un
quadrillage de carte, fiche de papier déchirée à gauche, titre en capitales, tampon rouge des dates, onglet de langue.
"""
import html, json, os, re, sys

RACINE = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
SERIE = os.path.join(RACINE, "dnl", "serie")

TXT = {
    "en": dict(
        mat="History", sur="Terminale · History · Ch. %d", ep="Episode", eps="episodes", part="Part %d/%d",
        titre="%s · The full chapter in %d episodes | DNL History Terminale",
        titre_p="%s (Part %d/%d) · Episodes %s | DNL History Terminale",
        intro=("The whole chapter %d of Terminale history, in English (DNL / European section): « %s ». %s "
               "Animated maps, archive images, key dates, figures and documents. About %s."),
        pause="In each episode, the « Your turn » screens invite you to pause the video and write your answer before the correction.",
        chap="CHAPTERS", cred="CREDITS", voix="Synthetic voices generated locally; original music composed for the series.",
        quiz="QUIZ · %d questions on the whole chapter (from the recap)", rep="ANSWERS", revoir="Rewatch: %s",
        reglages=["Category: Education. Video language: English. Audience: « No, it's not made for kids ».",
                  "Subtitles: upload %s.en.srt (English).", "Thumbnail: %s-miniature.png (1280 × 720).",
                  "Altered or synthetic content: the narration is a synthetic voice that imitates no real person; "
                  "declare it if YouTube asks."],
        pills=("%d episodes · %s", "Essay & DBQ")),
    "fr": dict(
        mat="Histoire", sur="Terminale · Histoire · Ch. %d", ep="Épisode", eps="épisodes", part="Partie %d/%d",
        titre="%s · Le chapitre complet en %d épisodes | Histoire Terminale",
        titre_p="%s (partie %d/%d) · Épisodes %s | Histoire Terminale",
        intro=("Tout le chapitre %d d'histoire de Terminale : « %s ». %s "
               "Cartes animées, images d'archives, dates, chiffres et documents clés. Environ %s."),
        pause="Dans chaque épisode, les écrans « À toi » t'invitent à mettre la vidéo en pause et à rédiger ta réponse avant la correction.",
        chap="CHAPITRES", cred="CRÉDITS", voix="Voix de synthèse générées localement ; musique originale composée pour la série.",
        quiz="QUIZ · %d questions sur tout le chapitre (tirées du récap)", rep="RÉPONSES", revoir="Revoir : %s",
        reglages=["Catégorie : Éducation. Langue de la vidéo : français. Public : « Non, elle n'est pas conçue pour les enfants ».",
                  "Sous-titres : importer %s.fr.srt (français).", "Miniature : %s-miniature.png (1280 × 720).",
                  "Contenu synthétique : la voix est une voix de synthèse qui n'imite aucune personne réelle ; "
                  "à déclarer si YouTube le demande."],
        pills=("%d épisodes · %s", "Composition & analyse de doc")),
}

CHAPITRES = {
    "H1": dict(num=1, dates="1929 – 1939", img="h1-wallstreet.jpg",
               gros={"en": "The Great Crash", "fr": "Le krach de 1929"},
               plan={"en": "Six episodes: the crash, the world crisis and its trauma, economic nationalism and political "
                           "answers, the democracies and the liberal order, then the essay and the DBQ, and a recap.",
                     "fr": "Six épisodes : le krach, la crise mondiale et le traumatisme, le nationalisme économique et les "
                           "réponses politiques, les démocraties et l'ordre libéral, puis la méthode (question problématisée, "
                           "analyse de document) et un récap."},
               tags={"en": ["Wall Street Crash", "1929 crash", "Great Depression", "New Deal", "Roosevelt", "Dawes Plan",
                            "economic nationalism", "1930s crisis", "DNL history", "European section", "history in English",
                            "Terminale history", "bac history", "essay DBQ"],
                     "fr": ["krach de 1929", "crise de 1929", "Grande Dépression", "New Deal", "Roosevelt", "plan Dawes",
                            "crise des années 1930", "histoire terminale", "bac histoire", "histoire géographie",
                            "question problématisée", "analyse de document", "cours complet"]}),
    "H2": dict(num=2, dates="1914 – 1939", img="h2-nuremberg-1936.jpg",
               gros={"en": "Totalitarian Regimes", "fr": "Les régimes totalitaires"},
               plan={"en": "Nine episodes: defining totalitarianism, from the Great War to power, three regimes and three "
                           "ideologies, the leader and the New Man, mass terror, hegemonic ambitions, appeasement and the "
                           "road to war, then the essay and the DBQ, and a recap.",
                     "fr": "Neuf épisodes : définir le totalitarisme, de la Grande Guerre au pouvoir, trois régimes et trois "
                           "idéologies, le chef et l'homme nouveau, la terreur de masse, les ambitions hégémoniques, "
                           "l'apaisement et la marche à la guerre, puis la méthode et un récap."},
               tags={"en": ["totalitarianism", "totalitarian regimes", "Nazism", "Stalinism", "Fascism", "Hitler", "Stalin",
                            "Mussolini", "appeasement", "Munich 1938", "DNL history", "European section",
                            "history in English", "Terminale history", "bac history", "essay DBQ"],
                     "fr": ["totalitarisme", "régimes totalitaires", "nazisme", "stalinisme", "fascisme", "Hitler", "Staline",
                            "Mussolini", "apaisement", "Munich 1938", "histoire terminale", "bac histoire",
                            "histoire géographie", "question problématisée", "analyse de document", "cours complet"]}),
    "H3": dict(num=3, dates="1939 – 1945", img="h3-blitz.jpg",
               gros={"en": "World War Two", "fr": "La Seconde Guerre mondiale"},
               plan={"en": "Seven episodes: a world war, the fall of France, Britain alone, Barbarossa and the war of "
                           "annihilation, towards the genocide, then the essay and the DBQ, and a recap.",
                     "fr": "Sept épisodes : une guerre mondiale, la défaite de la France, le Royaume-Uni seul, Barbarossa "
                           "et la guerre d'anéantissement, vers le génocide, puis la méthode et un récap."},
               tags={"en": ["World War Two", "WWII", "Second World War", "fall of France", "Blitz", "Barbarossa", "Stalingrad",
                            "Holocaust", "Shoah", "Vichy", "DNL history", "European section", "history in English",
                            "Terminale history", "bac history", "essay DBQ"],
                     "fr": ["Seconde Guerre mondiale", "Deuxième Guerre mondiale", "1939-1945", "défaite de 1940", "Vichy",
                            "Blitz", "Barbarossa", "Stalingrad", "Shoah", "génocide des Juifs", "histoire terminale",
                            "bac histoire", "histoire géographie", "question problématisée", "analyse de document"]}),
}

# clé → (chapitre, langue, épisodes, partie, nombre de parties)
KITS = {
    "H1-en": ("H1", "en", ["h1-%d" % i for i in range(1, 7)], 0, 0),
    "H2-en-1": ("H2", "en", ["h2-%d" % i for i in range(1, 5)], 1, 2),
    "H2-en-2": ("H2", "en", ["h2-%d" % i for i in range(5, 10)], 2, 2),
    "H3-en": ("H3", "en", ["h3-%d" % i for i in range(1, 8)], 0, 0),
    "H1-fr": ("H1", "fr", ["h1f-%d" % i for i in range(1, 7)], 0, 0),
    "H2-fr-1": ("H2", "fr", ["h2f-%d" % i for i in range(1, 5)], 1, 2),
    "H2-fr-2": ("H2", "fr", ["h2f-%d" % i for i in range(5, 10)], 2, 2),
    "H3-fr": ("H3", "fr", ["h3f-%d" % i for i in range(1, 8)], 0, 0),
}


def episode(code):
    d = open(os.path.join(SERIE, code + ".data.js"), encoding="utf-8").read()
    return json.loads(d[d.index("=") + 1:].strip().rstrip(";"))


def generique(ep):
    return max((v["t1"] for v in ep["vis"] if v["type"] == "generique"), default=0.0)


def hms(t, srt=False):
    t = max(0.0, t)
    h, r = divmod(t, 3600)
    m, s = divmod(r, 60)
    if srt:
        ms = min(999, int(round((s - int(s)) * 1000)))
        return "%02d:%02d:%02d,%03d" % (h, m, int(s), ms)
    return ("%d:%02d:%02d" % (h, m, int(s))) if h else ("%d:%02d" % (m, int(s)))


def decouper(t0, t1, txt, maxc=90):
    if len(txt) <= maxc:
        return [(t0, t1, txt)]
    out = []
    for m in re.split(r"(?<=[.!?…:;»”])\s+", txt):
        while len(m) > maxc:
            i = m.rfind(" ", 0, maxc)
            i = i if i > 20 else maxc
            out.append(m[:i].strip()); m = m[i:].strip()
        if m:
            out.append(m)
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


def plat(t):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", str(t))).strip()


def duree_txt(s, lang):
    h, m = divmod(round(s / 60), 60)
    if lang == "fr":
        return ("%d h %02d" % (h, m)) if h else ("%d min" % m)
    return ("%d h %02d min" % (h, m)) if h else ("%d min" % m)


def kit(cle, dossier):
    chap, lang, codes, part, nparts = KITS[cle]
    C, T = CHAPITRES[chap], TXT[lang]
    eps = [(c, episode(c)) for c in codes]
    notion = eps[0][1]["notion"]
    # décalages : chaque épisode commence après le générique coupé
    off, t, lignes_ch, sous, credits, vus = [], 0.0, [], [], [], set()
    for c, ep in eps:
        g = generique(ep)
        off.append(t - g)
        n = int(c.split("-")[-1])
        lignes_ch.append((t, "%s %d · %s" % (T["ep"], n, ep["titre"]), []))
        for s in ep["scenes"]:
            if s.get("chap") and s["t0"] > g + 20:
                lignes_ch[-1][2].append((t - g + s["t0"], s["chap"]))
        for a, b, x in ep["sous"]:
            if b > g:
                for l in decouper(max(a, g) - g + t, b - g + t, plat(x)):
                    sous.append(l)
        for cr in ep.get("credits", []):
            if re.match(r"(Photo|Image|Poster|Affiche|Painting|Tableau|Cartoon|Caricature|Map|Carte|Archive)", cr) and cr not in vus:
                vus.add(cr); credits.append(cr)
        t += ep["dur"] - g
    total = t
    if part:
        nums = "%d–%d" % (int(codes[0].split("-")[-1]), int(codes[-1].split("-")[-1]))
        titre = T["titre_p"] % (notion, part, nparts, nums)
    else:
        titre = T["titre"] % (notion, len(codes))
    assert len(titre) <= 100, (len(titre), titre)

    def chapitres(detail):
        out = []
        for t0, nom, sc in lignes_ch:
            out.append("%s %s" % (hms(t0), nom))
            if detail:
                for ts, n in sc:
                    out.append("%s   %s" % (hms(ts), n))
        out[0] = "0:00" + out[0][out[0].index(" "):]
        return out

    contenu = ("Content: the DNL History course of Terminale, as written on the revision site; animated maps of the site."
               if lang == "en" else
               "Contenu : le cours d'histoire de Terminale, tel qu'il est rédigé sur le site de révision ; cartes animées du site.")
    for detail in (True, False):
        desc = [T["intro"] % (C["num"], notion, C["plan"][lang], duree_txt(total, lang)), "", T["pause"], "",
                T["chap"]] + chapitres(detail) + ["", T["cred"], contenu] + credits + [T["voix"]]
        desc_txt = "\n".join(desc)
        if len(desc_txt) < 5000:
            break
    if len(desc_txt) >= 5000:  # crédits d'images abrégés en dernier recours
        desc = desc[:desc.index(T["cred"]) + 2] + [T["voix"]]
        desc_txt = "\n".join(desc)
    assert len(desc_txt) < 5000, len(desc_txt)
    tags = C["tags"][lang]
    assert len(", ".join(tags)) < 500
    # commentaire épinglé : le quiz du récap (dernier épisode de la série), questions puis réponses
    rc, rep = eps[-1][1], eps[-1]
    q = [T["quiz"] % len(rc["quiz"]), ""]
    r = ["", T["rep"]]
    for i, x in enumerate(rc["quiz"], 1):
        q.append("%d. %s" % (i, plat(x["q"])))
        for j, rr in enumerate(x["r"]):
            q.append("   %s) %s" % ("abcd"[j], plat(rr)))
        voir = x.get("voir", 0) + off[-1]
        r.append("%d. %s) %s. %s %s" % (i, "abcd"[x["ok"]], plat(x["r"][x["ok"]]), plat(x.get("ex", "")),
                                        T["revoir"] % hms(voir)))
    comm = "\n".join(q + r)
    blocs = ["TITRE (%d caractères)" % len(titre), titre, "",
             "DESCRIPTION (%d caractères)" % len(desc_txt), desc_txt, "",
             "TAGS", ", ".join(tags), "",
             "COMMENTAIRE ÉPINGLÉ (%d caractères)" % len(comm), comm, "",
             "RÉGLAGES CONSEILLÉS"] + [x % cle if "%s" in x else x for x in T["reglages"]]
    os.makedirs(dossier, exist_ok=True)
    open(os.path.join(dossier, cle + "-youtube.txt"), "w", encoding="utf-8").write("\n".join(blocs) + "\n")
    srt = "\n".join("%d\n%s --> %s\n%s\n" % (i, hms(a, True), hms(b, True), x) for i, (a, b, x) in enumerate(sous, 1))
    open(os.path.join(dossier, "%s.%s.srt" % (cle, lang)), "w", encoding="utf-8").write(srt)
    open(os.path.join(dossier, cle + "-miniature.html"), "w", encoding="utf-8").write(
        miniature(C, T, lang, len(codes) if not part else len(codes), duree_txt(total, lang), part, nparts, codes))
    print("%s : %s · %s · %d lignes de chapitres · %d sous-titres · description %d" % (
        cle, titre, duree_txt(total, lang), len(chapitres(detail)), len(sous), len(desc_txt)))


def miniature(C, T, lang, n, duree, part, nparts, codes):
    base = "http://localhost:8765/dnl/serie/"
    e = html.escape
    pill1 = T["pills"][0] % (n, duree)
    if part:
        pill1 = "%s · %s" % (T["part"] % (part, nparts), pill1)
    gros = e(C["gros"][lang])
    return """<!doctype html><html lang="%(lang)s"><head><meta charset="utf-8">
<link rel="stylesheet" href="%(base)sfonts.css">
<style>
html,body{margin:0;width:1280px;height:720px;overflow:hidden;background:#15130f}
.photo{position:absolute;inset:0 0 0 380px;background:url(%(base)simg/%(img)s) center/cover;
  filter:grayscale(1) sepia(.55) contrast(1.12) brightness(.92)}
.photo:after{content:"";position:absolute;inset:0;
  background:radial-gradient(ellipse at 70%% 45%%,rgba(0,0,0,0) 35%%,rgba(10,8,5,.65) 100%%)}
.grille{position:absolute;inset:0;
  background-image:linear-gradient(rgba(240,228,200,.10) 1px,transparent 1px),linear-gradient(90deg,rgba(240,228,200,.10) 1px,transparent 1px);
  background-size:80px 80px}
.fiche{position:absolute;left:0;top:0;bottom:0;width:700px;background:#efe5cf;
  background-image:radial-gradient(rgba(120,90,40,.10) 1px,transparent 1.5px);background-size:7px 7px;
  clip-path:polygon(0 0,100%% 0,96%% 7%%,99%% 15%%,95%% 24%%,98.5%% 33%%,94.5%% 43%%,98%% 52%%,95%% 61%%,99%% 70%%,95.5%% 80%%,98%% 89%%,96%% 100%%,0 100%%);
  filter:drop-shadow(10px 0 18px rgba(0,0,0,.55))}
.txt{position:absolute;left:62px;top:0;bottom:0;width:590px;display:flex;flex-direction:column;justify-content:center}
.sur{font-family:'JetBrains Mono',monospace;font-weight:700;font-size:25px;letter-spacing:.12em;text-transform:uppercase;color:#1f3a5f}
.trait{width:120px;height:5px;background:#a3241f;margin:18px 0 22px}
.gros{font-family:Archivo,sans-serif;font-weight:800;font-size:112px;line-height:.92;letter-spacing:-.01em;text-transform:uppercase;color:#1b1a17}
.bas{display:flex;flex-wrap:wrap;gap:12px;margin-top:40px}
.pill{font-family:Archivo,sans-serif;font-weight:700;font-size:25px;padding:10px 20px;border-radius:6px;background:#1f3a5f;color:#f4ecda}
.pill.c{background:transparent;color:#1f3a5f;border:3px solid #1f3a5f}
.tampon{position:absolute;right:70px;bottom:78px;transform:rotate(-7deg);font-family:'JetBrains Mono',monospace;font-weight:700;
  font-size:64px;color:#c8332b;border:7px solid #c8332b;border-radius:10px;padding:8px 26px;letter-spacing:.02em;
  background:rgba(239,229,207,.10);mix-blend-mode:normal;opacity:.93;text-shadow:0 0 1px #c8332b;
  -webkit-mask-image:radial-gradient(circle at 30%% 40%%,#000 60%%,rgba(0,0,0,.75) 100%%)}
.langue{position:absolute;right:0;top:44px;font-family:Archivo,sans-serif;font-weight:800;font-size:28px;letter-spacing:.1em;
  color:#15130f;background:#c8a35a;padding:10px 26px 10px 22px;border-radius:6px 0 0 6px}
</style></head><body>
<div class="photo"></div><div class="grille"></div>
<div class="fiche"></div>
<div class="txt">
  <div class="sur">%(sur)s</div>
  <div class="trait"></div>
  <div class="gros">%(gros)s</div>
  <div class="bas"><span class="pill">%(pill1)s</span><span class="pill c">%(pill2)s</span></div>
</div>
<div class="tampon">%(dates)s</div>
<div class="langue">%(lg)s</div>
<script>/* titre trop grand : on réduit */var g=document.querySelector(".gros"),f=112;
while((g.scrollWidth>g.clientWidth||g.offsetHeight>330)&&f>56){f-=4;g.style.fontSize=f+"px"}</script>
</body></html>""" % dict(base=base, img=C["img"], lang=lang, sur=e(T["sur"] % C["num"]), gros=gros, pill1=e(pill1),
                         pill2=e(T["pills"][1]), dates=e(C["dates"]), lg="ENGLISH" if lang == "en" else "FRANÇAIS")


def kit_episode(code, dossier):
    """Kit d'un seul épisode (publication en série, comme la philo) : <code>-youtube.txt, <code>.<langue>.srt, miniature."""
    ep = episode(code)
    lang = "fr" if re.match(r"h\df-", code) else "en"
    chap = "H" + code[1]
    C, T = CHAPITRES[chap], TXT[lang]
    n = int(code.split("-")[-1])
    notion = ep["notion"]
    ep_lbl = "Ep." if lang == "en" else "Ép."
    suff = ["DNL History Terminale", "DNL History", ""] if lang == "en" else ["Histoire Terminale", "Histoire", ""]
    for sf in suff:
        titre = "%s %d · %s | %s" % (ep_lbl, n, ep["titre"], C["gros"][lang]) + (" · " + sf if sf else "")
        if len(titre) <= 100:
            break
    if lang == "en":
        intro = ("Episode %d of the series « %s » (chapter %d of Terminale history, in English: DNL / European section). "
                 "Animated maps, archive images, key dates, figures and documents. About %d min." % (n, notion, C["num"], round(ep["dur"] / 60)))
        serie = "The whole series, episode by episode: see the playlist « %s · DNL History »." % notion
        contenu = "Content: the DNL History course of Terminale, as written on the revision site; animated maps of the site."
    else:
        intro = ("Épisode %d de la série « %s » (chapitre %d d'histoire de Terminale). "
                 "Cartes animées, images d'archives, dates, chiffres et documents clés. Environ %d min." % (n, notion, C["num"], round(ep["dur"] / 60)))
        serie = "Toute la série, épisode par épisode : voir la playlist « %s · Histoire Terminale »." % notion
        contenu = "Contenu : le cours d'histoire de Terminale, tel qu'il est rédigé sur le site de révision ; cartes animées du site."
    assert len(titre) <= 100, (len(titre), titre)
    vus, ch = set(), []
    for s in ep["scenes"]:
        c = s.get("chap")
        if c and c not in vus:
            vus.add(c); ch.append([s["t0"], c])
    ch.insert(0, [0, ep["titre"]])
    chapitres = ["%s %s" % (hms(t), c) for t, c in ch]
    credits = [c for c in ep.get("credits", []) if not re.match(r"(Content|Contenu|Narration|Voix|Music|Musique)", c)]
    desc = [intro, "", T["pause"], "", T["chap"]] + chapitres + ["", serie, "", T["cred"], contenu] + credits + [T["voix"]]
    desc_txt = "\n".join(desc)
    if len(desc_txt) >= 5000:
        desc_txt = "\n".join(desc[:desc.index(T["cred"]) + 2] + [T["voix"]])
    assert len(desc_txt) < 5000, len(desc_txt)
    tags = C["tags"][lang]
    q = [(T["quiz"] % len(ep["quiz"])).replace(" on the whole chapter (from the recap)", "").replace(" sur tout le chapitre (tirées du récap)", ""), ""]
    r = ["", T["rep"]]
    for i, x in enumerate(ep["quiz"], 1):
        q.append("%d. %s" % (i, plat(x["q"])))
        for j, rr in enumerate(x["r"]):
            q.append("   %s) %s" % ("abcd"[j], plat(rr)))
        r.append("%d. %s) %s. %s %s" % (i, "abcd"[x["ok"]], plat(x["r"][x["ok"]]), plat(x.get("ex", "")), T["revoir"] % hms(x.get("voir", 0))))
    comm = "\n".join(q + r)
    blocs = ["TITRE (%d caractères)" % len(titre), titre, "", "DESCRIPTION (%d caractères)" % len(desc_txt), desc_txt, "",
             "TAGS", ", ".join(tags), "", "COMMENTAIRE ÉPINGLÉ (%d caractères)" % len(comm), comm, "",
             "RÉGLAGES CONSEILLÉS"] + [x % code if "%s" in x else x for x in T["reglages"]] + [
             "Playlist : « %s » (un épisode après l'autre, dans l'ordre)." % (notion + (" · DNL History" if lang == "en" else " · Histoire Terminale"))]
    os.makedirs(dossier, exist_ok=True)
    open(os.path.join(dossier, code + "-youtube.txt"), "w", encoding="utf-8").write("\n".join(blocs) + "\n")
    sous = []
    for a_, b_, x in ep["sous"]:
        sous += decouper(a_, b_, plat(x))
    open(os.path.join(dossier, "%s.%s.srt" % (code, lang)), "w", encoding="utf-8").write(
        "\n".join("%d\n%s --> %s\n%s\n" % (i, hms(a_, True), hms(b_, True), x) for i, (a_, b_, x) in enumerate(sous, 1)))
    img = next((v["img"] + ".jpg" for v in ep["vis"] if v["type"] == "tableau" and v.get("img")), C["img"])
    C2 = dict(C, img=img, gros={lang: ep["titre"]})
    T2 = dict(T, sur=(T["mat"] + " · Ch. %d" + (" · Ep. %d" % n if lang == "en" else " · Ép. %d" % n)))
    T2["pills"] = (C["gros"][lang] + " · %d min" % round(ep["dur"] / 60) + "%.0s%.0s", T["pills"][1] if n == len(SERIE_N[chap]) - 1 else
                   ("Episode %d/%d" % (n, len(SERIE_N[chap])) if lang == "en" else "Épisode %d/%d" % (n, len(SERIE_N[chap]))))
    open(os.path.join(dossier, code + "-miniature.html"), "w", encoding="utf-8").write(
        miniature(C2, T2, lang, 0, "", 0, 0, [code]))
    print("%s : %s · %d chapitres · %d sous-titres · description %d · image %s" % (code, titre, len(chapitres), len(sous), len(desc_txt), img))


SERIE_N = {"H1": range(1, 7), "H2": range(1, 10), "H3": range(1, 8)}


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    for c in sys.argv[2:]:
        (kit if c in KITS else kit_episode)(c, sys.argv[1])
