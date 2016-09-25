from setuptools import setup
setup(name='ism_io',
      version="0.1",
      description="A python module to control 433 mhz sockets via rest or WEMO protocols",
      url="https://github.com/benfollis/ism_io",
      author="Ben Follis",
      license="GPLv3",
      packages=['ism_io', 'ism_io.config', 'ism_io.web', 'ism_io.bit_drivers', 'ism_io.socket_drivers'],
      zip_safe=False,
      scripts=['bin/ism_io_rest', 'bin/ism_io_fauxmo_config', 'bin/remote_scan'])
