# coding: utf-8

# mini serveur web
# print current time
# print HTTP headers in Python dict format
# launch on Windows: python server.py --bind 127.0.0.1
# launch on MacOS: python server.py --bind 0.0.0.0

import time

from http.server import SimpleHTTPRequestHandler
import socketserver

PORT = 8000

class GetHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        headers = '<br />'.join(["'{}': '{}',".format(key, value) for key, value in self.headers.items()])
        html = '<!doctype html><html>{}<br />{}</html>'.format(str(time.ctime()), headers)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(html, 'utf-8'))

def run():
    httpd = socketserver.TCPServer(("", PORT), GetHandler)
    print("serving at port", PORT)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
