print('############ Pesquisa de Contactos ################')
cont={'rene':850349991,"zefa":845488121,'mae':8424422327}
while True:
    cons=input('Digite o nome para a busca:\\ ')
    if cons=='':
        print("Fim da compra!")
        break
    if cons in cont:
        print(f'{cons} :\n {cont[cons]}')

    else:
        print(f"O numero do(a) {cons} nao foi encontrado!")
        lg=input('Deseja cadastrar o numero? N/S:\n\\: ')
        if lg=="s":
            num=input('Digite o numero: ')
            cont[cons]=num
            print('Lista atualizada')
        else:
            continue






















        
