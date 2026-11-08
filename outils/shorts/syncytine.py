"""Short « Sans un virus, tu ne serais pas né » (SVT, chapitre 2 « La complexification des génomes ») : le gène
de la syncytine, venu d'un rétrovirus, raconté à la deuxième personne.

Faits du cours (svt/index.html, page t2, « D. Les transferts viraux » ; script outils/serie-svt/svt_ch2.py) :
- un rétrovirus intègre son ADN (après transcription inverse) dans le génome de la cellule hôte ;
- s'il infecte une cellule de la lignée germinale, l'ADN viral intégré se transmet à la descendance « comme n'importe
  quel gène » : « c'est ce qui s'est produit chez un ancêtre des primates » (transfert horizontal puis transmission
  verticale) ; « gènes viraux intégrés depuis des millions d'années » ;
- les protéines ENV de rétrovirus comme MSRV font fusionner l'enveloppe du virus avec la membrane des cellules
  qu'ils infectent ; les syncytines font fusionner des membranes de cellules lors de la formation du placenta ;
- syncytine 1 : gène ENW1, chromosome 7 ; syncytine 1 / MSRV : 87 % de similitude (correction du TP), syncytine 2 /
  MSRV : 20 % (non utilisée ici) ; le gène de la syncytine est « devenu indispensable à la formation du placenta » ;
- syncytines présentes aussi chez les rongeurs ; près de 8 % du génome humain d'origine virale (« 8 à 10 % » ailleurs
  dans la page : le short dit « près de 8 % ») ; conclusion : transfert horizontal de gène viral.

Faits hors cours, vérifiés :
- Ancienneté : l'intégration du rétrovirus à l'origine de la syncytine 1 (famille HERV-W) date de plus de 25 et de
  moins de 40 millions d'années selon les sources (Atlas of Genetics and Cytogenetics in Oncology, fiche ERVW-1 ;
  Protein Spotlight, n° 50) ; le gène n'est conservé que chez les hominoïdes : le short dit seulement « des
  millions d'années » et « un singe, ton ancêtre ».
- Souris : A. Dupressoir et al., « Syncytin-A knockout mice demonstrate the critical role in placentation of a
  fusogenic, endogenous retrovirus-derived, envelope gene », PNAS, 2009, 106 (29), p. 12127-12132 : les embryons
  privés des deux copies de la syncytine A meurent in utero entre 11,5 et 13,5 jours de gestation (défaut de fusion
  des cellules du trophoblaste) ; commentaire de J. Stoye dans le même numéro.

Écartés : la découverte « par l'équipe de Thierry Heidmann en 2000 » (la syncytine 1 a été décrite en 2000 par
S. Mi et al., Nature, et J.-L. Blond et al., J. Virol. ; l'équipe de T. Heidmann a décrit la syncytine 2 en 2003 et
les syncytines de souris) ; une date précise d'infection (les estimations divergent) ; la fusion « des cellules de
l'embryon et des cellules maternelles » écrite dans le cours (le syncytiotrophoblaste naît de la fusion de cellules
du trophoblaste, d'origine embryonnaire) : le short dit seulement « elle a fait fusionner des cellules ».
"""
CODE = "syncytine"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"syncytine": "sincitine", "MSRV": "aime esse erre vé", "87": "quatre-vingt-sept",
                 "7": "sept", "8": "huit", "1": "un"}
PASSAGES = [
    ("s1", "Sans un virus, tu ne serais pas né.", 0.3),
    ("s2", "Pas malgré lui. Grâce à lui.", 0.35),
    ("s3", "Il y a des millions d'années, un virus infecte un singe. Ton ancêtre.", 0.15),
    ("s4", "Un rétrovirus : il glisse ses gènes dans l'ADN de la cellule.", 0.2),
    ("s5", "Mais cette fois, il touche une cellule qui va donner un ovule… ou un spermatozoïde.", 0.25),
    ("s6", "Le gène du virus passe aux enfants. Génération après génération.", 0.2),
    ("s7", "Ce gène fabrique une protéine qui fusionne les membranes. L'arme du virus pour entrer.", 0.3),
    ("s8", "Aujourd'hui, ce gène est toujours là. Dans ton ADN. Chromosome 7.", 0.2),
    ("s9", "Son nom : la syncytine.", 0.25),
    ("s10", "Quand tu étais embryon, elle a fusionné des cellules pour construire… ton placenta.", 0.3),
    ("s11", "L'organe qui t'a relié à ta mère.", 0.3),
    ("s12", "Des souris privées d'une syncytine ? Leurs embryons meurent avant de naître.", 0.4),
    ("s13", "La preuve ? On compare ta syncytine 1 à une protéine du virus MSRV.", 0.2),
    ("s14", "87 pour cent de ressemblance. Entre un virus et toi !", 0.3),
    ("s15", "Ça s'appelle un transfert horizontal de gènes. Près de 8 pour cent de ton ADN vient de virus.", 0.3),
    ("s16", "Montrez que des transferts horizontaux ont contribué à la diversification des génomes : sujet type bac. La réponse est sur Révisions Animées.", 0.3),
    ("s17", "La prochaine fois que tu maudis un virus… sans un virus, tu ne serais pas né.", 0.0),
]
