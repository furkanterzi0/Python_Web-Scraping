message = "  hello there. my name is furki"

message = message.upper()#buutun harfler buyuk
message = message.title()#sadece bas harfler buyuk
message = message.capitalize()#bas harf buyuk
message = message.strip()#basta bosuluk varsa bosluklari siler -- icine karkter girersen onlari da siler
                          #lstrip rstrip var sag sol
message =message.split()#kelimelere ayirir massage artik bir dizi olur elemani da kac kelime varsa o

message='--'.join(message)

index =message.find('furki')#bu kelime varsa kacinci oldugunu soyler yoksa -1 degerini dondurur
print(index)

isFound=message.startswith('h')# h ile mi baslio true false
isFound=message.endswith('i')# i ile mi bitiyo true false
print(isFound)

message=message.replace('furki','furkan') #furkiyi furkanla degistir

message=message.center(100,'*')

print(message)
