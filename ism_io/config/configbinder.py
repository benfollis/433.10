import json
from ism_io.bit_drivers.dummy import Dummy
try:
    from ism_io.bit_drivers.rpigpio import RpiGpio
    from ism_io.socket_drivers.rpi_energenie_remote import RpiEnergenieRemote
except ImportError:
    pass # fail later

from ism_io.socket_drivers.mercury import Mercury

# Basic config binder.
# Names are case insensitive, and will be converted to python strings from
# unicode. Hence it's not recommended to use non-ASCII names
class ConfigBinder:

    def __init__(self, config_file_path):
        config_file = open(config_file_path, "r")
        config_data = config_file.read()
        self.config = json.loads(config_data)
        self.bit_drivers = {}

    def bind(self):
        self.bound_config = {"sockets" : {}}
        for bit_driver in self.config["bit_drivers"]:
            self._create_bit_driver(bit_driver)
        for socket in self.config["sockets"]:
            self._create_socket(socket)
        if "rest" in self.config:
            self._create_rest_server(self.config["rest"])
        return self.bound_config

    def _create_rest_server(self, rest_config):
        self.bound_config["rest"] = { "port" : int(rest_config["port"])}
        
    def _create_bit_driver(self, bit_config):
        if bit_config["type"].lower() == "rpigpio":
            rpi_gpio = RpiGpio(bit_config["pin"], bit_config["default_pin_state"])
            self.bit_drivers[bit_config["name"]] = rpi_gpio
        if bit_config["type"].lower() == "dummy":
            dummy = Dummy()
            self.bit_drivers[str(bit_config["name"]).lower()] = dummy
        
    def _create_socket(self, socket_config):
        if socket_config["type"].lower() == "mercury":
            socket = Mercury(self.bit_drivers[socket_config["bit_driver"]], int(socket_config["socket_id"]))
            #unicode decode the name, since nobody expects string names to be unicode
        if socket_config["type"].lower() == "energenie_pimote":
            socket = RpiEnergenieRemote(int(socket_config["socket_id"]))

        self.bound_config["sockets"][str(socket_config["name"]).lower()] = socket
             
