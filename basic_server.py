# basic server to test the web server stuff, to be deleted
import bit_drivers
import socket_drivers
import web

import SimpleHTTPServer
import SocketServer


if __name__ == '__main__': # which it will:
    rpi_gpio = bit_drivers.RpiGpio(24, 0)
    mercury_socket_driver = socket_drivers.Mercury(rpi_gpio)
    handler = web.RestServer
    handler.sockets = {'sergio' : (mercury_socket_driver, 5)}
    server = SocketServer.TCPServer(('', 8080), web.RestServer)
    server.serve_forever()
    
