import serial

class ArduinoComm: 
    commands = []

    def __init__(self):
        self.ser = serial.Serial(port='/dev/cu.usbmodem101')
        self.commands = []

    def connect(self, port='/dev/cu.usbmodem101'):
        self.ser = serial.Serial(port=port)

    def register_command(self, command):
        self.commands.append(command)
    
    def send_command(self):
        self.ser.write()

    def receive_command(self):
        pass