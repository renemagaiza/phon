#!C:\Users\Rena\AppData\Local\Programs\Python\Python38\python.exe
import os
from mySO import back, imprimir
# trocando de directorio actual para D:\
os.chdir("D:\\")
palavras = ["ADJECTIVE", "NOUN", "ADVERB", "VERB"]
comandos = ['cd ..','help','dir',"open",'cd']

while True:
    print('Directorio Atual: ' + os.getcwd())
    cmd = str(input(">> "))
    while cmd.split()[0] not in comandos:
        print("O comando nao foi encontrado, introduz um valor valido!")
        cmd = str(input(">> "))
    if cmd == "cd ..":
        back.backer(os.getcwd())

    elif cmd == "dir":
        imprimir.printdir()

    elif len(cmd.split()) > 1 and cmd.split()[0] == 'cd' and cmd.split()[1] != "..":
        while cmd[3:] not in os.listdir():
            print("Nao foi possivel encontrar o directorio " + cmd.split()[1])
            cmd = str(input('>> '))
        os.chdir(os.getcwd() + "\\" + cmd[3:])

    elif len(cmd.split()) == 2 and cmd.split()[0] == "open":
        if os.path.isfile(cmd.split()[1]):
            with open(cmd.split()[1], 'r') as file :
                readfile = file.read()
            for pc in palavras:
                if pc in readfile:
                    sub = input(f"Valor para o {pc}: ")
                    readfile = readfile.replace(pc, sub)
            print(readfile)
        print("Edicao Completa")
