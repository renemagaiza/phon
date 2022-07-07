def printdir ():
    import os
    contDir = list(os.listdir())
    cont = 0
    cont1 = 4
    for pasta in contDir:
        cont +=1
        print('\033[35m' + pasta.ljust(25) + '\033[0m', end=" ")
        if cont == cont1:
            cont1 += 4
            print("")
    print(" ")