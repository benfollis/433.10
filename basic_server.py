# basic server to test the web server stuff, to be deleted
from bit_drivers import Rpi.GPIO
from socket_drivers import Mercury
from web import RestServer

import http.server
from http.server import BaseHTTPRequestHandler, HTTPServer

if __name__ == '__main__': # which it will:
    rpi_gpio = Rpi.GPIO(24, 0)
    mercury_socket_driver = Mercury(rpi_gpio)
    server = HTTPServer(('', 8080), RestServer)
    server.serve_forever()
    
