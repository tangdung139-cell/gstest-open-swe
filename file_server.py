"""
A lightweight Python file server to serve files from the current directory.
"""

from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

def start_server(port=8000):
    """Start a simple HTTP file server."""
    print("Starting server on port {}...".format(port))
    print("Serving files from directory: {}".format(os.getcwd()))
    try:
        httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    except OSError as e:
        print(f"Port {port} is not available. Trying with a random available port...")
        httpd = HTTPServer(("", 0), SimpleHTTPRequestHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.server_close()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Start a simple Python file server.")
    parser.add_argument("-p", "--port", type=int, default=9000, help="Port to serve on (default: 9000)")
    args = parser.parse_args()

    start_server(port=args.port)