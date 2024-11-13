import time
from pynput.keyboard import Key, Listener
import serial

ser = serial.Serial(port='/dev/cu.usbmodem13401', baudrate=9600)

count = 0

running = False

shape = (b'\x00\x00\x02', b'\x10\x00\x02', b'\x00\x00\02', b'\x00\x00\x02')

def convertNumToString(data):
    if data < 10:
        return f"0{data}"
    else: 
        return f"{data}"

def on_press(key):
    toTheRight = True
    if key == Key.f1:
        time.sleep(10)
        for i in range(10):
            y = 0
            # if toTheRight: 
            #     y = 13
            #     toTheRight = False
            # else:
            #     toTheRight = True


            print(f"X {i} Y {y}")

            if i == 1:
                ser.write(bytes([i, y, 2]))
                
            else:
                ser.write(bytes([i, y, 3]))
                


            # if i == 2:
            #     ser.write(bytes([i, y, 3]))
            # else:
            # ser.write(bytes([i, y, 4]))
            time.sleep(1)
            # print(generateByteData(i, y))
        # count += 1
        # if count == 4:
        #     count = 0
    if key == Key.f2:
        ser.write(bytes([1, 1, 2]))
    if key == Key.f3:
        ser.write(shape[2])
    if key == Key.f4:
        ser.write(shape[3])
    if key == Key.f5:
        ser.write(b'\x01\x00')
    if key == Key.f6:
        ser.write(bytes([0,0,0]))
    if key == Key.f7:
        ser.write(bytes([0,0,1]))
    # if key == Key.f6:
    #     ser.write(bytes())
        

def on_release(key):
    if key == Key.esc:
        return False

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
    # running = True if (f == 0xff) else False