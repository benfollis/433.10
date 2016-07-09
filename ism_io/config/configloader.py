# parses the command line args and uses the config binder to produce
# a loaded config. I.E. DRY for the scripts
import os
from optparse import OptionParser
from ism_io.config.configbinder import ConfigBinder
class ConfigLoader:

      def __init__(self):
          #load oour command line flags
            parser = OptionParser()
            parser.add_option("-c", "--config", dest="config", help="Config FILE to load", metavar="FILE")
            (options, args) = parser.parse_args();
            # parse the config file locaiton as relative to here
            config_path = os.path.join(os.getcwd(), options.config)
            config_binder = ConfigBinder(config_path)
            self.config = config_binder.bind()

      def get_config(self):
            return self.config
