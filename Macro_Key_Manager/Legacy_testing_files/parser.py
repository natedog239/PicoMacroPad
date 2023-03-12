import re

with open('parse_code.py') as f:
    code = f.read()
    for i in range(1, 10):
        button_text = ''
        for line_num, line in enumerate(code.split('\n')):
            if line.strip().startswith(f'if btn{i}.value'):
                print('Found button condition:', line.strip())
                next_line = code.split('\n')[line_num+1]
                key_codes = re.findall(r'Keycode\.[A-Za-z0-9_,]+', next_line)
                print('Key codes:', key_codes)
                button_text = ' + '.join(key_codes).replace('Keycode.', '')
        print(f'Button {i}: {button_text}')
