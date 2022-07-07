import os

import pyperclip
t="rene\nmagaiza"
text = pyperclip.paste()
txt=text.split()
print(txt)
# Separa as linhas e acrescenta os asteriscos.
#print(text)
lines = text.split('\n')
print(lines)
#print(text)
for i in range(len(lines)):
    lines[i] = '* ' + lines[i] + "*"# acrescenta um asterisco\n em cada string da
text ='\n'.join(lines)
pyperclip.copy(text)
print(text)
os.chdir("C:\\Users\\Rena\\Documents\\venv" )
print(os.getcwd())
os.system('cd C:\\Users\\Rena\\Documents\\phon\\ex02.py')