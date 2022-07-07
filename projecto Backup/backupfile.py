#!C:\Users\Rena\AppData\Local\Programs\Python\Python38\python.exe

import zipfile, os

def backupToZip(folder):
    # Faz backup de todo o conteúdo de "folder" em um arquivo ZIP.
    folder = os.path.abspath(folder) # garante que folder é um path absoluto
    # Determina o nome do arquivo que esse código deverá usar de acordo com
    # os arquivos já existentes
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1
    # TODO: Cria o arquivo ZIP.
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')
    # TODO: Percorre toda a árvore de diretório e compacta os arquivos de cada pasta.
    # Percorre toda a árvore de diretório e compacta os arquivos de cada pasta.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Acrescenta a pasta atual ao arquivo ZIP.
        backupZip.write(foldername, compress_type=zipfile.ZIP_DEFLATED)
        # Acrescenta todos os arquivos dessa pasta ao arquivo ZIP.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue  # não faz backup dos arquivos ZIP de backup anteriores
            backupZip.write(os.path.join(foldername, filename), compress_type=zipfile.ZIP_DEFLATED)
    backupZip.close()
    print('Done.')

backupToZip(r"D:\Biblioteca\mydoc")
