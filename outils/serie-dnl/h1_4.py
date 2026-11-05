"""DNL History · H1 « The Wall Street Crash and its Impact » — série vidéo, épisode 4 : « Democracies and the liberal order »
(partie II.3 du cours, « Great democracies reluctant to defend the Liberal order established in 1919 »).

Même chaîne que les épisodes H3 (voir outils/serie-dnl/h3_1.py) : outils/serie-philo/generer.py h1_4 ; sortie dans dnl/serie/.
Cartes animées (sc = numéros de scènes dans l'ordre chronologique de la carte) :
  H1 : 0 l'ordre libéral de 1919 · 18 Mandchourie, la SDN impuissante · 20 doctrine Stimson, Shanghai ·
       26 Neutrality Acts, USS Panay · 27 Éthiopie · 29 Rhénanie · 30 Anschluss et Munich · 31 Prague puis la Pologne ·
       32 cash and carry
Contenu : les huit idées de la partie II.3 dans le site (dnl/index.html, CHAPTERS.H1), les schémas H1League (faiblesses
structurelles / causes contextuelles), H1SlideAnim (les marches vers la guerre, 1931-1939) et H1Check (points à vérifier),
la carte d'essai du Key Issue « Blame for the origins of WWII lies in part with the great democratic powers themselves ».
Les dessins de David Low (The Doormat, Stepping Stones to Glory) ne sont pas dans le domaine public : décrits, pas montrés.
Hors cours, dit comme tel : Henry Cabot Lodge, le détail des Neutrality Acts de 1936 et 1937, le pacte anti-Komintern et le
pacte tripartite (1940), « peace for our time ». Corrections du cours dites sobrement : Hoover n'était pas un adversaire
de la SDN (il en défendait l'adhésion, avec réserves) ; la loi de 1937 n'imposait pas un embargo sur tout le commerce.
Le sujet d'essay vient du cours (Key Issue) ; le modèle de réponse suit la carte d'essai du site, écrit pour la vidéo.
"""

SITE = "dnl"
LANGUE = "en"
CODE = "h1-4"
NOTION = "The Wall Street Crash"
NUM = 4
TITRE = "Democracies and the liberal order"
SUIVANT = "Episode 5 · The crisis at the exam: essay and DBQ"
PRONONCIATION = {"Mukden": "Mook-den", "Manchukuo": "Man-choo-kwo", "Lytton": "Litten", "Kellogg": "Kellog",
                 "Briand": "Bree-on", "Stimson": "Stim-son", "Panay": "Pa-nye", "Daladier": "Da-la-dyay",
                 "Anschluss": "Ahn-shloos", "Sudeten": "Soo-day-ten", "Sudetenland": "Soo-day-ten-land",
                 "Vandenberg": "Vanden-berg", "Raven-Hill": "Raven Hill", "Rhineland": "Rine-land",
                 "Comintern": "Kom-in-tern", "Heston": "Hest-un"}

SCENES = [
    # ================================================================ ouverture
    dict(id="ouverture", chap="Opening", fond="guerre", humeur="mystere", carton=False,
         retenir="The question of this episode: in 1919 the democracies built a liberal world order. Why did they refuse to defend it in the 1930s?",
         beats=[
        "{g0}{q1}The first of September 1939. German troops cross into Poland. Two days later, France and Britain declare war. "
        "Twenty years after the peace of 1919, Europe is at war again.",
        "{-q1}{q2}But the great democracies had won the last war. They had written the peace, and built an order to keep it. "
        "So why did they let it collapse, step by step, without a fight?",
        "{-q2}{-g0}{plan}Here is the plan of this episode. {plan.1}First, the story on the map, from the peace of 1919 to the cash and carry of 1939. "
        "{plan.2}Then the liberal order of 1919, and why the League of Nations failed. "
        "{plan.3}Then America: words without action, then neutrality by law, then the Arsenal of Democracy. "
        "{plan.4}Then Britain and France: appeasement, its six reasons, and its consequences. "
        "{plan.5}And finally, an exam workshop: the key issue of the chapter, as an essay.",
        "{-plan}{titre}",
        ("P", 3.2),
    ], vis={
        "g0": dict(type="globe", code="H1", sc=[31]),
        "q1": dict(type="question", t="1 September 1939: war, again.", bande=True),
        "q2": dict(type="question", t="Why did the democracies let their order collapse?", bande=True),
        "plan": dict(type="liste", titre="Episode 4 · Democracies and the liberal order", items=[
            "On the map: from 1919 to 1939", "The liberal order and the League of Nations",
            "America: words, neutrality, then the Arsenal of Democracy", "Britain and France: appeasement and its consequences",
            "At the exam: the key issue, as an essay"], x=170, y=120, w=940),
        "titre": dict(type="titre", sur="DNL History · H1 · Episode 4", t="Democracies and the liberal order",
                      sous="1919 – 1939 · great democracies reluctant to defend the order of 1919"),
    }),

    # ================================================================ I. sur la carte : de 1919 à Shanghai
    dict(id="carte1", chap="From 1919 to Shanghai, on the map", fond="nuit", humeur="mystere",
         retenir="1918–19 Fourteen Points, Versailles, League of Nations in Geneva; the US Senate refuses · 18 Sept. 1931 Mukden, Manchuria · 7 Jan. 1932 the Stimson note, then Shanghai bombed.",
         beats=[
        "{g1}{g1.1}Nineteen eighteen, nineteen nineteen. The war is over. The American president, Woodrow Wilson, sets out his Fourteen Points: "
        "democracy, the self-determination of peoples, free trade. The Paris Peace Conference, the Treaty of Versailles "
        "and a League of Nations, seated in Geneva, give them institutions. "
        "But in Washington, the Senate refuses to ratify the treaty. The United States will never join the League.",
        "{g1.2}Twelve years later, the eighteenth of September 1931. At Mukden, in Manchuria, Japanese soldiers blow up a section of their own railway, "
        "blame the Chinese, and use it as a pretext to invade. Manchuria becomes a puppet state, Manchukuo. "
        "The League condemns, and Japan simply walks out.",
        "{g1.3}The seventh of January 1932. The American Secretary of State, Henry Stimson, announces that the United States "
        "will recognise no conquest by force in China. Japan answers by bombing Shanghai, with heavy civilian casualties. "
        "{!No American response}No American response follows.",
    ], vis={
        "g1": dict(type="globe", code="H1", sc=[0, 18, 20]),
    }),

    # ================================================================ II. sur la carte : de la neutralité à la guerre
    dict(id="carte2", chap="From neutrality to war, on the map", fond="nuit", humeur="tension",
         retenir="1935–37 Neutrality Acts, USS Panay · Oct. 1935 Ethiopia · 7 March 1936 Rhineland · March 1938 Anschluss, Sept. 1938 Munich · March 1939 Prague, 1 Sept. 1939 Poland · Nov. 1939 cash and carry.",
         beats=[
        "{g2}{g2.1}From 1935 to 1937, the American Congress passes the Neutrality Acts: America will stay out of other people's wars. "
        "In December 1937, Japanese planes sink the American gunboat USS Panay in China. Japan apologises and pays. And it goes further.",
        "{g2.2}October 1935. Mussolini's Italy invades Ethiopia. Britain refuses the oil embargo that would have stopped him.",
        "{g2.3}The seventh of March 1936. Hitler sends troops into the Rhineland, a region demilitarised by the Treaty of Versailles. "
        "France and Britain do not move.",
        "{-g2}{g3}{g3.1}March 1938: Germany annexes Austria, the Anschluss. September 1938: at Munich, the British and French prime ministers, "
        "Chamberlain and Daladier, hand Hitler the Sudetenland, a part of Czechoslovakia.",
        "{g3.2}March 1939: Germany occupies the rest of Czechoslovakia. The first of September: it invades Poland. "
        "France and Britain declare war.",
        "{g3.3}And in November 1939, once the war has begun, Roosevelt obtains a new law: cash and carry. "
        "The democracies may now buy American weapons. Ten years after the Crash, American factories start up again.",
        "{-g3}{fr1}Twenty years in eight dates. Copy them down. {fr1.1}Nineteen nineteen, the League of Nations. "
        "{fr1.2}Nineteen thirty-one, Manchuria. {fr1.3}Nineteen thirty-five, the first Neutrality Act, and Ethiopia. "
        "{fr1.4}Nineteen thirty-six, the Rhineland. {fr1.5}March 1938, the Anschluss. {fr1.6}September 1938, Munich. "
        "{fr1.7}March 1939, Prague. {fr1.8}And the first of September 1939, Poland.",
        ("P", 2.5),
    ], vis={
        "g2": dict(type="globe", code="H1", sc=[26, 27, 29]),
        "g3": dict(type="globe", code="H1", sc=[30, 31, 32]),
        "fr1": dict(type="frise", items=[
            dict(nom="League of Nations", d=1919, q="Geneva; the US stays out"), dict(nom="Manchuria", d=1931, q="18 Sept.: Mukden"),
            dict(nom="Ethiopia", d=1935, q="+ first Neutrality Act"), dict(nom="Rhineland", d=1936, q="7 March"),
            dict(nom="Anschluss", d=1938, q="March"), dict(nom="Munich", d=1938, q="September"),
            dict(nom="Prague", d=1939, q="March"), dict(nom="Poland", d=1939, q="1 September: war"),
        ]),
    }),

    # ================================================================ III. idée 1 : l'ordre libéral de 1919
    dict(id="wilson", chap="II.3 · The liberal order of 1919", fond="nuit", humeur="lumiere",
         retenir="The great democracies of 1919: Britain, France, the United States. Wilsonianism (Fourteen Points, 1918): democracy, self-determination, free trade. Institutions: Paris Peace Conference, Versailles, the League of Nations in Geneva. The US Senate refused to ratify: the US never joined.",
         beats=[
        "{q3}Now the course, idea by idea. First, what exactly were the democracies supposed to defend?",
        "{-q3}{pw}{lo1}The great democracies of 1919 are three: {lo1.1}Britain, {lo1.2}France, {lo1.3}and the United States.",
        "{-lo1}{wi}Their order rests on an idea: {!Wilsonianism}Wilsonianism. In his Fourteen Points speech of 1918, President Woodrow Wilson "
        "carries liberalism into foreign policy, through three principles. {wi.1}Democracy. {wi.2}The self-determination of peoples: "
        "each people should choose its own government. {wi.3}And free trade.",
        "{-wi}{inst}Then the peace gives these principles institutions. {inst.1}The Paris Peace Conference. {inst.2}The Treaty of Versailles. "
        "{inst.3}And the League of Nations, seated in Geneva, to keep the peace by collective security. "
        "This, says the course, is {!the liberal world order}the liberal world order.",
        "{-inst}{-pw}{gap}But its weakness is there from birth. Look at this cartoon from the British magazine Punch, December 1919, shown on Monsieur Ros's slides. "
        "The bridge of the League of Nations, designed by the President of the U.S.A. Belgium, France, England, Italy are in place. "
        "And Uncle Sam lounges on the bank, his feet up, leaning on the missing stone. {!Keystone USA}Keystone: U.S.A.",
        "{-gap}{sen}Why? Because the Republicans held the majority in the Senate, and the Senate refused to ratify the Treaty of Versailles, "
        "which contained the covenant of the League. {sen.1}A small correction here. The course names Hoover among the opponents of the League. "
        "In fact, Hoover himself was in favour of joining, with reservations; the opposition in the Senate was led by Henry Cabot Lodge, "
        "a name from outside the course. {sen.2}The result is the same, and it is the sentence to learn: "
        "the United States never joined the League its own president had conceived.",
    ], vis={
        "q3": dict(type="question", t="What were the democracies supposed to defend?"),
        "pw": dict(type="tableau", img="h1-wilson", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.15, .5, .25],
                   legende="Woodrow Wilson, 1919, by Harris & Ewing (Library of Congress, Wikimedia Commons, public domain)"),
        "lo1": dict(type="liste", titre="The great democracies of 1919", items=["Britain", "France", "The United States"],
                    x=270, y=170, w=740),
        "wi": dict(type="liste", titre="Wilsonianism · the Fourteen Points (1918)", cles=["Democracy", "self-determination", "free"],
                   items=["Democracy", "The self-determination of peoples", "Free trade"], x=270, y=170, w=740),
        "inst": dict(type="liste", titre="The institutions of the liberal order", items=[
            "The Paris Peace Conference", "The Treaty of Versailles", "The League of Nations, seated in Geneva"], x=270, y=170, w=740),
        "gap": dict(type="tableau", img="h1-gap-bridge", de=[1.0, .5, .5], a=[1.25, .78, .4],
                    legende="Leonard Raven-Hill, “The Gap in the Bridge”, Punch, 10 December 1919 (Wikimedia Commons, public domain)"),
        "sen": dict(type="note", terme="The Senate says no", cles=["Senate", "never", "joined"],
                    t="The Republican majority in the Senate refused to ratify Versailles, which contained the League's covenant.",
                    etape="Correction: Hoover favoured joining, with reservations; the opposition was led by Henry Cabot Lodge (outside the course).",
                    x=170, y=200, w=940),
    }),

    # ================================================================ IV. idée 2 : les faiblesses de la SDN
    dict(id="sdn", chap="II.3 · Why the League of Nations failed", fond="nuit", humeur="mystere",
         retenir="Structural weaknesses (from 1919): no US ratification · national before international interests · aggressors undermine it, helped by the depression · no army · a veto for every member, incomplete representation. Contextual (1930s): powerless before Italian, German, Japanese militarism.",
         beats=[
        "{pal}{d2}Second idea. The League of Nations failed, and the course separates two kinds of causes. "
        "{d2.1}Structural weaknesses, present from 1919. And contextual causes, the crises of the 1930s, which exposed them.",
        "{-d2}{str}The structural weaknesses, in the order of the slide. "
        "{str.1}One: the American Congress failed to ratify the Treaty of Versailles, which contained the covenant. "
        "{str.2}Two: member nations refused to put international interests before national ones. "
        "{str.3}Three: aggressor nations undermined its authority, as the depression encouraged states to be more aggressive towards each other. "
        "{str.4}Four: it had {!no army of its own}no army of its own. "
        "{str.5}Five: its voting structure. Every member state had a veto, so resolutions were hard to pass. "
        "And many of the world's nations were not represented at all.",
        "{-str}{ctx}Then the contextual causes. {ctx.1}The League was powerless before Italian militarism, "
        "{ctx.2}before German militarism, {ctx.3}and before Japanese militarism.",
        "{-ctx}{-pal}{lien}The link between the two lists is the key to an essay. {!Inevitable}Do not just list them. "
        "Use the five structural weaknesses to explain why the three failures of the 1930s were inevitable. "
        "A League with no army, where every member had a veto, could not stop a great power that decided to attack.",
        "{-lien}{low1}The British cartoonist David Low drew it in 1933, in a cartoon called The Doormat. We cannot show it here, "
        "so picture it. {low1.1}A Japanese soldier walks over the League of Nations, lying on the ground like a doormat. "
        "{low1.2}The League's officials bow. {low1.3}And the British Foreign Secretary, John Simon, powders the League's nose with a face-saving kit. "
        "The League is humiliated, and it pretends nothing has happened.",
    ], vis={
        "pal": dict(type="tableau", img="h1-palais-nations", fond=True, sombre=True, de=[1.0, .5, .5], a=[1.2, .5, .45],
                    legende="The Palais des Nations, Geneva, built for the League of Nations (1929–1938), photo 2014 (Vassil, Wikimedia Commons, CC0)"),
        "d2": dict(type="cols", g="Structural", gq="weaknesses present from 1919", d="Contextual",
                   dq="the crises of the 1930s, which exposed them", vs="+", repere="Why the League of Nations failed"),
        "str": dict(type="liste", titre="Structural weaknesses (from 1919)", cles=["ratify", "national", "aggressor", "army", "veto"], items=[
            "The US Congress failed to ratify Versailles, which contained the covenant",
            "Members refused to put international interests before national ones",
            "Aggressors undermined its authority, as the depression encouraged aggression",
            "No army of its own",
            "Every member had a veto; representation of the world's nations was incomplete"], x=110, y=110, w=1060),
        "ctx": dict(type="liste", titre="Contextual causes (1930s)", items=[
            "Powerless before Italian militarism", "Powerless before German militarism", "Powerless before Japanese militarism"],
                    x=170, y=160, w=940),
        "lien": dict(type="mot", t="Five weaknesses → three failures", g="the structure explains why the failures were inevitable", y=250, taille=70),
        "low1": dict(type="liste", titre="David Low, “The Doormat” (1933) · described, not shown", items=[
            "A Japanese soldier walks over the League, lying like a doormat", "The League's officials bow",
            "John Simon, British Foreign Secretary, powders its nose: a “face-saving kit”"], x=150, y=150, w=980),
    }),

    # ================================================================ V. idée 3 : la Mandchourie
    dict(id="mandch", chap="II.3 · Manchuria: the League against a great power", fond="nuit", humeur="tension",
         retenir="Korea already Japanese · 18 Sept. 1931 Mukden false flag → Manchukuo, a puppet state · Lytton Commission (report Oct. 1932, adopted Feb. 1933) · Japan quits the League (March 1933) · Hoover: no US military action · Kellogg–Briand (1928): war illegal, no enforcement.",
         beats=[
        "{g4}{mk}Third idea: the League proved unable to stop the aggression of a great power. The test case is Manchuria. "
        "{mk.1}Korea, next door, is already a Japanese possession. "
        "{mk.2}On the eighteenth of September 1931, Japanese soldiers organise a {!false-flag attack}false-flag attack on their own railway, at Mukden. "
        "{mk.3}It is the pretext to invade Manchuria, where they set up Manchukuo, a puppet state. "
        "{mk.4}The League sends an inquiry, the Lytton Commission. Its report comes only in October 1932, and it condemns Japan. "
        "{mk.5}When the League adopts the report, in February 1933, Japan simply leaves the League, in March 1933.",
        "{-mk}{-g4}{hv}And the United States? President Hoover wants no part in any American military action in the Far East.",
        "{-hv}{kb}One more piece of the order collapses here. {!Kellogg–Briand}The Kellogg–Briand Pact of 1928 had declared war illegal, "
        "and bound its signatories to negotiate. {kb.1}But it contained no mechanism to enforce that promise. "
        "Manchuria proved it, three years later.",
        "{-kb}{prom}Remember the formula: {!a promise without a mechanism}a promise without a mechanism.",
    ], vis={
        "g4": dict(type="globe", code="H1", sc=[18]),
        "mk": dict(type="liste", titre="Manchuria, 1931–1933", bande=True, petit=True, x=60, y=110, w=620,
                   cles=["Mukden", "puppet", "Lytton", "leaves"], items=[
                       "Korea: already Japanese", "18 Sept. 1931: false flag at Mukden",
                       "Invasion; Manchukuo, a puppet state", "Lytton Commission: report Oct. 1932, condemns Japan",
                       "Report adopted Feb. 1933 → Japan quits the League (March 1933)"]),
        "hv": dict(type="note", terme="Washington, 1931", cles=["Hoover", "no"],
                   t="President Hoover wants no part in any American military action in the Far East.",
                   etape="The League condemns; nobody acts", x=170, y=220, w=940),
        "kb": dict(type="def", terme="The Kellogg–Briand Pact (1928)", cles=["illegal", "negotiate"],
                   t="A treaty declaring war illegal and binding its signatories to negotiate.",
                   etape="But no mechanism to enforce it", x=170, y=200, w=940),
        "prom": dict(type="mot", t="A promise without a mechanism", g="Kellogg–Briand, 1928 → Manchuria, 1931", y=260, taille=76),
    }),

    # ================================================================ VI. idée 4 : la doctrine Stimson
    dict(id="stimson", chap="II.3 · America: words, not action", fond="nuit", humeur="tension",
         retenir="7 Jan. 1932, the Stimson note: no recognition of any situation brought about by force in China (sovereignty, territorial integrity, the open door). A doctrine of non-recognition, not of action. Japan bombs Shanghai (1932): no American response.",
         beats=[
        "{g5}{st}Fourth idea: the United States condemned aggression in words, but refused to act. "
        "{st.1}On the seventh of January 1932, the Secretary of State, Henry Stimson, sends a note to Japan and China. "
        "{st.2}The United States will not recognise any situation, treaty or agreement brought about by force "
        "that impairs American treaty rights in China. "
        "{st.3}That includes the sovereignty and territorial integrity of the Chinese Republic, "
        "{st.4}and the open door policy, which guaranteed the main powers equal access to commercial opportunities in China.",
        "{-st}{-g5}{od}Notice the American interest here: the open door. Stimson defends a principle of the 1919 order, "
        "but also American trade in China.",
        "{-od}{wa}So what is the Stimson doctrine? {!non-recognition}A doctrine of non-recognition, not of action.",
        "{-wa}{jp}And Japan's answer? {jp.1}Japan is infuriated. It points out that the United States had itself conquered new territories "
        "only a few decades earlier. {jp.2}Then it bombs Shanghai, in 1932, with massive casualties. "
        "{jp.3}No American response follows.",
    ], vis={
        "g5": dict(type="globe", code="H1", sc=[20]),
        "st": dict(type="liste", titre="The Stimson note · 7 January 1932", bande=True, petit=True, x=60, y=110, w=620,
                   cles=["recognise", "force", "open"], items=[
                       "To Japan and China", "No recognition of anything brought about by force",
                       "China's sovereignty and territorial integrity", "The open door: equal commercial access to China"]),
        "od": dict(type="def", terme="The open door policy", cles=["equal", "access"],
                   t="Equal access to commercial opportunities in China for all the main powers.",
                   etape="A principle, and an American trade interest", x=170, y=200, w=940),
        "wa": dict(type="cols", g="Words", gq="“we will not recognise” any conquest by force", d="Action",
                   dq="none: no sanction, no force, no response", vs="≠", repere="The Stimson doctrine"),
        "jp": dict(type="liste", titre="Japan's answer", items=[
            "Infuriated: “the United States conquered territories only decades ago”",
            "1932: Shanghai bombed, massive casualties", "No American response"], x=170, y=160, w=940),
    }),

    # ================================================================ VII. idée 5 : les lois de neutralité
    dict(id="neutre", chap="II.3 · The Neutrality Acts", fond="nuit", humeur="mystere",
         retenir="Isolationism after the Depression: domestic policy first. Neutrality Acts (Nye, Vandenberg): 1935 weapons and funding · 1936 no travel on ships of nations at war · 1937 all trade (course's summary). Roosevelt: “I hate war” (1936). Dec. 1937: USS Panay; Japan apologises, pays — and reads it as a licence.",
         beats=[
        "{fdr}{iso}Fifth idea: the Neutrality Acts made the largest democracy unavailable. "
        "{iso.1}The cause is the Great Depression. The United States turns to {!isolationism}isolationism, and turns a blind eye to international tensions. "
        "{iso.2}Congress and the presidents turn to domestic policy: protectionism, and a welfare state. That was episode three.",
        "{-iso}{na}Isolationist Republicans, among them Senators Gerald Nye and Arthur Vandenberg, pass the Neutrality Acts. "
        "The course gives three steps. {na.1}In 1935, an embargo on weapons and funding to any nation involved in a conflict. "
        "{na.2}In 1936, a ban on Americans travelling aboard ships of nations at war. "
        "{na.3}In 1937, an embargo on all trade with nations at war.",
        "{-na}{prec}Learn the course's summary, but know that historians describe the details a little differently. "
        "{prec.1}The ban on loans came in 1936, and the travel ban only became strict in 1937. "
        "{prec.2}And the law of 1937 did not ban all trade: it let nations at war buy goods other than weapons, if they paid cash "
        "and carried them away themselves. A first cash and carry, two years early. These details are outside the course.",
        "{-prec}{nye}Why such laws? An example: the Nye Committee, from 1934 to 1936, spent two years arguing that arms manufacturers and bankers "
        "had dragged America into the First World War. {nye.1}The Neutrality Acts were written to make sure it could not happen again, "
        "whatever happened in Europe or in Asia.",
        "{-nye}{-fdr}{rw}Even the president speaks the country's mood. In 1936, Franklin Roosevelt says:",
        ("C", "I hate war.", "c_war"),
        "{-c_war}{-rw}{g6}{pn}Then the test. {pn.1}In December 1937, Japan bombs the American gunboat USS Panay, and three American tankers, in China. "
        "{pn.2}Japan apologises, pays an indemnity, and promises no further attacks. "
        "{pn.3}And Japan interprets the American tone as a licence for further aggression.",
        "{-pn}{-g6}",
    ], vis={
        "fdr": dict(type="tableau", img="h1-roosevelt-1933", fond=True, sombre=True, de=[1.0, .5, .3], a=[1.15, .5, .25],
                    legende="Franklin D. Roosevelt, 1933, by Elias Goldensky (Wikimedia Commons, public domain)"),
        "iso": dict(type="liste", titre="America turns inward", cles=["isolationism", "domestic"], items=[
            "After the Depression: isolationism, a blind eye to international tensions",
            "Domestic policy first: protectionism and a welfare state"], x=170, y=170, w=940),
        "na": dict(type="liste", titre="The Neutrality Acts (course)", cles=["1935", "1936", "1937"], items=[
            "1935: embargo on weapons and funding to nations in a conflict",
            "1936: no Americans aboard ships of nations at war",
            "1937: embargo on all trade with nations at war"], x=150, y=150, w=980),
        "prec": dict(type="note", terme="More precisely · outside the course", cles=["loans", "travel", "cash"],
                     t="Loans banned in 1936; the travel ban strict only in 1937.",
                     etape="1937: non-military goods still sold, if paid cash and carried away — a first “cash and carry”.",
                     x=170, y=200, w=940),
        "nye": dict(type="note", terme="The Nye Committee (1934–1936)", cles=["arms", "bankers"],
                    t="Arms manufacturers and bankers, it argued, had dragged America into the First World War.",
                    etape="The Neutrality Acts: never again", x=170, y=200, w=940),
        "rw": dict(type="mot", t="The president speaks the country's mood", g="Franklin D. Roosevelt, 1936", y=150, taille=56),
        "c_war": dict(type="cit", a="Franklin D. Roosevelt", o="the “I hate war” speech, 1936", x=200, y=300, w=880),
        "g6": dict(type="globe", code="H1", sc=[26]),
        "pn": dict(type="liste", titre="The USS Panay · December 1937", bande=True, petit=True, x=60, y=130, w=620,
                   cles=["Panay", "apologises", "licence"], items=[
                       "Japan bombs the gunboat USS Panay and three US tankers in China",
                       "Japan apologises, pays, promises no further attacks",
                       "And reads the American tone as a licence for further aggression"]),
    }),

    # ================================================================ VIII. idée 6 : cash and carry
    dict(id="cash", chap="II.3 · From neutrality to the Arsenal of Democracy", fond="nuit", humeur="lumiere",
         retenir="Nov. 1939, after war began: the Neutrality Act of 1939, cash and carry (pay cash, carry on your own ships) → favours Britain and France, who control the sea. America, Arsenal of Democracy: rearmament, not the New Deal, ended the Depression.",
         beats=[
        "{g7}{cc}Sixth idea: from 1939, the United States moved from neutrality to supplying the democracies. "
        "{cc.1}Only after the war had begun did Roosevelt persuade Congress, in special session, to pass the Neutrality Act of 1939. "
        "{cc.2}The United States may now sell weapons to the European democracies, on a {!cash and carry}cash and carry basis: "
        "{cc.3}pay in cash, and carry the goods away on your own ships.",
        "{-cc}{fv}Who does it favour? {fv.1}Whoever controls the sea: Britain and France. "
        "{fv.2}But only if they have the cash. {fv.3}And it comes ten years after the crisis that had produced the isolation.",
        "{-fv}{-g7}{ars}The result: America becomes the {!Arsenal of Democracy}Arsenal of Democracy. "
        "Its factories, idle since 1929, restart to arm other people's wars.",
        "{-ars}{sh}An example from Monsieur Ros's slides: M4 Sherman tanks rolling off the line of the Detroit Tank Arsenal. "
        "{sh.1}That plant did not exist in 1939.",
        "{-sh}{cure}So here is a strong idea for an essay. {cure.1}The Depression ended not with the New Deal, but with rearmament. "
        "{cure.2}The same cure as Germany's, applied late, and on the other side.",
    ], vis={
        "g7": dict(type="globe", code="H1", sc=[32]),
        "cc": dict(type="liste", titre="The Neutrality Act of 1939", bande=True, petit=True, x=60, y=110, w=620,
                   cles=["special", "cash", "carry"], items=[
                       "After war began: Congress in special session", "Weapons sold to the European democracies",
                       "Pay cash · carry on your own ships"]),
        "fv": dict(type="liste", titre="Who does it favour?", bande=True, petit=True, x=60, y=130, w=620,
                   items=["Whoever controls the sea: Britain and France", "… but only if they have the cash",
                          "… and ten years after the crisis"]),
        "ars": dict(type="def", terme="The Arsenal of Democracy", cles=["idle", "1929", "restart"],
                    t="America as arms supplier to the democracies from 1939, without fighting itself.",
                    etape="Factories idle since 1929 restart to arm other people's wars", x=170, y=200, w=940),
        "sh": dict(type="note", terme="On M. Ros's slides", cles=["Sherman", "Detroit"],
                   t="M4 Sherman tanks rolling off the line of the Detroit Tank Arsenal.",
                   etape="A plant that did not exist in 1939", x=170, y=200, w=940),
        "cure": dict(type="cols", g="Germany", gq="rearmament absorbs the unemployed, from 1933", d="United States",
                     dq="rearmament ends the Depression, from 1939", vs="=", repere="Not the New Deal: rearmament"),
    }),

    # ================================================================ IX. idée 7 : l'apaisement et ses six raisons
    dict(id="apais", chap="II.3 · Appeasement, and six rational reasons", fond="nuit", humeur="tension",
         retenir="Appeasement (key term): conceding to an aggressor's demands in the hope of avoiding war. 1935 Ethiopia: no oil embargo · 1936 Rhineland: no intervention. Six reasons: pacifism · an empire to police, no money to rearm · sympathy for Germany · economic problems first · American isolationism · fear of communism more than fascism.",
         beats=[
        "{ap}Seventh idea. On the other side of the Atlantic, Britain and France follow a policy with a name. The key term of this episode: "
        "{!Appeasement}appeasement. {ap.1}Conceding to an aggressor's demands, in the hope of avoiding war.",
        "{-ap}{dbl}Together with American isolationism, appeasement countered every effort the League made to prevent conflict. Two tests. "
        "{dbl.1}In 1935, when Mussolini attacks Ethiopia, Britain refuses to impose the oil embargo that would have stopped him.",
        "{-dbl}{g8}{rh}{rh.1}And in March 1936, Hitler sends troops into the Rhineland, demilitarised by Versailles. France and Britain decide not to intervene. "
        "{rh.2}The example of the course: the German army marched in with orders to withdraw at the first sign of French resistance. "
        "{!There was none}There was none. {rh.3}Hitler later said the forty-eight hours after the march were the most nerve-racking of his life.",
        "{-rh}{-g8}{six}Why did they give way? The course gives six reasons, and they must be learned. "
        "{six.1}One: pacifism. Both countries were desperate to avoid another world war. "
        "{six.2}Two: Britain was policing its empire, and could not afford major rearmament. "
        "{six.3}Three: many Britons sympathised with a Germany they felt had been treated unfairly in 1918. "
        "{six.4}Four: both countries were seriously weakened, and their own economic problems came first. "
        "{six.5}Five: both believed that American isolationism left them unprotected. "
        "{six.6}And six: both feared communism more than fascism.",
        "{-six}{ns}Now the important sentence. {!None of these reasons is stupid}None of these reasons is stupid. "
        "Together, they explain why democracies that could have acted chose not to.",
    ], vis={
        "ap": dict(type="def", terme="Key term · Appeasement", cles=["Conceding", "aggressor", "avoiding"],
                   t="Conceding to an aggressor's demands in the hope of avoiding war.",
                   etape="Britain and France, from Ethiopia (1935) to Munich (1938)", x=170, y=200, w=940),
        "dbl": dict(type="note", terme="Test 1 · Ethiopia, 1935", cles=["oil", "embargo"],
                    t="Mussolini attacks Ethiopia. Britain refuses the oil embargo that would have stopped him.",
                    etape="Appeasement + American isolationism: the League is blocked", x=170, y=200, w=940),
        "g8": dict(type="globe", code="H1", sc=[29]),
        "rh": dict(type="liste", titre="Test 2 · the Rhineland, 7 March 1936", bande=True, petit=True, x=60, y=130, w=620,
                   cles=["intervene", "withdraw", "forty-eight"], items=[
                       "Demilitarised by Versailles: France and Britain do not intervene",
                       "German orders: withdraw at the first sign of French resistance",
                       "Hitler: the forty-eight hours after the march, the most nerve-racking of his life"]),
        "six": dict(type="liste", titre="Six rational reasons for appeasement", cles=["pacifism", "empire", "unfairly", "economic", "isolationism", "communism"], items=[
            "Pacifism: avoid another world war at all costs", "Britain polices its empire; it cannot afford major rearmament",
            "Sympathy for a Germany treated unfairly in 1918", "Weakened countries: their own economic problems first",
            "American isolationism leaves them unprotected", "They fear communism more than fascism"], x=120, y=105, w=1040),
        "ns": dict(type="mot", t="None of these reasons is stupid", g="democracies that could have acted chose not to", y=250, taille=72),
    }),

    # ================================================================ X. idée 8 : les conséquences jusqu'en septembre 1939
    dict(id="consq", chap="II.3 · Consequences: stepping stones to war", fond="guerre", humeur="tension",
         retenir="1931 Manchuria → 1935 Ethiopia → 1936 Rhineland → March 1938 Anschluss → Sept. 1938 Munich (the Sudetenland ceded) → March 1939 Prague → 1 Sept. 1939 Poland; 3 Sept. France and Britain declare war. Every concession was followed by a larger demand.",
         beats=[
        "{q4}Last idea of the course: the consequences. Appeasement enabled Nazi Germany to go further, until September 1939. "
        "The course gives a chain. Learn it in order.",
        "{-q4}{sl}{sl.1}Nineteen thirty-one, Manchuria. The League condemns, Japan walks out. No sanction. "
        "{sl.2}Nineteen thirty-five, Ethiopia. Britain refuses the oil embargo. "
        "{sl.3}Nineteen thirty-six, the Rhineland. France and Britain do not move. "
        "{sl.4}March 1938, the Anschluss: Germany annexes Austria. "
        "{sl.5}September 1938, Munich. Hitler demands part of Czechoslovakia, and Chamberlain and Daladier, meeting Hitler and Mussolini, accept it. "
        "The Czechs are not even invited. "
        "{sl.6}March 1939, Prague: Germany occupies the whole of Czechoslovakia. "
        "{sl.7}And the first of September 1939, Poland. On the third, France and Britain declare war.",
        "{-sl}{mun}Munich is the defining act of appeasement. The agreement accepts",
        ("C", "the cession to Germany of the Sudeten German territory", "c_mun"),
        "{-c_mun}{ch}Here is Neville Chamberlain, back from Munich, on the thirtieth of September 1938, at Heston aerodrome near London, "
        "waving the paper he has signed with Hitler. {ch.1}That evening, outside the course, he speaks of {!peace for our time}peace for our time. "
        "{ch.2}Six months later, Germany occupies Prague. Munich had bought nothing.",
        "{-ch}{-mun}{axe}Meanwhile, the three militarist powers draw together. The course speaks of the Rome–Berlin–Tokyo pact, the Axis. "
        "{axe.1}Be precise about the dates, which are outside the course: Germany and Japan sign the Anti-Comintern Pact in 1936, "
        "Italy joins it in 1937, and the formal Rome–Berlin–Tokyo pact is only signed in September 1940.",
        "{-axe}{low2}David Low drew the whole chain two years before Munich, in July 1936, in a cartoon called Stepping Stones to Glory. "
        "Again, picture it. {low2.1}Hitler climbs a staircase made of the bent backs of the spineless leaders of democracy. "
        "{low2.2}The steps are marked rearmament, the Rhineland, {low2.3}and the top step: Boss of the Universe.",
        "{-low2}{arg}This is the central argument against appeasement: {!a larger demand}every concession was followed by a larger demand. "
        "European turmoil worsened at every concession.",
    ], vis={
        "q4": dict(type="question", t="What did appeasement lead to?"),
        "sl": dict(type="liste", titre="Stepping stones to war, 1931–1939", cles=["Manchuria", "Ethiopia", "Rhineland", "Anschluss", "Munich", "Prague", "Poland"], items=[
            "1931 · Manchuria: the League condemns, Japan quits", "1935 · Ethiopia: no oil embargo",
            "1936 · Rhineland: no intervention", "March 1938 · Anschluss: Austria annexed",
            "Sept. 1938 · Munich: the Sudetenland ceded", "March 1939 · Prague: all of Czechoslovakia",
            "1 Sept. 1939 · Poland: invasion; war on 3 Sept."], x=120, y=95, w=1040),
        "mun": dict(type="tableau", img="h1-chamberlain-munich", fond=True, sombre=True, de=[1.0, .5, .4], a=[1.25, .52, .4],
                    legende="Neville Chamberlain back from Munich, Heston aerodrome, 30 September 1938 (Ministry of Information, Wikimedia Commons, public domain)"),
        "c_mun": dict(type="cit", a="The Munich Agreement", o="29–30 September 1938", x=200, y=200, w=880),
        "ch": dict(type="liste", titre="Heston aerodrome · 30 September 1938", bande=True, petit=True, x=60, y=430, w=620,
                   items=["“Peace for our time” (that evening; outside the course)", "March 1939: Prague. Munich bought nothing."]),
        "axe": dict(type="note", terme="The Axis · dates outside the course", cles=["1936", "1937", "1940"],
                    t="Anti-Comintern Pact: Germany and Japan 1936, Italy joins 1937.",
                    etape="The formal Rome–Berlin–Tokyo pact: September 1940", x=170, y=200, w=940),
        "low2": dict(type="liste", titre="David Low, “Stepping Stones to Glory” (July 1936) · described", items=[
            "Hitler climbs on the bent backs of “the spineless leaders of democracy”",
            "The steps: rearmament, the Rhineland …", "The top step: “Boss of the Universe”"], x=150, y=150, w=980),
        "arg": dict(type="mot", t="Each concession, a larger demand", g="the central argument against appeasement", y=250, taille=74),
    }),

    # ================================================================ XI. à vérifier
    dict(id="verif", chap="Watch out: points to check", fond="aube", humeur="calme",
         retenir="Check with M. Ros: Nye Committee (beyond the slides) · Hoover favoured the League (with reservations) · the Neutrality Acts in detail · the Axis pact signed only in 1940.",
         beats=[
        "{chk}Before the exam, four points to check with Monsieur Ros, as the site's checklist suggests. "
        "{chk.1}The Nye Committee is an example added by the site, from outside the slides. It is accurate, but prefer the course's own examples if he does. "
        "{chk.2}Hoover was not an opponent of the League: the opposition was led by Lodge. "
        "{chk.3}The Neutrality Acts: learn the course's three steps, but do not write that the 1937 Act banned all trade. "
        "{chk.4}And the Rome–Berlin–Tokyo pact: if you date it, write 1940.",
    ], vis={
        "chk": dict(type="liste", titre="To confirm with M. Ros", cles=["Nye", "Hoover", "1937", "1940"], items=[
            "The Nye Committee: added by the site, beyond the slides", "Hoover favoured the League; Lodge led the opposition",
            "1937 Act: not an embargo on all trade", "Rome–Berlin–Tokyo pact: September 1940"], x=150, y=140, w=980),
    }),

    # ================================================================ XII. à l'examen : le key issue en essay
    dict(id="essai", chap="Your turn · the key issue as an essay", fond="aube", humeur="calme",
         retenir="Key issue: “Blame for the origins of WWII lies in part with the great democratic powers themselves. How far do you agree?” · Agree in part: they built an order they would not underwrite, weakened it after 1929, refused to defend it — but the initiative lay with the militarist regimes.",
         beats=[
        "{ki}Now the exam. This is the key issue of the chapter, for the oral and for the essay. "
        "{ki.1}Blame for the origins of the Second World War lies in part with the great democratic powers themselves. How far do you agree?",
        "{-ki}{mots}First, read the question. {mots.1}In part: it invites a measured answer, not yes or no. "
        "{mots.2}The great democratic powers: Britain, France and the United States, the guarantors of the order of 1919. "
        "{mots.3}How far: arguments for, arguments against, and a judgement.",
        "{-mots}{pa1}",
        ("P", 2.0),
        "{-pa1}{pl}Here is a model plan, from the essay card of the site. {pl.1}One: they built an order they would not underwrite. "
        "The Senate refused Versailles; the League had no army, every member a veto; Kellogg–Briand had no mechanism. "
        "{pl.2}Two: they weakened it economically after 1929. Smoot–Hawley and the retaliation cut world trade by two thirds, "
        "the recall of American loans destabilised Germany, and the defence of the Gold Standard deepened unemployment. "
        "{pl.3}Three: they refused to defend it when tested. Manchuria and the Stimson note, the Neutrality Acts and the Panay, "
        "no oil embargo on Italy, the Rhineland, Munich. "
        "{pl.4}And four, the other side: the initiative lay with the militarist regimes, in Berlin, Rome and Tokyo.",
        "{-pl}{pa2}",
        ("P", 2.0),
        "{-pa2}{par}Here is a model of that last paragraph, written for this video. "
        "{par.1}However, the democracies were reluctant, not responsible for the decision to go to war. "
        "{par.2}Militarism was a deliberate choice in Berlin, Rome and Tokyo: armed build-up, military control of government, aggressive foreign policy. "
        "{par.3}Economic distress gave the Nazis an audience, but it compelled no one to plunder conquered nations. "
        "{par.4}And appeasement had rational reasons: pacifism, an empire to police, a fear of communism. "
        "{par.5}So the democracies made aggression easier; the aggressors chose war.",
        "{-par}{ccl}And the conclusion. {ccl.1}Agree in part: the democracies are responsible for an order they weakened and would not defend; "
        "the aggressors are responsible for the war. {ccl.2}And use the course's own word. {!reluctant}Reluctant. They could have acted, and chose not to.",
    ], vis={
        "ki": dict(type="question", t="“Blame for the origins of WWII lies in part with the great democratic powers themselves.” How far do you agree?"),
        "mots": dict(type="liste", titre="Read the question", cles=["part", "democratic", "How"], items=[
            "“In part”: a measured answer", "“The great democratic powers”: Britain, France, the United States",
            "“How far”: for, against, a judgement"], x=150, y=150, w=980),
        "pa1": dict(type="pause", t="How far were the great democracies to blame for the origins of WWII? Write your plan: three or four parts.",
                    sous="Pause the video, write your plan, then play on to compare."),
        "pl": dict(type="liste", titre="A model plan (essay card of the site)", petit=True, items=[
            "They built an order they would not underwrite", "They weakened it economically after 1929",
            "They refused to defend it when tested", "But the initiative lay with the militarist regimes"], x=150, y=140, w=980),
        "pa2": dict(type="pause", t="Write the “however” paragraph: why the democracies were not the main culprits.",
                    sous="Pause the video, write five sentences, then play on for a model."),
        "par": dict(type="liste", titre="A model paragraph (written for the video)", petit=True, items=[
            "However: reluctant, not responsible for the decision for war",
            "Militarism, a deliberate choice in Berlin, Rome, Tokyo",
            "Distress gave the Nazis an audience; it compelled no plunder",
            "Appeasement had rational reasons", "So: democracies made aggression easier; aggressors chose war"], x=130, y=120, w=1020),
        "ccl": dict(type="def", terme="Conclusion", cles=["part", "reluctant"],
                    t="Agree in part: responsible for an order they weakened and would not defend; the aggressors, for the war.",
                    etape="The course's word: “reluctant”. They could have acted, and chose not to.", x=170, y=200, w=940),
    }),

    # ================================================================ récap
    dict(id="recap", chap="Recap", fond="nuit", humeur="calme", beats=[
        "{carte}Let's sum up. {carte.1}In 1919, the democracies built a liberal order on Wilson's principles, "
        "but the United States never joined the League, which had no army and a veto for every member. "
        "{carte.2}In the 1930s, the League condemned Japan in Manchuria, and nothing followed; America condemned in words, with the Stimson note, "
        "then shut itself away with the Neutrality Acts, until cash and carry in 1939. "
        "{carte.3}Britain and France chose appeasement, for six rational reasons, from Ethiopia and the Rhineland to Munich. "
        "{carte.4}And every concession was followed by a larger demand, until Poland, in September 1939.",
        ("P", 4.0),
        "{-carte}{fin}Next episode: the crisis at the exam. Essay and DBQ on the whole chapter, with model answers.",
        ("P", 2.0),
    ], vis={
        "carte": dict(type="carte", centre="RELUCTANT DEMOCRACIES", branches=[
            dict(t="The order of 1919", items=["Wilson: 3 principles", "the US never joins", "no army, a veto each"]),
            dict(t="America", items=["Stimson: words only", "Neutrality Acts 1935–37", "cash and carry, Nov. 1939"]),
            dict(t="Appeasement", items=["Ethiopia, Rhineland", "six rational reasons", "Munich, Sept. 1938"]),
            dict(t="Consequences", items=["Anschluss, Prague", "each concession, a larger demand", "1 Sept. 1939: Poland"])]),
        "fin": dict(type="mot", t="Next: the crisis at the exam", g="Episode 5 · essay and DBQ", y=270, taille=80),
    }),
]

QUIZ = [
    dict(q="Which three principles did Wilson's Fourteen Points carry into foreign policy?",
         r=["Democracy, self-determination of peoples, free trade", "Isolation, protection, neutrality",
            "Empire, rearmament, the Gold Standard", "Communism, pacifism, autarky"], ok=0, voir="wi",
         ex="Wilsonianism: the basis of the liberal world order of 1919, given institutions at Paris, Versailles and Geneva."),
    dict(q="Which is one of the League of Nations' STRUCTURAL weaknesses?",
         r=["It had no army of its own", "It was powerless before Italian militarism",
            "Japan invaded Manchuria", "Germany remilitarised the Rhineland"], ok=0, voir="str",
         ex="Structural: present from 1919 (no US ratification, national interests first, no army, a veto for every member). The other answers are contextual events of the 1930s."),
    dict(q="What happened after the League adopted the Lytton report in February 1933?",
         r=["Japan left the League", "Japan withdrew from Manchuria", "The United States sent troops", "Britain imposed an oil embargo"],
         ok=0, voir="mk", ex="Japan left the League in March 1933: the League could not stop a great power."),
    dict(q="The Stimson note of 7 January 1932 was…",
         r=["a doctrine of non-recognition, not of action", "a declaration of war on Japan",
            "an embargo on all trade with Japan", "the American entry into the League"], ok=0, voir="wa",
         ex="Words without action: Japan answered by bombing Shanghai in 1932, and no American response followed."),
    dict(q="How did Japan read the American response to the sinking of the USS Panay (December 1937)?",
         r=["As a licence for further aggression", "As a declaration of war", "As a reason to leave China", "As a call to join the League"],
         ok=0, voir="pn", ex="Japan apologised and paid an indemnity — and concluded that America would not act."),
    dict(q="What did the Neutrality Act of 1939, “cash and carry”, allow?",
         r=["The democracies could buy US weapons if they paid cash and carried them on their own ships",
            "The US could lend weapons without payment", "American soldiers could fight in Europe",
            "Germany could buy American tanks"], ok=0, voir="cc",
         ex="It favoured whoever controlled the sea, Britain and France — if they had the cash."),
    dict(q="Which is NOT one of the course's six reasons for appeasement?",
         r=["A military alliance with Nazi Germany", "Pacifism", "A greater fear of communism than of fascism",
            "Sympathy for a Germany treated unfairly in 1918"], ok=0, voir="six",
         ex="The six: pacifism, an empire to police, sympathy for Germany, economic problems first, American isolationism, fear of communism."),
    dict(q="What did Chamberlain and Daladier accept at Munich in September 1938?",
         r=["The cession of the Sudetenland to Germany", "The Anschluss of Austria", "The occupation of Prague",
            "The invasion of Poland"], ok=0, voir="sl",
         ex="Munich, appeasement's defining act; in March 1939 Germany occupied all of Czechoslovakia: Munich had bought nothing."),
]

CREDITS = [
    "Content: M. Ros's course (DNL History, H1 · Part II.3, “Great democracies reluctant to defend the Liberal order established in 1919”) "
    "as written on the site, with its diagrams (why the League failed, stepping stones to war, points to check) and the essay card of the key issue; "
    "animated map of chapter 1 (site). Outside the course: Henry Cabot Lodge, the details of the Neutrality Acts of 1936 and 1937, "
    "the Anti-Comintern Pact and the Tripartite Pact (1940), “peace for our time”. David Low's cartoons are described, not reproduced. "
    "The model paragraph was written for this video.",
    "Photograph: Woodrow Wilson, 1919, by Harris & Ewing (Library of Congress, Wikimedia Commons, public domain).",
    "Cartoon: Leonard Raven-Hill, “The Gap in the Bridge”, Punch, 10 December 1919 (Wikimedia Commons, public domain).",
    "Photograph: the Palais des Nations, Geneva, 2014, by Vassil (Wikimedia Commons, CC0).",
    "Photograph: Franklin D. Roosevelt, 1933, by Elias Goldensky (Wikimedia Commons, public domain).",
    "Photograph: Neville Chamberlain at Heston aerodrome, 30 September 1938, Ministry of Information official photographer (Wikimedia Commons, public domain).",
    "Narration: synthetic voices generated locally (Qwen3-TTS); original music.",
]
