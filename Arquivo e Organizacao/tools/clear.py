#!C:\Users\Rena\AppData\Local\Programs\Python\Python38\python.exe
"""
clear.py e um modulo que eliminar arquivos ou pastas
"""
# importacao de modulos
import shutil, os, sys
def clear(path):
    if not os.path.exists(path):
        print(path)
        print("A pasta ou o arquivo passado nao existe!!")
        return 0
    # verifica se o path e um arquivo ou nao
    if os.path.isfile(path):
        os.chdir(os.path.dirname(path))
        sorn = str(input("Tem certeza que deseja eliminar o ficheiro \(N\\S\): "))
        if sorn == "n":
            print("Cancelado!!")
            return 0
        elif sorn == "s":
            print("A eliminar o ficheiro...")
            os.unlink(path)
            print("Eliminacao completa.")
    elif not os.path.isfile(path):
        os.chdir(os.path.dirname(path))
        sorn = str(input("Tem certeza que deseja eliminar o ficheiro \(N\\S\): "))
        if sorn == "n":
            print("Cancelado!!")
            return 0
        elif sorn == "s":
            print("A eliminar o ficheiro...")
            try:
                shutil.rmtree(path)
            except Exception as erro:
                print(f"A eliminacao falhou!!!!\n Motivo: {erro.__class__}")
            else:
                print("Eliminacao completa.")