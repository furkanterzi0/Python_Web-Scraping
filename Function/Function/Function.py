def sayHallo():
    print("hello")

sayHallo()
def deneme(*params):
    return params
print(deneme(1,2,3,'r'))

def pr(**a):
    for key,value in a.items():
        print('{} is {}'.format(key,value))

pr(name='furkan',age=36)
