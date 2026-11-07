#!/bin/bash
# File d'attente des shorts : une voix à la fois, puis planche et vidéo (jamais de navigateur pendant une voix).
# Ajouter un code : echo <code> >> outils/shorts/sortie/file.txt ; lancer : bash outils/shorts/file.sh (s'arrête quand la file est vide 20 min)
cd "$(dirname "$0")/../.."
F=outils/shorts/sortie/file.txt; FAIT=outils/shorts/sortie/fait.txt; touch $F $FAIT
attente=0
while [ $attente -lt 120 ]; do
  code=$(grep -vxF -f $FAIT $F | head -1)
  if [ -z "$code" ]; then sleep 10; attente=$((attente+1)); continue; fi
  attente=0
  echo "== $code : voix $(date +%H:%M)"
  SSL_CERT_FILE=/root/.ccr/ca-bundle.crt REQUESTS_CA_BUNDLE=/root/.ccr/ca-bundle.crt python3 outils/shorts/voix.py $code > outils/shorts/sortie/voix-$code.log 2>&1 || { echo "ÉCHEC voix $code"; echo $code >> $FAIT; continue; }
  tail -1 outils/shorts/sortie/voix-$code.log
  node outils/shorts/verifier.js $code
  curl -s -o /dev/null localhost:8765 || (nohup python3 -m http.server 8765 >/dev/null 2>&1 &); sleep 1
  node outils/shorts/rendu.js $code a --planche 2>&1 | grep -E "erreur|planche"
  node outils/shorts/rendu.js $code a 2>&1 | grep -E "erreur|écrit"
  echo "== $code : fini $(date +%H:%M)"
  echo $code >> $FAIT
done
