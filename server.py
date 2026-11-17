from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlsplit, unquote
import os
import threading
import webbrowser

ROOT = Path(__file__).resolve().parent
HOST = os.environ.get('HOST', '127.0.0.1')
PORT = int(os.environ.get('PORT', '8000'))
OPEN_BROWSER = os.environ.get('OPEN_BROWSER', '0') == '1'

class Handler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Keep every request inside the demo folder.
        raw = unquote(urlsplit(path).path).lstrip('/')
        candidate = (ROOT / raw).resolve()
        try:
            candidate.relative_to(ROOT)
        except ValueError:
            return str(ROOT / '__not_found__')
        return str(candidate)

    def do_GET(self):
        if urlsplit(self.path).path == '/health':
            body = b'{"status":"ok","app":"AgriPulse"}'
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if urlsplit(self.path).path == '/data/details.json':
            target = ROOT / 'data' / 'details.json.gz'
            if not target.is_file():
                self.send_error(404, 'Missing compressed detail data')
                return
            payload = target.read_bytes()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Content-Encoding', 'gzip')
            self.send_header('Content-Length', str(len(payload)))
            self.send_header('Cache-Control', 'no-cache')
            self.end_headers()
            self.wfile.write(payload)
            return
        return super().do_GET()

if __name__ == '__main__':
    os.chdir(ROOT)
    url = f'http://{HOST}:{PORT}'
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f'AgriPulse đang chạy: {url}')
    print('Giữ cửa sổ này mở. Nhấn Ctrl+C để dừng.')
    if OPEN_BROWSER:
        threading.Timer(1.0, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nĐã dừng AgriPulse.')
    finally:
        server.server_close()
