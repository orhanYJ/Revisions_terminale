"""Exécute chaque programme Python affiché dans le site et compare la sortie affichée.

Tous les chapitres src/chN.js sont lus. Usage : python3 outils/specialites/maths/verif/python_sorties.py
"""
import json, os, subprocess, sys
ICI = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ICI, "..", "src")
NUMS = sorted(int(f[2:-3]) for f in os.listdir(SRC) if f.startswith("ch") and f[2:-3].isdigit())
MOTEUR = "var R=String.raw;var ANIMS={};var ANIM={e:x=>x,l:x=>x,p:x=>x,nf:x=>x};var TeX={fmt:x=>x};var WIDGETS={};"
js = MOTEUR + "\n".join(open(os.path.join(SRC, "ch%d.js" % i), encoding="utf-8").read() for i in NUMS)
liste = ",".join("CH%d" % i for i in NUMS)
js += "\nconsole.log(JSON.stringify([" + liste + "].map(function(c){return (c.algos||[]).map(function(a){return {t:a.t,code:a.code,sortie:a.sortie||''};});})));"
data = json.loads(subprocess.run(["node", "-"], input=js, capture_output=True, text=True, check=True).stdout)
ok = True
for i, algos in zip(NUMS, data):
    for a in algos:
        r = subprocess.run([sys.executable, "-c", a["code"]], capture_output=True, text=True)
        out = r.stdout.strip()
        if a["sortie"].startswith("(une"):
            etat = "aléatoire (" + ("OK" if r.returncode == 0 else "ERREUR") + ")"
        else:
            etat = "OK" if out == a["sortie"].strip() and r.returncode == 0 else "DIFFÉRENT"
        if etat not in ("OK", "aléatoire (OK)"):
            ok = False
            print("---", out, "--- attendu ---", a["sortie"], r.stderr[-300:])
        print(f"ch{i} | {a['t'][:50]:50} | {etat}")
sys.exit(0 if ok else 1)
