#!C:\Users\Rena\AppData\Local\Programs\Python\Python38\python.exe
# Programa para gerenciamento da logistica
import os, shelve
# troca o directorio de trabalho atual para o diretorio Projeto_Conta
os.chdir(r"C:\Users\Rena\Documents\phon\Projeto_Conta")
loginfile = open("login.txt", "a")
loginfile.close()
dados=shelve.open('mydata')
dados['mercadoria'] = mercadoria = {}
dados['resultados'] = resultados = list()
def login():
    print('#'*40)
    print('#'+'PRIMAVERA BSS'.center(38)+"#")
    print('#' * 40)
    nomeempresa=str(input("Nome da entidade: "))
    cont = str(input("Contacto: "))
    prov = str(input("Provincia: "))
    pais = str(input("Pais: "))
    li = [nomeempresa, cont, prov, pais]
    for i in li:
        loginfile = open("login.txt", "a")
        loginfile.write(i+"\n")
        loginfile.close()
    loginfile = open("login.txt", "r")
    log = loginfile.read()
    print(log)
    loginfile.close()
    logistica()
def logistica():
    #cabecalho
    loginfile = open("login.txt", "r")
    log = loginfile.read()
    listlog = log.split("\\n")
    loginfile.close()
    print('#' * 79)
    for i in listlog:
        print('\033[32m '.ljust(14)+i+"\033[0m")
    print('#' * 79)
    #print('#' * 79)
    print("#" + "\033[32m 8.Resultados".center(30) + "6.Gastos e perdas".ljust(30) + "F.Fundo de maneio" + "     \033[0m#")
    print("#"+" \033[32m41.Clientes".center(30)+"45.Outros Devedores".ljust(30)+"22.Mercadorias" + "        \033[0m#")
    print("#  NB: Digite exit, para sair!".ljust(78)+"#")
    print('#' * 79)
    #corpo
    # Contas do programa
    while True:
        conta=str(input('conta>> ')).strip()
        while conta not in ['8', '6', 'F', '41', '45', '22', 'exit']:
            print(f"\033[31mA conta {conta} nao existe!\033[0m")
            conta = str(input("Conta>> ")).strip()
        if conta == '22':
            print(dados['mercadoria'])
            data2 = str(input("Data(dia/mes/ano)>>"))
            mmer = int(input("Motante>> "))
            dados['mercadoria'][data2] = mmer
            dados['resultados'].append(mmer*10/100)
        if conta == "exit":
            break
# Verificao do usuario
if os.path.getsize("login.txt") < 2:
   login()
else:
    logistica()
dados.close()
