import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
import board
import digitalio
# These are the corresponding GPIOs on the Pi Pico
# that you soldered
btn1_pin = board.GP2
btn2_pin = board.GP3
btn3_pin = board.GP4
btn4_pin = board.GP6
btn5_pin = board.GP7
btn6_pin = board.GP8
btn7_pin = board.GP10
btn8_pin = board.GP11
btn9_pin = board.GP12
btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN
btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN
btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN
btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN
btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN
btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN
btn7 = digitalio.DigitalInOut(btn7_pin)
btn7.direction = digitalio.Direction.INPUT
btn7.pull = digitalio.Pull.DOWN
btn8 = digitalio.DigitalInOut(btn8_pin)
btn8.direction = digitalio.Direction.INPUT
btn8.pull = digitalio.Pull.DOWN
btn9 = digitalio.DigitalInOut(btn9_pin)
btn9.direction = digitalio.Direction.INPUT
btn9.pull = digitalio.Pull.DOWN
keyboard = Keyboard(usb_hid.devices)
# below are the key values that you can change to
# fit your preferences. Change Keycode.ONE for example to
# (Keycode.CONTROL, Keycode.F4) for CTRL + F4
# on the first button.
# See the official CircuitPython docs
# for additional help
while True:
    if btn1.value:
        keyboard.send(Keycode.ONE) #1    
        print('1')
        time.sleep(0.1) 
    if btn2.value:
        keyboard.send(Keycode.TWO) #4
        print('4')
        time.sleep(0.1)
    if btn3.value:  
        keyboard.send(Keycode.THREE) #7 
        print('7')
        time.sleep(0.1)
    if btn4.value:
        keyboard.send(Keycode.FOUR) #2
        print('2')
        time.sleep(0.1)
    if btn5.value:
        keyboard.send(Keycode.FIVE) #5
        print('5')
        time.sleep(0.1)
    if btn6.value:
        keyboard.send(Keycode.SIX) #8
        print('8')
        time.sleep(0.1)
    if btn7.value:
        keyboard.send(Keycode.SEVEN) #3
        print('3')
        time.sleep(0.1)
    if btn8.value:
        keyboard.send(Keycode.EIGHT) #6
        print('6')
        time.sleep(0.1)
    if btn9.value:
        keyboard.send(Keycode.NINE) #9
        print('9')
        time.sleep(0.1)
    time.sleep(0.05)
time.sleep(0.1)
