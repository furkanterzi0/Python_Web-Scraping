numbers=[]
names=[]
emails=[]

for i in range(3):
    numbers.append(input(str(i+1)+'.numara: '))
    names.append(input(str(i+1)+'.name: '))
    emails.append(input(str(i+1)+'.email: '))
students={
    numbers[0]:{
        'name':names[0],
        'email':emails[0]
        },
    numbers[1]:{
        'name':names[1],
        'email':emails[2]
        },
    numbers[2]:{
        'name':names[2],
        'email':emails[2]
        },
    
    }
print(students['10'])
