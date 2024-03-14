class Person:
    def __init__(self,fname,lname):
        print("person created")
        self.fname=fname
        self.lname=lname
    def who_am_i(self):
        print(f'merhaba ben {self.fname} {self.lname}')
    
class Student(Person):
    def __init__(self,fname,lname,number):
        super().__init__(fname,lname)
        self.number=number

    #override
    def who_am_i(self):
        print(f'merhaba ben {self.fname} {self.lname} numaram : {self.number}')


class Teacher(Person):
    def __init__(self, fname, lname,branch):
        super().__init__(fname, lname)
        self.branch=branch

    #override
    def who_am_i(self):
        print(f'hello i am {self.fname} {self.lname} . i am a {self.branch} teacher')


p1=Person('feyza','terzi')
p1.who_am_i()

s1=Student('furkan','terzi',2203013065)
s1.who_am_i()

t1=Teacher('erkan','terzi','Math')
t1.who_am_i()