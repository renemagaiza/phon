#! C:\Users\Rena\AppData\Local\Programs\Python\Python38\python.exe
# O programa salva e carrega porcoes de textos no clipboard.
# Descricao do Funcionamento:
# py.exe mcp.pyw save <palavra chave> - Salva clipboard na palavra chave.
# py.exe mcp.pyw <palavra chave> - carrega a palavra chave no clipboard.
# py.exe mcp.pyw list - carrega todas as palavras chaves no clipboard.

import shelve
import sys
import pyperclip
mcpshelfe= shelve.open("mcp")

if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcpshelfe[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcpshelfe.keys())))
    elif sys.argv[1] in mcpshelfe:
        pyperclip.copy(mcpshelfe[sys.argv[1]])
if len(sys.argv) == 3 and sys.argv[1].lower() == 'delete' and sys.argv[2] in mcpshelfe:
    del mcpshelfe[sys.argv[2]]
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'delete':
    mcpshelfe.clear()
mcpshelfe.close()