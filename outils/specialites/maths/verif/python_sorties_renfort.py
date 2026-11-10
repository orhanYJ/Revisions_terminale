"""Exécute les programmes Python affichés dans les chapitres donnés et compare aux sorties affichées.

Usage : python3 outils/specialites/maths/verif/python_sorties_renfort.py 10 11 12 13 14 15
"""
import json, os, subprocess, sys
ICI = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ICI, "..", "src")
nums = sys.argv[1:] or ["10", "11", "12", "13", "14", "15"]
pre = "var window=globalThis;var R=String.raw;var ANIMS={};var WIDGETS={};var ANIM={};"
js = pre + "".join(open(os.path.join(SRC, f"ch{n}.js"), encoding="utf-8").read() for n in nums)
js += ";console.log(JSON.stringify([" + ",".join("CH" + n for n in nums) + "].map(c=>c.algos.map(a=>({t:a.t,code:a.code,sortie:a.sortie||''})))))"
data = json.loads(subprocess.run(["node", "-"], input=js, capture_output=True, text=True, check=True).stdout)
ok = True
for n, algos in zip(nums, data):
    for a in algos:
        r = subprocess.run([sys.executable, "-c", a["code"]], capture_output=True, text=True)
        out = r.stdout.strip()
        etat = "OK" if out == a["sortie"].strip() and r.returncode == 0 else "DIFFÉRENT"
        if etat != "OK":
            ok = False
            print("--- obtenu ---\n" + out + "\n--- affiché ---\n" + a["sortie"] + "\n" + r.stderr[-300:])
        print(f"ch{n} | {a['t'][:55]:55} | {etat}")
sys.exit(0 if ok else 1)
