#!C:\Users\Rena\AppData\Local\Programs\Python\Python38\python.exe
#Zipcompact.py: e um progrma que faz compactacao de arquivos de extensoes especificas
# modulos a serem usados
"""
zipcompact.zip e um modulo que te permite faze compactacao e descompactacao de ficheiros no geral
Este programa e constituido pelos seguintes metodos oou funcoes: compact(),
"""
import zipfile, os, clear
#funcao extcompact() que faz a compactacao dos arquivos
def compact(path,ext=str()):
    #autenticacao do path
    if not os.path.exists(path):
        print("O PATH nao foi encontrado!")
        return None
    #criando o arquivo zip
    os.chdir(path)
    zipname = os.path.basename(path)
    compactfile = zipfile.ZipFile(zipname + ".zip", "w")
    #percorrendo o directorio adionando arquivos
    for pasta, subpasta, arquivo in os.walk(path):
        for arq in arquivo:
            if arq.endswith(ext):
                print(f"compactando o arquivo {arq} da pasta {pasta}...")
                compactfile.write(pasta + '\\' + arq)
    compactfile.close()
    print("Compactacao concluida ")

#funcao decompact() faz a descompatacao dos arquivos zip
def decompact(path):
    #autenticacao do path
    if not os.path.exists(path):
        print("O PATH nao foi encontrado!")
        return None
    if os.path.isdir(path):
        sorn = input("O caminho passado e um directorio, deseja compactar\? n\\s: ")
        if sorn == "s":
            compact(path)
            return 1
        print("Operacao cancelada!!")
        return 0
    # se for um arquivo e ter extensao zip fara o seguinte
    if os.path.isfile(path) and os.path.basename(path).endswith(".zip"):
        os.chdir(os.path.dirname(path))
        compactfile = zipfile.ZipFile(path)
        compactfile.extractall()
    else:
        print(f"Esse arquivo {os.path.basename(path)} nao tem uma extensao .zip, por tanto nao pode ser descompactado!")

decompact("C:\\Users\\Rena\\Documents\\phon\\Arquivo e Organizacao")
