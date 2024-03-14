names=['Ali','Yagmur','Hakan','Deniz']
years=[1998,2000,1998,1987]

names.append('Cenk')
names.insert(0,'Sena')
print(names.index('Deniz'))
names.remove('Deniz')

print('Ali' in names)
print(names[::-1])
names.sort()
print(names)

my_name='Furkan Terzi'.split(' ')#bosluktan ayirarak listeye cevir
print(my_name)

new_list=[]
a=input()
new_list.append(a)
print(new_list)

print(min(years))
print(max(years))