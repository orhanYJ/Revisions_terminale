"""Short « Ta main gauche choisit une pelle » (philo, la conscience) : le patient au cerveau divisé P.S. et
« l'interprète » de l'hémisphère gauche, racontés à la deuxième personne.

Faits vérifiés :
- M. S. Gazzaniga, « Principles of Human Brain Organization Derived from Split-Brain Studies », Neuron, 1995,
  14, p. 217-228 : patients opérés (section du corps calleux) pour une épilepsie rebelle ; test des deux
  concepts simultanés : une patte de poulet (« chicken claw ») montrée en éclair à l'hémisphère gauche, une scène
  de neige à l'hémisphère droit ; images à choisir posées devant le patient ; le cas P.S. prend la pelle de la
  main gauche et le poulet de la main droite ; l'hémisphère gauche répond : « Oh, that's simple. The chicken
  claw goes with the chicken, and you need a shovel to clean out the chicken shed. » ; « We called this left
  hemisphere process the "interpreter." »
- M. S. Gazzaniga, « Forty-five years of split-brain research and still going strong », Nature Reviews
  Neuroscience, 2005, 6, p. 653-659 : la parole n'est produite que par l'hémisphère gauche chez la plupart des
  gens ; Gazzaniga commence ces études avec Roger Sperry ; le concept d'« interprète » est introduit par
  Gazzaniga et LeDoux dans The Integrated Mind (1978), d'où « années 1970 ».
- Le cerveau à tous les niveaux (Université McGill), module « Ce que les cerveaux divisés nous apprennent sur le
  langage » : champ visuel gauche → hémisphère droit ; main gauche commandée par l'hémisphère droit ; après
  l'opération, la vie quotidienne de ces patients est presque inchangée.
- Prix Nobel de physiologie ou médecine 1981 : Roger W. Sperry, « pour ses découvertes sur la spécialisation
  fonctionnelle des hémisphères cérébraux » (nobelprize.org).
- Corps calleux : environ 200 millions de fibres (axones), estimation d'Aboitiz et al., 1992.
Cette expérience n'est pas dans la série « La conscience » : le short pose la question du bac et renvoie à la
série (Descartes, Freud, Nietzsche) pour la réponse philosophique.
"""
CODE = "cerveau"
TEMPO = 1.1
ACCEL = 1.1
PRONONCIATION = {"Gazzaniga": "Gazaniga", "Sperry": "Spéri", "P.S.": "Pé Esse", "1970": "mille neuf cent soixante-dix",
                 "200": "deux cents"}
PASSAGES = [
    ("s1", "Ta main gauche choisit une pelle. Tu ne sais pas pourquoi.", 0.3),
    ("s2", "Et pourtant… tu vas l'expliquer.", 0.45),
    ("s3", "Années 1970. Tu es le patient P.S. Pour stopper ton épilepsie, on t'opère.", 0.15),
    ("s4", "On coupe ton corps calleux : le pont entre les deux moitiés du cerveau.", 0.2),
    ("s5", "200 millions de fibres. Tes deux moitiés ne se parlent plus.", 0.3),
    ("s6", "Au quotidien ? Presque rien ne change.", 0.3),
    ("s7", "Michael Gazzaniga, élève du futur Nobel Roger Sperry, te fait passer un test.", 0.2),
    ("s8", "Tu fixes un point sur un écran. Deux images, en un éclair.", 0.2),
    ("s9", "Le secret : l'image de gauche ne va que dans ton cerveau droit.", 0.25),
    ("s10", "Ton cerveau gauche voit une patte de poulet. Le droit, un paysage de neige.", 0.25),
    ("s11", "Devant toi, des images. Ta main droite montre le poulet. Ta main gauche… la pelle.", 0.3),
    ("s12", "Logique. Sauf que ton cerveau droit ne parle pas.", 0.3),
    ("s13", "On te demande pourquoi. Ton cerveau gauche répond. Lui n'a jamais vu la neige.", 0.4),
    ("s14", "Oh, c'est simple. La patte va avec le poulet, et il faut une pelle pour nettoyer le poulailler.", 0.45),
    ("s15", "Il invente. Aussitôt. Gazzaniga appelle ça : l'interprète.", 0.3),
    ("s16", "Et si, toi aussi, tu expliquais tes choix après coup ?", 0.3),
    ("s17", "Suis-je ce que j'ai conscience d'être ? Question de bac. Descartes, Freud et Nietzsche y répondent sur Révisions Animées.", 0.3),
    ("s18", "Alors… ta main gauche. Pourquoi la pelle ?", 0.0),
]
