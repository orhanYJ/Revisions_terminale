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
                  PAR_HEURE questions par heure.

   Le site choisit tout dans assistant.js, sans recoller ce code dans Cloudflare :
   - « modele » : le modèle qui rédige, parmi la liste MODELES ;
   - « relecteur » (facultatif) : un second modèle qui vérifie la réponse (dates,
     chiffres, noms, définitions, calculs refaits), la corrige et la complète ;
   - « effort » (facultatif : low, medium, high) : profondeur de raisonnement, pour
     les modèles qui la prennent en charge.

   Les modèles marqués « payant » ne répondent qu'avec l'offre Workers Paid ; sur
   l'offre gratuite ils renvoient une erreur et le site l'affiche. */

const ORIGINES = ["https://orhanyj.github.io"];

// Modèles autorisés et longueur maximale générée (les modèles qui raisonnent avant
// de répondre comptent leur raisonnement dans ces jetons).
const MODELES = {
  "@cf/meta/llama-3.3-70b-instruct-fp8-fast": 900,
  "@cf/openai/gpt-oss-120b": 6000,
  "@cf/nvidia/nemotron-3-120b-a12b": 6000,
  "@cf/google/gemma-4-26b-a4b-it": 4000,
  "@cf/qwen/qwen3.8-27b": 4000,
  "@cf/mistralai/mistral-small-3.1-24b-instruct": 1500,
  "@cf/moonshotai/kimi-k2.5": 6000,
  // payants (offre Workers Paid)
  "@cf/moonshotai/kimi-k2.6": 6000,
  "@cf/zai-org/glm-5.3": 6000,
  "@cf/deepseek-ai/deepseek-v4-pro-0813": 6000,
  "@cf/deepseek-ai/deepseek-v4-flash-0731": 6000
};
// Modèles qui acceptent une profondeur de raisonnement (« effort »).
const AVEC_EFFORT = ["@cf/openai/gpt-oss-120b"];
const EFFORTS = ["low", "medium", "high"];
const MODELE_DEFAUT = "@cf/meta/llama-3.3-70b-instruct-fp8-fast";

const MAX_QUESTION = 1500;   // caractères par message
const MAX_HISTORIQUE = 6;    // messages précédents gardés pour les questions de suite
const PAR_HEURE = 30;        // questions par visiteur et par heure (si COMPTEURS existe)
// Budget de neurones par jour, tous visiteurs confondus (si COMPTEURS existe). Sur l'offre
// gratuite, Cloudflare plafonne de toute façon à 10 000. Avec l'offre Workers Paid, chaque
// tranche de 1 000 neurones au-delà de 10 000 coûte 0,011 $ : 40 000 par jour plafonnent
// la dépense à environ 0,33 $ par jour, soit 10 $ par mois au pire.
const PLAFOND_JOUR = 40000;

const MATIERES = {
  svt: "la spécialité SVT (sciences de la vie et de la Terre)",
  pc: "la spécialité physique-chimie",
  dnl: "l'histoire-géographie en DNL, dans la section britannique du Baccalauréat français international (cours et épreuves en anglais)"
};

function consignes(matiere) {
  // DNL : consigne en anglais, sinon le modèle répond en français aux questions posées en anglais.
  if (matiere === "dnl") {
    return "You are a revision assistant for a French Terminale student in the British section of the " +
      "Baccalauréat français international: history and geography are taught and examined in English. " +
      "Answer the question clearly and accurately, at final-year secondary school level. " +
      "Be concise: a few paragraphs at most, with a list when it helps. " +
      "Check chronology: never present a later event as a cause of an earlier one. " +
      "If any point of your answer is uncertain (a date, a figure, a name, a definition), end with one " +
      "last line starting with \"To check:\" that names it; if nothing is uncertain, do not add that line. " +
      "Always answer in the language of the student's last message: a question in English gets an answer " +
      "in English; a question in French gets an answer in French, with the key English terms in brackets.";
  }
  const texte =
    "Tu es un assistant de révision pour un élève de Terminale en France, en " + MATIERES[matiere] + ". " +
    "Réponds à la question posée, clairement et précisément, au niveau du programme de Terminale. " +
    "Sois concis : quelques paragraphes au plus, avec une liste quand elle aide. " +
    "Écris les formules en texte simple (par exemple C = n / V, CO2, 10^-3), sans LaTeX. " +
    "Si un point de ta réponse est incertain (une date, un chiffre, un nom, une définition), termine par " +
    "une dernière ligne commençant par « À vérifier : » qui le précise ; si rien n'est incertain, n'ajoute pas cette ligne. " +
    "Réponds dans la langue de la question.";
  return texte;
}

// Consigne du relecteur : il reçoit la conversation et le brouillon, et rend la réponse finale.
function consignesRelecture(matiere) {
  if (matiere === "dnl") {
    return "You are a demanding expert reviewer (a history and geography examiner). You receive a student's question " +
      "and a draft answer written by another assistant. Check every single claim: dates (day, month, year), figures, " +
      "names, places, the order of events, definitions, causes and consequences. Never present a later event as a cause " +
      "of an earlier one. Fix every error or imprecision, add what is essential and missing to answer the question, " +
      "remove what is false or off-topic. Return only the final corrected answer, written for the student, without " +
      "mentioning the review or the draft. Be concise: a few paragraphs at most, with a list when it helps. " +
      "If a point is still uncertain after checking, end with one last line starting with \"To check:\" that names it; " +
      "otherwise do not add that line. Answer in the language of the student's question.";
  }
  return "Tu es un relecteur expert et exigeant (professeur agrégé de " +
    (matiere === "svt" ? "SVT" : "physique-chimie") + "). Tu reçois la question d'un élève de Terminale et un brouillon " +
    "de réponse rédigé par un autre assistant. Vérifie une à une chaque affirmation : définitions, mécanismes, vocabulaire " +
    "exact (par exemple chromosomes homologues et chromatides sœurs ne sont pas interchangeables), noms, lieux, dates, " +
    "valeurs numériques et unités. Refais chaque calcul. Corrige toute erreur ou imprécision, ajoute ce qui manque " +
    "d'essentiel pour répondre à la question, supprime ce qui est faux ou hors sujet. Rends uniquement la réponse finale " +
    "corrigée, rédigée pour l'élève, sans mentionner la relecture ni le brouillon. Sois concis : quelques paragraphes au " +
    "plus, avec une liste quand elle aide. Écris les formules en texte simple (par exemple C = n / V, CO2, 10^-3), sans LaTeX. " +
    "Si un point reste incertain après vérification, termine par une dernière ligne commençant par « À vérifier : » qui le " +
    "précise ; sinon n'ajoute pas cette ligne. Réponds dans la langue de la question.";
}

function demandeRelecture(messages, brouillon) {
  const avant = messages.slice(0, -1).map((m) => (m.role === "user" ? "Élève : " : "Assistant : ") + m.content).join("\n\n");
  return (avant ? "Conversation précédente :\n" + avant + "\n\n" : "") +
    "Question de l'élève :\n" + messages[messages.length - 1].content +
    "\n\nBrouillon de réponse à relire :\n" + brouillon;
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

// Récupère le texte final, quelle que soit la forme de sortie du modèle :
// { response }, format « chat completions » ({ choices }) ou « Responses » ({ output }).
function texteDe(sortie) {
  if (!sortie) return "";
  let texte = "";
  if (typeof sortie === "string") texte = sortie;
  else if (typeof sortie.response === "string") texte = sortie.response;
  else if (typeof sortie.output_text === "string") texte = sortie.output_text;
  else if (Array.isArray(sortie.choices) && sortie.choices[0]) {
    const m = sortie.choices[0].message || {};
    texte = typeof m.content === "string" ? m.content : (sortie.choices[0].text || "");
  } else if (Array.isArray(sortie.output)) {
    texte = sortie.output
      .filter((o) => o && o.type === "message" && Array.isArray(o.content))
      .map((o) => o.content.filter((c) => c && typeof c.text === "string" && c.type !== "reasoning_text").map((c) => c.text).join(""))
      .join("\n");
  }
  // certains modèles laissent leur raisonnement entre balises <think>
  return String(texte || "").replace(/<think>[\s\S]*?<\/think>/g, "").trim();
}

// Appelle un modèle ; si la profondeur de raisonnement est refusée, réessaie sans.
async function appeler(env, modele, messages, effort) {
  const base = { messages: messages, max_tokens: MODELES[modele] };
  if (effort && AVEC_EFFORT.includes(modele)) {
    try {
      return await env.AI.run(modele, Object.assign({ reasoning: { effort: effort } }, base));
    } catch (e) {
      const msg = String((e && e.message) || e);
      if (msg.includes("3036") || /daily free allocation/i.test(msg)) throw e;
    }
  }
  return env.AI.run(modele, base);
}

function neurones(sortie) {
  return (sortie && sortie.usage && typeof sortie.usage.neurons === "number") ? sortie.usage.neurons : 0;
}

// Budget quotidien commun (clé du jour UTC), seulement si COMPTEURS est relié.
function cleJour() {
  return "neurones:" + new Date().toISOString().slice(0, 10);
}
async function budgetEpuise(env) {
  if (!env.COMPTEURS) return false;
  return parseFloat((await env.COMPTEURS.get(cleJour())) || "0") >= PLAFOND_JOUR;
}
async function compter(env, n) {
  if (!env.COMPTEURS || !n) return;
  const deja = parseFloat((await env.COMPTEURS.get(cleJour())) || "0");
  await env.COMPTEURS.put(cleJour(), String(Math.round(deja + n)), { expirationTtl: 2 * 86400 });
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
    const modele = corps.modele == null ? MODELE_DEFAUT : corps.modele;
    if (!Object.prototype.hasOwnProperty.call(MODELES, modele)) return erreur("requete", 400, origine);
    const relecteur = corps.relecteur == null ? null : corps.relecteur;
    if (relecteur !== null && !Object.prototype.hasOwnProperty.call(MODELES, relecteur)) return erreur("requete", 400, origine);
    const effort = EFFORTS.includes(corps.effort) ? corps.effort : null;

    if (await depasseLimite(env, request)) return erreur("limite", 429, origine);
    if (await budgetEpuise(env)) return erreur("quota", 429, origine);

    try {
      const sortie = await appeler(env, modele, [{ role: "system", content: consignes(matiere) }].concat(messages), effort);
      const brouillon = texteDe(sortie);
      if (!brouillon) {
        // forme de sortie inconnue : un aperçu aide à adapter texteDe
        return repondre({ erreur: "erreur", apercu: JSON.stringify(sortie).slice(0, 400) }, 502, origine);
      }
      let texte = brouillon, relu = false, neuronesRelecture = 0;
      if (relecteur) {
        // la relecture est un plus : si elle échoue, on rend le brouillon
        try {
          const revue = await appeler(env, relecteur, [
            { role: "system", content: consignesRelecture(matiere) },
            { role: "user", content: demandeRelecture(messages, brouillon) }
          ], effort);
          const corrige = texteDe(revue);
          neuronesRelecture = neurones(revue);
          if (corrige) { texte = corrige; relu = true; }
        } catch (e) { /* brouillon rendu tel quel */ }
      }
      await compter(env, neurones(sortie) + neuronesRelecture);
      return repondre({
        reponse: texte, modele: modele, relecteur: relu ? relecteur : null, effort: effort,
        usage: { neurons: neurones(sortie) + neuronesRelecture, redaction: sortie.usage || null }
      }, 200, origine);
    } catch (e) {
      const msg = String((e && e.message) || e);
      // 3036 : quota gratuit du jour épuisé ; 3040 : capacité momentanément dépassée.
      if (msg.includes("3036") || /daily free allocation|neurons/i.test(msg)) return erreur("quota", 429, origine);
      if (msg.includes("3040") || /capacity/i.test(msg)) return erreur("occupe", 503, origine);
      return repondre({ erreur: "erreur", detail: msg.slice(0, 200) }, 502, origine);
    }
  }
};
