furkanHesap={
    'ad':'furkan',
    'hesapNo':2203013065,
    'bakiye':3000,
    'ekBakiye':2000
    }
bakiye=furkanHesap['bakiye']
ekBakiye=furkanHesap['ekBakiye']
print('Hosgeldin {0} \nHesap no: {1}'.format(furkanHesap['ad'],furkanHesap['hesapNo']))
print('Bakiye: {0} \nEk Bakiye: {1}'.format(furkanHesap['bakiye'],furkanHesap['ekBakiye']))
tutar=int(input('cekmek istediginiz tutar: '))

def paraCekme(value):
    global bakiye,ekBakiye
    if bakiye+ekBakiye<value:
        print('bb')
    else:
        if value<=bakiye:
            bakiye-=value
            print(f'kalan bakiye {bakiye}')
        else:
            print('mevcut bakiye yetersiz ek hesaptan cekilsin mi ?')
            secim=int(input('(0) hayir (1) evet'))
            if secim==0:
                print('cikis yapiliyor')
            elif secim==1:
                ekBakiye-=(value-bakiye)
                bakiye=0
                print(f'kalan bakiye {bakiye}\nkalan ek bakiye {ekBakiye} ')
            else:
                print('bb')czbjkhcszhc
paraCekme(tutar)