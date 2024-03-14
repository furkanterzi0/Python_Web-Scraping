
def howManyPrint(value,count):
    for i in range(count):
        print(value)
howManyPrint('furkan',4)

def createList(*params):
    new_list=[]
    new_list.append(params)
    print(new_list)
createList(1,2,3,4,5)

def asalNumberFinder(a,b):
    
    for i in range(a,b):
        count=0
        if i==0:
            continue
        for x in range(2,i):
            if (i%x==0):
                count+=1

        if count==0:
            print(i)
asalNumberFinder(0,50)

def square(num):
    return num ** 2

numbers=[1,2,3,4,5,6,7,8]

result=list(map(square,numbers))# numbersteki her elememani tek tek squre icine atar
print(result)



