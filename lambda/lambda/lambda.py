#lamdba isimsiz fonksiyon genelde 1 kere kullanilcak fonk.lar icin kullanilir

numbers=[1,2,3,4,5,6]

result=list(map(lambda num:num**2,numbers))
print(result)

answer=list(filter(lambda number:number%2==0,numbers)) #filter ve lambda ile cift sayilari cektim
print(answer)