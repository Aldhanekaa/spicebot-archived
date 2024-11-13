from pynput.keyboard import Key, Listener
import serial

ser = serial.Serial(port='/dev/cu.usbmodem1101')

count = 0

running = False

shape = (b'\x01\x00', b'\x03\x00', b'\x03\x03', b'\x00\x03', b'\x00\x00')

def on_press(key):
    global count
    
    if key == Key.f1:
        print(f'go to {count}')
        ser.write(shape[count])

        count += 1

        if count > len(shape):
            count = 0

def on_release(key):
    if key == Key.esc:
        return False

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
    # f = ser.read(1)
    # running = True if (f == 0xff) else False