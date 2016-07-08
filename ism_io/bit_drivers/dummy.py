# A dummy bit driver to assist with testing, and debuging
class Dummy:

    def send_bit(self, bit, symbol_duration):
        print "Told to send bit " + str(bit) + " for duration " + str(symbol_duration)

    def send_sequence(self, sequence, symbol_duration):
        print "Told to send sequence " + sequence + " with symbol duration " + str(symbol_duration)
        
