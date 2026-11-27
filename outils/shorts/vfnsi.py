"""Short « NSI : vrai ou faux ? » (spécialité NSI de Terminale), format 4 : cinq affirmations, habillage néon,
musique hardtekk2.

La chaîne n'a pas de cours de NSI : thèmes du programme officiel de Terminale (BO spécial n° 8 du 25 juillet 2019 :
réseaux et protocoles, histoire de l'informatique, calculabilité et décidabilité), faits vérifiés le 27/11/2026 :
1. FAUX — Internet et le Web ne sont pas la même chose : Internet est le réseau (conçu à partir de 1973, en service
   en 1983) ; le Web est un service qui l'utilise, proposé par Tim Berners-Lee au CERN en mars 1989 ; le courrier
   électronique passe par Internet sans passer par le Web (CERN, « A short history of the Web »,
   home.cern/science/computing/birth-web/short-history-web).
2. VRAI — une adresse IPv4 tient sur 32 bits, soit 4 octets (RFC 791, septembre 1981 : « Addresses are fixed length
   of four octets (32 bits) ») ; 2**32 = 4 294 967 296 adresses (calculé) ; IPv6 a été créé pour en avoir davantage.
3. FAUX — le mot « bug » ne vient pas de l'insecte de 1947 : le 9 septembre 1947, l'équipe du Harvard Mark II trouve
   une mite coincée dans le relais n° 70 et la colle dans le journal avec la mention « First actual case of bug being
   found » (Smithsonian, National Museum of American History, objet 1994.0191.01 ; Computer History Museum, « This Day
   in History », 9 septembre) : « actual » montre que le mot existait déjà. Thomas Edison l'emploie dans ses lettres
   de 1878 (IEEE Spectrum, « Did You Know? Edison Coined the Term "Bug" » ; l'OED cite même 1875 : non dit).
   Le journal n'était probablement pas celui de Grace Hopper (Smithsonian) : la voix ne la nomme pas.
4. VRAI — Ada Lovelace publie en 1843, dans ses notes sur la machine analytique de Charles Babbage (Note G),
   un algorithme de calcul des nombres de Bernoulli, considéré comme le premier programme publié ; la machine n'a
   jamais été construite (Scientific American ; Wikipédia « Note G » ; certains historiens rappellent que Babbage
   avait écrit des programmes non publiés, d'où « publié » dans l'affirmation).
5. FAUX — il existe des problèmes qu'aucun programme ne résout, quel que soit le temps : le problème de l'arrêt est
   indécidable (programme de Terminale : « montrer, sans formalisme théorique, que le problème de l'arrêt est
   indécidable » ; Turing, 1936).
Écartés : « le premier bug était un vrai insecte » dit tel quel (formule ambiguë : l'insecte est réel mais le mot est
plus ancien), l'épuisement des adresses IPv4 (dates différentes selon les registres), Tim Berners-Lee nommé
(la date suffit).
Images : outils/shorts/img/ (Wikimedia Commons, licences dans vfnsi.plan.js et la description).
"""
CODE = "vfnsi"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"IPv4": "i-pé-vé-quatre", "IPv6": "i-pé-vé-six", "Web": "ouèbe", "bug": "beugue", "bugs": "beugues",
                 "Edison": "Édissonne", "Lovelace": "Lovelèsse", "19e": "dix-neuvième",
                 "4": "quatre", "5": "cinq", "32": "trente-deux",
                 "1843": "dix-huit cent quarante-trois", "1878": "dix-huit cent soixante-dix-huit",
                 "1947": "mille neuf cent quarante-sept", "1989": "mille neuf cent quatre-vingt-neuf"}
PASSAGES = [
    ("v1", "5 affirmations sur l'informatique. Combien tu en as justes ?", 0.3),
    ("v2", "Top chrono.", 0.3),
    ("a1", "Première. Internet et le Web, c'est la même chose. Vrai… ou faux ?", 1.8),
    ("b1", "Faux. Internet, c'est le réseau. Le Web, inventé en 1989, n'est qu'un service posé dessus. Comme le mail.", 0.3),
    ("a2", "Deuxième. Une adresse IPv4 tient sur 32 bits. Vrai… ou faux ?", 1.8),
    ("b2", "Vrai. 4 octets : un peu plus de 4 milliards d'adresses. Trop peu pour la planète, d'où l'IPv6.", 0.3),
    ("a3", "Troisième. Le mot bug vient d'un vrai insecte, trouvé dans un ordinateur en 1947. Vrai… ou faux ?", 1.8),
    ("b3", "Faux ! L'insecte est réel : une mite, coincée dans un relais. Mais Edison parlait déjà de bugs en 1878.", 0.3),
    ("a4", "Quatrième. Le premier programme publié a été écrit par une femme, au 19e siècle. Vrai… ou faux ?", 1.8),
    ("b4", "Vrai. Ada Lovelace, en 1843. Un algorithme pour une machine… qui n'a jamais été construite.", 0.3),
    ("a5", "Dernière. Avec assez de temps, un ordinateur peut résoudre n'importe quel problème. Vrai… ou faux ?", 1.8),
    ("b5", "Faux. Aucun programme ne peut prédire si n'importe quel programme s'arrête. Le problème de l'arrêt est indécidable.", 0.3),
    ("e1", "Alors, ton score ? Dis-le en commentaire.", 0.3),
    ("e2", "Plus de défis sur Révisions Animées.", 0.0),
]
