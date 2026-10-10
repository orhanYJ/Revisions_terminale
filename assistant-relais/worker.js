/* Relais de l'assistant de révision — Cloudflare Worker
   Reçoit la question posée depuis un site de révision, la transmet à Workers AI
   et renvoie la réponse. Aucune clé d'API : l'IA est appelée par la liaison « AI »
   du Worker. Le plafond quotidien est celui de l'offre gratuite de Cloudflare
   (10 000 neurones par jour, remis à zéro à 00:00 UTC) : au-delà, Workers AI
   refuse et le site affiche « reviens demain ». Rien n'est facturé sur l'offre
   gratuite.

   Liaisons à créer dans le tableau de bord Cloudflare (voir GUIDE.md) :
   - AI         : Workers AI (obligatoire)
   - COMPTEURS  : espace KV (facultatif) ; s'il existe, limite chaque visiteur à
                  PAR_HEURE questions par heure. */

const ORIGINES = ["https://orhanyj.github.io"];
const MODELE = "@cf/meta/llama-3.3-70b-instruct-fp8-fast";

const MAX_QUESTION = 1500;   // caractères par message
const MAX_HISTORIQUE = 6;    // messages précédents gardés pour les questions de suite
const MAX_REPONSE = 900;     // jetons générés au plus
const PAR_HEURE = 30;        // questions par visiteur et par heure (si COMPTEURS existe)

const MATIERES = {
  svt: "la spécialité SVT (sciences de la vie et de la Terre)",
  pc: "la spécialité physique-chimie",
  dnl: "l'histoire-géographie en DNL, dans la section britannique du Baccalauréat français international (cours et épreuves en anglais)"
};

function consignes(matiere) {
  let texte =
    "Tu es un assistant de révision pour un élève de Terminale en France, en " + MATIERES[matiere] + ". " +
    "Réponds à la question posée, clairement et précisément, au niveau du programme de Terminale. " +
    "Sois concis : quelques paragraphes au plus, avec une liste quand elle aide. " +
    "Écris les formules en texte simple (par exemple C = n / V, CO2, 10^-3), sans LaTeX. " +
    "Si tu n'es pas sûr d'un fait, d'une date ou d'un chiffre, dis-le. " +
    "Réponds dans la langue de la question.";
  if (matiere === "dnl") {
    texte += " Quand tu réponds en français, donne aussi les termes clés en anglais.";
  }
  return texte;
}

function entetes(origine) {
  const h = { "Content-Type": "application/json; charset=utf-8", "Vary": "Origin" };
  if (ORIGINES.includes(origine)) {
    h["Access-Control-Allow-Origin"] = origine;
    h["Access-Control-Allow-Methods"] = "POST, OPTIONS";
    h["Access-Control-Allow-Headers"] = "Content-Type";
    h["Access-Control-Max-Age"] = "86400";
  }
  return h;
}

function repondre(corps, statut, origine) {
  return new Response(JSON.stringify(corps), { status: statut, headers: entetes(origine) });
}

function erreur(code, statut, origine) {
  return repondre({ erreur: code }, statut, origine);
}

// Vérifie la forme de la conversation envoyée par le site.
function lireMessages(liste) {
  if (!Array.isArray(liste) || liste.length === 0) return null;
  const garde = liste.slice(-(MAX_HISTORIQUE + 1));
  const propres = [];
  for (const m of garde) {
    if (!m || (m.role !== "user" && m.role !== "assistant")) return null;
    if (typeof m.content !== "string") return null;
    const contenu = m.content.trim();
    if (!contenu || contenu.length > (m.role === "user" ? MAX_QUESTION : 6000)) return null;
    propres.push({ role: m.role, content: contenu });
  }
  while (propres.length && propres[0].role !== "user") propres.shift();
  if (!propres.length || propres[propres.length - 1].role !== "user") return null;
  return propres;
}

// Limite par visiteur, seulement si l'espace KV COMPTEURS est relié.
async function depasseLimite(env, request) {
  if (!env.COMPTEURS) return false;
  const ip = request.headers.get("CF-Connecting-IP") || "inconnu";
  const heure = Math.floor(Date.now() / 3600000);
  const cle = "q:" + ip + ":" + heure;
  const n = parseInt((await env.COMPTEURS.get(cle)) || "0", 10);
  if (n >= PAR_HEURE) return true;
  await env.COMPTEURS.put(cle, String(n + 1), { expirationTtl: 3700 });
  return false;
}

export default {
  async fetch(request, env) {
    const origine = request.headers.get("Origin") || "";

    if (request.method === "OPTIONS") {
      return new Response(null, { status: ORIGINES.includes(origine) ? 204 : 403, headers: entetes(origine) });
    }
    if (request.method === "GET") {
      return new Response("Relais de l'assistant : en service.", {
        headers: { "Content-Type": "text/plain; charset=utf-8" }
      });
    }
    if (request.method !== "POST") return erreur("requete", 405, origine);
    if (!ORIGINES.includes(origine)) return erreur("origine", 403, origine);
    if (!env.AI) return erreur("configuration", 500, origine);

    let corps;
    try {
      corps = await request.json();
    } catch (e) {
      return erreur("requete", 400, origine);
    }
    const matiere = corps && corps.matiere;
    if (!Object.prototype.hasOwnProperty.call(MATIERES, matiere)) return erreur("requete", 400, origine);
    const messages = lireMessages(corps.messages);
    if (!messages) return erreur("requete", 400, origine);

    if (await depasseLimite(env, request)) return erreur("limite", 429, origine);

    try {
      const sortie = await env.AI.run(MODELE, {
        messages: [{ role: "system", content: consignes(matiere) }].concat(messages),
        max_tokens: MAX_REPONSE
      });
      const texte = sortie && typeof sortie.response === "string" ? sortie.response.trim() : "";
      if (!texte) return erreur("erreur", 502, origine);
      return repondre({ reponse: texte }, 200, origine);
    } catch (e) {
      const msg = String((e && e.message) || e);
      // 3036 : quota gratuit du jour épuisé ; 3040 : capacité momentanément dépassée.
      if (msg.includes("3036") || /daily free allocation|neurons/i.test(msg)) return erreur("quota", 429, origine);
      if (msg.includes("3040") || /capacity/i.test(msg)) return erreur("occupe", 503, origine);
      return erreur("erreur", 502, origine);
    }
  }
};
