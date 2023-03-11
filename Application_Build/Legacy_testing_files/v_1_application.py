import tkinter as tk
import re

def create_buttons(window):
    with open('code.py') as f:
        code = f.read()

    button_frame = tk.Frame(window)
    button_frame.pack()

    button_positions = {
        '1': (2, 0),
        '2': (2, 1),
        '3': (2, 2),
        '4': (1, 0),
        '5': (1, 1),
        '6': (1, 2),
        '7': (0, 0),
        '8': (0, 1),
        '9': (0, 2)
    }

    buttons = []

    for i in range(1, 10):
        button_text = ''
        for line_num, line in enumerate(code.split('\n')):
            match = re.search(r'#(\d+)$', line.strip())
            if match and match.group(1) == str(i):
                key_codes = re.findall(r'Keycode\.[A-Za-z0-9_,]+', line)
                button_text = '  + '.join(key_codes).replace('Keycode.', '')
                button_text = button_text.replace(', ', '')
                break

        print(f'Button {i}: {button_text}')
        button = tk.Button(button_frame, text=button_text, width=20, height=5)
        buttons.append(button)

    for i, button in enumerate(buttons):
        button.grid(row=button_positions[str(i+1)][0], column=button_positions[str(i+1)][1])

    return button_frame



def main():
    window = tk.Tk()
    window.title("Macro Pad")
    create_buttons(window)
    window.mainloop()

if __name__ == '__main__':
    main()