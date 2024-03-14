import os

print(os.name)
#os.chdir('..')#1ustsinfia
#os.chdir('../..') #2ust sinifa
print(os.getcwd())#hangi klasorde oldugunu ogrenme

#os.makedirs("newdirectory/yeni")
#os.chdir('C:\\') yer secebiliriz yoksa oldugu yere kurar
#os.mkdir("newdirectory")

#listeleme
print(os.listdir())
#print(os.listdir('C:\\'))
for dosya in os.listdir():
    if dosya.endswith('.py'):
        print (dosya)
print('****************************')
print(os.stat("OS_Module.py"))

os.system("notepad.exe") #uygulama acma

result=os.path.dirname(os.path.abspath("OS_Module"))
print(result)