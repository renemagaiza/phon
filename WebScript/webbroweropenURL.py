#!C:\Users\Rena\AppData\Local\Programs\Python\Python38\python.exe
# webbroweropenURL.py – Inicia um mapa no navegador usando um endereço da
# linha de comando ou do clipboard.

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])
else:
    address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + address)
