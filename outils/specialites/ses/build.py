"""Assemble ses/index.html à partir des sources de src/ (CSS, données, application)."""
import os, subprocess, sys, tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ICI, "src")
SORTIE = os.path.join(ICI, "..", "..", "..", "ses", "index.html")
DONNEES = ["data-commun.js", "data-pages.js", "data-e1.js", "data-e2.js", "data-s1.js", "data-s2.js"]


def lire(nom):
    with open(os.path.join(SRC, nom), encoding="utf-8") as f:
        return f.read()


def verifier(js, nom):
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
        f.write(js)
    r = subprocess.run(["node", "--check", f.name], capture_output=True, text=True)
    os.unlink(f.name)
    if r.returncode:
        print("ERREUR", nom, r.stderr[:600])
        sys.exit(1)


SANS = sys.argv[sys.argv.index("--sans") + 1].split(",") if "--sans" in sys.argv else []
AUTRES = sorted(f for f in os.listdir(SRC) if f.startswith("data-") and f.endswith(".js") and f not in DONNEES and f not in SANS)
donnees = "\n".join(lire(n) for n in ["anim-moteur.js"] + DONNEES + AUTRES if os.path.exists(os.path.join(SRC, n)))
app = lire("app.js")
verifier(donnees, "données")
verifier(donnees + "\n" + app, "application")
for a in ("</script", "<!--"):
    assert a not in donnees and a not in app, a
html = lire("shell.html").replace("/*STYLE*/", lire("style.css")).replace("/*DATA*/", donnees).replace("/*APP*/", app)
with open(SORTIE, "w", encoding="utf-8") as f:
    f.write(html)
print("ses/index.html :", round(len(html.encode("utf-8")) / 1024), "Ko")
