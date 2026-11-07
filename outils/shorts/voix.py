"""Voix d'un short : enregistre chaque passage (voix clonée des séries, voix_qwen.py), les met bout à bout
et écrit <CODE>.voix.wav et <CODE>.data.js (temps de chaque mot) dans outils/shorts/sortie/.

Usage : python3 outils/shorts/voix.py libet          voix définitive (cache par passage dans .cache/)
        SHORT_MUET=1 python3 outils/shorts/voix.py libet   brouillon sans voix, 2,9 mots/s, pour régler les images
"""
import hashlib, importlib, json, os, re, subprocess, sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
sys.path.insert(0, os.path.join(ICI, "..", "serie-philo"))
SORTIE = os.path.join(ICI, "sortie")
CACHE = os.path.join(ICI, ".cache")
SR = 48000


def lu(texte, prono):
    for a, b in sorted(prono.items(), key=lambda x: -len(x[0])):
        texte = re.sub(r"(?<!\w)(?<!\d,)%s(?!\w)(?!,\d)" % re.escape(a), b, texte)
    return texte.replace("1983", "mille neuf cent quatre-vingt-trois")


def decoder(mp3):
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", mp3, "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"],
                       capture_output=True, check=True)
    return np.frombuffer(r.stdout, dtype=np.float32)


def main(nom):
    m = importlib.import_module(nom)
    os.makedirs(SORTIE, exist_ok=True)
    os.makedirs(CACHE, exist_ok=True)
    muet = os.environ.get("SHORT_MUET") == "1"
    morceaux, segs, t = [], [], 0.25
    morceaux.append(np.zeros(int(0.25 * SR), np.float32))
    for sid, texte, apres in m.PASSAGES:
        mots_aff = re.findall(r"[\wÀ-ÿœæ'’-]+", texte)
        if muet:
            d = len(mots_aff) / 2.9
            mots = [[round(t + i * d / len(mots_aff), 3), round(d / len(mots_aff), 3), w] for i, w in enumerate(mots_aff)]
            audio = np.zeros(int(d * SR), np.float32)
        else:
            import voix_qwen
            parle = lu(texte, m.PRONONCIATION)
            h = hashlib.sha1(f"{parle}|{m.TEMPO}".encode()).hexdigest()[:10]
            ch = os.path.join(CACHE, f"{m.CODE}-{sid}-{h}.mp3")
            if not os.path.exists(ch):
                print("voix", sid, parle[:50], flush=True)
                sc = voix_qwen.dire(parle, "narrateur", ch, tempo=m.TEMPO)
                print("   score", round(sc, 3), flush=True)
            audio = decoder(ch)
            # coupe les silences de bord pour un rythme serré
            idx = np.where(np.abs(audio) > 0.01)[0]
            a0 = max(0, idx[0] - int(0.03 * SR)) if len(idx) else 0
            a1 = min(len(audio), idx[-1] + int(0.08 * SR)) if len(idx) else len(audio)
            audio = audio[a0:a1]
            brut = json.load(open(ch + ".json", encoding="utf-8"))
            # mots reconnus sur le texte lu → on remet les mots affichés (même découpe sauf prononciations)
            mots_lus = [w for _, _, w in brut]
            nl = sum(max(1, len(re.findall(r"[\wÀ-ÿœæ'’-]+", lu(w, m.PRONONCIATION)))) for w in mots_aff)
            if nl != len(mots_lus):
                print("  ATTENTION découpe différente", sid, nl, len(mots_lus))
            # chaque mot affiché correspond à un ou plusieurs mots lus (« 1983 » → « mille neuf cent… »)
            mots, j = [], 0
            for w in mots_aff:
                nlus = max(1, len(re.findall(r"[\wÀ-ÿœæ'’-]+", lu(w, m.PRONONCIATION))))
                o = brut[min(j, len(brut) - 1)][0]
                k = min(j + nlus, len(brut)) - 1
                fin = brut[k][0] + brut[k][1]
                mots.append([round(t + o - a0 / SR, 3), round(max(.05, fin - o), 3), w])
                j += nlus
        segs.append({"id": sid, "t0": round(t, 3), "t1": round(t + len(audio) / SR, 3), "texte": texte, "mots": mots})
        morceaux.append(audio)
        t += len(audio) / SR
        morceaux.append(np.zeros(int(apres * SR), np.float32))
        t += apres
    fin = 0.6
    morceaux.append(np.zeros(int(fin * SR), np.float32))
    voix = np.concatenate(morceaux)
    dur = round(len(voix) / SR, 3)
    import soundfile as sf
    sf.write(os.path.join(SORTIE, f"{m.CODE}.voix.wav"), voix, SR)
    with open(os.path.join(SORTIE, f"{m.CODE}.data.js"), "w", encoding="utf-8") as f:
        f.write("window.SHORT = " + json.dumps({"code": m.CODE, "dur": dur, "segs": segs}, ensure_ascii=False) + ";\n")
    print(f"{m.CODE} : {dur} s, {sum(len(s['mots']) for s in segs)} mots", "(muet)" if muet else "")


if __name__ == "__main__":
    main(sys.argv[1])
