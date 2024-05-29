#!/usr/bin/python3
'''3. Develop a simple API using Python with the `http.server` module'''


import http.server
import json
from http import HTTPStatus

class GestionnaireDeRequetesSimple(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Bonjour, ceci est une API simple !")
        elif self.path == '/data':
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == '/status':
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            status = {"status": "OK"}
            self.wfile.write(json.dumps(status).encode('utf-8'))
        else:
            self.send_response(HTTPStatus.NOT_FOUND)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_message = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error_message).encode('utf-8'))

# Configuration et lancement du serveur
adresse_serveur = ('', 8000)
httpd = http.server.HTTPServer(adresse_serveur, GestionnaireDeRequetesSimple)
print("Démarrage du serveur HTTP sur le port 8000")
httpd.serve_forever()
