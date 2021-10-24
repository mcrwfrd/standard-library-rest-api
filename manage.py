import json
from http import server

class Server(server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            data = 'Hello, World!'
            self.send_response(200)
        elif self.path == '/ping':
            data = {'data': [{'ping': 'pong'}]}
            self.send_response(200)
        else:
            data = 'Not Found'
            self.send_response(404)

        self.send_header('Conent-Type', 'application/json')        
        self.end_headers()
        response = bytes(json.dumps(data), 'UTF-8')
        self.wfile.write(response)

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = server.HTTPServer(server_address, Server)
    httpd.serve_forever()
