#!C:\Users\Rena\AppData\Local\Programs\Python\Python38\python.exe
print("#"*100)
print("#" + "\033[33mPesquisa palavras nos arquivos\033[0m".center(107) + "#")
print("#"*100)
import os, re
found = dict()
path = input("Informe o caminho da pasta a ser aberta: ")
os.chdir(path)
for file in os.listdir():
    if os.path.isfile(file) and file.endswith(".txt"):
        print("#" + file.center(98) + "#")
pchave = list(input("A palavra a ser pesquisada: "))
for i in range(0, len(pchave)):
    if pchave[i].isdigit() or pchave[i].isdecimal():
        pchave[i] = "\d"
    elif pchave[i].isalpha():
        continue
    elif pchave[i].isspace():
        pchave[i] = "\s"
    elif pchave[i] in ['#','-','_','=','+','(',')','@','#','%','$',"!"]:
        pchave[i] = pchave[i]
pchave = "".join(pchave)
spchave = re.compile(r"" + pchave)
for file in os.listdir():
    if os.path.isfile(file) and file.endswith(".txt"):
        with open(file, 'r') as readfile:
            content = readfile.read()
        contentfind = spchave.findall(content)
        found[file] = contentfind
print("Resultados encontrados:".center(100,"#"))
for k, v in found.items():
    print(f"No arquivo \'{k}\' - Correspondencias: {v}")
