#jogo de advinha
from random import randint
numsecreto=randint(1,20)
print("Advinhe um numero de 1 a 20")
for i in range(0,6):
    print("Qual e o palpite:")
    while True:
        palpite=int(input())
        if palpite.isnumeric():
            break
        else:
            print("Digite apenas numeros")
    if palpite < numsecreto:
        print("Foi baixo")
    elif palpite > numsecreto:
        print("Foi alto)
    else:
        print(palpite)
        break
if palpite==numsecreto:
    print(" Boa voce acertou")
else:
    print(f"Errou nas 6 tentativas. o numero sorteado foi {numsecreto}")