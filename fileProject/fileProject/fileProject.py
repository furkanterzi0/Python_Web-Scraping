name=input('Adiniz: ')
lname=input('Soyadiniz: ')
gradeList=[]
for i in range(0,3):
    grade=int(input(f'{i+1}. not : '))
    gradeList.append(grade)

with open("data.txt","a",encoding='utf-8') as file:
    file.write(f'{name}\n')
    file.write(f'{lname}\n')
    for x in gradeList:
        file.write(f'{str(x)}\n')
    file.close()
sum=0  
for j in gradeList:
    sum+=int(j)
average=sum/3
with open("gradeAverage.txt","a",encoding='utf-8') as file:
    file.write(str(f'{average}\n'))
    file.close()

with open("data.txt","r",encoding='utf-8') as file:
    a=0
    b=1
    liste=file.readlines()
    print(liste[a]+liste[b])