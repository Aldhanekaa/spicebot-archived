import time
from pynput.keyboard import Key, Listener
import serial

ser = serial.Serial(port='/dev/cu.usbserial-10')

count = 0

running = False

shape = (b'\x00\x00\x02', b'\x10\x00\x02', b'\x00\x00\02', b'\x00\x00\x02')

# ser.write(bytes([2,3]))
ser.write(bytes("dsdfasd", "utf-8"))

def read_byte_array():
    if ser.in_waiting > 0:  # Check if any data is available
        try:
            data = ser.readline().decode('utf-8').rstrip()
            print(data)
        except: 
            pass
        # Read the exact number of bytes expected (in this case, 5 bytes)
        # byte_array = ser.read(5)
        # return byte_array
    return None


while True:
    # pass
    data = read_byte_array()
    # if data:
        # Convert byte array to a list of integers
        # byte_list = list(data)
        # print(f"Received byte array: {byte_list}")
