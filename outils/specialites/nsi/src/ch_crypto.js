/* ===================== Réseaux — sécurisation des communications (chiffrement, HTTPS) ===================== */
C("cr-cesar", String.raw`
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cesar(texte, cle):
    """Décale chaque lettre de cle rangs dans l'alphabet (les autres caractères restent)."""
    resultat = ""
    for c in texte:
        if c in ALPHABET:
            resultat = resultat + ALPHABET[(ALPHABET.index(c) + cle) % 26]
        else:
            resultat = resultat + c
    return resultat

chiffre = cesar("ATTAQUE A L AUBE", 3)
print(chiffre)
print(cesar(chiffre, -3))          # déchiffrer = décaler dans l'autre sens`, { fichier: "cesar.py", out: "DWWDTXH D O DXEH\nATTAQUE A L AUBE" });

C("cr-force", String.raw`
intercepte = "CPYOPK GZFD OPGLYE WP WJNPP"
for cle in range(1, 26):                     # seulement 25 clés possibles
    essai = cesar(intercepte, -cle)
    if "VOUS" in essai:                      # un mot qu'on s'attend à trouver
        print(cle, essai)`, { deps: ["cr-cesar"], out: "11 RENDEZ VOUS DEVANT LE LYCEE" });

C("cr-frequences", String.raw`
def lettre_la_plus_frequente(texte):
    compte = {}
    for c in texte:
        if c in ALPHABET:
            compte[c] = compte.get(c, 0) + 1
    return max(compte, key=compte.get)

intercepte = "SLZ LSLCLZ KL ALYTPUHSL YLCPZLUA SLBY LWYLBCL KL ZWLJPHSPAL HCLJ WHAPLUJL"
x = lettre_la_plus_frequente(intercepte)
cle = (ALPHABET.index(x) - ALPHABET.index("E")) % 26     # en français, E est la plus fréquente
print(x, cle, cesar(intercepte, -cle))`, { deps: ["cr-cesar"], out: "L 7 LES ELEVES DE TERMINALE REVISENT LEUR EPREUVE DE SPECIALITE AVEC PATIENCE" });

C("cr-xor-bits", String.raw`
>>> 0b1100 ^ 0b1010          # 1 si les deux bits sont différents
6
>>> bin(0b1100 ^ 0b1010)
'0b110'
>>> m, k = 0b01001110, 0b01001011
>>> (m ^ k) ^ k == m         # appliquer deux fois la même clé redonne le message
True`, { console: true });

C("cr-xor", String.raw`
def xor_octets(donnees, cle):
    """Combine chaque octet des données avec un octet de la clé (répétée si besoin)."""
    return bytes(d ^ cle[i % len(cle)] for i, d in enumerate(donnees))

message = "Rendez-vous à 18 h".encode("utf-8")   # texte -> octets
cle = b"NSI"
chiffre = xor_octets(message, cle)
print(chiffre.hex())                              # illisible sans la clé
print(xor_octets(chiffre, cle).decode("utf-8"))   # même opération pour déchiffrer`, { fichier: "xor.py", out: "1c36272a36336325263b20698df3697f6b6926\nRendez-vous à 18 h" });

C("cr-masque", String.raw`
import secrets

message = "Rendez-vous à 18 h".encode("utf-8")
masque = secrets.token_bytes(len(message))       # clé aléatoire aussi longue que le message
chiffre = xor_octets(message, masque)
print(xor_octets(chiffre, masque) == message, len(masque) == len(message))`, { deps: ["cr-xor"], out: "True True" });

C("cr-nb-cles", String.raw`
def cles_symetriques(n):
    """Nombre de clés secrètes pour que chaque paire de personnes ait la sienne."""
    return n * (n - 1) // 2

for n in [2, 10, 100, 1000]:
    print(n, "personnes :", cles_symetriques(n), "clés secrètes, ou", 2 * n, "clés en asymétrique")`, { out: "2 personnes : 1 clés secrètes, ou 4 clés en asymétrique\n10 personnes : 45 clés secrètes, ou 20 clés en asymétrique\n100 personnes : 4950 clés secrètes, ou 200 clés en asymétrique\n1000 personnes : 499500 clés secrètes, ou 2000 clés en asymétrique" });

C("cr-rsa", String.raw`
# RSA « jouet » : de très petits nombres, pour voir le principe (jamais pour de vrai !)
p, q = 61, 53                   # deux nombres premiers, gardés secrets
n = p * q                       # 3233 : public
phi = (p - 1) * (q - 1)         # 3120 : secret
e = 17                          # exposant public, sans diviseur commun avec phi
d = pow(e, -1, phi)             # 2753 : exposant privé, inverse de e modulo phi
print("clé publique :", (n, e), "clé privée :", (n, d), "e*d mod phi =", e * d % phi)

m = 65                          # le message, codé par un nombre < n
c = pow(m, e, n)                # chiffrement avec la clé PUBLIQUE : m**e mod n
print("chiffré :", c, "déchiffré :", pow(c, d, n))   # déchiffrement avec la clé PRIVÉE`, { fichier: "rsa_jouet.py", out: "clé publique : (3233, 17) clé privée : (3233, 2753) e*d mod phi = 1\nchiffré : 2790 déchiffré : 65" });

C("cr-signature", String.raw`
empreinte = 1234                # résumé du document (en vrai : une fonction de hachage)
signature = pow(empreinte, d, n)        # signée avec la clé PRIVÉE du serveur
print(signature, pow(signature, e, n) == empreinte)   # tout le monde vérifie avec la clé PUBLIQUE
print(pow(signature + 1, e, n) == empreinte)           # une signature modifiée ne passe pas`, { deps: ["cr-rsa"], out: "1512 True\nFalse" });

C("cr-hybride", String.raw`
import secrets

# 1. Le serveur a publié sa clé publique (n, e) ; lui seul connaît d.
# 2. Le client choisit une clé de session secrète, au hasard.
cle_session = secrets.randbelow(255) + 1          # de 1 à 255 : un octet (jouet)
# 3. Il l'envoie chiffrée avec la clé PUBLIQUE du serveur.
envoi = pow(cle_session, e, n)
# 4. Le serveur la déchiffre avec sa clé PRIVÉE : ils partagent maintenant la même clé.
recue = pow(envoi, d, n)
# 5. Tout le reste de l'échange est chiffré en SYMÉTRIQUE avec cette clé (ici, XOR).
requete = xor_octets(b"GET /notes.html", bytes([recue]))
print(recue == cle_session, xor_octets(requete, bytes([cle_session])))`, { deps: ["cr-rsa", "cr-xor"], out: "True b'GET /notes.html'" });

C("cr-hachage", String.raw`
>>> import hashlib
>>> hashlib.sha256(b"bonjour").hexdigest()[:16]
'2cb4b1431b84ec15'
>>> hashlib.sha256(b"Bonjour").hexdigest()[:16]
'9172e8eec99f144f'
>>> len(hashlib.sha256(b"un texte de n'importe quelle longueur").hexdigest()) * 4
256`, { console: true });

C("cr-tr-cesar", String.raw`
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cesar(texte, cle):
    resultat = ""
    for c in texte:
        i = ALPHABET.index(c)
        resultat = resultat + ALPHABET[(i + cle) % 26]
    return resultat

print(cesar("NSIZ", 3))`, { fichier: "cesar_pas_a_pas.py", trace: true, titreTrace: "cesar(\"NSIZ\", 3)", out: "QVLC" });

/* prédis la sortie */
C("cr-x1", String.raw`
print(cesar("NSI", 13), cesar(cesar("NSI", 13), 13))`, { deps: ["cr-cesar"], out: "AFV NSI" });

C("cr-x2", String.raw`
print(5 ^ 3, 5 ^ 5, 5 ^ 0, (5 ^ 3) ^ 3)`, { out: "6 0 5 5" });

C("cr-x3", String.raw`
n, e, d = 55, 3, 27
c = pow(8, e, n)
print(c, pow(c, d, n))`, { out: "17 8" });

C("cr-x4", String.raw`
m = b"AAAA"
print(xor_octets(m, b"\x01"), xor_octets(m, b"\x01\x02"))`, { deps: ["cr-xor"], out: "b'@@@@' b'@C@C'" });

/* épreuve pratique */
C("cr-ep-fourni", String.raw`
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vigenere(texte, cle, sens=1):
    """Chiffre (sens = 1) ou déchiffre (sens = -1) texte, en majuscules sans accents :
    la lettre de rang i est décalée du rang de la lettre cle[i % len(cle)].
    Les caractères hors de l'alphabet sont recopiés et ne consomment pas de lettre de la clé."""
    resultat = ""
    i = 0
    for c in texte:
        ...
    return resultat`, { fichier: "vigenere.py", run: false, trous: [10] });

C("cr-ep-corr", String.raw`
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vigenere(texte, cle, sens=1):
    assert sens in (1, -1) and len(cle) > 0
    resultat = ""
    i = 0
    for c in texte:
        if c in ALPHABET:
            decalage = ALPHABET.index(cle[i % len(cle)])
            resultat = resultat + ALPHABET[(ALPHABET.index(c) + sens * decalage) % 26]
            i = i + 1
        else:
            resultat = resultat + c
    return resultat

def test_vigenere():
    assert vigenere("AAAA", "BC") == "BCBC"
    assert vigenere("ATTAQUE", "A") == "ATTAQUE"              # clé A : décalage nul
    c = vigenere("RENDEZ VOUS A MIDI", "NSI")
    assert c == "EWVQWH IGCF S UVVQ"
    assert vigenere(c, "NSI", -1) == "RENDEZ VOUS A MIDI"
    assert vigenere("", "NSI") == ""

test_vigenere()
print(vigenere("RENDEZ VOUS A MIDI", "NSI"))`, { fichier: "vigenere.py", out: "EWVQWH IGCF S UVVQ" });

C("cr-ep-freq", String.raw`
print(vigenere("EEEEEE", "NSI"), cesar("EEEEEE", 13))`, { deps: ["cr-cesar", "cr-ep-corr"], out: "RWMRWM RRRRRR" });

/* épreuve écrite */
C("cr-ecrit-verif", String.raw`
p, q, e = 5, 11, 3
n, phi = p * q, (p - 1) * (q - 1)
d = pow(e, -1, phi)
print(n, phi, d, pow(8, e, n), pow(pow(8, e, n), d, n))`, { out: "55 40 27 17 8" });

/* ---------- animation : le XOR bit à bit ---------- */
WIDGETS_EXT["arch-xor"] = function (z, opt, O) {
  archStyle();
  var M = "01001110", K = "01001011", X = M.split("").map(function (b, i) { return b === K[i] ? "0" : "1"; }).join("");
  var E = [
    { l: ["m"], msg: "On chiffre un octet : la lettre <b>N</b>, codée 78 en ASCII, soit <b>01001110</b> en binaire." },
    { l: ["m", "k"], msg: "La <b>clé</b> secrète est un autre octet, connu seulement des deux correspondants : ici <b>01001011</b>." },
    { l: ["m", "k", "x"], col: true, msg: "Le <b>XOR</b> (ou exclusif) se calcule colonne par colonne : <b>1</b> si les deux bits sont <b>différents</b>, <b>0</b> s’ils sont égaux. 0⊕0 = 0, 0⊕1 = 1, 1⊕0 = 1, 1⊕1 = 0." },
    { l: ["m", "k", "x"], msg: "Résultat : <b>00000101</b>. Sans la clé, cet octet ne dit rien de la lettre de départ : chaque bit du message a pu être inversé ou non." },
    { l: ["x", "k", "m2"], col: true, msg: "Pour <b>déchiffrer</b>, le destinataire refait <b>la même opération</b> avec <b>la même clé</b> : 00000101 ⊕ 01001011 = 01001110. On retrouve N." },
    { l: ["x", "k", "m2"], msg: "Pourquoi ça marche : (m ⊕ k) ⊕ k = m ⊕ (k ⊕ k) = m ⊕ 0 = m. C’est un chiffrement <b>symétrique</b> : une seule clé, pour chiffrer et pour déchiffrer. Avec une clé aléatoire aussi longue que le message et jamais réutilisée (masque jetable), il est même incassable." }
  ];
  var LIG = { m: ["message", M, "var(--bleu)"], k: ["clé", K, "var(--ambre)"], x: ["chiffré", X, "var(--rouge)"], m2: ["message", M, "var(--vert)"] };
  function dessine(scene, e, i, Et, saut) {
    var s = '<svg viewBox="0 0 400 ' + (30 + e.l.length * 40) + '" role="img" aria-label="Calcul d’un XOR bit à bit">';
    e.l.forEach(function (k, r) {
      var L = LIG[k], y = 20 + r * 40;
      if (r === 2) s += '<line x1="96" y1="' + (y - 12) + '" x2="392" y2="' + (y - 12) + '" stroke="var(--encre2)" stroke-width="1.5"/><text class="gd" x="80" y="' + (y - 24) + '" text-anchor="middle">⊕</text>';
      s += '<text x="6" y="' + (y + 16) + '" style="font-weight:700;fill:' + L[2] + '">' + L[0] + "</text>";
      L[1].split("").forEach(function (b, j) {
        var anim = r === 2 && e.col && !saut;
        s += '<g' + (anim ? ' class="neuf" style="animation-delay:' + (j * 0.18).toFixed(2) + 's"' : "") + '><rect x="' + (100 + j * 36) + '" y="' + y + '" width="30" height="26" rx="5" style="fill:var(--bg2);stroke:' + L[2] + ';stroke-width:1.6"/><text class="gd" x="' + (115 + j * 36) + '" y="' + (y + 18) + '" text-anchor="middle" style="fill:' + L[2] + '">' + b + "</text></g>";
      });
    });
    scene.innerHTML = s + "</svg>";
  }
  O.lecteur(z, { titre: "le XOR, chiffrement symétrique élémentaire", sous: "bit à bit", etapes: function () { return E; }, prepare: function (scene) { scene.parentNode.parentNode.classList.add("ar"); }, dessine: dessine, vitesse: 2600 });
};

/* ---------- animation : la poignée de main TLS ---------- */
WIDGETS_EXT["arch-tls"] = function (z, opt, O) {
  archStyle();
  /* chaque message : [sens (1 = client → serveur), libellé, détail, chiffré ?] */
  var SC = {
    prog: [
      { m: [], msg: "Le navigateur (client) veut ouvrir <code>https://exemple.fr</code>. Il se connecte au port <b>443</b> du serveur. Pour l’instant, rien n’est secret : un espion sur le réseau voit tout." },
      { m: [[1, "ClientHello", "versions, méthodes de chiffrement connues, nombre aléatoire"]], msg: "<b>1.</b> Le client salue le serveur : versions de TLS et méthodes de chiffrement qu’il connaît, un nombre aléatoire." },
      { m: [[-1, "ServerHello + certificat", "méthode choisie, nombre aléatoire, clé PUBLIQUE signée par une autorité"]], msg: "<b>2.</b> Le serveur répond et envoie son <b>certificat</b> : son nom de domaine, sa <b>clé publique</b>, et la <b>signature</b> d’une autorité de certification (AC)." },
      { m: [], verif: true, msg: "<b>3.</b> Le client <b>vérifie le certificat</b> : la signature de l’autorité est-elle valide (il connaît les clés publiques des autorités reconnues) ? le nom est-il bien <code>exemple.fr</code> ? la date de validité est-elle bonne ? Sinon, le navigateur affiche une alerte." },
      { m: [[1, "clé de session chiffrée", "secret tiré au hasard, chiffré avec la clé PUBLIQUE du serveur"]], cle: "client", msg: "<b>4.</b> Le client tire au hasard un <b>secret</b> qui servira à fabriquer la <b>clé de session</b>, le <b>chiffre avec la clé publique</b> du serveur et l’envoie. Un espion voit passer un message chiffré qu’il ne peut pas ouvrir." },
      { m: [], cle: "deux", msg: "<b>5.</b> Seul le serveur peut le déchiffrer, avec sa <b>clé privée</b>. Client et serveur partagent maintenant le même secret, et en déduisent la même clé de session : c’est l’échange d’une clé <b>symétrique</b> grâce au chiffrement <b>asymétrique</b>." },
      { m: [[1, "Finished", "résumé de l’échange", true], [-1, "Finished", "résumé de l’échange", true]], cle: "deux", msg: "<b>6.</b> Chacun envoie un résumé chiffré de tout l’échange : si un intermédiaire avait modifié un message, les résumés ne correspondraient pas." },
      { m: [[1, "GET /index.html", "requête HTTP chiffrée (AES)", true], [-1, "200 OK + page", "réponse HTTP chiffrée (AES)", true]], cle: "deux", msg: "<b>7.</b> Le reste de la connexion est du <b>HTTP ordinaire</b>, chiffré en <b>symétrique</b> (AES) avec la clé de session : rapide, et illisible pour l’espion. C’est HTTPS = HTTP + TLS." }
    ],
    tls13: [
      { m: [], msg: "Version actuelle, <b>TLS 1.3</b> (2018) : la clé de session n’est plus envoyée chiffrée par RSA, elle est <b>calculée des deux côtés</b> par un échange de Diffie-Hellman. Le principe reste : de l’asymétrique pour s’accorder sur une clé, du symétrique pour les données." },
      { m: [[1, "ClientHello", "méthodes connues, nombre aléatoire, part publique d’un échange de clé"]], msg: "<b>1.</b> Dès son premier message, le client envoie sa <b>part publique</b> d’un échange de Diffie-Hellman (sa part privée reste chez lui)." },
      { m: [[-1, "ServerHello", "méthode choisie, part publique du serveur"]], cle: "deux", msg: "<b>2.</b> Le serveur répond avec sa propre part publique. Chacun combine sa part privée avec la part publique de l’autre : ils obtiennent <b>le même secret</b>, que l’espion ne peut pas calculer à partir des seules parts publiques." },
      { m: [[-1, "certificat + signature", "clé publique signée par une AC ; signature de l’échange avec la clé PRIVÉE", true]], cle: "deux", msg: "<b>3.</b> Déjà chiffré : le serveur envoie son <b>certificat</b> et <b>signe</b> l’échange avec sa <b>clé privée</b>. Il prouve ainsi qu’il est bien le propriétaire du certificat." },
      { m: [], verif: true, cle: "deux", msg: "<b>4.</b> Le client vérifie le certificat (signature de l’autorité, nom, dates) et la signature de l’échange avec la clé publique du certificat. Personne ne s’est glissé au milieu." },
      { m: [[1, "Finished", "résumé de l’échange", true], [1, "GET /index.html", "requête chiffrée", true], [-1, "200 OK + page", "réponse chiffrée", true]], cle: "deux", msg: "<b>5.</b> Le client confirme et peut envoyer sa requête aussitôt : un seul aller-retour avant les données. Tout est chiffré en symétrique (AES ou ChaCha20) avec la clé de session." }
    ]
  };
  function dessine(scene, e, i, E, saut) {
    var hist = [];
    for (var k = 0; k <= i; k++) E[k].m.forEach(function (m) { hist.push({ m: m, neuf: k === i }); });
    var H = 96 + hist.length * 58 + (e.verif ? 34 : 0);
    function coupe(t) { if (t.length <= 46) return [t]; var k = t.lastIndexOf(" ", 46); if (k < 20) k = t.indexOf(" ", 46); return k < 0 ? [t] : [t.slice(0, k), t.slice(k + 1)]; }
    var s = '<svg viewBox="0 0 420 ' + H + '" role="img" aria-label="Poignée de main TLS entre le navigateur et le serveur">';
    s += '<g class="bl' + (e.cle ? " ok" : "") + '"><rect x="8" y="8" width="112" height="44" rx="8"/><text class="gd" x="64" y="28" text-anchor="middle">navigateur</text><text class="pt" x="64" y="44" text-anchor="middle">client</text></g>';
    s += '<g class="bl' + (e.cle ? " ok" : "") + '"><rect x="300" y="8" width="112" height="44" rx="8"/><text class="gd" x="356" y="28" text-anchor="middle">serveur</text><text class="pt" x="356" y="44" text-anchor="middle">exemple.fr · 443</text></g>';
    s += '<line x1="64" y1="52" x2="64" y2="' + (H - 6) + '" stroke="var(--ligne2)" stroke-width="2" stroke-dasharray="4 4"/><line x1="356" y1="52" x2="356" y2="' + (H - 6) + '" stroke="var(--ligne2)" stroke-width="2" stroke-dasharray="4 4"/>';
    if (e.cle) s += '<text x="64" y="70" text-anchor="middle" class="pt" style="fill:var(--vert)">🔑 clé de session</text>' + (e.cle === "deux" ? '<text x="356" y="70" text-anchor="middle" class="pt" style="fill:var(--vert)">🔑 clé de session</text>' : "");
    hist.forEach(function (h, k) {
      var y = 100 + k * 58, m = h.m, x1 = m[0] > 0 ? 66 : 354, x2 = m[0] > 0 ? 350 : 70, cl = m[3] ? "ok" : "on";
      var d = "M" + x1 + " " + y + " L" + x2 + " " + y;
      s += '<path class="fil ' + cl + (h.neuf && !saut ? " trace" : "") + '" style="--l:290" d="' + d + '"/><path class="tete-f ' + cl + '" d="M' + (x2 + (m[0] > 0 ? 6 : -6)) + " " + y + " l" + (m[0] > 0 ? -10 : 10) + ' -6 l0 12z"/>';
      s += '<text x="210" y="' + (y - 7) + '" text-anchor="middle" style="font-weight:700">' + (m[3] ? "🔒 " : "") + m[1] + '</text>' + coupe(m[2]).map(function (l, j) { return '<text class="pt" style="font-size:11.5px" x="210" y="' + (y + 17 + j * 14) + '" text-anchor="middle">' + l + "</text>"; }).join("");
      if (h.neuf && !saut) s += archJeton(d, m[3] ? "v" : "", 0.8, 0);
    });
    if (e.verif) s += '<text x="64" y="' + (H - 16) + '" text-anchor="middle" style="font-weight:700;fill:var(--vert)">✓ certificat vérifié</text>';
    scene.innerHTML = s + "</svg>";
  }
  O.lecteur(z, { titre: "la poignée de main de HTTPS", sous: "TLS", choix: [{ k: "prog", t: "le modèle du programme" }, { k: "tls13", t: "TLS 1.3 aujourd’hui" }],
    etapes: function (k) { return SC[k]; }, prepare: function (scene) { scene.parentNode.parentNode.classList.add("ar"); }, dessine: dessine, vitesse: 3200 });
};

CH.push({
  id: "crypto", court: "chiffrement", fichier: "chiffrement.py",
  titre: "Sécurisation des communications",
  rubrique: "Rubrique « Architectures matérielles, systèmes d’exploitation et réseaux » : sécurisation des communications",
  accroche: "Chiffrement symétrique (César, XOR, AES), asymétrique (RSA, clé publique et clé privée), échange de clé, certificats, et comment HTTPS combine tout cela.",
  essentiel: [
    "<b>Chiffrement symétrique</b> : une seule clé secrète, partagée, sert à chiffrer et à déchiffrer (César, XOR, AES). Rapide, mais il faut d’abord partager la clé.",
    "<b>Chiffrement asymétrique</b> : chacun a une <b>clé publique</b> (diffusée, pour chiffrer) et une <b>clé privée</b> (secrète, pour déchiffrer). RSA en est l’exemple. Pas besoin de secret commun, mais calcul lent.",
    "<b>Échange de clé</b> : on chiffre une clé symétrique avec la clé publique du destinataire ; ensuite tout l’échange se fait en symétrique. C’est le <b>chiffrement hybride</b>.",
    "Un <b>certificat</b>, signé par une autorité de certification, garantit qu’une clé publique appartient bien au site visité : sans lui, un intermédiaire pourrait se faire passer pour le serveur.",
    "<b>HTTPS</b> = HTTP + <b>TLS</b> (port 443) : poignée de main (certificat, échange de la clé de session), puis données chiffrées en symétrique."
  ],
  attendus: [
    "Décrire les principes de chiffrement symétrique (clef partagée) et asymétrique (avec clef privée/clef publique).",
    "Décrire l’échange d’une clef symétrique en utilisant un protocole asymétrique pour sécuriser une communication HTTPS.",
    "Le programme précise : les protocoles peuvent être illustrés « en mode débranché, éventuellement avec description d’un chiffrement particulier » ; « la négociation de la méthode de chiffrement du protocole SSL (<i>Secure Sockets Layer</i>) n’est pas abordée »."
  ],
  intro: `<div class="boite ex"><div class="lab"># le vocabulaire compte</div><p><b>Chiffrer</b> : rendre un message illisible avec une clé. <b>Déchiffrer</b> : le rendre lisible <b>avec</b> la clé. <b>Décrypter</b> : le lire <b>sans</b> connaître la clé (casser le chiffrement). « Crypter » n’est pas employé en français correct. Le message lisible s’appelle le <b>texte clair</b>, le message chiffré le <b>cryptogramme</b>.</p></div>`,
  idees: [
    { id: "i1", t: "Les trois objectifs de la sécurité des échanges", h: `
<p>Sur Internet, un paquet traverse des réseaux et des routeurs qui n’appartiennent ni à l’expéditeur ni au destinataire (chapitre « Protocoles de routage »). N’importe lequel pourrait lire ou modifier ce qui passe. Sécuriser une communication, c’est garantir :</p>
<ul><li>la <b>confidentialité</b> : seul le destinataire peut lire le message (chiffrement) ;</li>
<li>l’<b>intégrité</b> : le message n’a pas été modifié en route ;</li>
<li>l’<b>authenticité</b> : on parle bien à celui qu’on croit (le vrai site de la banque, pas une imitation).</li></ul>
<p><b>Exemple</b> : sur un Wi-Fi public, une page en <code>http://</code> circule en clair : le mot de passe tapé dans un formulaire peut être lu par un autre utilisateur du réseau. En <code>https://</code>, il voit seulement des octets chiffrés.</p>
<div class="boite histoire"><div class="lab"># git log --histoire</div><p><span class="commit">1883 <b>·</b></span> Auguste Kerckhoffs énonce dans <i>La Cryptographie militaire</i> un principe toujours suivi : la sécurité d’un chiffrement doit reposer sur le secret de la <b>clé</b>, pas sur le secret de la <b>méthode</b>. AES et RSA sont publics ; seules les clés sont secrètes.</p></div>` },

    { id: "i2", t: "Le chiffrement symétrique : César", h: `
<div class="boite def"><div class="lab">"""définition"""</div><p>Un chiffrement est <b>symétrique</b> quand la <b>même clé</b> sert à chiffrer et à déchiffrer. Les deux correspondants doivent donc partager cette clé, et la garder secrète.</p></div>
<p>Le plus ancien exemple connu : le <b>chiffre de César</b>, que Suétone attribue à Jules César : chaque lettre est remplacée par celle qui se trouve 3 rangs plus loin dans l’alphabet (A → D, B → E… Z → C). La clé est le décalage.</p>
[[cr-cesar]]
<p>Exécute-le pas à pas : regarde l’indice <code>i</code> de chaque lettre et le modulo 26 qui fait revenir Z sur C.</p>
[[w-trace|cr-tr-cesar]]
<p>Il est très faible : il n’y a que 25 clés possibles, on les essaie toutes (attaque par <b>force brute</b>).</p>
[[cr-force]]
<p>Même avec une substitution plus compliquée, chaque lettre est toujours remplacée par la même : l’<b>analyse des fréquences</b>, décrite dès le IXe siècle par le savant arabe al-Kindi, retrouve la lettre qui code E, la plus fréquente en français.</p>
[[cr-frequences]]` },

    { id: "i3", t: "XOR et chiffrements modernes (AES)", h: `
<p>Un ordinateur chiffre des <b>octets</b>, pas des lettres. L’opération de base est le <b>XOR</b> (« ou exclusif », <code>^</code> en Python) : bit à bit, le résultat vaut 1 si les deux bits sont différents. Son intérêt : appliquer deux fois la même clé redonne le message, (m ⊕ k) ⊕ k = m.</p>
[[w-arch-xor]]
[[cr-xor-bits]]
[[cr-xor]]
<p>Si la clé est <b>aléatoire, aussi longue que le message et utilisée une seule fois</b>, le chiffrement est parfaitement sûr : c’est le <b>masque jetable</b> (Gilbert Vernam, 1917 ; Claude Shannon prouve en 1949 qu’il est incassable). Mais il faut échanger à l’avance une clé aussi longue que tous les messages futurs : inutilisable pour le Web.</p>
[[cr-masque]]
<p>Les chiffrements symétriques modernes combinent XOR, substitutions et permutations sur des blocs, en plusieurs tours. Le standard actuel est l’<b>AES</b> (<i>Advanced Encryption Standard</i>), choisi par l’agence américaine NIST en 2000 à l’issue d’un concours public (algorithme Rijndael, des Belges Joan Daemen et Vincent Rijmen) et publié en 2001 : blocs de 128 bits, clés de 128, 192 ou 256 bits. Avec une clé de 128 bits, il y a 2¹²⁸ clés possibles : la force brute est hors de portée. Les processeurs ont des instructions dédiées : il chiffre des gigaoctets par seconde.</p>
<div class="boite attention"><div class="lab">⚠ le problème du symétrique</div><p>Comment Alice et un site web qu’elle n’a jamais visité pourraient-ils partager une clé secrète, alors que tout ce qu’ils s’envoient peut être lu ? Et il faut une clé par paire de correspondants : pour n personnes, n(n − 1) / 2 clés.</p>[[cr-nb-cles]]</div>` },

    { id: "i4", t: "Le chiffrement asymétrique : clé publique, clé privée", h: `
<div class="boite def"><div class="lab">"""définition"""</div><p>Dans un chiffrement <b>asymétrique</b>, chacun possède une <b>paire de clés</b> liées mathématiquement : une <b>clé publique</b>, que tout le monde peut connaître, et une <b>clé privée</b>, que lui seul connaît. Ce qui est chiffré avec la clé publique ne peut être déchiffré qu’avec la clé privée correspondante.</p></div>
<p><b>Image</b> : Bob distribue des cadenas ouverts (clé publique) ; n’importe qui peut fermer une boîte avec, mais seul Bob a la clé qui les ouvre (clé privée). Plus besoin d’échanger un secret à l’avance.</p>
<p>L’algorithme le plus connu est <b>RSA</b> (Rivest, Shamir et Adleman, 1977). Sa sécurité repose sur un problème difficile : à partir de n = p × q, retrouver les deux grands nombres premiers p et q. Multiplier est facile ; factoriser un nombre de plus de 600 chiffres est hors de portée des ordinateurs actuels.</p>
<details class="repli"><summary>RSA avec de petits nombres (le calcul, pour comprendre)</summary><div class="corps">
<ol><li>Choisir deux nombres premiers p et q ; calculer n = p × q et φ = (p − 1)(q − 1).</li>
<li>Choisir e sans diviseur commun avec φ ; calculer d tel que e × d ≡ 1 (mod φ).</li>
<li>Clé publique (n, e) ; clé privée (n, d).</li>
<li>Chiffrer un nombre m &lt; n : c = mᵉ mod n. Déchiffrer : m = cᵈ mod n.</li></ol>
[[cr-rsa]]
<p>La fonction <code>pow(a, b, n)</code> calcule aᵇ mod n rapidement (exponentiation rapide, comme la puissance du chapitre « Récursivité »). Les calculs de modulo et la démonstration du fonctionnement ne sont pas au programme de NSI.</p></div></details>
<p>Contrepartie : le chiffrement asymétrique est beaucoup plus <b>lent</b> que le symétrique (calculs sur des nombres de milliers de bits). On ne l’utilise donc pas pour chiffrer une vidéo entière, mais pour échanger une clé ou signer.</p>
<div class="boite hp"><div class="lab"># la signature numérique</div><p>Dans l’autre sens : ce qui est « chiffré » avec la clé <b>privée</b> peut être vérifié par tous avec la clé <b>publique</b>. Seul le détenteur de la clé privée a pu produire cette valeur : c’est une <b>signature</b>. On signe en pratique une <b>empreinte</b> du document, calculée par une fonction de hachage.</p>[[cr-signature]]</div>
<div class="boite histoire"><div class="lab"># git log --histoire</div><p><span class="commit">1976 <b>·</b></span> Whitfield Diffie et Martin Hellman publient l’idée de la cryptographie à clé publique et une méthode pour fabriquer un secret commun à travers un canal espionné. <span class="commit">1977 <b>·</b></span> Rivest, Shamir et Adleman proposent RSA. (Des chercheurs du renseignement britannique avaient trouvé des idées voisines quelques années plus tôt, restées secrètes jusqu’en 1997.)</p></div>` },

    { id: "i5", t: "Échanger une clé symétrique grâce à l’asymétrique", h: `
<p>On combine le meilleur des deux : l’asymétrique pour partager un secret, le symétrique pour tout le reste. C’est le <b>chiffrement hybride</b>, au cœur de la capacité du programme :</p>
<ol><li>le serveur possède une paire de clés ; il donne sa <b>clé publique</b> au client ;</li>
<li>le client tire au hasard une <b>clé de session</b> symétrique ;</li>
<li>il la <b>chiffre avec la clé publique</b> du serveur et l’envoie ;</li>
<li>le serveur la <b>déchiffre avec sa clé privée</b> ; un espion qui a tout vu passer ne peut pas la lire ;</li>
<li>les deux chiffrent ensuite tous leurs messages avec cette clé de session, en <b>symétrique</b> (AES), ce qui est rapide.</li></ol>
[[cr-hybride]]
<p>Une nouvelle clé de session est tirée à chaque connexion : la découverte de l’une ne compromet pas les autres échanges.</p>` },

    { id: "i6", t: "Certificats et autorités de certification", h: `
<p>Reste une faille : quand le client reçoit « la clé publique du serveur », comment sait-il qu’elle vient vraiment du serveur ? Un attaquant placé entre les deux (attaque de l’<b>homme du milieu</b>) pourrait envoyer <b>sa</b> clé publique, déchiffrer la clé de session, puis relayer les messages en lisant tout.</p>
<div class="boite def"><div class="lab">"""définition"""</div><p>Un <b>certificat</b> est un document électronique qui associe un <b>nom de domaine</b> (par exemple <code>exemple.fr</code>) à une <b>clé publique</b>, avec des dates de validité, et qui est <b>signé</b> par une <b>autorité de certification</b> (AC) après vérification que le demandeur contrôle bien ce domaine.</p></div>
<p>Le navigateur et le système d’exploitation contiennent la liste des clés publiques des autorités reconnues (autorités « racines »). En recevant un certificat, le navigateur vérifie la signature de l’autorité, le nom de domaine et les dates. Si quelque chose ne va pas, il affiche une alerte (« Votre connexion n’est pas privée »). Un attaquant ne peut pas fabriquer un certificat valide pour <code>exemple.fr</code> : il n’a pas la clé privée de l’autorité.</p>
<p><b>Exemple</b> : l’autorité Let’s Encrypt, lancée en 2015, délivre gratuitement des certificats à n’importe quel site qui prouve contrôler son domaine ; elle a beaucoup contribué à généraliser HTTPS.</p>
<div class="boite hp"><div class="lab"># pour aller plus loin : l’empreinte</div><p>Pour signer et pour vérifier l’<b>intégrité</b>, on utilise une <b>fonction de hachage</b> (SHA-256) : elle donne une empreinte de taille fixe ; changer une seule lettre change toute l’empreinte, et on ne sait pas retrouver le texte à partir d’elle.</p>[[cr-hachage]]</div>` },

    { id: "i7", t: "HTTPS : HTTP dans un tunnel TLS", h: `
<p><b>HTTPS</b> est le protocole HTTP du Web, transporté dans une connexion sécurisée par <b>TLS</b> (<i>Transport Layer Security</i>, successeur de SSL). Le serveur écoute sur le port <b>443</b> (au lieu de 80 pour HTTP). La connexion commence par une <b>poignée de main</b> (<i>handshake</i>) :</p>
<ol><li>le client annonce les versions et méthodes de chiffrement qu’il connaît ;</li>
<li>le serveur choisit et envoie son <b>certificat</b> (clé publique signée) ;</li>
<li>le client vérifie le certificat ;</li>
<li>client et serveur établissent une <b>clé de session</b> symétrique (dans le modèle du programme : le client l’envoie chiffrée avec la clé publique du serveur) ;</li>
<li>tout le reste (requêtes, pages, mots de passe, cookies) est chiffré en symétrique avec cette clé.</li></ol>
[[w-arch-tls]]
<p>Le cadenas du navigateur signifie : la connexion est chiffrée, et le certificat est valide pour ce nom de domaine. Il ne dit <b>pas</b> que le site est honnête : un site d’hameçonnage peut avoir un certificat valide pour son propre nom (<code>banque-securite-connexion.com</code>). Il faut aussi lire l’adresse.</p>
<div class="boite hp"><div class="lab"># ce qui se fait aujourd’hui</div><p>Dans TLS 1.3 (RFC 8446, 2018), la clé de session n’est plus envoyée chiffrée par RSA : elle est calculée des deux côtés par un échange de Diffie-Hellman, et le serveur <b>signe</b> l’échange avec sa clé privée pour prouver son identité. Ainsi, même si la clé privée du serveur était volée plus tard, les échanges passés resteraient secrets. Le principe exigé par le programme est le même : asymétrique pour s’accorder sur une clé, symétrique pour les données.</p></div>
<div class="boite histoire"><div class="lab"># git log --histoire</div><p><span class="commit">1995 <b>·</b></span> Netscape diffuse SSL 2.0 dans son navigateur. <span class="commit">1999 <b>·</b></span> TLS 1.0 lui succède (RFC 2246). <span class="commit">2018 <b>·</b></span> TLS 1.3. SSL et les premières versions de TLS sont aujourd’hui abandonnées, à cause de failles.</p></div>` }
  ],
  pieges: [
    { t: "Inverser clé publique et clé privée", h: `<p>Pour <b>chiffrer</b> un message à Bob : clé <b>publique</b> de Bob. Pour le <b>déchiffrer</b> : clé <b>privée</b> de Bob. Pour <b>signer</b> : clé privée de l’expéditeur ; pour vérifier la signature : sa clé publique.</p>` },
    { t: "Dire que HTTPS utilise seulement l’asymétrique", h: `<p>L’asymétrique ne sert qu’au début (échange de la clé de session, authentification). Les données sont chiffrées en symétrique, beaucoup plus rapide.</p>` },
    { t: "Croire que le cadenas garantit un site de confiance", h: `<p>Il garantit une connexion chiffrée avec le détenteur du certificat de <b>ce</b> nom de domaine. Un faux site a lui aussi un cadenas pour son propre nom.</p>` },
    { t: "Confondre déchiffrer et décrypter", h: `<p>Déchiffrer : avec la clé. Décrypter : sans la clé, en cassant le chiffrement.</p>` },
    { t: "Réutiliser un masque jetable", h: `<p>Avec deux messages chiffrés par la même clé XOR, (m₁ ⊕ k) ⊕ (m₂ ⊕ k) = m₁ ⊕ m₂ : la clé disparaît, et l’analyse des deux messages devient possible. Le masque n’est sûr que s’il sert une seule fois.</p>` }
  ],
  retenir: `
<h2>Vocabulaire</h2>
<p>Chiffrer / déchiffrer (avec la clé) / décrypter (sans la clé). Confidentialité, intégrité, authenticité.</p>
<h2>Symétrique</h2>
<ul><li>Une seule clé, partagée, pour chiffrer et déchiffrer.</li><li>César (décalage, 25 clés, analyse des fréquences), XOR ((m ⊕ k) ⊕ k = m), masque jetable, <b>AES</b> (2001, blocs de 128 bits).</li><li>Rapide ; problème : partager la clé (n(n − 1) / 2 clés pour n personnes).</li></ul>
<h2>Asymétrique</h2>
<ul><li>Paire de clés : <b>publique</b> (chiffrer, vérifier une signature) / <b>privée</b> (déchiffrer, signer).</li><li><b>RSA</b> (1977) : difficulté de factoriser n = p × q. Lent.</li></ul>
<h2>Échange de clé (hybride)</h2>
<ol><li>Le client tire une clé de session.</li><li>Il la chiffre avec la clé publique du serveur.</li><li>Le serveur la déchiffre avec sa clé privée.</li><li>Échange chiffré en symétrique avec la clé de session.</li></ol>
<h2>Certificat</h2>
<p>Nom de domaine + clé publique + dates, signé par une autorité de certification ; protège contre l’homme du milieu.</p>
<h2>HTTPS</h2>
<p>HTTP + TLS, port 443. Poignée de main : certificat, vérification, clé de session ; puis données en symétrique (AES).</p>`,
  predis: [
    { code: "cr-x1", niv: "facile", rep: "N + 13 = A, S + 13 = F, I + 13 = V. Avec 26 lettres, décaler deux fois de 13 revient à décaler de 26 : on retrouve le texte (c’est le « ROT13 »)." },
    { code: "cr-x2", niv: "moyen", rep: "101 ⊕ 011 = 110 = 6 ; x ⊕ x = 0 ; x ⊕ 0 = x ; et (5 ⊕ 3) ⊕ 3 = 5 : appliquer la même clé deux fois redonne le message." },
    { code: "cr-x3", niv: "moyen", rep: "8³ = 512 = 9 × 55 + 17, donc c = 17. Avec d = 27 (3 × 27 = 81 = 2 × 40 + 1), 17²⁷ mod 55 redonne 8." },
    { code: "cr-x4", niv: "difficile", rep: "« A » vaut 65 = 0b1000001. 65 ⊕ 1 = 64, le caractère « @ ». Avec la clé de deux octets, les A de rang impair sont combinés avec 2 : 65 ⊕ 2 = 67, « C ». Avec une clé d’un seul octet, des lettres identiques donnent des octets identiques : l’analyse des fréquences marche encore." }
  ],
  ep: [
    { titre: "Le chiffre de Vigenère", enonce: `<p>Le chiffre de Vigenère (XVIe siècle) améliore César : le décalage change à chaque lettre, selon un mot-clé. Avec la clé « NSI », la 1re lettre est décalée de 13 (N), la 2e de 18 (S), la 3e de 8 (I), la 4e de nouveau de 13, etc.</p>[[cr-ep-fourni]]`,
      questions: [
        { q: "Compléter <code>vigenere</code>.", c: `<p>Pour chaque lettre de l’alphabet, décaler de <code>sens × rang(cle[i % len(cle)])</code> modulo 26, puis augmenter <code>i</code> ; recopier les autres caractères sans toucher à <code>i</code>.</p>` },
        { q: "Écrire un jeu de tests : clé « A », clé de deux lettres, aller-retour chiffrement / déchiffrement, texte vide.", c: `[[cr-ep-corr]]` },
        { q: "Pourquoi Vigenère résiste-t-il mieux que César à l’analyse des fréquences ? Le montrer sur un texte de E.", c: `[[cr-ep-freq]]<p>Avec César, la même lettre est toujours chiffrée de la même façon (EEEEEE → RRRRRR). Avec Vigenère, elle donne trois lettres différentes selon sa position : les fréquences sont « lissées ». Il reste cassable (Babbage, Kasiski au XIXe siècle) en trouvant d’abord la longueur de la clé.</p>` },
        { q: "À l’oral : Vigenère est-il un chiffrement symétrique ou asymétrique ?", c: `<p>Symétrique : la même clé (le mot « NSI ») sert à chiffrer et à déchiffrer ; les deux correspondants doivent la partager.</p>` }
      ] }
  ],
  ecrit: { titre: "Chiffrer un échange, du César au HTTPS", points: "≈ 7 points · 40 min", note: "Exercice inventé pour le site, au format de l’épreuve écrite.",
    enonce: `<p>Alice veut envoyer des messages à un serveur web sans qu’un espion connecté au même réseau Wi-Fi puisse les lire.</p>`,
    questions: [
      { q: "Alice et le serveur utilisent le chiffre de César. Chiffrer « BAC » avec la clé 3. Expliquer pourquoi l’espion peut casser ce chiffrement très vite.", pts: "1 pt", c: `<p>« EDF ». Il n’y a que 25 clés : l’espion les essaie toutes (force brute) et garde le texte qui a un sens.</p>` },
      { q: "Rappeler ce qu’est un chiffrement symétrique, et donner la difficulté principale de son utilisation sur le Web.", pts: "1 pt", c: `<p>Une même clé sert à chiffrer et déchiffrer. Il faut la partager à l’avance, secrètement ; or Alice n’a jamais rencontré le serveur, et tout ce qu’ils s’envoient peut être lu.</p>` },
      { q: "Le serveur publie la clé publique RSA (n, e) = (55, 3) ; sa clé privée est d = 27. Alice code sa clé de session par le nombre 8. Que transmet-elle ? Montrer que le serveur retrouve 8.", pts: "2 pts", c: `<p>Elle envoie 8³ mod 55 = 512 mod 55 = 17. Le serveur calcule 17²⁷ mod 55 = 8. L’espion voit 17 mais, sans d, ne peut pas retrouver 8 (avec de vrais nombres de plusieurs centaines de chiffres).</p>[[cr-ecrit-verif]]` },
      { q: "Décrire, en quatre étapes, comment HTTPS utilise le chiffrement asymétrique pour échanger une clé symétrique.", pts: "2 pts", c: `<p>1. Le serveur envoie son certificat, qui contient sa clé publique. 2. Le client vérifie le certificat (signature d’une autorité, nom, dates) puis tire au hasard une clé de session. 3. Il la chiffre avec la clé publique du serveur et l’envoie ; seul le serveur peut la déchiffrer avec sa clé privée. 4. La suite de l’échange est chiffrée en symétrique (AES) avec la clé de session.</p>` },
      { q: "À quoi sert l’autorité de certification ? Quelle attaque empêche-t-elle ?", pts: "1 pt", c: `<p>Elle signe le certificat qui lie le nom du site à sa clé publique. Sans elle, un attaquant placé entre Alice et le serveur pourrait envoyer sa propre clé publique et lire la clé de session : l’attaque de l’homme du milieu.</p>` }
    ],
    methode: `<p>Dans toute question sur les clés, précise <b>de qui</b> est la clé (du serveur, d’Alice) et <b>laquelle</b> (publique ou privée). Pour HTTPS, distingue bien les deux phases : poignée de main (asymétrique) puis données (symétrique).</p>` },
  qcm: [
    { q: "Qu’est-ce qu’un chiffrement symétrique ?", c: ["Un chiffrement dont la clé est un palindrome", "Un chiffrement où la même clé sert à chiffrer et à déchiffrer", "Un chiffrement avec une clé publique et une clé privée", "Un chiffrement sans clé"], a: 1, e: "Les deux correspondants partagent la même clé secrète.", ref: "i2" },
    { q: "Combien de clés différentes (non nulles) le chiffre de César offre-t-il ?", c: ["3", "25", "26 × 26", "2¹²⁸"], a: 1, e: "Les décalages de 1 à 25 ; un décalage de 26 redonne le texte.", ref: "i2" },
    { q: "Quelle méthode casse une substitution lettre à lettre ?", c: ["Le hachage", "L’analyse des fréquences", "Le routage", "Le tri fusion"], a: 1, e: "La lettre la plus fréquente du cryptogramme code souvent E.", ref: "i2" },
    { q: "Que vaut <code>12 ^ 10</code> en Python ?", c: ["22", "6", "2", "120"], a: 1, e: "1100 ⊕ 1010 = 0110 = 6.", ref: "i3" },
    { q: "Pourquoi le XOR convient-il au chiffrement symétrique ?", c: ["Il est irréversible", "(m ⊕ k) ⊕ k = m : la même clé chiffre et déchiffre", "Il compresse le message", "Il ne demande pas de clé"], a: 1, e: "C’est sa propriété clé.", ref: "i3" },
    { q: "AES est…", c: ["un chiffrement asymétrique", "le standard actuel de chiffrement symétrique", "une autorité de certification", "un protocole de routage"], a: 1, e: "Advanced Encryption Standard (2001), blocs de 128 bits.", ref: "i3" },
    { q: "Combien faut-il de clés secrètes pour que 10 personnes puissent chacune communiquer en privé avec chaque autre en symétrique ?", c: ["10", "20", "45", "100"], a: 2, e: "10 × 9 / 2 = 45 : une par paire.", ref: "i3" },
    { q: "Pour envoyer un message confidentiel à Bob en asymétrique, Alice le chiffre avec…", c: ["sa propre clé privée", "la clé publique de Bob", "la clé privée de Bob", "sa propre clé publique"], a: 1, e: "Seul Bob, avec sa clé privée, pourra le déchiffrer.", ref: "i4" },
    { q: "Sur quoi repose la sécurité de RSA ?", c: ["Le secret de l’algorithme", "La difficulté de factoriser un grand nombre n = p × q", "La vitesse du réseau", "La longueur du message"], a: 1, e: "Connaître n ne permet pas, en pratique, de retrouver p et q.", ref: "i4" },
    { q: "Pourquoi n’utilise-t-on pas RSA pour chiffrer toute une vidéo ?", c: ["Il est trop lent", "Il ne chiffre que du texte", "Il est cassé", "Il demande une clé par image"], a: 0, e: "On l’utilise pour échanger une clé ; les données sont chiffrées en symétrique.", ref: "i5" },
    { q: "Dans le chiffrement hybride, la clé de session est…", c: ["la clé privée du serveur", "une clé symétrique tirée au hasard, transmise chiffrée avec la clé publique du serveur", "le mot de passe de l’utilisateur", "la même pour tous les clients"], a: 1, e: "Elle sert ensuite à chiffrer tout l’échange en symétrique.", ref: "i5" },
    { q: "Que contient un certificat de site web ?", c: ["La clé privée du site", "Le nom de domaine, la clé publique du site, des dates, la signature d’une autorité", "Le mot de passe de l’administrateur", "La liste des visiteurs"], a: 1, e: "La clé privée ne quitte jamais le serveur.", ref: "i6" },
    { q: "Contre quelle attaque le certificat protège-t-il ?", c: ["La force brute", "L’homme du milieu, qui se ferait passer pour le serveur", "L’interblocage", "Le débordement de tableau"], a: 1, e: "Sans certificat, rien ne prouve que la clé publique reçue est celle du vrai serveur.", ref: "i6" },
    { q: "HTTPS, c’est…", c: ["HTTP sur le port 80", "HTTP transporté dans une connexion TLS, en général sur le port 443", "un protocole de routage", "un format de page web"], a: 1, e: "TLS chiffre et authentifie ; HTTP reste le protocole du Web.", ref: "i7" },
    { q: "Dans une connexion HTTPS établie, les pages sont chiffrées…", c: ["avec la clé publique du serveur", "en symétrique, avec la clé de session", "avec la clé privée du client", "elles ne sont pas chiffrées"], a: 1, e: "L’asymétrique ne sert qu’à la poignée de main.", ref: "i7" }
  ],
  cartes: [
    { r: "Chiffrer / déchiffrer / décrypter", v: "Rendre illisible avec la clé / rendre lisible avec la clé / lire sans la clé." },
    { r: "Confidentialité, intégrité, authenticité", v: "Seul le destinataire lit ; rien n’est modifié ; on parle au bon interlocuteur." },
    { r: "Chiffrement symétrique", v: "Une même clé secrète, partagée, pour chiffrer et déchiffrer. Rapide." },
    { r: "Chiffre de César", v: "Décalage des lettres (3 pour César) ; 25 clés ; cassé par force brute ou analyse des fréquences." },
    { r: "XOR", v: "Bit à bit : 1 si les bits diffèrent. (m ⊕ k) ⊕ k = m." },
    { r: "Masque jetable", v: "Clé aléatoire aussi longue que le message, utilisée une fois : incassable (Vernam 1917, Shannon 1949)." },
    { r: "AES", v: "Standard de chiffrement symétrique (2001), blocs de 128 bits, clés de 128 à 256 bits." },
    { r: "Chiffrement asymétrique", v: "Clé publique (chiffrer) et clé privée (déchiffrer), liées mathématiquement. Lent." },
    { r: "RSA", v: "Rivest, Shamir, Adleman (1977) ; repose sur la difficulté de factoriser n = p × q." },
    { r: "Signature numérique", v: "Calculée avec la clé privée de l’auteur, vérifiée par tous avec sa clé publique." },
    { r: "Chiffrement hybride", v: "Clé de session symétrique envoyée chiffrée avec la clé publique du destinataire ; puis symétrique." },
    { r: "Certificat", v: "Nom de domaine + clé publique + dates, signé par une autorité de certification." },
    { r: "Homme du milieu", v: "Attaquant entre client et serveur qui se fait passer pour chacun ; contré par les certificats." },
    { r: "HTTPS", v: "HTTP + TLS, port 443 : poignée de main (certificat, clé de session) puis données en symétrique." },
    { r: "Repères", v: "Kerckhoffs 1883 · Diffie-Hellman 1976 · RSA 1977 · SSL 1995 · AES 2001 · TLS 1.3 2018." }
  ]
});
