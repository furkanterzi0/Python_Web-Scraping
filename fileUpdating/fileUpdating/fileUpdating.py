'''
with open("newfile.txt","r+",encoding='utf-8') as file: #r+ hem okuma hem yazma

    file.write("deneme123\n")


with open("newfile.txt","r+",encoding='utf-8') as file: #r+ hem okuma hem yazma
    print(file.read())
'''

with open("newfile.txt","a",encoding="utf-8") as file:
    file.write("deneme")
    
with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())
