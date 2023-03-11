import re
import time
from adafruit_hid.keycode import Keycode

while True:
    if btn1.value:
        keyboard.send(Keycode.CONTROL, Keycode.ALT, Keycode.B)
        time.sleep(0.1) 
    if btn2.value:
        keyboard.send(Keycode.CONTROL, Keycode.ALT, Keycode.J)
        time.sleep(0.1)
    if btn3.value:
        keyboard.send(Keycode.F2)
        time.sleep(0.1)
    if btn4.value:
        keyboard.send(Keycode.CONTROL, Keycode.ALT, Keycode.N)
        time.sleep(0.1)
        keyboard.send(Keycode.CONTROL, Keycode.V)
        time.sleep(0.1)
        keyboard.send(Keycode.TAB)
    if btn5.value:
        keyboard.send(Keycode.CONTROL, Keycode.ALT, Keycode.K)
        time.sleep(0.1)
    if btn6.value:
        keyboard.send(Keycode.CONTROL, Keycode.ALT, Keycode.O)
        time.sleep(0.1)
    if btn7.value:
        keyboard.send(Keycode.CONTROL, Keycode.ALT, Keycode.M)
        time.sleep(0.1)
        keyboard.send(Keycode.CONTROL, Keycode.V)
        time.sleep(0.1)
        keyboard.send(Keycode.TAB)
    if btn8.value:
        keyboard.send(Keycode.CONTROL, Keycode.ALT, Keycode.L)
        time.sleep(0.1)
    if btn9.value:
        keyboard.send(Keycode.CONTROL, Keycode.ALT, Keycode.P)
        time.sleep(0.1)