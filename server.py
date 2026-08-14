import http.server
import socketserver
import threading
import subprocess
import os

PORT = int(os.environ.get("PORT", 7860))

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hermes Agent is running!")

def run_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving HTTP on port {PORT}")
        httpd.serve_forever()

def run_gateway():
    subprocess.run(["hermes", "gateway"])

if __name__ == "__main__":
    t_server = threading.Thread(target=run_server, daemon=True)
    t_server.start()
    run_gateway()
