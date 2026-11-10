/* Annales liées à chaque entrée et sujets d'essai supplémentaires (avec pistes). Rattachés par identifiant d'entrée. */
(function (H) {
  function e(id) { for (var i = 0; i < H.ENTREES.length; i++) if (H.ENTREES[i].id === id) return H.ENTREES[i]; return null; }
  function poser(id, champ, val) { var x = e(id); if (x) x[champ] = val; }
  function p(probleme, i, ii, iii) {
    return "<p><b>Problème.</b> " + probleme + "</p><ol class='puces'><li>" + i + "</li><li>" + ii + "</li><li>" + iii + "</li></ol>";
  }

  poser("e1", "annales", [
    ["Bac 2025, métropole, jour 1", "Condorcet, <i>Cinq mémoires sur l’instruction publique</i> (1791) : interprétation philosophique « Pourquoi, d’après ce texte, faut-il “exercer l’âme des enfants” à la pitié ? » ; essai littéraire « La littérature a-t-elle pour vocation d’éduquer à la sensibilité ? »", "Copie modèle commentée dans la page L’épreuve."]
  ]);
  poser("e1", "entrainement", [
    ["Peut-on apprendre à être libre ? (essai philosophique)", p("La liberté semble ne pas pouvoir s’enseigner (on ne force pas quelqu’un à penser par lui-même), mais personne ne naît capable de juger seul.",
      "La liberté ne s’apprend pas comme un savoir : c’est un acte (Kant, « Sapere aude ») ; un maître qui commande la liberté se contredit.",
      "Pourtant, elle a des conditions qui s’enseignent : la discipline et l’instruction (Kant, 1803), l’instruction qui rend « capable d’apprécier et de corriger » la loi (Condorcet, 1791).",
      "On n’apprend pas la liberté, on apprend à s’en servir : l’éducation donne les moyens du jugement, l’élève fait le reste (Rousseau, l’éducation « négative » qui laisse faire l’expérience).")],
    ["L’école libère-t-elle ? (essai philosophique)", p("L’école promet l’émancipation, mais elle impose aussi des règles, des savoirs, une socialisation.",
      "Oui : Condorcet et les lois Ferry font de l’instruction une condition de l’égalité réelle et de la citoyenneté.",
      "Mais elle conforme : Durkheim parle de « socialisation méthodique » ; Vallès raconte l’ennui et l’humiliation ; la sociologie montre la reproduction des inégalités (pour aller plus loin : <i>Les Héritiers</i>, 1964).",
      "Elle libère quand elle transmet de quoi juger, y compris de quoi la juger elle-même (Arendt : transmettre un monde ancien pour protéger le nouveau).")],
    ["Les récits d’enfance disent-ils la vérité sur l’éducation reçue ? (essai littéraire)", p("Le récit d’enfance prétend témoigner, mais il est écrit par un adulte qui reconstruit.",
      "Ils dénoncent avec force des violences réelles : la dédicace de <i>L’Enfant</i> (1878).",
      "Mais ce sont des récits construits : point de vue de l’enfant, ironie de l’adulte, roman autobiographique (Jacques Vingtras), mémoire qui comble des « vides » (Rousseau, <i>Confessions</i>).",
      "Leur vérité est d’un autre ordre : ils montrent ce que l’éducation a fait d’un être, ce qu’aucun document ne dit.")],
    ["Faut-il obéir pour apprendre ? (essai philosophique)", p("Apprendre suppose de faire confiance à un maître, mais penser par soi-même suppose de ne pas tout recevoir sur parole.",
      "L’apprentissage commence par la discipline (Kant) et l’autorité du maître (Arendt).",
      "Mais Montaigne veut qu’on fasse tout passer « par l’étamine » du jugement ; Rousseau préfère l’expérience aux leçons ; Kant critique la paresse d’être mineur.",
      "On obéit pour apprendre, puis on apprend à ne plus obéir sans raison : l’autorité légitime vise sa propre disparition.")]
  ]);

  poser("e2", "annales", [
    ["Bac 2023, métropole, jour 1", "Octave Mirbeau, <i>Le Journal d’une femme de chambre</i>, ch. VII (1900) : interprétation littéraire « Dans cet extrait, comment la poésie permet-elle à l’héroïne de “redevenir un être nouveau” ? » ; essai philosophique « Le savoir nuit-il à la sensibilité ? »", ""],
    ["Bac 2024, métropole, jour 2", "Hugo, <i>Ruy Blas</i>, III, 3 (1838) : interprétation littéraire « Comment se manifeste le sentiment amoureux dans cette scène de théâtre ? » ; essai philosophique « Que gagne l’amour à être déclaré ? »", ""],
    ["Bac 2025, métropole, jour 1", "Condorcet, <i>Cinq mémoires sur l’instruction publique</i> (1791) : essai littéraire « La littérature a-t-elle pour vocation d’éduquer à la sensibilité ? »", "Copie modèle commentée dans la page L’épreuve."]
  ]);
  poser("e2", "entrainement", [
    ["Le savoir nuit-il à la sensibilité ? (essai philosophique, sujet 2023)", p("Savoir semble refroidir l’émotion (analyser, c’est mettre à distance), mais la connaissance peut aussi affiner ce que l’on sent.",
      "Le savoir peut tuer la fraîcheur du sentir : Rousseau trouve le bonheur « sans prendre la peine de penser » ; Bergson montre que le mot « brutal » recouvre l’impression.",
      "Mais sans savoir, la sensibilité reste confuse : on apprend à voir un tableau, à entendre une musique ; Proust a besoin d’un effort de l’esprit pour retrouver Combray.",
      "Le savoir ne nuit qu’à la sensibilité qu’il remplace ; il enrichit celle qu’il éclaire (Baudelaire, critique d’art et poète).")],
    ["Peut-on partager ce que l’on ressent ? (essai philosophique)", p("Mes sensations sont à moi, mais nous parlons de nos émotions, pleurons ensemble au théâtre, compatissons.",
      "L’expérience vécue semble incommunicable (Bergson et le « mot brutal »).",
      "Pourtant la pitié nous fait souffrir de la souffrance d’autrui (Rousseau, Condorcet), et nous apprenons à nommer nos émotions avec les autres (Wittgenstein).",
      "L’art est le lieu de ce partage : « Par l’art seulement, nous pouvons sortir de nous » (Proust).")],
    ["La littérature apprend-elle à sentir ? (essai littéraire)", p("Les livres semblent former la sensibilité, mais ils peuvent aussi la fausser.",
      "Oui : les lecteurs de <i>La Nouvelle Héloïse</i> et de <i>Werther</i> découvrent un langage du cœur ; Lamartine donne des mots au deuil.",
      "Mais Emma Bovary a une sensibilité façonnée par les romans du couvent : Flaubert montre les clichés du sentiment.",
      "La littérature apprend à sentir quand elle invente des manières de sentir (Baudelaire, Proust) et rend lucide sur les émotions convenues (Flaubert).")],
    ["La nature n’est-elle qu’un miroir de nos états d’âme ? (essai littéraire)", p("Les romantiques projettent leurs sentiments sur les paysages ; mais la nature résiste et parfois parle d’elle-même.",
      "Le paysage état d’âme : <i>René</i>, « Le Lac », le spleen baudelairien.",
      "Mais la nature est aussi ce qui nous dépasse (le sublime chez Kant) et ce qui nous apaise sans nous ressembler (Rousseau sur le lac de Bienne).",
      "Chez Baudelaire, elle devient un « temple » de symboles à déchiffrer : ni miroir ni décor, une langue.")]
  ]);

  poser("e3", "annales", [
    ["Bac 2022, métropole, jour 1 (sujet 1)", "Pierre Albert-Birot, « L’affaire Narcisse », <i>Poésies</i> (1926) : essai philosophique « Se connaître soi-même, est-ce se découvrir “pièce unique” ? »", ""],
    ["Bac 2022, métropole, jour 2 (sujet 1)", "Rousseau, <i>Lettres morales</i>, VI (1758) : interprétation philosophique « Dans quelle mesure pouvons-nous redevenir nous-mêmes ? » ; essai littéraire « Lire permet-il d’accéder à une meilleure connaissance de soi ? »", ""],
    ["Bac 2023, métropole, jour 2", "Nietzsche, <i>Aurore</i> (1881) : interprétation philosophique « D’après ce texte pourquoi sommes-nous tous autre chose que ce que nous paraissons être ? » ; essai littéraire « La littérature permet-elle de déchiffrer “l’alphabet […] de notre moi” ? »", ""],
    ["Bac 2026, métropole, jour 2", "Raymond Aron, <i>Introduction à la philosophie de l’histoire</i> : interprétation philosophique « Dans quelle mesure peut-on, selon ce texte, se connaître authentiquement ? » ; essai littéraire « La littérature permet-elle “de discerner les sentiments que l’on éprouve et ceux que l’on se figure éprouver” ? »", ""],
    ["Sujet zéro n° 2 (Éduscol, 2020)", "Jacques Rivière, lettre à Antonin Artaud (8 juin 1924) : « En quoi la réflexion de Jacques Rivière expose-t-elle les déchirements du Moi ? » ; « Parvient-on jamais à être soi-même ? »", ""]
  ]);
  poser("e3", "entrainement", [
    ["Se connaître soi-même, est-ce se découvrir « pièce unique » ? (essai philosophique, sujet 2022)", p("Se connaître semble révéler une singularité, mais la connaissance de soi découvre aussi ce que j’ai de commun avec les autres.",
      "Oui : Rousseau, « Je ne suis fait comme aucun de ceux que j’ai vus » ; l’autobiographie fonde sa valeur sur l’unicité.",
      "Mais Montaigne trouve en lui « la forme entière de l’humaine condition » ; Hugo : « quand je vous parle de moi, je vous parle de vous ».",
      "Et la « pièce » n’est pas un bloc : Montaigne peint « le passage », Rimbaud découvre un autre en lui. On se découvre unique, mais pas un.")],
    ["Lire permet-il de mieux se connaître ? (essai littéraire, sujet 2022)", p("Lire, c’est sortir de soi ; comment cela ferait-il mieux connaître ce qu’on est ?",
      "La lecture comme miroir : « Prenez donc ce miroir, et regardez-vous-y » (Hugo) ; Proust : chaque lecteur lit en lui-même.",
      "Mais elle peut égarer : Emma Bovary se rêve en héroïne ; on se prend pour un personnage.",
      "Lire fait connaître parce qu’il fait voir « ce que voit un autre » (Proust) : on se connaît par différence, pas par simple reflet.")],
    ["Sommes-nous ce que les autres voient de nous ? (essai philosophique)", p("Le regard d’autrui semble superficiel, mais je ne me vois jamais sans lui.",
      "Non : le moi intime échappe aux apparences (Bergson, moi profond ; Rousseau, « Je sens mon cœur »).",
      "Pourtant, le regard des autres façonne : Lorenzo devenu son masque ; Pirandello, <i>Un, personne et cent mille</i> ; Sartre, <i>Huis clos</i>.",
      "Nous ne sommes ni ce qu’on voit ni un secret caché : nous sommes ce que nous faisons de ces regards (Sartre, la mauvaise foi consiste justement à se figer dans un rôle).")],
    ["Est-on toujours maître de soi ? (essai philosophique)", p("Je crois décider de mes actes et de mes pensées ; mais j’ai des rêves, des lapsus, des passions.",
      "Descartes : la pensée m’appartient, c’est même la seule certitude.",
      "Mais Rimbaud (« On me pense »), Nietzsche, Freud (« pas maître dans sa propre maison »), Maupassant (<i>Le Horla</i>) montrent un moi dépossédé.",
      "La maîtrise de soi n’est pas un fait mais une tâche : Bergson, la liberté quand nos actes « émanent de notre personnalité entière » ; Nietzsche, « deviens celui que tu es ».")]
  ]);

  poser("e4", "entrainement", [
    ["La nouveauté est-elle une valeur ? (essai philosophique)", p("Nous valorisons l’originalité, mais ce qui est nouveau n’est pas pour autant meilleur.",
      "Oui : sans nouveauté, l’art se répète ; les avant-gardes, Rimbaud (« absolument moderne »).",
      "Mais nouveau ≠ progrès (Apollinaire) ; Kant exige que l’œuvre originale soit aussi exemplaire ; la mode est nouvelle et vite usée.",
      "La nouveauté n’est une valeur que si elle renouvelle notre regard sur ce qui existait déjà (Eliot, Picasso et Velázquez).")],
    ["Une œuvre doit-elle choquer ? (essai littéraire)", p("Les grandes ruptures ont fait scandale, mais choquer n’est pas créer.",
      "Le scandale accompagne la nouveauté : <i>Hernani</i> (1830), les procès de 1857, <i>Le Sacre du printemps</i> (1913), <i>Fontaine</i> (1917).",
      "Mais la provocation s’use et devient une convention (la « tradition du nouveau ») ; beaucoup de chefs-d’œuvre ne choquent pas.",
      "Une œuvre doit surprendre plutôt que choquer : déranger nos habitudes de voir et de lire (Apollinaire, « la surprise »).")],
    ["Réécrire, est-ce créer ? (essai littéraire)", p("Reprendre un mythe ou une œuvre semble manquer d’originalité ; pourtant la littérature n’a cessé de réécrire.",
      "La réécriture peut n’être qu’imitation.",
      "Mais Anouilh fait d’<i>Antigone</i> (1944) une pièce sur la résistance et le compromis ; Picasso transforme <i>Les Ménines</i> en 58 variations.",
      "Créer, c’est toujours reprendre : la langue, les genres, les mythes ; l’original est une manière neuve de reprendre.")]
  ]);
})(HLP);
