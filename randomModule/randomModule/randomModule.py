import random

result = random.random()#default olarak 0.0'dan 1.0'a kadar herhangi bir deger
result= int(random.uniform(10,100))
result=random.randint(1,100)

names=['ali','yagmur','deniz','cenk']
result=names[random.randint(0,len(names)-1)]

result=random.choice(names)

liste=list(range(10))#10 elemanli liste 1,2,3,4,5...
random.shuffle(liste) #liste icindeki elemanlarin yerlerini karistirir

liste2=range(100)
print(random.sample(liste2,3))#liste icinnden rastgle 3 deger cek
print(random.sample(names,2))

print(result)
print(liste)