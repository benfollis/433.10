import json
from .. import bit_drivers
from .. import socket_drivers

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
            rpi_gpio = bit_drivers.RpiGpio(bit_config["pin"], bit_confg["default_pin_state"])
            self.bit_drivers[bit_config["name"]] = rpi_gpio
        if bit_config["type"].lower() == "dummy":
            dummy = bit_drivers.Dummy()
            self.bit_drivers[str(bit_config["name"]).lower()] = dummy
        
    def _create_socket(self, socket_config):
        if socket_config["type"].lower() == "mercury":
            socket = socket_drivers.Mercury(self.bit_drivers[socket_config["bit_driver"]], int(socket_config["socket_id"]))
            #unicode decode the name, since nobody expects string names to be unicode
            self.bound_config["sockets"][str(socket_config["name"]).lower()] = socket
        
