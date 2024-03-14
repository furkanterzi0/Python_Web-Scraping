with open("newfile.txt","r",encoding='utf_8') as file :
    content=file.read()
    print(content)
    file.seek(0)#konumu en basa gonderdik
    print(file.tell())
    content2=file.read()
    print(content2)
