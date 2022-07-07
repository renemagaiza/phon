#!C:\Users\Rena\AppData\Local\Programs\Python\Python38\python.exe
#sessao de importacao
import sys ,os
import re
import time
#Desenvolvimento
isIP=re.compile(r"\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3}")
if isIP.search(sys.argv[1])==None:
    print(" Nenhum IP encontrado!")
else:
    print(isIP.search(sys.argv[1]).group())
for i in range(9,0,-1):
    print('encerrando em ',i,'s')
    time.sleep(1)
    os.system('cls')
os.system('echo LoadinG....')
time.sleep(3)
#isIP.search(sys.argv[1]).group()
#