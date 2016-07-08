from energenie import switch_on, switch_off

# class that switches via the Raspberry pi  Energenie remote python module
# No bit driver is needed since the module has its own

class RpiEnergenieRemote:

    def __init__(self, socket_id):
        self.socket_id = int(socket_id)

    def switch_socket(self, state):
        if state == 'on':
            switch_on(self.socket_id)
        if state == 'off':
            switch_off(self.socket_id)
