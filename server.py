from http.server import HTTPServer, BaseHTTPRequestHandler

INDEX_LOCATION = "html"
HOST_LOCATION = ("localhost", 8080)

# WARNING: BaseHTTPRequestHandler does not have any security
# This allows malicious actors to access files on your computer
# without your knowledge.

# USE AT YOUR OWN RISK

class MyServer(BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        pass

    def do_GET(self):
        if self.path == '/':
            self.path = f"/{INDEX_LOCATION}/index.html"
            print(self.path)
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print("Received data:", post_data.decode('utf-8'))
        self.send_response(303)
        self.send_header("Location", f"/{INDEX_LOCATION}/index.html")
        self.end_headers()




Server = HTTPServer(HOST_LOCATION, MyServer)

try:
    print("Server Started")
    print(Server.server_address)
    Server.serve_forever()
except KeyboardInterrupt:
    Server.shutdown()
    print("Server Shutdown")