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
