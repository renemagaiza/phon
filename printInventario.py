#criacao de um programa de inventario
print('#'*70)
print(' '*24 + 'Inventario ')
print('#'*70)
count=0
dadosInve=dict()
while True:
    count+=1
    d=input('Digite ENTER para iniciar, e EXIT para finalizar \\: ')
    if d=='exit':
        print('Inventario Fechado!')
        break
    else:
        d=input(f'Digite o {count}* Bem \\: ')
        n=int(input(f'Digite a quantidade de {d} \\: '))
        dadosInve.setdefault(d,n)
print('#'*70)
print(' Inventario:')
print('#'*12)
count=0
for k,v in dadosInve.items():
    print(f'{v} {k}')
    count+=v
print(f'Total do patrimonio: {count}')