"""Vérifie les programmes de la vidéo NSI du chapitre 1 (outils/serie-nsi/nsi_ch1.py) : chaque visuel de type code est
exécuté avec Python 3 (avec, avant lui, les classes dont il a besoin) et sa sortie est comparée, caractère pour caractère, à
la sortie affichée dans la vidéo (champ sortie) ; un programme qui finit par une erreur doit afficher exactement la ligne
d'erreur annoncée (champ erreur) ; une session interactive (console=True) est rejouée comme un doctest. Les extraits qui
ne s'exécutent pas seuls (méthodes isolées, classe abrégée par « ... ») sont au moins compilés, et les méthodes isolées
du parking et de la médiathèque sont remises dans leur classe pour rejouer les tests du site.

Usage : python3 outils/serie-nsi/verif_ch1.py
"""
import contextlib, doctest, io, os, subprocess, sys, tempfile, textwrap

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nsi_ch1 as E  # noqa: E402

J = "\n".join
# ce qu'il faut exécuter avant chaque programme (classes définies ailleurs dans la vidéo)
AVANT = {
    "usage": [E.COMPTE], "self_code": [E.COMPTE], "acc": [E.COMPTE], "alc": [E.COMPTE], "fo": [E.COMPTE],
    "vir_u": [E.VIR], "gu": [E.GS], "bqu": [E.COMPTE, E.BANQUE], "k1": [E.PARKING],
}
SEUL_COMPILE = {"tr_code", "k2", "k3", "k4", "md1", "md2"}   # extraits : compilés seulement (rejoués plus bas dans leur classe)


def executer(src):
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False, encoding="utf-8") as f:
        f.write(src)
    r = subprocess.run([sys.executable, f.name], capture_output=True, text=True)
    os.unlink(f.name)
    return r


IND = lambda lignes: J("    " + x if x else x for x in lignes)
AVANT["md3"] = [E.LIVRE, E.MEDIA[:7] + [""] + IND(E.MD_EMPR).split("\n") + [""] + IND(E.MD_NB).split("\n")]


def main():
    err, n = [], 0
    for sc in E.SCENES:
        for ident, v in sc["vis"].items():
            if v.get("type") != "code":
                continue
            n += 1
            src = J(v["lignes"])
            for k, r in enumerate(v.get("rep", [])):
                src = src.replace("@%d" % (k + 1), r)
            if v.get("console"):
                t = doctest.DocTestParser().get_doctest(src, {}, ident, ident, 0)
                sortie = io.StringIO()
                with contextlib.redirect_stdout(sortie):
                    res = doctest.DocTestRunner(verbose=False).run(t)
                if res.failed:
                    err.append(f"{ident} : session interactive différente\n{sortie.getvalue()}")
                continue
            if ident in SEUL_COMPILE:
                try:
                    compile(textwrap.dedent(src), ident, "exec")
                except SyntaxError as e:
                    err.append(f"{ident} : ne compile pas ({e})")
                continue
            r = executer(J(J(x) for x in AVANT.get(ident, [])) + "\n" + src)
            attendu = v.get("sortie")
            if attendu is not None and r.stdout.rstrip("\n") != attendu:   # (sans sortie affichée : « prédis la sortie », le programme doit seulement tourner)
                err.append(f"{ident} : sortie {r.stdout!r}, la vidéo affiche {attendu!r}")
            if v.get("erreur"):
                derniere = r.stderr.strip().split("\n")[-1] if r.stderr.strip() else ""
                if derniere != v["erreur"]:
                    err.append(f"{ident} : erreur {derniere!r}, la vidéo affiche {v['erreur']!r}")
            elif r.returncode:
                err.append(f"{ident} : le programme échoue\n{r.stderr}")
    # les méthodes du parking remises dans la classe, puis les tests du corrigé du site (c1-ecrit-corr)
    ind = IND
    parking = J(E.PARKING) + "\n\n" + ind(E.PK_PLEIN) + "\n\n" + ind(E.PK_GARER) + "\n\n" + ind(E.PK_SORTIR) + "\n"
    r = executer(parking + textwrap.dedent('''
        p = Parking(3)
        print(p.garer(Vehicule("AB-123-CD", "voiture")), p.garer(Vehicule("EF-456-GH", "moto")))
        print(p.sortir("AB-123-CD"), p.sortir("ZZ-000-ZZ"), p.nb_libres())
        print(p.garer(Vehicule("IJ-789-KL", "moto")), p.est_plein())
        q = Parking(1)
        print(q.garer(Vehicule("A", "moto")), q.garer(Vehicule("B", "moto")), q.est_plein())
        v = Vehicule("AB-123-CD", "voiture")
        q2 = Parking(2)
        q2.garer(v)
        v.categorie = "moto"
        print(q2.places[0].categorie)
    '''))
    if r.stdout != "0 1\nTrue False 2\n0 False\n0 -1 True\nmoto\n":
        err.append(f"parking corrigé : {r.stdout!r} {r.stderr}")
    # la médiathèque : la version fournie se trompe (1 au lieu de 3), la version corrigée passe les tests
    livres = textwrap.dedent('''
        m = Mediatheque()
        m.ajouter(Livre("Les Misérables", "Victor Hugo", 1862))
        m.ajouter(Livre("Notre-Dame de Paris", "Victor Hugo", 1831))
        m.ajouter(Livre("Le Rouge et le Noir", "Stendhal", 1830))
        print(m.nombre_disponibles())
    ''')
    r = executer(J(E.LIVRE) + "\n" + J(E.MEDIA) + "\n" + livres)
    if r.stdout != "1\n":
        err.append(f"médiathèque fournie : {r.stdout!r} (1 attendu, l'erreur de l'énoncé) {r.stderr}")
    media = J(E.MEDIA[:7]) + "\n" + ind(E.MD_EMPR) + "\n\n" + ind(E.MD_NB) + "\n"
    r = executer(J(E.LIVRE) + "\n" + media + "\n" + J(E.MD_TESTS))
    if r.stdout != "tous les tests passent\n":
        err.append(f"médiathèque corrigée : {r.stdout!r} {r.stderr}")
    print(f"{n} programmes de la vidéo vérifiés, plus le parking et la médiathèque complets")
    for e in err:
        print("  ERREUR", e)
    return not err


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
