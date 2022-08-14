#!C:\Users\Rena\AppData\Local\Programs\Python\Python38\python.exe
"""
• Fazer download de páginas com o módulo requests.
• Encontrar o URL da imagem da tirinha em uma página usando o Beautiful
Soup.
• Fazer download e salvar a imagem da tirinha no disco rígido usando
iter_content().
• Encontrar o URL do link Previous Comic (Tirinha anterior) e repetir.
          ****Tirinhas_Download.py****
"""
import sys

import requests
import os
import bs4

total = 0
url = 'http://xkcd.com'  # url inicial
os.chdir(r"C:\Users\Rena\Documents\phon\WebScript")
os.makedirs('xkcd', exist_ok=True)  # armazena as tirinhas em xkcd
while not url.endswith('#'):
    comicUrl = ""
    # Faz download da página.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # Encontra o URL da imagem da tirinha.
    comicElem = soup.select('#comic img')
    if comicElem:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        # Faz o download da imagem.
        print('Downloading image %s...' % comicUrl)
        res = requests.get(comicUrl)
        res.raise_for_status()
        # Salva a imagem em ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    # Obtém o url do botão Prev.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')
    total = os.path.getsize("./xkcd/" + os.path.basename(comicUrl))
print('Done.')
print(total)
