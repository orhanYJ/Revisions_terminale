"""Short « Sauf les amis » (histoire, les régimes totalitaires) : l'assassinat de Léon Trotski à Mexico, août 1940.

Le cours (chapitre « Les régimes totalitaires ») : en octobre 1917, les bolcheviks menés par Lénine et Trotski prennent
le pouvoir ; Trotski dirige l'Armée rouge pendant la guerre civile ; en URSS, la lutte se joue à l'intérieur du parti,
Trotski est expulsé en 1929 ; « la terreur n'est pas un échec de l'ordre mais une méthode de gouvernement » ;
« la terreur se retourne contre les hommes du régime, et c'est ce qui la rend totale » : « la terreur atteint même
l'étranger : Léon Trotski, le rival le plus influent de Staline, est assassiné au Mexique en 1940 par un agent de la
police soviétique » ; procès de Moscou et Grande Purge (1937-1938).

Faits du récit, pris hors du cours et vérifiés :
- History.com, Christopher Klein, « The Trotsky Assassination, 75 Years Ago » (history.com/articles/the-trotsky-
  assassination-75-years-ago) : exclu du Politburo et du parti, exilé au Kazakhstan, banni d'URSS en 1929 ; environ
  quatre ans en Turquie, passages en France et en Norvège ; asile au Mexique (1936), maison de Coyoacán à Mexico, hauts
  murs et gardes armés ; le 24 mai 1940, une vingtaine d'hommes armés mitraillent la maison et le manquent ; on relève
  alors les murs, on mure des fenêtres, on ajoute des miradors ; Ramón Mercader, communiste espagnol recruté par le
  NKVD, se fait appeler Jacques Mornard ; il séduit Sylvia Ageloff, militante trotskiste, et passe par elle pour entrer
  dans la maison ; dans les semaines qui précèdent, les gardes le voient « comme un membre de la famille » ; le 20 août
  1940, il arrive avec un imperméable sur le bras, inhabituel par ce temps ensoleillé, et un article à faire relire ;
  dans le bureau, il frappe Trotski avec un piolet au manche raccourci ; Trotski se débat, les gardes accourent ;
  il meurt le soir du 21 août 1940 ; Mercader est libéré en 1960 et fait héros de l'Union soviétique.
- Wikipédia (« Assassination of Leon Trotsky », « Ramón Mercader ») et World Socialist Web Site (récits de 2020) :
  mêmes dates ; raid de mai mené par le peintre Siqueiros ; Mercader condamné à 20 ans de prison, libéré en 1960.
Écartés : la blessure, le sang et les derniers mots (sordide inutile) ; le petit-fils blessé au pied et la façon dont le
couple s'est protégé en mai (récits divergents) ; le nom de Siqueiros et de Sylvia Ageloff (on dit « une militante ») ;
la condamnation de Mercader (date incertaine : 1940 ou 1943 selon les sources) ; la condamnation à mort
par contumace ; la médaille secrète de 1940.
Lien : chapitre « Les régimes totalitaires », partie sur la terreur. La dernière phrase relance la première.
"""
CODE = "trotski"
TEMPO = 1.0
VOIX = "energique"   # voix des shorts choisie par Cengiz le 08/11/2026 (voix C)
CIBLE = 75           # durée visée en secondes (accélération calculée, au plus 15 %)
PRONONCIATION = {"Mercader": "Mèrcadère", "Ramón": "Ramone", "Mornard": "Mornar",
                 "NKVD": "ènne ka vé dé", "Coyoacán": "Coyoacane",
                 "1917": "mille neuf cent dix-sept", "1929": "mille neuf cent vingt-neuf",
                 "1940": "mille neuf cent quarante", "20": "vingt"}
PASSAGES = [
    ("s1", "Tu as commandé l'Armée rouge… et maintenant, tu te caches derrière des murs ?", 0.35),
    ("s2", "Mexico, 1940. Tu es Léon Trotski.", 0.25),
    ("s3", "1917 : avec Lénine, tu fais la révolution. Puis tu commandes l'Armée rouge.", 0.2),
    ("s4", "Mais Staline prend le pouvoir. Ton rival.", 0.25),
    ("s5", "Chassé du parti. En 1929, chassé d'URSS.", 0.2),
    ("s6", "Turquie. France. Norvège. Mexique. Staline ne t'oublie pas.", 0.3),
    ("s7", "Mai 1940. Une nuit, des hommes armés mitraillent ta maison.", 0.3),
    ("s8", "Tu survis. On relève les murs. On ajoute des miradors.", 0.2),
    ("s9", "Ta maison devient une forteresse. Personne n'entre… sauf les amis.", 0.35),
    ("s10", "Un jeune homme, Jacques Mornard, sort avec une de tes militantes.", 0.2),
    ("s11", "Il vient souvent. Les gardes le traitent comme un proche.", 0.25),
    ("s12", "20 août 1940. Il t'apporte un article à relire. Et un imperméable au bras. En plein soleil.", 0.3),
    ("s13", "Seuls, dans ton bureau. Tu te penches sur le texte.", 0.35),
    ("s14", "Sous l'imperméable : un piolet.", 0.45),
    ("s15", "Tu te débats. Les gardes accourent. Tu meurs le lendemain.", 0.3),
    ("s16", "Son vrai nom : Ramón Mercader. Agent du NKVD, la police de Staline.", 0.3),
    ("s17", "Même au bout du monde, la terreur frappe. Même les anciens chefs du régime.", 0.3),
    ("s18", "En quoi la terreur est-elle au cœur du régime stalinien ? Une question de bac. La réponse est sur Révisions Animées.", 0.3),
    ("s19", "Et toi… à qui tu aurais ouvert la porte ?", 0.0),
]
