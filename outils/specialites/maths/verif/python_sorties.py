"""Exécute chaque programme Python affiché dans le site et compare la sortie affichée.

Usage : python3 outils/specialites/maths/verif/python_sorties.py
"""
import json, os, subprocess, sys
ICI = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ICI, "..", "src")
js = "var R=String.raw;" + "".join(open(os.path.join(SRC, f"ch{i}.js"), encoding="utf-8").read() for i in range(1, 6))
js += ";console.log(JSON.stringify([CH1,CH2,CH3,CH4,CH5].map(c=>c.algos.map(a=>({t:a.t,code:a.code,sortie:a.sortie||''})))))"
data = json.loads(subprocess.run(["node", "-"], input=js, capture_output=True, text=True, check=True).stdout)
ok = True
for i, algos in enumerate(data, 1):
    for a in algos:
        r = subprocess.run([sys.executable, "-c", a["code"]], capture_output=True, text=True)
        out = r.stdout.strip()
        if a["sortie"].startswith("(une"):
            etat = "aléatoire (" + ("OK" if r.returncode == 0 else "ERREUR") + ")"
        else:
            etat = "OK" if out == a["sortie"].strip() else "DIFFÉRENT"
        if etat not in ("OK", "aléatoire (OK)"):
            ok = False
            print("---", out, "--- attendu ---", a["sortie"], r.stderr[-300:])
        print(f"ch{i} | {a['t'][:50]:50} | {etat}")
sys.exit(0 if ok else 1)
