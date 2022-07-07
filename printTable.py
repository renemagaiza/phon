#!C:\Users\Rena\AppData\Local\Programs\Python\Python38\python.exe
#Funcao do programa: Recebe uma lista de lista e exibe em forma de uma tabela
import os
def table(lista):
    numlista=len(lista)
    for x in range(numlista):
        for y in range(len(lista[x])-1):
            if len(lista[x][y]) > len(lista[x][y+1]):
                pal=len(lista[x][y])
            else:
                pal=len(lista[x][y+1])
        if x == 0:
            pal1=pal
        if pal1<pal:
            pal1=pal
    for i in range(len(lista)):
        print(lista[0][i].ljust(pal1+2),
              lista[1][i].ljust(pal1+2),
              lista[2][i].ljust(pal1+2))
    return ""
tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]
os.chdir("D:\Biblioteca\Informatica\Livros\T.I\Programação\Python")
pal=table(tableData)
print(pal)
print(os.getcwd())
print(os.listdir())
