"""Minimal static server for button-app. No extra deps."""
import http.server
import functools
import pathlib

DIR = pathlib.Path(__file__).parent.resolve()
PORT = 8000

try:
    import mimetypes
    mimetypes.add_type("application/manifest+json", ".webmanifest")
except Exception:
    pass


class PWAHandler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        ".webmanifest": "application/manifest+json",
    }


Handler = functools.partial(PWAHandler, directory=str(DIR))

if __name__ == "__main__":
    with http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler) as httpd:
        print(f"Serving {DIR} at http://127.0.0.1:{PORT}")
        httpd.serve_forever()
