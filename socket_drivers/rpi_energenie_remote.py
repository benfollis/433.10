from energenie import switch_on, switch_off

# class that switches via the Raspberry pi  Energenie remote python module
# No bit driver is needed since the module has its own

class RpiEnergenieRemote:

    def __init__(self):

    def switch_socket(self, socket_id, state):
        if state == 'on':
            switch_on(socket_id)
        if state == 'off':
            switch_off(socket_id)
