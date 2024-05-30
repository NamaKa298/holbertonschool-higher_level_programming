#!/usr/bin/python3
'''3. Develop a simple API using Python with the `http.server` module'''


import http.server
import json
import socketserver
from http import HTTPStatus


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        '''handles GET requests'''
        if self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == '/':
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
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


PORT = 8000


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
