/* ===================== Chapitre 6 — Bases de données ===================== */
/* Base d'exemple : une petite bibliothèque. Les tables affichées et le script SQL sont produits à partir des mêmes données. */
var BIB = {
  Auteur: { cols: ["id_auteur", "nom", "prenom", "naissance"], cle: "id_auteur", lignes: [
    [1, "Hugo", "Victor", 1802], [2, "Sand", "George", 1804], [3, "Verne", "Jules", 1828], [4, "Zola", "Émile", 1840], [5, "Colette", "Sidonie-Gabrielle", 1873]] },
  Livre: { cols: ["id_livre", "titre", "annee", "id_auteur"], cle: "id_livre", etr: { id_auteur: "Auteur" }, lignes: [
    [1, "Les Misérables", 1862, 1], [2, "Notre-Dame de Paris", 1831, 1], [3, "Les Contemplations", 1856, 1], [4, "Indiana", 1832, 2],
    [5, "La Mare au diable", 1846, 2], [6, "De la Terre à la Lune", 1865, 3], [7, "Germinal", 1885, 4], [8, "L'Assommoir", 1877, 4]] },
  Emprunt: { cols: ["id_emprunt", "id_livre", "adherent", "date_emprunt"], cle: "id_emprunt", etr: { id_livre: "Livre" }, lignes: [
    [1, 7, "Ada", "2026-10-02"], [2, 1, "Alan", "2026-10-05"], [3, 7, "Grace", "2026-10-20"], [4, 6, "Ada", "2026-11-03"]] }
};
function bibSql() {
  var types = { id_auteur: "INTEGER", nom: "TEXT", prenom: "TEXT", naissance: "INTEGER", id_livre: "INTEGER", titre: "TEXT", annee: "INTEGER", id_emprunt: "INTEGER", adherent: "TEXT", date_emprunt: "TEXT" };
  var s = [];
  Object.keys(BIB).forEach(function (t) {
    var T = BIB[t], def = T.cols.map(function (c) { return "    " + c + " " + types[c] + (c === T.cle ? " PRIMARY KEY" : "") + (T.etr && T.etr[c] ? " REFERENCES " + T.etr[c] + "(" + c + ")" : ""); });
    s.push("CREATE TABLE " + t + " (\n" + def.join(",\n") + "\n);");
  });
  Object.keys(BIB).forEach(function (t) {
    BIB[t].lignes.forEach(function (l) { s.push("INSERT INTO " + t + " VALUES (" + l.map(function (v) { return typeof v === "number" ? v : "'" + String(v).replace(/'/g, "''") + "'"; }).join(", ") + ");"); });
  });
  return s.join("\n");
}
function bibTable(t, opts) {
  opts = opts || {};
  var T = BIB[t];
  return '<div class="tab-wrap table-bd"><table><caption class="mono">' + t + '</caption><tr>' + T.cols.map(function (c) { return "<th" + (c === T.cle ? ' class="pk"' : T.etr && T.etr[c] ? ' class="fk"' : "") + ">" + (T.etr && T.etr[c] ? "#" : "") + c + "</th>"; }).join("") + "</tr>" +
    T.lignes.map(function (l) { return "<tr>" + l.map(function (v) { return "<td>" + String(v).replace(/&/g, "&amp;").replace(/</g, "&lt;") + "</td>"; }).join("") + "</tr>"; }).join("") + "</table></div>";
}

C("c6-schema", bibSql(), { sql: true, fichier: "bibliotheque.sql", out: "" });

C("c6-select", String.raw`
SELECT titre, annee
FROM Livre
WHERE annee < 1850
ORDER BY annee;`, { sql: true, deps: ["c6-schema"], out: "titre | annee\nNotre-Dame de Paris | 1831\nIndiana | 1832\nLa Mare au diable | 1846" });

C("c6-etoile", String.raw`
SELECT * FROM Auteur WHERE naissance >= 1828 AND naissance < 1870;`, { sql: true, deps: ["c6-schema"], out: "id_auteur | nom | prenom | naissance\n3 | Verne | Jules | 1828\n4 | Zola | Émile | 1840" });

C("c6-distinct", String.raw`
SELECT DISTINCT id_auteur FROM Livre ORDER BY id_auteur DESC;`, { sql: true, deps: ["c6-schema"], out: "id_auteur\n4\n3\n2\n1" });

C("c6-agregats", String.raw`
SELECT COUNT(*) AS nb_livres,
       MIN(annee) AS plus_ancien,
       MAX(annee) AS plus_recent
FROM Livre
WHERE id_auteur = 1;`, { sql: true, deps: ["c6-schema"], out: "nb_livres | plus_ancien | plus_recent\n3 | 1831 | 1862" });

C("c6-avg", String.raw`
SELECT AVG(naissance) AS moyenne, SUM(naissance) AS somme FROM Auteur WHERE id_auteur <= 2;`, { sql: true, deps: ["c6-schema"], out: "moyenne | somme\n1803.0 | 3606" });

C("c6-jointure", String.raw`
SELECT Livre.titre, Auteur.nom
FROM Livre
JOIN Auteur ON Livre.id_auteur = Auteur.id_auteur
WHERE Auteur.naissance > 1820
ORDER BY Livre.annee;`, { sql: true, deps: ["c6-schema"], out: "titre | nom\nDe la Terre à la Lune | Verne\nL'Assommoir | Zola\nGerminal | Zola" });

C("c6-jointure3", String.raw`
SELECT Emprunt.adherent, Livre.titre, Auteur.nom
FROM Emprunt
JOIN Livre ON Emprunt.id_livre = Livre.id_livre
JOIN Auteur ON Livre.id_auteur = Auteur.id_auteur
ORDER BY Emprunt.date_emprunt;`, { sql: true, deps: ["c6-schema"], out: "adherent | titre | nom\nAda | Germinal | Zola\nAlan | Les Misérables | Hugo\nGrace | Germinal | Zola\nAda | De la Terre à la Lune | Verne" });

C("c6-colette", String.raw`
SELECT COUNT(*) AS nb FROM Livre JOIN Auteur ON Livre.id_auteur = Auteur.id_auteur WHERE Auteur.nom = 'Colette';`, { sql: true, deps: ["c6-schema"], out: "nb\n0" });

C("c6-produit", String.raw`
SELECT COUNT(*) AS nb_lignes FROM Livre JOIN Auteur;   -- condition ON oubliée`, { sql: true, deps: ["c6-schema"], out: "nb_lignes\n40" });

C("c6-insert", String.raw`
INSERT INTO Livre VALUES (9, 'Le Blé en herbe', 1923, 5);
INSERT INTO Livre (id_livre, titre, annee, id_auteur) VALUES (10, 'Vingt mille lieues sous les mers', 1870, 3);
SELECT COUNT(*) AS nb FROM Livre;`, { sql: true, deps: ["c6-schema"], out: "nb\n10" });

C("c6-update", String.raw`
UPDATE Emprunt SET adherent = 'Linus' WHERE id_emprunt = 4;
SELECT * FROM Emprunt WHERE adherent = 'Linus';`, { sql: true, deps: ["c6-schema"], out: "id_emprunt | id_livre | adherent | date_emprunt\n4 | 6 | Linus | 2026-11-03" });

C("c6-delete", String.raw`
DELETE FROM Emprunt WHERE date_emprunt < '2026-10-10';
SELECT id_emprunt, adherent FROM Emprunt;`, { sql: true, deps: ["c6-schema"], out: "id_emprunt | adherent\n3 | Grace\n4 | Ada" });

C("c6-err-pk", String.raw`
INSERT INTO Auteur VALUES (3, 'Dumas', 'Alexandre', 1802);   -- 3 est déjà pris`, { sql: true, deps: ["c6-schema"], err: "UNIQUE constraint failed: Auteur.id_auteur" });

C("c6-err-fk", String.raw`
INSERT INTO Livre VALUES (11, 'Le Comte de Monte-Cristo', 1844, 6);  -- aucun auteur n° 6`, { sql: true, deps: ["c6-schema"], err: "FOREIGN KEY constraint failed" });

C("c6-err-suppr", String.raw`
DELETE FROM Auteur WHERE nom = 'Zola';   -- des livres le référencent encore`, { sql: true, deps: ["c6-schema"], err: "FOREIGN KEY constraint failed" });

C("c6-redondance", String.raw`
-- Une seule grande table : l'auteur est répété à chaque livre
CREATE TABLE LivreTout (titre TEXT, annee INTEGER, nom TEXT, prenom TEXT, naissance INTEGER);
INSERT INTO LivreTout VALUES ('Les Misérables', 1862, 'Hugo', 'Victor', 1802);
INSERT INTO LivreTout VALUES ('Notre-Dame de Paris', 1831, 'Hugo', 'Victor', 1802);
INSERT INTO LivreTout VALUES ('Les Contemplations', 1856, 'Hugo', 'Victor', 1820);   -- erreur de saisie
SELECT DISTINCT nom, naissance FROM LivreTout;`, { sql: true, out: "nom | naissance\nHugo | 1802\nHugo | 1820" });

C("c6-python", String.raw`
import sqlite3

base = sqlite3.connect(":memory:")       # une base en mémoire (ou un fichier .db)
base.executescript(SCRIPT)               # SCRIPT : le script de la bibliothèque

def livres_de(nom):
    """Titres des livres d'un auteur, du plus ancien au plus récent."""
    requete = """SELECT Livre.titre FROM Livre
                 JOIN Auteur ON Livre.id_auteur = Auteur.id_auteur
                 WHERE Auteur.nom = ? ORDER BY Livre.annee"""
    return [ligne[0] for ligne in base.execute(requete, (nom,))]   # ? reçoit nom

print(livres_de("Hugo"))
print(livres_de("Colette"))`, { deps: ["c6-python-script"], out: "['Notre-Dame de Paris', 'Les Contemplations', 'Les Misérables']\n[]" });
C("c6-python-script", "SCRIPT = " + JSON.stringify(bibSql()), { run: false });

/* prédis la sortie */
C("c6-x1", String.raw`
SELECT titre FROM Livre
WHERE id_auteur = 1 AND annee > 1840
ORDER BY annee;`, { sql: true, deps: ["c6-schema"], out: "titre\nLes Contemplations\nLes Misérables" });

C("c6-x2", String.raw`
SELECT COUNT(*) AS nb, MIN(annee) AS premier
FROM Livre
WHERE id_auteur = 4;`, { sql: true, deps: ["c6-schema"], out: "nb | premier\n2 | 1877" });

C("c6-x3", String.raw`
SELECT DISTINCT adherent FROM Emprunt ORDER BY adherent;`, { sql: true, deps: ["c6-schema"], out: "adherent\nAda\nAlan\nGrace" });

C("c6-x4", String.raw`
SELECT Auteur.nom, Livre.titre
FROM Emprunt
JOIN Livre ON Emprunt.id_livre = Livre.id_livre
JOIN Auteur ON Livre.id_auteur = Auteur.id_auteur
WHERE Emprunt.adherent = 'Ada'
ORDER BY Emprunt.date_emprunt;`, { sql: true, deps: ["c6-schema"], out: "nom | titre\nZola | Germinal\nVerne | De la Terre à la Lune" });

/* épreuve pratique 1 */
C("c6-ep1-fourni", String.raw`
import sqlite3

base = sqlite3.connect(":memory:")
base.executescript(SCRIPT)

def titres_apres(annee):
    """Titres des livres parus strictement après annee, triés par titre."""
    requete = ...
    return [l[0] for l in base.execute(requete, (annee,))]

def livres_et_auteurs():
    """Couples (titre, nom de l'auteur), un par livre."""
    requete = "SELECT Livre.titre, Auteur.nom FROM Livre, Auteur"
    return base.execute(requete).fetchall()

print(len(livres_et_auteurs()))`, { fichier: "bibliotheque.py", run: false, trous: [8] });

C("c6-ep1-bug", String.raw`
import sqlite3
base = sqlite3.connect(":memory:")
base.executescript(SCRIPT)
requete = "SELECT Livre.titre, Auteur.nom FROM Livre, Auteur"
print(len(base.execute(requete).fetchall()))`, { deps: ["c6-python-script"], fichier: "essai.py", out: "40" });

C("c6-ep1-corr", String.raw`
import sqlite3

base = sqlite3.connect(":memory:")
base.executescript(SCRIPT)

def titres_apres(annee):
    requete = "SELECT titre FROM Livre WHERE annee > ? ORDER BY titre"
    return [l[0] for l in base.execute(requete, (annee,))]

def livres_et_auteurs():
    requete = """SELECT Livre.titre, Auteur.nom FROM Livre
                 JOIN Auteur ON Livre.id_auteur = Auteur.id_auteur"""
    return base.execute(requete).fetchall()

def nb_emprunts(titre):
    requete = """SELECT COUNT(*) FROM Emprunt
                 JOIN Livre ON Emprunt.id_livre = Livre.id_livre
                 WHERE Livre.titre = ?"""
    return base.execute(requete, (titre,)).fetchone()[0]

def test():
    assert titres_apres(1870) == ["Germinal", "L'Assommoir"]
    assert titres_apres(1900) == []
    assert len(livres_et_auteurs()) == 8                 # un couple par livre
    assert ("Indiana", "Sand") in livres_et_auteurs()
    assert nb_emprunts("Germinal") == 2
    assert nb_emprunts("Indiana") == 0

test()
print("tous les tests passent")`, { deps: ["c6-python-script"], fichier: "bibliotheque.py", out: "tous les tests passent" });

/* épreuve pratique 2 */
C("c6-ep2-fourni", String.raw`
livres = [{"titre": "Germinal", "id_auteur": 4}, {"titre": "Indiana", "id_auteur": 2},
          {"titre": "Les Misérables", "id_auteur": 1}]
auteurs = [{"id_auteur": 1, "nom": "Hugo"}, {"id_auteur": 2, "nom": "Sand"},
           {"id_auteur": 4, "nom": "Zola"}]

def jointure(livres, auteurs):
    """Liste des couples (titre, nom de l'auteur), dans l'ordre de livres."""
    res = []
    for l in livres:
        for a in auteurs:
            ...
    return res`, { fichier: "jointure.py", run: false, trous: [11] });

C("c6-ep2-corr", String.raw`
livres = [{"titre": "Germinal", "id_auteur": 4}, {"titre": "Indiana", "id_auteur": 2},
          {"titre": "Les Misérables", "id_auteur": 1}]
auteurs = [{"id_auteur": 1, "nom": "Hugo"}, {"id_auteur": 2, "nom": "Sand"},
           {"id_auteur": 4, "nom": "Zola"}]

def jointure(livres, auteurs):
    """Version naïve : deux boucles imbriquées, len(livres) x len(auteurs) comparaisons."""
    res = []
    for l in livres:
        for a in auteurs:
            if l["id_auteur"] == a["id_auteur"]:
                res.append((l["titre"], a["nom"]))
    return res

def jointure_index(livres, auteurs):
    """Version avec un dictionnaire id -> nom : un seul parcours de chaque table."""
    index = {a["id_auteur"]: a["nom"] for a in auteurs}
    return [(l["titre"], index[l["id_auteur"]]) for l in livres if l["id_auteur"] in index]

def test():
    attendu = [("Germinal", "Zola"), ("Indiana", "Sand"), ("Les Misérables", "Hugo")]
    assert jointure(livres, auteurs) == attendu
    assert jointure_index(livres, auteurs) == attendu
    assert jointure([], auteurs) == []
    assert jointure([{"titre": "X", "id_auteur": 9}], auteurs) == []    # pas d'auteur 9

test()
print("tous les tests passent")`, { fichier: "jointure.py", out: "tous les tests passent" });

/* épreuve écrite */
var CINE = String.raw`
CREATE TABLE Realisateur (id_real INTEGER PRIMARY KEY, nom TEXT, pays TEXT);
CREATE TABLE Film (id_film INTEGER PRIMARY KEY, titre TEXT, annee INTEGER,
                   id_real INTEGER REFERENCES Realisateur(id_real));
CREATE TABLE Seance (id_seance INTEGER PRIMARY KEY, id_film INTEGER REFERENCES Film(id_film),
                     salle INTEGER, jour TEXT);
INSERT INTO Realisateur VALUES (1, 'Méliès', 'France'), (2, 'Lang', 'Allemagne'),
                               (3, 'Chaplin', 'Royaume-Uni'), (4, 'Renoir', 'France');
INSERT INTO Film VALUES (1, 'Le Voyage dans la Lune', 1902, 1), (2, 'Metropolis', 1927, 2),
                        (3, 'M le maudit', 1931, 2), (4, 'Les Temps modernes', 1936, 3),
                        (5, 'La Grande Illusion', 1937, 4), (6, 'Le Dictateur', 1940, 3);
INSERT INTO Seance VALUES (1, 2, 1, 'vendredi'), (2, 4, 2, 'samedi'), (3, 5, 2, 'samedi'),
                          (4, 3, 3, 'samedi'), (5, 4, 1, 'dimanche'), (6, 6, 2, 'dimanche');`;
C("c6-cine", CINE, { sql: true, fichier: "cinema.sql", out: "" });
C("c6-e1", String.raw`
SELECT titre, annee FROM Film
WHERE annee >= 1930 AND annee <= 1939
ORDER BY annee;`, { sql: true, deps: ["c6-cine"], out: "titre | annee\nM le maudit | 1931\nLes Temps modernes | 1936\nLa Grande Illusion | 1937" });
C("c6-e2", String.raw`
SELECT COUNT(*) AS nb FROM Seance WHERE salle = 2;`, { sql: true, deps: ["c6-cine"], out: "nb\n3" });
C("c6-e3", String.raw`
SELECT DISTINCT Film.titre, Realisateur.nom
FROM Seance
JOIN Film ON Seance.id_film = Film.id_film
JOIN Realisateur ON Film.id_real = Realisateur.id_real
WHERE Seance.jour = 'samedi'
ORDER BY Film.titre;`, { sql: true, deps: ["c6-cine"], out: "titre | nom\nLa Grande Illusion | Renoir\nLes Temps modernes | Chaplin\nM le maudit | Lang" });
C("c6-e4", String.raw`
INSERT INTO Seance VALUES (7, 9, 1, 'lundi');`, { sql: true, deps: ["c6-cine"], err: "FOREIGN KEY constraint failed" });
C("c6-e5", String.raw`
UPDATE Seance SET salle = 1 WHERE salle = 3;
SELECT id_seance, salle FROM Seance WHERE id_seance = 4;`, { sql: true, deps: ["c6-cine"], out: "id_seance | salle\n4 | 1" });
C("c6-e6", String.raw`
DELETE FROM Seance WHERE id_film IN (SELECT id_film FROM Film WHERE id_real = 3);
DELETE FROM Film WHERE id_real = 3;
DELETE FROM Realisateur WHERE id_real = 3;
SELECT COUNT(*) AS films_restants FROM Film;`, { sql: true, deps: ["c6-cine"], out: "films_restants\n4" });

C("c6-retenir", String.raw`
SELECT col1, col2             -- colonnes voulues (* pour toutes), DISTINCT pour sans doublon
FROM Table1
JOIN Table2 ON Table1.cle = Table2.cle   -- jointure sur clé étrangère = clé primaire
WHERE condition               -- AND, OR, NOT, =, <>, <, <=, >, >=
ORDER BY col1 DESC;           -- tri (ASC par défaut)

INSERT INTO Table1 VALUES (v1, v2, v3);
UPDATE Table1 SET col = valeur WHERE condition;
DELETE FROM Table1 WHERE condition;`, { sql: true, run: false });

/* ---------- animation : une jointure qui assemble les lignes ---------- */
WIDGETS_EXT["jointure"] = function (z, opt, O) {
  var L = BIB.Livre.lignes, A = BIB.Auteur.lignes;
  function etapes(k) {
    var E = [], res = [], filtre = k === "where";
    E.push({ res: [], msg: "<code>FROM Livre JOIN Auteur ON Livre.id_auteur = Auteur.id_auteur</code> : pour chaque ligne de <b>Livre</b>, on cherche dans <b>Auteur</b> la ligne dont la clé primaire vaut la clé étrangère du livre." + (filtre ? " Puis <code>WHERE naissance &gt; 1820</code> ne garde que certaines lignes." : "") });
    L.forEach(function (l, i) {
      var j = -1; A.forEach(function (a, k2) { if (a[0] === l[3]) j = k2; });
      E.push({ res: res.slice(), li: i, ai: j, msg: "Livre n° " + l[0] + " « " + l[1] + " » : <code>id_auteur = " + l[3] + "</code>. Dans Auteur, la ligne de clé " + l[3] + " est <b>" + A[j][1] + "</b>." });
      var garde = !filtre || A[j][3] > 1820;
      if (garde) res.push([l[1], A[j][1]]);
      E.push({ res: res.slice(), li: i, ai: j, neuf: garde, rejet: !garde, msg: garde ? "Les deux lignes sont <b>assemblées</b> ; la projection <code>SELECT titre, nom</code> n’en garde que deux colonnes." : A[j][1] + " est né en " + A[j][3] + " : la condition <code>naissance &gt; 1820</code> est fausse, la ligne assemblée est <b>écartée</b>." });
    });
    E.push({ res: res.slice(), msg: "Résultat : <b>" + res.length + " lignes</b>. " + (filtre ? "" : "Colette (n° 5) n’apparaît pas : aucun livre ne la référence, et la jointure ne garde que les lignes qui se correspondent.") + " Un SGBD n’essaie pas toutes les paires : un <b>index</b> sur la clé primaire lui donne directement la bonne ligne, comme un dictionnaire." });
    return E;
  }
  function tab(nom, cols, lignes, vise, cl) {
    return '<div class="tab-wrap table-bd"><table><caption class="mono">' + nom + "</caption><tr>" + cols.map(function (c) { return "<th>" + c + "</th>"; }).join("") + "</tr>" +
      lignes.map(function (l, i) { return '<tr class="' + (i === vise ? cl : "") + '">' + l.map(function (v) { return "<td>" + O.esc(v) + "</td>"; }).join("") + "</tr>"; }).join("") + "</table></div>";
  }
  function dessine(sc, e) {
    var res = e.res.map(function (r) { return r; });
    sc.innerHTML = '<div class="jointure"><div class="j-sources">' + tab("Livre", ["id_livre", "titre", "#id_auteur"], L.map(function (l) { return [l[0], l[1], l[3]]; }), e.li, "vise") + tab("Auteur", ["id_auteur", "nom", "naissance"], A.map(function (a) { return [a[0], a[1], a[3]]; }), e.ai, "trouve") + '</div><div class="j-res">' +
      tab("résultat", ["titre", "nom"], res, e.neuf ? res.length - 1 : -1, "neuf") + (e.rejet ? '<div class="rejet mono">✘ ligne écartée par WHERE</div>' : "") + "</div></div>";
  }
  O.lecteur(z, { titre: "jointure SQL pas à pas", sous: "SELECT titre, nom", choix: [{ k: "join", t: "JOIN … ON" }, { k: "where", t: "JOIN + WHERE naissance > 1820" }], etapes: etapes, dessine: dessine, vitesse: 1500 });
};

CH.push({
  id: "ch6", n: 6, court: "bases_de_donnees", fichier: "ch6_bases_de_donnees.py",
  titre: "Bases de données",
  rubrique: "Rubrique « Bases de données » : modèle relationnel, base de données relationnelle, SGBD, langage SQL",
  accroche: "Relations, clés primaires et étrangères, contraintes d’intégrité, requêtes SQL (SELECT, JOIN, INSERT, UPDATE, DELETE) et rôle d’un SGBD.",
  essentiel: [
    "Une <b>base de données relationnelle</b> range les données dans des <b>relations</b> (tables) dont les lignes sont des enregistrements et les colonnes des <b>attributs</b>, chacun d’un <b>domaine</b>.",
    "La <b>clé primaire</b> identifie chaque ligne de façon unique ; une <b>clé étrangère</b> fait référence à la clé primaire d’une autre table.",
    "Le <b>schéma relationnel</b> (la structure) est distinct du <b>contenu</b> ; un bon schéma évite les redondances et les anomalies.",
    "<b>SQL</b> interroge (<code>SELECT … FROM … JOIN … ON … WHERE … ORDER BY</code>) et met à jour (<code>INSERT</code>, <code>UPDATE</code>, <code>DELETE</code>).",
    "Un <b>SGBD</b> assure la persistance, gère les accès concurrents, traite efficacement les requêtes et sécurise les accès."
  ],
  attendus: [
    "Identifier les concepts du modèle relationnel : relation, attribut, domaine, clé primaire, clé étrangère, schéma relationnel.",
    "Distinguer la structure d’une base de son contenu ; repérer des anomalies dans un schéma (redondances, anomalies d’insertion, de suppression, de mise à jour).",
    "Identifier les services rendus par un SGBD : persistance, accès concurrents, efficacité, sécurité.",
    "Construire des requêtes d’interrogation avec SELECT, FROM, WHERE, JOIN ; de mise à jour avec INSERT, UPDATE, DELETE.",
    "Limite du programme : DISTINCT, ORDER BY et les fonctions d’agrégation sont utilisables, mais <b>pas</b> GROUP BY ni HAVING."
  ],
  intro: `<div class="boite ex"><div class="lab"># la base d’exemple de tout le chapitre</div><p>Une petite bibliothèque, en trois tables. Les clés primaires sont soulignées, les clés étrangères précédées de <code>#</code>. Tous les résultats affichés ont été obtenus en exécutant les requêtes avec SQLite.</p>` + bibTable("Auteur") + bibTable("Livre") + bibTable("Emprunt") + `<details class="repli"><summary>Le script SQL qui crée cette base</summary><div class="corps">[[c6-schema]]</div></details></div>`,
  idees: [
    { id: "i1", t: "Pourquoi une base de données ?", h: `
<p>En Première, tu as manipulé des données en table : un fichier CSV lu en Python. Cela devient insuffisant dès que les données sont <b>nombreuses</b> (des millions de lignes), <b>partagées</b> (plusieurs programmes ou utilisateurs en même temps), <b>liées</b> entre elles (un livre et son auteur), et qu’elles doivent rester <b>cohérentes</b> et <b>durables</b> malgré les pannes.</p>
<p>Une <b>base de données</b> est un ensemble organisé de données ; un <b>système de gestion de bases de données</b> (SGBD) est le logiciel qui la stocke et répond aux requêtes. Exemples de SGBD relationnels : SQLite (inclus dans Python, dans Android et dans iOS), PostgreSQL, MySQL, Oracle. Les plus grands systèmes gèrent des volumes de l’ordre du pétaoctet (10<sup>15</sup> octets).</p>
<div class="boite histoire"><div class="lab"># git log --histoire</div><p><span class="commit">1970 <b>·</b></span> Edgar F. Codd, chercheur chez IBM, publie <i>A Relational Model of Data for Large Shared Data Banks</i> : le modèle relationnel.<br><span class="commit">années 1970 <b>·</b></span> IBM développe le langage SEQUEL, qui deviendra <b>SQL</b>.</p></div>` },

    { id: "i2", t: "Le modèle relationnel : relation, attribut, domaine", h: `
<div class="boite def"><div class="lab">"""définitions"""</div>
<p>Une <b>relation</b> (une table) est un ensemble de <b>n-uplets</b> (les lignes, ou enregistrements). Chaque colonne est un <b>attribut</b>, qui prend ses valeurs dans un <b>domaine</b> (entier, texte, date…). Le <b>schéma d’une relation</b> donne son nom et ses attributs avec leurs domaines : <code>Auteur(id_auteur : INT, nom : TEXT, prenom : TEXT, naissance : INT)</code>.</p></div>
<p>Dans la table Auteur ci-dessus, la ligne <code>(3, 'Verne', 'Jules', 1828)</code> est un n-uplet ; <code>naissance</code> est un attribut de domaine « entier ». Une relation est un <b>ensemble</b> : l’ordre des lignes n’a pas de sens et deux lignes ne peuvent pas être identiques.</p>` },

    { id: "i3", t: "Clé primaire, clé étrangère, schéma relationnel", h: `
<div class="boite def"><div class="lab">"""définitions"""</div>
<p>Une <b>clé primaire</b> est un attribut (ou un groupe d’attributs) dont la valeur identifie <b>une seule</b> ligne de la table : <code>id_auteur</code> pour Auteur. Une <b>clé étrangère</b> est un attribut qui contient la clé primaire d’une ligne d’une autre table : <code>Livre.id_auteur</code> fait référence à <code>Auteur.id_auteur</code>.</p></div>
<p>Le <b>schéma relationnel</b> d’une base est l’ensemble des schémas de ses relations. Notation courante à l’écrit (clé primaire soulignée, clé étrangère précédée de #) :</p>
<p class="mono petit">Auteur(<u>id_auteur</u>, nom, prenom, naissance)<br>Livre(<u>id_livre</u>, titre, annee, #id_auteur)<br>Emprunt(<u>id_emprunt</u>, #id_livre, adherent, date_emprunt)</p>
<p>Pourquoi un identifiant numérique plutôt que le nom ? Deux auteurs peuvent porter le même nom, et un nom peut changer : la clé primaire doit être unique et stable. Grâce aux clés étrangères, l’auteur n’est écrit qu’<b>une fois</b> et chaque livre y renvoie.</p>` },

    { id: "i4", t: "Les contraintes d’intégrité", h: `
<p>Le SGBD refuse toute modification qui rendrait la base incohérente. Trois contraintes sont au programme :</p>
<ul><li><b>Contrainte de domaine</b> : chaque valeur appartient au domaine de son attribut.</li>
<li><b>Contrainte de relation</b> (ou d’entité) : la clé primaire est unique (et non vide).</li>
[[c6-err-pk]]
<li><b>Contrainte de référence</b> : une clé étrangère doit désigner une ligne qui existe.</li></ul>
[[c6-err-fk]]
<p>Elle joue aussi à la suppression : on ne peut pas supprimer un auteur dont des livres dépendent encore. Il faut d’abord supprimer (ou modifier) les lignes qui y font référence.</p>
[[c6-err-suppr]]
<div class="boite hp"><div class="lab"># remarque technique</div><p>SQLite ne vérifie les clés étrangères que si l’on active <code>PRAGMA foreign_keys = ON</code> (c’est le cas pour les exemples de cette page). Les autres SGBD les vérifient par défaut. SQLite est aussi souple sur les domaines : il accepte parfois un texte dans une colonne entière.</p></div>` },

    { id: "i5", t: "Structure, contenu et anomalies de conception", h: `
<p>La <b>structure</b> d’une base est son schéma (les tables, leurs attributs, leurs clés) ; son <b>contenu</b> est l’ensemble des lignes à un instant donné. La structure change rarement ; le contenu, tout le temps.</p>
<p>Un mauvais schéma provoque des <b>redondances</b> : la même information est écrite plusieurs fois. Exemple : tout mettre dans une seule table.</p>
[[c6-redondance]]
<ul><li><b>Anomalie de mise à jour</b> : l’année de naissance de Hugo est écrite trois fois ; une faute dans une seule copie rend la base contradictoire (1802 ou 1820 ?).</li>
<li><b>Anomalie d’insertion</b> : impossible d’ajouter un auteur qui n’a pas encore de livre dans la base sans laisser des cases vides.</li>
<li><b>Anomalie de suppression</b> : supprimer le dernier livre d’un auteur efface aussi tout ce qu’on savait de l’auteur.</li></ul>
<p>Le remède : <b>découper</b> en plusieurs tables reliées par des clés (Auteur et Livre), pour que chaque information soit écrite une seule fois.</p>` },

    { id: "i6", t: "Interroger : SELECT, FROM, WHERE, ORDER BY", h: `
<p>Une requête d’interrogation dit <b>quelles colonnes</b> (SELECT), <b>de quelle table</b> (FROM), <b>pour quelles lignes</b> (WHERE) et <b>dans quel ordre</b> (ORDER BY). Le résultat est lui-même une table.</p>
[[c6-select]]
<p><code>SELECT *</code> garde toutes les colonnes ; les conditions se combinent avec <code>AND</code>, <code>OR</code>, <code>NOT</code> ; les chaînes s’écrivent entre apostrophes simples.</p>
[[c6-etoile]]
<p><code>DISTINCT</code> supprime les doublons du résultat ; <code>ORDER BY … DESC</code> trie par ordre décroissant.</p>
[[c6-distinct]]
<p>Les <b>fonctions d’agrégation</b> résument toutes les lignes sélectionnées en une seule : <code>COUNT</code>, <code>SUM</code>, <code>AVG</code>, <code>MIN</code>, <code>MAX</code>. <code>AS</code> renomme une colonne du résultat.</p>
[[c6-agregats]]
[[c6-avg]]
<div class="boite attention"><div class="lab">⚠ limite du programme</div><p>Pas de <code>GROUP BY</code> ni de <code>HAVING</code> au bac : une agrégation porte sur toutes les lignes retenues par le WHERE.</p></div>` },

    { id: "i7", t: "Croiser les tables : la jointure", h: `
<p>Pour afficher le titre d’un livre <b>et</b> le nom de son auteur, il faut réunir les deux tables : c’est une <b>jointure</b>. <code>JOIN … ON</code> assemble chaque ligne de la première table avec la ligne de la seconde qui vérifie la condition, presque toujours « clé étrangère = clé primaire ».</p>
[[c6-jointure]]
[[w-jointure]]
<p>On peut enchaîner plusieurs jointures. Préfixer les attributs par le nom de leur table (<code>Livre.titre</code>) lève toute ambiguïté quand deux tables ont un attribut de même nom.</p>
[[c6-jointure3]]
<p>Une jointure ne garde que les lignes qui se correspondent : Colette n’a aucun livre, elle n’apparaît dans aucun résultat de jointure avec Livre.</p>
[[c6-colette]]` },

    { id: "i8", t: "Mettre à jour : INSERT, UPDATE, DELETE", h: `
<p><code>INSERT INTO</code> ajoute des lignes, en donnant les valeurs dans l’ordre des colonnes, ou en nommant les colonnes :</p>
[[c6-insert]]
<p><code>UPDATE … SET … WHERE</code> modifie les lignes qui vérifient la condition :</p>
[[c6-update]]
<p><code>DELETE FROM … WHERE</code> supprime les lignes qui vérifient la condition (les dates au format AAAA-MM-JJ se comparent comme des chaînes) :</p>
[[c6-delete]]
<div class="boite attention"><div class="lab">⚠ le WHERE oublié</div><p>Sans WHERE, <code>UPDATE</code> modifie <b>toutes</b> les lignes et <code>DELETE FROM Emprunt</code> vide toute la table. Toujours écrire (et relire) la condition.</p></div>` },

    { id: "i9", t: "Le rôle du SGBD, et SQL depuis Python", h: `
<p>Le programme demande d’identifier les services d’un SGBD, sans détailler leur fonctionnement :</p>
<div class="tab-wrap"><table><tr><th>service</th><th>ce que ça veut dire</th><th>exemple</th></tr>
<tr><td>persistance</td><td>les données survivent à l’arrêt du programme et aux pannes</td><td>après une coupure de courant, les emprunts enregistrés sont toujours là</td></tr>
<tr><td>accès concurrents</td><td>plusieurs utilisateurs modifient la base en même temps sans la corrompre</td><td>deux bibliothécaires ne peuvent pas prêter le même exemplaire au même instant</td></tr>
<tr><td>efficacité</td><td>le SGBD choisit comment exécuter la requête et utilise des index</td><td>trouver un livre parmi des millions sans tout parcourir</td></tr>
<tr><td>sécurisation des accès</td><td>comptes, mots de passe, droits de lecture ou d’écriture par table</td><td>un adhérent consulte le catalogue mais ne modifie pas les emprunts</td></tr></table></div>
<p>Les traitements combinent souvent SQL et un langage de programmation. En Python, le module standard <code>sqlite3</code> envoie des requêtes à une base SQLite ; les valeurs se passent par des <code>?</code>, jamais en collant du texte dans la requête.</p>
[[c6-python]]
<div class="boite hp"><div class="lab"># pour aller plus loin : injection SQL et transactions</div><p>Construire une requête en concaténant ce qu’a tapé un utilisateur permet à un attaquant d’y glisser du code SQL (injection SQL) : les <code>?</code> l’empêchent. Une <b>transaction</b> regroupe plusieurs modifications qui réussissent toutes ou échouent toutes (un virement débite un compte et en crédite un autre).</p></div>` }
  ],
  pieges: [
    { t: "Oublier la condition de jointure", h: `[[c6-produit]]<p>Sans <code>ON</code>, chaque livre est associé à <b>chaque</b> auteur : 8 × 5 = 40 lignes (produit cartésien). La condition est presque toujours « clé étrangère = clé primaire ».</p>` },
    { t: "Oublier le WHERE d’un UPDATE ou d’un DELETE", h: `<p>Toute la table est modifiée ou vidée. Pour vérifier, écrire d’abord le <code>SELECT</code> avec le même WHERE et regarder quelles lignes il renvoie.</p>` },
    { t: "Confondre clé primaire et clé étrangère", h: `<p>La clé primaire est <b>dans sa propre table</b> et identifie la ligne (unique). La clé étrangère est <b>dans une autre table</b> et pointe vers une clé primaire (elle peut se répéter : Hugo a trois livres).</p>` },
    { t: "Supprimer dans le mauvais ordre", h: `<p>On supprime d’abord les lignes qui font référence (Emprunt, puis Livre), et en dernier la ligne référencée (Auteur). Sinon : contrainte de référence violée.</p>` },
    { t: "Mettre des guillemets doubles autour d’un texte", h: `<p>En SQL standard, une chaîne s’écrit entre apostrophes simples : <code>WHERE nom = 'Zola'</code>. Une apostrophe dans le texte se double : <code>'L''Assommoir'</code>.</p>` },
    { t: "Utiliser GROUP BY", h: `<p>Hors programme : au bac, les agrégations portent sur toutes les lignes sélectionnées. Pour un total par auteur, on fait une requête par auteur (ou on le traite en Python).</p>` }
  ],
  retenir: `
<h2>Vocabulaire</h2>
<div class="tab-wrap"><table><tr><th>mot</th><th>sens</th></tr>
<tr><td>relation (table)</td><td>ensemble de n-uplets (lignes)</td></tr><tr><td>attribut</td><td>colonne, avec un domaine (type)</td></tr>
<tr><td>clé primaire</td><td>identifie une ligne de façon unique</td></tr><tr><td>clé étrangère</td><td>référence la clé primaire d’une autre table</td></tr>
<tr><td>schéma relationnel</td><td>structure : tables, attributs, clés. Notation <code>Livre(<u>id_livre</u>, titre, #id_auteur)</code></td></tr>
<tr><td>contraintes d’intégrité</td><td>de domaine, de relation (clé primaire unique), de référence (clé étrangère existante)</td></tr>
<tr><td>anomalies</td><td>redondance, anomalies d’insertion, de suppression, de mise à jour</td></tr>
<tr><td>SGBD</td><td>persistance, accès concurrents, efficacité, sécurisation</td></tr></table></div>
<h2>SQL au programme</h2>
[[c6-retenir]]
<p>Agrégations : <code>COUNT(*)</code>, <code>SUM</code>, <code>AVG</code>, <code>MIN</code>, <code>MAX</code>. Pas de GROUP BY ni de HAVING.</p>
<h2>Les réflexes</h2>
<ul><li>Jointure : toujours une condition <code>ON clé_étrangère = clé_primaire</code>.</li><li>Préfixer les attributs ambigus : <code>Table.attribut</code>.</li><li>UPDATE / DELETE : vérifier le WHERE avec un SELECT avant.</li><li>Supprimer d’abord les lignes qui référencent.</li><li>Chaînes entre apostrophes simples.</li></ul>`,
  predis: [
    { code: "c6-x1", niv: "facile", q: "Quelle table cette requête renvoie-t-elle ?", rep: "Livres de Hugo (id_auteur = 1) parus après 1840 : Les Misérables (1862) et Les Contemplations (1856), triés par année croissante. Notre-Dame de Paris (1831) est écartée." },
    { code: "c6-x2", niv: "facile", q: "Quelle table cette requête renvoie-t-elle ?", rep: "Zola (id 4) a deux livres : Germinal (1885) et L’Assommoir (1877). COUNT donne 2, MIN donne 1877. Une agrégation renvoie une seule ligne." },
    { code: "c6-x3", niv: "facile", q: "Quelle table cette requête renvoie-t-elle ?", rep: "Ada a emprunté deux fois, mais DISTINCT supprime le doublon : trois adhérents, triés par ordre alphabétique." },
    { code: "c6-x4", niv: "moyen", q: "Quelle table cette requête renvoie-t-elle ?", rep: "Les emprunts d’Ada sont le n° 1 (livre 7, Germinal, de Zola, le 2 octobre) et le n° 4 (livre 6, De la Terre à la Lune, de Verne, le 3 novembre). La double jointure va d’Emprunt à Livre puis à Auteur." }
  ],
  ep: [
    { titre: "Requêtes depuis Python", note: "Le module sqlite3 fait partie de la bibliothèque standard ; <code>SCRIPT</code> contient le script de création de la bibliothèque (donné en tête de chapitre).", enonce: `[[c6-ep1-fourni]]`,
      questions: [
        { q: "Compléter la requête de <code>titres_apres</code> (ligne 8), en utilisant un paramètre <code>?</code>.", c: `<p><code>"SELECT titre FROM Livre WHERE annee &gt; ? ORDER BY titre"</code>. Le <code>?</code> reçoit la valeur du tuple <code>(annee,)</code>.</p>` },
        { q: "Le programme affiche 40 alors qu’il y a 8 livres. Expliquer et corriger <code>livres_et_auteurs</code>.", code: "[[c6-ep1-bug]]", c: `<p>La requête ne contient aucune condition de jointure : chaque livre est associé à chacun des 5 auteurs (8 × 5 = 40, produit cartésien). Correction : <code>FROM Livre JOIN Auteur ON Livre.id_auteur = Auteur.id_auteur</code>.</p>` },
        { q: "Écrire <code>nb_emprunts(titre)</code>, qui renvoie le nombre d’emprunts d’un livre, puis des tests.", c: `[[c6-ep1-corr]]` },
        { q: "À l’oral : pourquoi passer les valeurs par <code>?</code> plutôt que de construire la chaîne avec <code>+</code> ?", c: `<p>Le SGBD traite la valeur comme une donnée et non comme du code SQL : pas d’injection SQL possible, pas de problème d’apostrophes (<code>L'Assommoir</code>), et le bon type est conservé.</p>` }
      ] },
    { titre: "Programmer une jointure", enonce: `<p>Sans SGBD, deux tables peuvent être représentées par des listes de dictionnaires (comme les fichiers CSV de Première). On veut programmer soi-même la jointure.</p>[[c6-ep2-fourni]]`,
      questions: [
        { q: "Compléter la fonction <code>jointure</code> (ligne 11).", c: `<p><code>if l["id_auteur"] == a["id_auteur"]: res.append((l["titre"], a["nom"]))</code>.</p>` },
        { q: "Combien de comparaisons fait cette fonction pour <i>n</i> livres et <i>m</i> auteurs ?", c: `<p><i>n</i> × <i>m</i> : chaque livre est comparé à chaque auteur. Pour 100 000 livres et 10 000 auteurs, un milliard de comparaisons.</p>` },
        { q: "Écrire <code>jointure_index</code>, qui construit d’abord un dictionnaire <code>id_auteur → nom</code>, et des tests.", c: `<p>Un parcours des auteurs pour construire l’index, puis un parcours des livres avec un accès en temps constant (moyen) : de l’ordre de <i>n</i> + <i>m</i> opérations. C’est ce que fait un SGBD avec un index.</p>[[c6-ep2-corr]]` },
        { q: "À l’oral : que se passe-t-il pour un livre dont l’auteur n’est pas dans la table ?", c: `<p>Il n’apparaît pas dans le résultat (comme avec <code>JOIN</code> en SQL). Dans une vraie base, la contrainte de référence empêche d’ailleurs ce cas.</p>` }
      ] }
  ],
  ecrit: { titre: "La base d’un ciné-club", points: "≈ 6 points · 45 min", note: "Exercice inventé pour le site, au format de l’épreuve écrite. Tous les résultats ont été vérifiés avec SQLite.",
    enonce: `<p>Un ciné-club gère sa programmation avec trois relations :</p><p class="mono petit">Realisateur(<u>id_real</u>, nom, pays)<br>Film(<u>id_film</u>, titre, annee, #id_real)<br>Seance(<u>id_seance</u>, #id_film, salle, jour)</p><details class="repli"><summary>Le contenu de la base</summary><div class="corps">[[c6-cine]]</div></details>`,
    questions: [
      { q: "Donner la clé primaire et la ou les clés étrangères de la relation Seance. À quoi sert <code>id_film</code> ?", pts: "0,5 pt", c: `<p>Clé primaire : <code>id_seance</code>. Clé étrangère : <code>id_film</code>, qui fait référence à <code>Film.id_film</code> : elle indique quel film est projeté.</p>` },
      { q: "Écrire une requête qui donne le titre et l’année des films sortis de 1930 à 1939, du plus ancien au plus récent.", pts: "1 pt", c: `[[c6-e1]]` },
      { q: "Écrire une requête qui donne le nombre de séances prévues en salle 2.", pts: "0,75 pt", c: `[[c6-e2]]` },
      { q: "Écrire une requête qui donne, sans doublon, le titre et le nom du réalisateur des films projetés le samedi.", pts: "1,5 pt", c: `<p>Deux jointures : Seance → Film → Realisateur.</p>[[c6-e3]]` },
      { q: "On exécute <code>INSERT INTO Seance VALUES (7, 9, 1, 'lundi')</code>. La base refuse. Pourquoi ?", pts: "0,5 pt", c: `[[c6-e4]]<p>Aucun film n’a la clé 9 : la contrainte de référence (clé étrangère) est violée.</p>` },
      { q: "La salle 3 ferme pour travaux. Écrire la requête qui déplace toutes ses séances en salle 1.", pts: "0,75 pt", c: `[[c6-e5]]` },
      { q: "On veut supprimer le réalisateur Chaplin (id_real = 3). Pourquoi <code>DELETE FROM Realisateur WHERE id_real = 3</code> échoue-t-il ? Écrire, dans l’ordre, les requêtes qui permettent de le supprimer avec ses films et leurs séances.", pts: "1 pt", c: `<p>Ses films y font référence (et leurs séances font référence aux films) : il faut supprimer dans l’ordre inverse des références. La première requête utilise une sous-requête ; on peut aussi écrire <code>DELETE FROM Seance WHERE id_film = 4 OR id_film = 6</code>.</p>[[c6-e6]]` }
    ],
    methode: `<p>Pour écrire une requête : 1) quelles colonnes en sortie (SELECT) ; 2) quelles tables les contiennent (FROM + JOIN, en suivant les clés étrangères) ; 3) quelles lignes (WHERE) ; 4) quel ordre (ORDER BY), sans doublon (DISTINCT) ? Préfixe les attributs par leur table dès qu’il y a une jointure.</p>` },
  qcm: [
    { q: "Dans le modèle relationnel, une relation est…", c: ["un lien entre deux tables", "une table : un ensemble de n-uplets", "une requête SQL", "une clé étrangère"], a: 1, e: "Relation = table ; ses lignes sont des n-uplets (enregistrements).", ref: "i2" },
    { q: "Qu’est-ce qu’un domaine ?", c: ["Le nom de la base", "L’ensemble des valeurs que peut prendre un attribut", "Une ligne de la table", "Un serveur"], a: 1, e: "Par exemple entier, texte, date.", ref: "i2" },
    { q: "Une clé primaire…", c: ["peut prendre deux fois la même valeur", "identifie de façon unique chaque ligne de sa table", "fait référence à une autre table", "est toujours un texte"], a: 1, e: "Contrainte de relation : unique et non vide.", ref: "i3" },
    { q: "Dans <code>Livre(id_livre, titre, annee, #id_auteur)</code>, que désigne <code>#id_auteur</code> ?", c: ["La clé primaire de Livre", "Une clé étrangère vers Auteur", "Un commentaire", "Un attribut calculé"], a: 1, e: "Elle contient la clé primaire d’une ligne d’Auteur.", ref: "i3" },
    { q: "Insérer un livre avec un <code>id_auteur</code> qui n’existe pas viole…", c: ["la contrainte de domaine", "la contrainte de relation", "la contrainte de référence", "aucune contrainte"], a: 2, e: "La clé étrangère doit désigner une ligne existante.", ref: "i4" },
    { q: "Une table qui répète l’année de naissance de l’auteur pour chacun de ses livres présente…", c: ["une redondance, source d’anomalies de mise à jour", "une jointure", "une clé étrangère", "aucun défaut"], a: 0, e: "Une modification oubliée dans une copie rend la base contradictoire.", ref: "i5" },
    { q: "Quelle clause filtre les lignes ?", c: ["SELECT", "FROM", "WHERE", "ORDER BY"], a: 2, e: "SELECT choisit les colonnes, WHERE les lignes.", ref: "i6" },
    { q: "Que renvoie <code>SELECT COUNT(*) FROM Livre WHERE id_auteur = 2</code> sur la base du chapitre ?", c: ["1", "2", "3", "4"], a: 1, e: "Sand a deux livres : Indiana et La Mare au diable.", ref: "i6" },
    { q: "Quel mot-clé supprime les doublons d’un résultat ?", c: ["UNIQUE", "DISTINCT", "SINGLE", "ORDER BY"], a: 1, e: "<code>SELECT DISTINCT …</code>.", ref: "i6" },
    { q: "Quelle est la bonne condition de jointure entre Livre et Auteur ?", c: ["<code>ON Livre.id_livre = Auteur.id_auteur</code>", "<code>ON Livre.id_auteur = Auteur.id_auteur</code>", "<code>ON Livre.titre = Auteur.nom</code>", "Aucune condition n’est nécessaire"], a: 1, e: "Clé étrangère de Livre = clé primaire d’Auteur.", ref: "i7" },
    { q: "Sans condition ON, une jointure entre 8 livres et 5 auteurs donne…", c: ["8 lignes", "5 lignes", "13 lignes", "40 lignes"], a: 3, e: "Chaque ligne est associée à chaque ligne : produit cartésien.", ref: "i7" },
    { q: "Que fait <code>DELETE FROM Emprunt</code> sans WHERE ?", c: ["Rien", "Supprime la table et sa structure", "Supprime toutes les lignes de la table", "Provoque une erreur"], a: 2, e: "La table reste (sa structure), mais elle est vidée.", ref: "i8" },
    { q: "Lequel n’est pas un service rendu par un SGBD ?", c: ["La persistance des données", "La gestion des accès concurrents", "La sécurisation des accès", "La compilation des programmes Python"], a: 3, e: "Les quatre services au programme : persistance, concurrence, efficacité, sécurité.", ref: "i9" }
  ],
  cartes: [
    { r: "Relation", v: "Table : ensemble de n-uplets (lignes) décrits par des attributs (colonnes)." },
    { r: "Attribut / domaine", v: "Colonne d’une relation / ensemble des valeurs permises (entier, texte, date…)." },
    { r: "Clé primaire", v: "Attribut(s) qui identifient de façon unique chaque ligne. Unique, non vide." },
    { r: "Clé étrangère", v: "Attribut qui contient la clé primaire d’une ligne d’une autre table. Notée # dans un schéma." },
    { r: "Schéma relationnel", v: "Structure de la base : relations, attributs, domaines, clés. Ex. <code>Livre(<u>id_livre</u>, titre, #id_auteur)</code>." },
    { r: "Les 3 contraintes d’intégrité", v: "Domaine (bon type), relation (clé primaire unique), référence (clé étrangère existante)." },
    { r: "Anomalies de conception", v: "Redondance ; anomalies d’insertion, de suppression, de mise à jour. Remède : découper en tables reliées par des clés." },
    { r: "Ordre d’une requête", v: "<code>SELECT … FROM … JOIN … ON … WHERE … ORDER BY …</code>" },
    { r: "Fonctions d’agrégation", v: "COUNT, SUM, AVG, MIN, MAX. Sans GROUP BY (hors programme)." },
    { r: "Jointure", v: "<code>FROM A JOIN B ON A.cle_etrangere = B.cle_primaire</code> : assemble les lignes qui se correspondent." },
    { r: "Produit cartésien", v: "Jointure sans condition : chaque ligne avec chaque ligne (n × m lignes)." },
    { r: "INSERT / UPDATE / DELETE", v: "<code>INSERT INTO T VALUES (…)</code> ; <code>UPDATE T SET a = v WHERE …</code> ; <code>DELETE FROM T WHERE …</code>." },
    { r: "SGBD : 4 services", v: "Persistance, gestion des accès concurrents, efficacité des requêtes, sécurisation des accès." },
    { r: "SQL depuis Python", v: "<code>import sqlite3</code> ; <code>base.execute(requete, (valeur,))</code> avec des <code>?</code>." },
    { r: "Edgar F. Codd, 1970", v: "Chercheur d’IBM, auteur du modèle relationnel." }
  ]
});
