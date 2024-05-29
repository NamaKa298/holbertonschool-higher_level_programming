#!/usr/bin/python3
'''3. Develop a simple API using Python with the `http.server` module'''


import http.server
import json
import socketserver


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        '''handles GET requests'''
        if self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))
            

PORT = 8080

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()