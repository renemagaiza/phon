#! python3
#programacao de um jogo
print('#'*27 + "  Jogo Da Velha  " + "#"*27)
dados={"a":[' ',' ',' '],"b":[' ',' ',' '],"c":[' ',' ',' ']}
#mostra tabuleiro
def tabuleiro(tabe):
    print('#'*70)
    print('                             c= 0   1   2')
    print(f"                             a| {tabe['a'][0]} | {tabe['a'][1]} | {tabe['a'][2]}|")
    print(f"                             b| {tabe['b'][0]} | {tabe['b'][1]} | {tabe['b'][2]}|")
    print(f"                             c| {tabe['c'][0]} | {tabe['c'][1]} | {tabe['c'][2]}|")
    print('Jogador 1: usa X\nJogador 2: usa O')
#logistica
def autenticacao(tabe,jogador):
    for i in tabe.values():
        if i==['X','X','X'] or i==['O','O','O']:
            print(f'O {jogador} ganhou!!!!')
            break
    if tabe["a"][0] and tabe["b"][1] and tabe["c"][2]=="X" or tabe["a"][0] and tabe["b"][1] and tabe["c"][2]=="O":
        print(f'O jogador  {jogador[1]} ganhou!!')
    elif tabe["a"][2] and tabe["b"][1] and tabe["c"][0]=="X" or tabe["a"][2] and tabe["b"][1] and tabe["c"][0]=="O":
        print(f'O jogador{jogador[1]} ganhou!!')
    elif tabe["a"][0] and tabe["b"][0] and tabe["c"][0]=="X" or tabe["a"][0] and tabe["b"][0] and tabe["c"][0]=="O":
        print(f'O jogador {jogador[1]} ganhou!!')
    elif tabe["a"][2] and tabe["b"][2] and tabe["c"][2]=="X" or tabe["a"][2] and tabe["b"][2] and tabe["c"][2]=="O":
        print(f'O jogador {jogador[1]} ganhou!!')
#area de entrada de dados
for i in range(3):
    tabuleiro(dados)
    jog1=input("Jogador 1: Digite a posicao para X: ")
    while dados[jog1[0]][int(jog1[1])]!=" ":
        jog1= input("A posicao esta ocupada, escolha outra: ")
    dados[jog1[0]][int(jog1[1])]="X"
    autenticacao(dados,jog1)
    tabuleiro(dados)
    jog1=''
    jog2= input("Jogador 2: Digite a posicao para O: ")
    while dados[jog2[0]][int(jog2[1])]!=" ":
        jog2= input("A posicao esta ocupada, escolha outra: ")
    dados[jog2[0]][int(jog2[1])]="O"
    autenticacao(dados, jog2)
    tabuleiro(dados)
    jog2=''
#deslocando os dados
for i in range(6):
    pos1=input("mover X da posicao: ")
    while dados[pos1[0]][int(pos1[1])]!="X":
        pos1= input("A posicao escolhida esta ocupada, escolhe ourta: ")
    jog1 = input('para: ')
    dados[pos1[0]][int(pos1[1])]=dados[jog1[0]][int(jog1[1])] = "X"
    dados[pos1[0]][int(pos1[1])]=' '
    tabuleiro(dados)
    autenticacao(dados, jog1)
    jog1 = ''
    pos2 = input("mover O da posicao: ")
    while dados[pos2[0]][int(pos2[1])] != "O":
        pos2=input("A posicao escolhida esta ocupada, escolhe ourta: ")
    jog2= input('para: ')
    dados[pos2[0]][int(pos2[1])] = dados[jog2[0]][int(jog2[1])] = "O"
    dados[pos2[0]][int(pos2[1])]=' '
    tabuleiro(dados)
    autenticacao(dados, jog2)
    jog1 = ''
tabuleiro(dados)

