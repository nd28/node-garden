"""Minimal static server for button-app. No extra deps."""
import http.server
import functools
import pathlib

DIR = pathlib.Path(__file__).parent.resolve()
PORT = 8000

Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(DIR))

if __name__ == "__main__":
    with http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler) as httpd:
        print(f"Serving {DIR} at http://127.0.0.1:{PORT}")
        httpd.serve_forever()
