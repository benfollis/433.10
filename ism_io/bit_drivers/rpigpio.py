# Bit driver using the Raspberri Pi GPIO
import time
import sys
import RPi.GPIO as GPIO

# This class represents a bit driver for Rasberry PI gpio pins.
# When instantiated it will set the GPIO pin to the default bit,
# and after every transmission will return the GPIO pin to the default bit
# Two threads with the same GPIO pin are not thread safe
class RpiGpio:
    
    def __init__(self, gpio_pin, default_bit):
        self.gpio_pin = gpio_pin
        self.default_bit = default_bit
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)
        GPIO.output(self.gpio_pin, default_bit)
    
    def send_bit(self, bit, symbol_duration):
        GPIO.output(self.gpio_pin, bit)
        time.sleep(symbol_duration)
        #reset to default
        GPIO.output(self.gpio_pin, self.default_bit)

    def send_sequence(self, sequence, symbol_duration):
        # sequences are usually timing sensitive, so we'll not use
        # function calls and keep it in the for loop
        for i in sequence:
            if i == '1':
                GPIO.output(self.gpio_pin, 1)
            elif i == '0':
                GPIO.output(self.gpio_pin, 0)
            time.sleep(symbol_duration)
            GPIO.output(self.gpio_pin, self.default_bit)
                                                


        
