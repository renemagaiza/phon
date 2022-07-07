import os
n = 1
os.chdir(r"D:\Filmes e Series\Series\The Big Bang Theory 10")
for file in os.listdir("."):
    if os.path.isfile(file):
        os.rename(file,"The.Big.Bang.Theory S1_" + str(n) + ".mp4")
        n += 1