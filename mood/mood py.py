from http.server import BaseHTTPRequestHandler, HTTPServer

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyServer)
    print('Server running at localhost:8000')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
