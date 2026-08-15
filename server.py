import http.server
import socketserver
import threading
import subprocess
import os
import shutil

PORT = int(os.environ.get("PORT", 7860))

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hermes Agent gateway is active!")

def run_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving HTTP on port {PORT}")
        httpd.serve_forever()

def run_gateway():
    # Ensure ~/.hermes directory exists and copy config.yaml there
    hermes_dir = os.path.expanduser("~/.hermes")
    os.makedirs(hermes_dir, exist_ok=True)
    if os.path.exists("config.yaml"):
        shutil.copy("config.yaml", os.path.join(hermes_dir, "config.yaml"))
        print("Copied config.yaml to ~/.hermes/config.yaml")

    print("Starting hermes gateway process...")
    process = subprocess.Popen(
        ["hermes", "gateway"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True
    )
    for line in process.stdout:
        print("[Gateway]", line, end="")

if __name__ == "__main__":
    t_server = threading.Thread(target=run_server, daemon=True)
    t_server.start()
    run_gateway()
