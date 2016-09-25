# Parent class of all OOK (On/Off Keyed) sockets


class OokSocket:

    def __init__(self, bit_driver, socket_id):
        self.bit_driver = bit_driver
        self.socket_id = int(socket_id)

    def switch_socket(self, state):
        print("setting socket " + str(self.socket_id) + " to " + state)
        code = self.SOCKET_CODES[self.socket_id][state]
        print("using code " + code)
        for t in range(self.TRANSMIT_ATTEMPTS):
            self.bit_driver.send_sequence(code, self.SYMBOL_DURATION)
            # bring the socket low for the attempt delay
            self.bit_driver.send_bit(0, self.ATTEMPT_DELAY)
