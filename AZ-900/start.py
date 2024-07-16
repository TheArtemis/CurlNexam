import http.server
import socketserver
import os
import argparse

DEFAULT_PORT = 1234
DIRECTORY = "pages"

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def parse_args():
    parser = argparse.ArgumentParser(description="Run a simple HTTP server.")
    parser.add_argument("-p", "--port", type=int, default=DEFAULT_PORT, help="Specify port number, default is 1234.")
    return parser.parse_args()       


def run_server(port=DEFAULT_PORT):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with socketserver.TCPServer(("", port), CustomHandler) as httpd:
        print(f"Serving pages at http://localhost:{port}")
        httpd.serve_forever()

if __name__ == "__main__":
    args = parse_args()
    run_server(port=args.port)