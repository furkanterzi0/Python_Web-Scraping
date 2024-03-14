from datetime import datetime
from time import strptime
from datetime import timedelta

now=datetime.now()

nowYear=datetime.now().year

nowMonth=datetime.now().month

nowDay=datetime.now().day


simdi=datetime.now()

datetime.ctime(simdi)
datetime.strftime(simdi, '%Y')
datetime.strftime(simdi, '%X')
datetime.strftime(simdi, '%d' )
datetime.strftime(simdi, '%A' )
datetime.strftime(simdi, '%B' )
datetime.strftime(simdi, '%Y %B %A')

tarih='26 April 2023 14:22:32'

result=datetime.strptime(tarih, '%d %B %Y %H:%M:%S')
print(result)

birthday=datetime(2003,9,21)
print(f'my birthday:{birthday}')

a=datetime.timestamp(birthday) # saniye
datetime.fromtimestamp(a) # saniye to datetime



value=datetime.now() - birthday
print(value)

value=value.days
print(value)


simdi=datetime.now()
print(simdi)
result=simdi+timedelta(days=730)#730 gun ekledi
result=simdi-timedelta(days=70)#70 gun silindi
print(result)
#***************************************

print('what is your birthday: ')
x=input()
userBirthday=datetime.strptime(x,'%d %B %Y')
print(userBirthday)

day=datetime.now()-userBirthday
value=int(day.days/365)

if value<18:
    print('yas 18denn kucuk')



