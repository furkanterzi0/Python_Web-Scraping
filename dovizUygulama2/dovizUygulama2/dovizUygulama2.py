import requests
from bs4 import BeautifulSoup

eur='https://www.bloomberght.com/doviz/euro'
eurPage=requests.get(eur)
chf='https://www.bloomberght.com/doviz/isvicre-frangi'
chfPage=requests.get(chf)

eurHtml=BeautifulSoup(eurPage.content,"html.parser")
chfHtml=BeautifulSoup(chfPage.content,"html.parser")

eurPrice=eurHtml.find("span",class_="LastPrice upGreen")
eurPrice=float(eurPrice.replace(",","."))
eurChange=eurHtml.find("span",class_="bulk PercentChange").getText()

chfPrice=chfHtml.find("span",class_="LastPrice downRed").getText()
chfPrice=float(chfPrice.replace(",","."))
chfChange=chfHtml.find("span",class_="bulk PercentChange").getText()

eurChange=eurChange.replace('% ','')
eurChange=float(eurChange.replace(',','.'))

chfChange=chfChange.replace('% ','')
chfChange=float(chfChange.replace(',','.'))

date=chfHtml.find("span",class_="date").getText()
print(date+' itibari ile;\n')
if eurChange>0:
    print(f'Mevcut euro kuru: {eurPrice} TL (%{eurChange} oraninda artista)')
else:
    print(f'Mevcut euro kuru: {eurPrice} TL (%{eurChange} oraninda dususte)')
if chfChange>0:
    print(f'Mevcut isvicre frangi: {chfPrice} TL (%{chfChange} oraninda artista)\n')
else:
    print(f'Mevcut isvicre frangi: {chfPrice} TL (%{chfChange} oraninda dususte)\n')

print('yapay zeka yorumu:\n')
if chfChange<eurChange:
    print("""    isvicre frangi son 1 yil grafigine bakildiginda genel olarak artista fakat dalgalanma cok
    dususteyken alabilirsiniz fakat arttiginda hemen satmanizi oneriyorum.
    ayrica euro suan zirvede ve turkiye 2023 secimlerine kadar eurodan uzak durmanizi tavsiye ederim\n""")
else:
    print('euro al')