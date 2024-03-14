class Person:
    addres='no information'
    def __init__(self,name,age):#costructor
        self.name=name
        self.age=age

    def intro(self):
        print('Hello There I am '+self.name)



p1= Person('furkan',19)
p2= Person('feyza',14)
p1.intro()
p2.intro()
print(f'p1: name: {p1.name} year: {p1.age} addres: {p1.addres}')
