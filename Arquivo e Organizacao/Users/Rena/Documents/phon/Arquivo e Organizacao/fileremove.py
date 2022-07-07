#!C:\Users\Rena\AppData\Local\Programs\Python\Python38\python.exe
import os

path=os.getcwd()
content=os.listdir(path)
for file in content:
    if file == "fileremove.py" or file == "Proj_arquivoAleatorio.py":
        continue
    else:
        os.remove(path+"\\"+file)
"""==____________________________________________________________________________________________________=="""
arquivo = open("Banco de dados.txt", "a")
arquivo.close()
with open("Banco de dados.txt", "a") as arquivo:
    print(arquivo.write("oy tudo bem"))
with open("Banco de dados.txt", "r") as arquivo:
    print(arquivo.readline())
