print('########MERCADO DE fRUTAS##############')
print('#######################################')
n=int(0)
listastr=''
print('Digete a sua lista de frutas, presione enter para terminar...')
lista=[]
listastr=''
def strprint(lista):
    listastr=''
    for fruta in lista:
        if fruta == lista[-1]:
            listastr = listastr + 'e ' + fruta
        else:
            listastr = listastr + fruta + ' ,'
    print(f'A/O snhor(a) pediu os seguintes itens:\n{listastr}')
while True:
    n+=1
    Fruta = input(f' A {n} fruta: ')
    lista.append(Fruta)
    if Fruta == '':
        del lista[-1]
        break
strprint(lista)

