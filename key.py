from pynput.keyboard import Key, Listener, KeyCode

count = 0

def on_press(key):
    global count
    
    if key == KeyCode(char="a"):
        print("hey")
    
    if key == KeyCode(char="d"):
        print("p")

def on_release(key):
    if key == Key.esc:
        return False

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()