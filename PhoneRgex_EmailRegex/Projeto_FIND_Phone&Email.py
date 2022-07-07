#!C:\Users\Rena\AppData\Local\Programs\Python\Python38\python.exe
import pyperclip, re
print('\033[40m rene')
#Regex para encontrar Numeros de telefone

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # código de área
(\s|-|\.)? # separador
(\d{3}) # primeiros 3 dígitos
(\s|-|\.) # separador
(\d{4}) # últimos 4 dígitos
(\s*(ext|x|ext.)\s*(\d{2,5}))? # extensão
)''', re.VERBOSE)

#Regex para enderecos de E-mail

emailRegex=re.compile(r'''(
[a-zA-Z0-9. - %+-]+ # nome do usuario
@ # simbolo arouba
[a-zA-Z0-9-]+ # nome do dominio
(\. [a-zA-Z]{2,4})
)''',re.VERBOSE)
# Encontra as correspondências no texto do clipboard.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):  # se a list aestar vazia o loop nao sera executado.
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
if not matches:
    print("Number not found!")
for groups in emailRegex.findall(text): # se a list aestar vazia o loop nao sera executado.
    matches.append(groups[0])
if not emailRegex.findall(text):
    print("Email not found!")
# Copia os resultados para o clipboard.
d=31
for i in range(len(matches)):
    d+=i
    if d >37:
        d=30
    matches[i]=f'\033[{d}m'+matches[i]+'\033[0m'
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('\033[32m Copied to clipboard:\033[0m')
    print('\n'.join(matches))
else:
    print('\033[31mNo phone numbers or email addresses found.\033[0m')
nvp=phoneRegex.sub('Number:\033[31m \1 \033[0m',text)
pyperclip.copy(nvp)
print(nvp)
