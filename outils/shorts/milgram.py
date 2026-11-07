"""Short « Tu aurais appuyé ? » (philo, le devoir) : l'expérience de Milgram racontée à la deuxième personne.

Faits vérifiés sur l'article original : S. Milgram, « Behavioral Study of Obedience », Journal of Abnormal and
Social Psychology, 1963, 67 (4), p. 371-378 : 40 hommes de 20 à 50 ans recrutés par annonce, payés 4,50 dollars ;
« élève » joué par un comptable de 47 ans, complice, attaché sur une chaise, électrode au poignet ; 30 interrupteurs
de 15 à 450 volts (« Danger : choc violent », puis « XXX ») ; à 300 volts il cogne contre le mur et ne répond plus,
de nouveau à 315 volts, puis plus rien ; l'expérimentateur en blouse grise ; quatre incitations (« Veuillez
continuer », « L'expérience exige que vous continuiez », « Il est absolument indispensable que vous continuiez »,
« Vous n'avez pas le choix, vous devez continuer ») ; 14 étudiants de Yale prédisaient de 0 à 3 % (moyenne 1,2 %) ;
26 sur 40 vont jusqu'à 450 volts ; sueur, tremblements, rires nerveux (14 sur 40), 3 crises. L'article s'ouvre sur
les camps de la mort nazis. Lien avec la série « Le devoir », épisode 5 (Eichmann, Arendt, Milgram).
"""
CODE = "milgram"
TEMPO = 1.1
PRONONCIATION = {"Yale": "Yèle", "Milgram": "Milgrame", "450": "quatre cent cinquante", "15": "quinze",
                 "45": "quarante-cinq", "75": "soixante-quinze", "150": "cent cinquante", "300": "trois cents",
                 "315": "trois cent quinze", "1961": "mille neuf cent soixante et un", "26": "vingt-six", "40": "quarante"}
PASSAGES = [
    ("s1", "Est-ce que tu enverrais 450 volts à un inconnu… juste parce qu'on te le demande ?", 0.3),
    ("s2", "Non ? Eux aussi, ils pensaient que non.", 0.4),
    ("s3", "1961, université Yale. Une petite annonce : quatre dollars cinquante pour une expérience sur la mémoire.", 0.15),
    ("s4", "Dans la pièce d'à côté, un homme est attaché sur une chaise. Une électrode au poignet.", 0.15),
    ("s5", "Toi, tu poses les questions. À chaque erreur, tu appuies. Et à chaque erreur… 15 volts de plus.", 0.2),
    ("s6", "45 volts. 75. 150.", 0.25),
    ("s7", "À 300 volts, l'homme cogne contre le mur.", 0.3),
    ("s8", "Tu te retournes. Un homme en blouse grise te dit, calmement : veuillez continuer.", 0.2),
    ("s9", "315 volts. Il cogne encore. Puis… plus rien. Le silence.", 0.45),
    ("s10", "L'expérience exige que vous continuiez. Vous n'avez pas le choix.", 0.3),
    ("s11", "Avant l'expérience, des étudiants de Yale l'avaient prédit : à peine une personne sur cent irait jusqu'au bout.", 0.2),
    ("s12", "Résultat : 26 sur 40. Presque deux sur trois. Jusqu'à 450 volts.", 0.3),
    ("s13", "Ils transpirent, ils tremblent, certains éclatent d'un rire nerveux… mais ils appuient.", 0.35),
    ("s14", "Le plus fou ? L'homme était un acteur. Il n'a jamais reçu la moindre décharge. Eux ne le savaient pas.", 0.3),
    ("s15", "Milgram voulait comprendre une chose : comment des gens ordinaires avaient pu obéir aux nazis.", 0.3),
    ("s16", "Obéir, est-ce faire son devoir ? C'est une vraie question de bac. La réponse est sur Révisions Animées.", 0.3),
    ("s17", "Et toi… tu aurais appuyé ?", 0.0),
]
