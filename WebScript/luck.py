#!C:\Users\Rena\AppData\Local\Programs\Python\Python39\python.exe

#Secao de importacao de modulos
import requests, bs4, pyperclip, webbrowser, sys, time

# obtendo a palavras chaves a pesquisar
if len(sys.argv) > 1:
    url = "https://www.google.com/search?q=" + "+".join(sys.argv[1:])
elif pyperclip.paste() != "":
    url = "https://www.google.com/search?q=" + pyperclip.paste()
else:
    print("Por favor informe algo a ser pesquisado no Google e tente novamente!")
    time.sleep(60)
jan = list()

# pesquisando e solicitando a pagina html
try:
    r = requests.get(url)
except:
    print("Falha na coneccao, por favor verifique a sua coneccao e tente novamente.\nObrigado!")
    time.sleep(60)
    sys.exit()

# Passando o resultado do requests para o bs4
html = bs4.BeautifulSoup(r.text, "html.parser")
# extraindo as divs com os links do resultado da pesquisa e passando o reultado para o bs4

divlink = bs4.BeautifulSoup(str(html.find_all("div",{"class":"egMi0 kCrYT"})), "html.parser")
# extraindo as tags <a> das divs

link = divlink.select("a")

# extaindo os atributos href dos links e adicionando na lista jan

for lk in link:
    ancora = str(lk.get("href"))[7:str(lk.get("href")).find("&")]
    jan.append(ancora)

# imprimindo os resultados do parse dos links

print("Resultados da pesquisa:")
for sitelink in jan:
    print(sitelink)

# Abrindo janelas no navegador para cada link
for site in range(min(4,len(jan))):
    webbrowser.open(jan[site])
print("Processo terminado!")
time.sleep(60)
