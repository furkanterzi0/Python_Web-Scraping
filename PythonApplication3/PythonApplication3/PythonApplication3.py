numbers=[1,10,5,16,4,9,10]
letters=['a','g','s','b','y','a','s']

val=min(numbers)
val=max(numbers)
val=min(letters)
val=max(letters)

numbers.insert(3,78)#3.indexe 78eklendi
numbers.pop(2)
numbers.remove(4)


numbers.sort()#kucukten buyuge
numbers.reverse()#buyukten kuculk

print(numbers.count(10))#numberste kac tane 10 var
print(numbers)
print(val)
