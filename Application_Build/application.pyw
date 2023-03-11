import tkinter as tk
import tkinter.simpledialog as sd
import re
import fileinput


def create_buttons(window):
    with open('E:\code.py') as f:
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

        #print(f'Button {i}: {button_text}')
        button = tk.Button(button_frame, text=button_text, width=20, height=5)
        button.config(command=lambda i=i: set_key_combination(i))
        buttons.append(button)

    for i, button in enumerate(buttons):
        button.grid(row=button_positions[str(i+1)][0], column=button_positions[str(i+1)][1])

    return button_frame

def update_key_combination(btn_num, new_key_combo):
    with fileinput.FileInput('E:\code.py', inplace=True) as file:
        for line in file:
            match = re.search(r'#(\d+)$', line.strip())
            if match and match.group(1) == str(btn_num):
                key_codes = ', '.join([f'Keycode.{key}' for key in new_key_combo])
                line = re.sub(r'keyboard\.send\(.*?\)', f'keyboard.send({key_codes})', line)
            print(line, end='')
            
def refresh_buttons():
    for i in range(1, 10):
        button_text = ''
        with open('E:\code.py') as f:
            code = f.read()

        for line_num, line in enumerate(code.split('\n')):
            match = re.search(r'#(\d+)$', line.strip())
            if match and match.group(1) == str(i):
                key_codes = re.findall(r'Keycode\.[A-Za-z0-9_,]+', line)
                button_text = '  + '.join(key_codes).replace('Keycode.', '')
                button_text = button_text.replace(', ', '')
                break

        buttons[i-1].config(text=button_text)

def set_key_combination(btn_num):
    new_key_combo = sd.askstring("Set key combination", f"Enter new key combination for button {btn_num} (separate keys with comma)")
    if new_key_combo:
        new_key_combo = [key.strip() for key in new_key_combo.split(',')]
        update_key_combination(btn_num, new_key_combo)
        refresh_buttons()


def main():
    global buttons
    window = tk.Tk()
    window.title("Macro Pad")
    buttons_frame = create_buttons(window)
    buttons = buttons_frame.winfo_children()
    window.mainloop()


if __name__ == '__main__':
    main()
