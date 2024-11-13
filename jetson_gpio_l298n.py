import time
import Jetson.GPIO as GPIO
from pynput.keyboard import Key, Listener, KeyCode

count = 0


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

INA_PIN = 32
# INB_PIN = 33

INA = GPIO.setup(INA_PIN, GPIO.OUT)
# INB = GPIO.setup(33,GPIO.OUT) 

motor = [35,36]
pwm = [GPIO.PWM(INA_PIN,50)]
GPIO.setup(motor[0],GPIO.OUT,initial=GPIO.LOW) 
GPIO.setup(motor[1],GPIO.OUT,initial=GPIO.LOW)

pwm[0].start(0)

def on_press(key):
    global count

    if key == KeyCode(char="a"):
        GPIO.setup(motor[0],GPIO.OUT,initial=GPIO.HIGH) 
        GPIO.setup(motor[1],GPIO.OUT,initial=GPIO.LOW)
        pwm[0].ChangeDutyCycle(100)

    
    if key == KeyCode(char="d"):
        GPIO.setup(motor[0],GPIO.OUT,initial=GPIO.HIGH) 
        GPIO.setup(motor[1],GPIO.OUT,initial=GPIO.HIGH)
        pwm[0].ChangeDutyCycle(-100)
        
    if key == KeyCode(char="s"):
        GPIO.setup(motor[0],GPIO.OUT,initial=GPIO.LOW) 
        GPIO.setup(motor[1],GPIO.OUT,initial=GPIO.HIGH)
        pwm[0].ChangeDutyCycle(50)

    if key == KeyCode(char="w"):
        GPIO.setup(motor[0],GPIO.OUT,initial=GPIO.LOW) 
        GPIO.setup(motor[1],GPIO.OUT,initial=GPIO.LOW)
        pwm[0].ChangeDutyCycle(0)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()