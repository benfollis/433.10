# Implementation of a rest interface to the sockets
from http.server import SimpleHTTPRequestHandler

class RestServer(SimpleHTTPRequestHandler): 

    # sockets is a hash keyed by socket logical name (a string)
    # wieht each value consisting of a tuple of socket_driver and socket_id

    def do_GET(self):
        path = self.path
        partition = path.rpartition('/')
        state = partition[2].lower()
        # remove leading / in path
        socket_name = partition[0][1:].lower()
        #if the socket name doesn't exist, send a 404
        if socket_name not in self.sockets:
            self.send_error(404, "Switch not found: %s" % socket_name)
        
        socket = self.sockets[socket_name]
        socket.switch_socket(state)
        
        self.send_response(200)
        self.send_header('Content-type','text/html')
        
        self.end_headers()
        message = str("[" + socket_name + "]")
        self.wfile.write(message.encode("utf-8"))
        return
    
    
