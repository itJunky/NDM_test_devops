#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 80


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        client_ip = self.client_address[0]
        xff_headers = self.headers.get_all("X-Forwarded-For") or []

        lines = [
            f"Remote IP: {client_ip}",
            "",
        ]

        if xff_headers:
            lines.append("X-Forwarded-For headers:")
            for value in xff_headers:
                lines.append(f"  {value}")
        else:
            lines.append("X-Forwarded-For: (not present)")

        body = "\n".join(lines) + "\n"

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body.encode())))
        self.end_headers()
        self.wfile.write(body.encode())

    def log_message(self, fmt, *args):
        print(f"{self.client_address[0]} - {fmt % args}")


if __name__ == "__main__":
    server = HTTPServer(("", PORT), Handler)
    print(f"Listening on port {PORT}")
    server.serve_forever()
