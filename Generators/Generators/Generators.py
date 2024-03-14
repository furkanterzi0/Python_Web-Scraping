'''
def cube():
    result=[]

    for i in range(5):
        result.append(i**3)
    return result

print(cube())
'''
#Yerine
def cube():
    for i in range(5):
      yield i**3 ## bu deger anlik olarak uretilir ve silinir bellekte yer tutmaz 2.kere cagiramassin

#iterator=cube()

for x in cube():
    print(x)


liste=[i**3 for i in range(5)]
print(liste)

#eger bunu yaparsan
generator=(i**3 for i in range(5)) #generator olur

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))