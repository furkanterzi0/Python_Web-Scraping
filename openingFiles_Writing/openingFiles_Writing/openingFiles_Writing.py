# Dosya acmak ve olusturmak icin open() fonksiyonu kullanilir.
# Kullanimi: open (dosya_adi, dosya_erisme_modu)
# dosya_erisme_modu => dosyay1 hangi amacla actig1m1z1 belirtir.
# "w" : (Write) yazma modu. Dosyay1 konumda olusturur.icindeki seyi siler son yazdigini yazar
# "a": (Append) ekleme. Dosya konumda yoksa olusturur.icine ekler
# "x" : (Create) olusturma. Dosya zaten varsa hata verir.
# "r": (Read) okuma. varsayilan. dosya konumda yoksa hata verir.
#w
file= open("newfile.txt","w",encoding='utf-8')
file.write("furki")
file.close()

#file2=open("C:/Users/terzi/OneDrive/newfile2.txt","w")

#a
file2= open("newfile2.txt","a",encoding='utf-8')
file2.write("\nfurki")
file2.close()

#x
try:
    file3= open("newfile3.txt","x",encoding='utf-8')
    file3.close()
except Exception as ex:
    print(f'olusturmak istediginiz dosya onceden olusturulmus: {ex} ')
#r
file4= open("newfile2.txt","r",encoding="utf_8")#varsayilan olarak r atanir

#for i in file4:
#    print(i,end="")

print(file4.read())
print('------')

print(file4.read(3))

print(file4.readline())#her seferinde tek line

print(file4.readlines())#her bir satirdaki yaziyi listeye ekler

file4.close()