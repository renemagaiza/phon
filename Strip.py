#!C:\Users\Rena\AppData\Local\Programs\Python\Python38\python.exe
# programa emitador do metodo strip
import re
def restrip( text,sub="") :
    ######################################################
    if text.isspace() or len(sub)>len(text):
        return "ERROR\n Verifique a sua expressao e tente novamente!"
    def instring(textP,textB):
        textP=textP.upper()
        textB=textB.upper()
        for i in textP:
            vl=i in textB
            if vl=="False":
                return vl
        return vl
    restrip=re.compile(r'\S[a-zA-Z0-9 .,?\=+@$#%&]+\S')
    if sub == "" or sub.isspace():
        if restrip.search(text):
            return restrip.search(text).group()
    else:
        lsub = text[:len(sub)]
        rsub = text[len(text)-len(sub)]
        if not (instring(sub,lsub) and instring(sub,rsub)) :
            return text
        else:
            return restrip

##########################################################
txt = "  ola mundo   "
out = restrip(txt)
print(out+" len=", len(out))
