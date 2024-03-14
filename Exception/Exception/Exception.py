#error handling -> hata yonetimi

'''
while True:
    try:
        x=int(input('x: '))
        y=int(input('y: '))
        print(x/y)
    except (ZeroDivisionError,ValueError) as e: #except : olursa butun hepsini alir ama hata turunu bulamazsin
        print('yanlis bilgi girildi')
        print(e)
    else: #exceptin elsesi
        print('her sey yolunda')
        break
'''
while True:
    try:
        x=int(input('x: '))
        y=int(input('y: '))
        print(x/y)
    except Exception as ex:
        print('error: ')
        print(ex)
    else: #exceptin elsesi
        print('her sey yolunda')
        break
    finally:#her turlu calisir
        print('try except sonlandi')