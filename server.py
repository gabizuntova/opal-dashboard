import http.server, socketserver, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
with socketserver.TCPServer(("", 3456), http.server.SimpleHTTPRequestHandler) as httpd:
    print("Serving opal-dashboard on http://localhost:3456")
    httpd.serve_forever()
