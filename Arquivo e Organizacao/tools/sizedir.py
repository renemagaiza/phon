#!C:\Users\Rena\AppData\Local\Programs\Python\Python38\python.exe
"""
sizedir.py e um programa que e responsavel pela identificar a pasta e orquivo mais grandes
"""
#portacao de modulos
import os, shutil
#variaveis globais

dirsize = dict()
def maxdirsize (path):
    dirmax = ''
    dirma = 0
    #autenticacao do path
    if not os.path.exists(path):
        print("O directorio informado nao foi encontraddo!!")
        return None
    elif os.path.isfile(path):
        print("Passou um arquivo, e o seu tamanho e:\n")
        os.path.getsize(path)
        return True
    #percorre o directorio e contabiliza os tamanhos dos arquivos
    os.chdir(path)
    for pasta, subpasta, arquivo in os.walk(path):
        dirsize[pasta] = 0
        for arq in arquivo:
            print(arq)
            dirsize[pasta] += os.path.getsize(pasta + "\\" + arq)
            if os.path.getsize(pasta + "\\" + arq) > float(dirma):
                dirma = os.path.getsize(pasta + "\\" + arq)
    for key, value in dirsize.items():
        print(f"O arquivo\033[35m {key}\033[0m tem como tamanho {value/1048576}MB")
    print(f"o arquivo maior foi {dirma/1048576}")
maxdirsize("D:\\Programas")