import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = "pages"

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving pages at http://localhost:{PORT}")
    httpd.serve_forever()