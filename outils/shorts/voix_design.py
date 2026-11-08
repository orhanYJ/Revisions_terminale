"""Création de voix candidates pour les shorts (Qwen3-TTS VoiceDesign : une voix fabriquée d'après une description).

Demande de Cengiz (08/11/2026) : la voix des séries (grave, posée) est « trop ennuyée » pour TikTok ; il veut une
voix masculine plus aiguë, plus vive. Chaque candidate lit le même texte ; la voix choisie sert ensuite de
référence de clonage (voix_ref/narrateur_short.wav) pour que le timbre reste identique d'un short à l'autre.
Usage : python3 outils/shorts/voix_design.py   → outils/shorts/voix_essais/<nom>.wav et .mp3
"""
import os, subprocess, sys
import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "voix_essais")
TEXTE = ("Est-ce que tu enverrais quatre cent cinquante volts à un inconnu… juste parce qu'on te le demande ? "
         "Non ? Eux aussi, ils pensaient que non. Mille neuf cent soixante et un, université Yèle. "
         "Une petite annonce : quatre dollars cinquante pour une expérience sur la mémoire.")
CANDIDATES = {
    "1-createur": "A young French man in his mid-twenties with a bright tenor voice. Energetic, enthusiastic storyteller "
                  "like a popular TikTok creator: fast pace, punchy emphasis on key words, lively rising and falling intonation, "
                  "short dramatic pauses. Native Parisian French accent.",
    "2-vulgarisateur": "A French male science YouTuber around thirty, medium-high pitch, warm and excited, curious and captivating. "
                       "Very expressive melody, slightly fast delivery, smiling tone, clear articulation. Native French accent.",
    "3-thriller": "A young French man with a light, medium-high voice telling a true-crime story on social media: suspenseful and "
                  "intense, lowering his voice on mysterious words then bursting with energy on the reveals. Very expressive, "
                  "fast-paced, native French accent.",
    "4-radio": "An energetic French male radio host in his late twenties, crisp mid-high voice, confident and punchy, upbeat "
               "rhythm, strong emphasis, dynamic and vivid, native French accent.",
    "5-ado": "A lively French man about twenty-two, fairly high-pitched for a man, playful and dynamic, speaking quickly with "
             "excitement and wonder, big intonation contrasts, native French accent.",
    # 2e série (08/11/2026) : la 1re sortait trop aiguë (210 à 270 Hz) ; on vise un homme adulte vers 130-170 Hz
    "6-conteur": "Male, 28 years old, adult man's voice, tenor with a medium pitch (not high, not deep). A captivating French "
                 "storyteller on social media: energetic, fast, lively intonation, punchy on key words, slight smile. Clearly a man.",
    "7-mystere": "Male, 30 years old, adult man, medium pitch baritone-tenor, clearly masculine. Suspenseful French narrator of "
                 "true stories: tension in the voice, quick rhythm, dramatic pauses, then energetic reveals. Very expressive.",
    "8-energique": "Male, 25 years old, young adult man with a clear masculine tenor voice, medium pitch. Dynamic French YouTuber, "
                   "enthusiastic and vivid, fast delivery, strong emphasis, big intonation contrasts but never shrill.",
    "9-docu": "Male, 32 years old, masculine voice, medium pitch, bright timbre. Modern French documentary voice-over for "
              "short videos: vivid, engaging, fast and rhythmic, curious tone, strong emphasis on surprising facts.",
}


def main(noms=None):
    import torch, soundfile as sf
    from qwen_tts import Qwen3TTSModel
    torch.set_num_threads(os.cpu_count() or 4)
    m = Qwen3TTSModel.from_pretrained("Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign", device_map="cpu", dtype=torch.float32)
    os.makedirs(SORTIE, exist_ok=True)
    import librosa
    for nom, desc in CANDIDATES.items():
        if noms and nom not in noms:
            continue
        torch.manual_seed(7)
        w, sr = m.generate_voice_design(text=TEXTE, instruct=desc, language="French")
        a = w[0].astype(np.float32)
        f = os.path.join(SORTIE, nom + ".wav"); sf.write(f, a, sr)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f, "-af", "loudnorm=I=-16", "-b:a", "128k", f[:-4] + ".mp3"], check=True)
        f0, _, _ = librosa.pyin(librosa.resample(a, orig_sr=sr, target_sr=16000), fmin=60, fmax=400, sr=16000)
        print(nom, f"{len(a) / sr:.1f} s", f"hauteur médiane {np.nanmedian(f0):.0f} Hz", flush=True)


if __name__ == "__main__":
    main(sys.argv[1:] or None)
