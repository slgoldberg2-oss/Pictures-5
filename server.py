import http.server, os

port = int(os.environ.get('PORT', 5000))
handler = http.server.SimpleHTTPRequestHandler
server = http.server.HTTPServer(('0.0.0.0', port), handler)
print(f'Serving on port {port}')
server.serve_forever()
