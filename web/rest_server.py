# Implementation of a rest interface to the sockets

class RestServer:

    # sockets is a hash keyed by socket logical name (a string)
    # wieht each value consisting of a tuple of socket_driver and socket_id
    def __init__(self, sockets):
        super.__init__()
        self.sockets = sockets

    def do_GET(self):
        path = self.path
        partition = path.rpartition('/')
        state = partition[2].lower()
        sub_partition = partition[0].rpartition('/')

        socket = self.sockets[socket_name]
        socket_driver = socket[0]
        socket_id = socket[1]
        socket_driver.switch_socket(socket_id, state)
        
        self.send_response(200)
        self.send_header('Content-type','text/html')
        
        self.end_headers()
        self.wfile.write(bytes("FFFF[" + str(switch) + "]FFFFF", "utf-8"))
        return
    
    
