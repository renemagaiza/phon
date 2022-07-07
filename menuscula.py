#!C:\Users\Rena\AppData\Local\Programs\Python\Python38\python.exe
# O programa recebi um argumento string e passa para
# menusculo e copia para o clipboard
import sys, pyperclip, time
if len(sys.argv)<2:
    print("Passe o texto a ser transformado em letras menusculas\ncomo argumento")
    time.sleep(4)
    sys.exit()
#else:
texto=" ".join(sys.argv[1:])
texto=texto.lower()
pyperclip.copy(texto)
print("O texto foi copiado para a area de transferencia!")
time.sleep(4)


