#!C:\Users\Rena\AppData\Local\Programs\Python\Python38\python.exe
import re
def ispohene(numero):
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    if phoneNumRegex.search(numero):
        mo = phoneNumRegex.search(numero)
        return  mo.group()
    else:
        print('numero nao foi encontrado')
r=ispohene("fsxdghkfj444-777-97  76orrespondência completa, ou seja, 415-555-4242.")
print(r)
agentNamesRegex = re.compile(r'(Agent (\w\w*))')
m=agentNamesRegex.sub(r'Agent\033[31m \2**** \033[0m','Agent Alice told Agent Carol that Agent Eve knew Agent bob was a double agent.')
print(m)