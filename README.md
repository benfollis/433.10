ism_io
======
ism_io (ISM ON/OFF) aims to provide a simple REST interface to 433MHZ radio controlled sockets.
These sockets typically use On/Off Keying, and GPIO OOK boards can be cheaply purchased from a number of sites.
Please note, this is a Python3 package, and will not work under Python 2.x

Installation
------------
No release has been made to Python's package system hence you'll need to clone the source and install it via setup.py as follows
`
git clone https://github.com/benfollis/ism_io.git
cd ism_io
python3 setup.py install
`
The package makes available two binaries, ism_io_rest and ism_io_fauxmo_config which are the rest server, and fauxmo config generator

Configuration
-------------
After installation of the package we need to create a config file. Assuming this is to run as a service it's usually best to place config in /etc so we'll start out by copying the
sample config to an appropriate etc location. Please note, if this is running on a Raspberry PI with the GPIO driver, the service will likely need to run as root in order to access the GPIO pins
`
sudo su
mkdir /etc/ism_io
cp ism_io/sample_config.json /etc/ism_io/config.json
vi /etc/ism_io/config.json
`
At this point you should have a text editor open with the sample sockets config file.
The file itself is in JSON format and is divided into the keys/sections below
* bit_drivers - describes the bit drivers available to the socket drivers
* sockets - describes the sockets available
* rest - the configuration information for the rest server

All bit drivers and sockets require a "name" by which they can be refered to later in the confguration and a "type" which tells ism_io which driver to use.

### bit_drivers
There are currently two bit driver types:
1. dummy - A bit driver used to test socket drivers when either the hardware is not present on the dev machine, or we want to debug the socket driver. It has no confiuration besides it's name
2. rpigpio - A bit driver that uses the Raspberry PI GPIO system. The required configuration parameters are
   * "pin" - the GPIO pin the transmitter is using to signal on / off
   * "default_pin_state" - the default state that the GPIO should be set to after sending a symbol. The rpigpio driver will allways return the pin to this state after settig it to a 1 or 0 during symbol transmission

### socket_drivers
All socket drivers require a bit driver to function (they don't usually send bits themselves), this is specified via setting the "bit_driver" key to the name of the bit driver you want to use.
There is currently one socket driver type:
1. mercury - A socket driver that cantrol the Mercury 350.115 sockets [https://www.amazon.co.uk/dp/B0051NIJA4]. This driver requires a the "socket_id" to be configured for the particular socket under control. The valid socket ids are 1,2,3,4 and 5.

### rest
At present the only configuration for the rest server is the port, as the rest server itself will bind to any available IP. The port may be sepecified by the "port" key under the rest section. Integer is prefered over string.

Configuration as a service
--------------------------
To run the ism_io rest service as a system service, and assuming you're on the Raspberry Ii, do the following
`
sudo su
mkdir /var/ism_io_rest
cp ism_io/extras/ism_io_rest.service /etc/systemd/system/
systemctl enable ism_io_rest.service
systemctl start ism_io_rest.service
`

Integration with fauxmo
-----------------------
If you want to integrate your switches with Amazon Echo you'll need to suport the wemo protocol. Fortunately, there is an exellent project that already does that, which can be found at
[https://github.com/n8henrie/fauxmo].
In order to make that integration easier the ism_io package provides a utility to read the ism_io config file and produce a valid fauxmo configuration that makes all ism_io sockets available via fauxmo. Assuming you have already configured fauxo as a service, then do the following
`
sudo su
ism_io_fauxmo_config -c /etc/ism_io/config.json > /etc/fauxmo/config.json
systemctl stop fauxmo.service
systemctl start fauxmo.service
`

Adding new socket types
-----------------------
The source is designed to make it as easy as possible to support a new socket manufacturer's protocol, and there
are several good guides on how to determine what they are. The one I used is here
[http://www.instructables.com/id/Super-Simple-Raspberry-Pi-433MHz-Home-Automation/]
The basic idea is that once you have a waveform of the remote's emissions then you need to get your transmitter
to emit the same waveform. Since most of these usually use OOK, that boils down to determining the:
* symbol duration I.E. the smallest unit of time the transmitter is on or off for
* on/off pattern in terms of the sumbol duration
For example, if the symbol duration is one second, (represented by a -)and the on off pattern is 010011100001 then you would expect a waveform something like
`
1  |-|  |---|    |-|
*  | |  |   |    | |
*  | |  |   |    | |
*  | |  |   |    | |
*  | |  |   |    | |
0 _| |__|   |____| |
Time ->
`

To determine the symbol duration, you can either use the techique in the article above, or rig up a 433MHZ GPIO reciever and listen for the shortest time the
GPIO bit is recieving a 1.

Once you've determined the above, make a class under the socket_driver package, and modify config/configbinder to allow your socket to be used. If you can't find a bit driver
for your hardware under bit_drivers, you will need to create one for your hardware and place it under bit_drivers, and again modify configbinder to inform the sytem of how to use it.






