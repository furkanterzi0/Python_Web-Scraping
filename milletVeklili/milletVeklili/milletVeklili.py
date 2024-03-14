mSayisi=int(input("kac milletvekili secilecegini girin: "))
aAlinan=int(input("A Partisi alinan oy sayisi: "))
bAlinan=int(input("B Partisi alinan oy sayisi: "))
cAlinan=int(input("C Partisi alinan oy sayisi: "))
dAlinan=int(input("D Partisi alinan oy sayisi: "))

array=[]
maxArray=[]
for i in range(1,(mSayisi+1)):
    aBolum=aAlinan/i
    bBolum=bAlinan/i
    cBolum=cAlinan/i
    dBolum=dAlinan/i
    array.append(int(aBolum))
    array.append(int(bBolum))
    array.append(int(cBolum))
    array.append(int(dBolum))

aCount=bCount=cCount=dCount=0
for j in range(1,(mSayisi+1)):
    maxArray.append(max(array))
    array.remove(max(array))

for x in maxArray:
    for k in range(1,(mSayisi+1)):
        aKontrol=int(aAlinan/k)
        bKontrol=int(bAlinan/k)
        cKontrol=int(cAlinan/k)
        dKontrol=int(dAlinan/k)
        if aKontrol==x:
            aCount=aCount+1
            break
        if bKontrol==x:
            bCount=bCount+1
            break
        if cKontrol==x:
            cCount=cCount+1
            break
        if dKontrol==x:
            dCount=dCount+1
            break
print("\nA partisinden cikan milletvekili sayisi: "+str(aCount))
print("B partisinden cikan milletvekili sayisi: "+str(bCount))
print("C partisinden cikan milletvekili sayisi: "+str(cCount))
print("D partisinden cikan milletvekili sayisi: "+str(dCount)+"\n")
