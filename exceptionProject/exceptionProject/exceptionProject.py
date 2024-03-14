import re

#1
liste = ["1","2","3","5a","10b","abc"]
sayisalOlmayanlar=[]
sayisalOlanlar=[]
for i in range(len(liste)-1):
    try:
        value=int(liste[i])
    except Exception: 
        sayisalOlmayanlar.append(liste[i])
    else:
        sayisalOlanlar.append(liste[i])

print('liste:{0} '.format(liste))
print(f'sayisal olanlar: {sayisalOlanlar}\nsayisal olmayanlar: {sayisalOlmayanlar}')


#2
while True:
    value2=input('sayi: ')
    if value2=='q':
        break
    else:
        try:
            value3=int(value2)
        except ValueError:
            print('gecersiz sayi')
            
        else:
            print('tamam')

#3
def factorial(x):
    x=int(x)
    if x<0:
        raise ValueError('negatif deger')
    result =1
    for i in range(1,x+1):
        result*=i
    return result

for x in [5,10,20,-3,'10a']:
    try:
        y=factorial(x)
    except ValueError as err:
        print(err)
        continue
    print(y)
