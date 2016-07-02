# Implementation of a rest interface to the sockets
from SimpleHTTPServer import SimpleHTTPRequestHandler

class RestServer(SimpleHTTPRequestHandler): 

    # sockets is a hash keyed by socket logical name (a string)
    # wieht each value consisting of a tuple of socket_driver and socket_id

    def do_GET(self):
        path = self.path
        partition = path.rpartition('/')
        state = partition[2].lower()
        print state
        # remove leading / in path
        socket_name = partition[0][1:].lower()
        print socket_name
        socket = self.sockets[socket_name]
        print socket
        socket_driver = socket[0]
        socket_id = socket[1]
        socket_driver.switch_socket(socket_id, state)
        
        self.send_response(200)
        self.send_header('Content-type','text/html')
        
        self.end_headers()
        message = unicode("[" + socket_name + "]")
        self.wfile.write(message.encode("utf-8"))
        return
    
    
