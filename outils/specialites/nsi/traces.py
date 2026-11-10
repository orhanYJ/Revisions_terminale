#!/usr/bin/env python3
"""Traces d'exécution pas à pas (lignes, variables, pile d'appels, sortie) des extraits marqués trace: true.

Appelé par build.py : les traces sont calculées en exécutant réellement le code avec sys.settrace,
puis rangées dans la constante TRACES du site (lue par l'animation « trace »).
"""
import inspect
import io
import json
import pathlib
import subprocess
import sys

ICI = pathlib.Path(__file__).resolve().parent
LIMITE = 400

EXTRAIRE = r"""
const fs = require("fs"), path = require("path");
const fichiers = JSON.parse(process.argv[1]);
const js = fichiers.map(f => fs.readFileSync(f, "utf8")).join("\n");
const ctx = {};
new Function("ctx", js + "\nctx.CODE = CODE;")(ctx);
const res = {};
for (const [id, c] of Object.entries(ctx.CODE)) if (c.trace === true) res[id] = c.src.replace(/^\n+|\s+$/g, "");
process.stdout.write(JSON.stringify(res));
"""


def court(v):
    try:
        r = repr(v)
    except Exception:
        return "(objet en cours de construction)"
    return r if len(r) <= 70 else r[:67] + "..."


def tracer(src):
    etapes, sortie = [], io.StringIO()
    code = compile(src, "<prog>", "exec")

    def variables(f):
        return {k: court(v) for k, v in f.f_locals.items()
                if not k.startswith("__") and not callable(v) and type(v).__name__ != "module"}

    def pile(f):
        cadres = []
        while f is not None and f.f_code.co_filename == "<prog>":
            if corps_de_classe(f):
                f = f.f_back
                continue
            nom = f.f_code.co_name
            cadres.append({"f": "programme principal" if nom == "<module>" else nom + "()", "v": variables(f)})
            f = f.f_back
        return cadres[::-1]

    def corps_de_classe(f):
        return not (f.f_code.co_flags & inspect.CO_OPTIMIZED) and f.f_code.co_name != "<module>"

    def suivre(frame, evenement, arg):
        if frame.f_code.co_filename != "<prog>" or corps_de_classe(frame):
            return None
        if evenement == "line" or (evenement == "return" and frame.f_code.co_name != "<module>"):
            if len(etapes) >= LIMITE:
                raise RuntimeError("trace trop longue")
            e = {"l": frame.f_lineno, "p": pile(frame), "o": sortie.getvalue()}
            if evenement == "return":
                e["r"] = court(arg)
                e["f"] = frame.f_code.co_name
            etapes.append(e)
        return suivre

    vrai = sys.stdout
    sys.stdout = sortie
    erreur = None
    sys.settrace(suivre)
    try:
        exec(code, {"__name__": "__main__"})
    except Exception as exc:  # l'erreur fait partie de la trace
        erreur = type(exc).__name__ + ": " + str(exc)
    finally:
        sys.settrace(None)
        sys.stdout = vrai
    return {"etapes": etapes, "err": erreur, "o": sortie.getvalue()}


def calculer(fichiers):
    sources = json.loads(subprocess.run(["node", "-e", EXTRAIRE, json.dumps([str(f) for f in fichiers])],
                                        capture_output=True, text=True, check=True).stdout)
    return {i: tracer(s) for i, s in sources.items()}


if __name__ == "__main__":
    src = sys.stdin.read()
    print(json.dumps(tracer(src), ensure_ascii=False, indent=1))
