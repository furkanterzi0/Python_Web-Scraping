def outer(num1):
    print('outer')
    def inner(num1):
        print('inner')
        return num1+1
    num2= inner(num1)
    print(num1,num2)

outer(10)


def factroial(number):

    if not isinstance(number,int):
        raise TypeError("number must be an integer")
    if not number>=0:
        raise TypeError("number must be zero or positive")

    def inner_factorial(number):
        if number<=1:
            return 1

        return number*inner_factorial(number-1)
    return inner_factorial(number)

print(factroial(5))

def islem(islem_adi):
     def toplam(*args):
        toplam =0
        for i in args:
            toplam+=i
        return toplam
     def carpma(*args):
        carpim = 1
        for i in args:
             carpim*=i
        return carpim
     if islem_adi=="toplama":
         return toplam
     if islem_adi=="carpma":
         return carpma
toplama=islem("toplama")
print(toplama(1,2,3,4))