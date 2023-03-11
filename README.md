# Creating a 9 key programmable Macropad using a Pi Pico + CircuitPython. 

## Description: 

This code imports several modules and libraries, including time, usb_hid, Keycode from adafruit_hid, Keyboard from adafruit_hid, board, and digitalio.

The GPIO pins that the buttons are connected to on the Pico are specified using the board module, and each button is set up as a digital input with a pulldown resistor using the digitalio module.

The Keyboard class is initialized with the usb_hid.devices parameter, which allows the Pico to send keyboard commands to the connected computer.

The program runs in an infinite while loop that continuously checks the state of each button. When a button is pressed, the corresponding keyboard command is sent to the computer using the keyboard.send() method, and then the program waits for a short period of time using time.sleep() before checking for button presses again.

The specific keyboard commands sent for each button press are specified in the if statements within the while loop. The commands include pressing combinations of modifier keys (Keycode.CONTROL, Keycode.ALT) and specific keys (Keycode.B, Keycode.F2, etc.), as well as sending multiple commands in sequence with a short delay in between.

## Application:

Reference \lib\adafruit_hid\keycode.py for keycode call mappings. 

Testing a executable application that can manage the Macropad key combinations. 

Current limitations:
Path to the CircuitPython device is hard coded as device drive letter. 
Updating key combos is text input that is separated by commas, not the actual keystroke. 
Multi line key combinatiions for a single button are not supported. 

v.3 Application is able to update the code.py file and refresh with the applied change. 

![Wiring Diagram](/Photos/Macro_Program.jpg)

## Pictures: 

Wiring Diagram
![Wiring Diagram](/Photos/wiring.jpg)

Revision 1 finished project
![Rev1](/Photos/pic1.jpg)

Internal view
![Internals1](/Photos/pic2.jpg)

Backplane 
![Internals2](/Photos/pic3.jpg)

