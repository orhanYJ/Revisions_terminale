"""Serveur local de test qui gère les requêtes par plages (Range), comme GitHub Pages.

Usage (depuis la racine du dépôt) : python3 outils/serie-philo/serveur.py   (port 8765, pour video.js et les tests du lecteur)
"""
import os, re, http.server, socketserver


class H(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def send_head(self):
        self._n = None
        rng = self.headers.get('Range')
        path = self.translate_path(self.path)
        if not rng or not os.path.isfile(path):
            return super().send_head()
        m = re.match(r'bytes=(\d*)-(\d*)', rng)
        size = os.path.getsize(path)
        a = int(m.group(1) or 0)
        b = min(int(m.group(2) or size - 1), size - 1)
        f = open(path, 'rb')
        f.seek(a)
        self._n = b - a + 1
        self.send_response(206)
        self.send_header('Content-Type', self.guess_type(path))
        self.send_header('Content-Range', f'bytes {a}-{b}/{size}')
        self.send_header('Content-Length', str(self._n))
        self.send_header('Accept-Ranges', 'bytes')
        self.end_headers()
        return f

    def copyfile(self, src, dst):
        n = self._n
        if n is None:
            return super().copyfile(src, dst)
        while n > 0:
            c = src.read(min(65536, n))
            if not c:
                break
            dst.write(c)
            n -= len(c)


socketserver.ThreadingTCPServer.allow_reuse_address = True
with socketserver.ThreadingTCPServer(('', 8765), H) as s:
    s.serve_forever()
