from bs4 import BeautifulSoup
import requests
import datetime

url1='https://www.google.com/finance/quote/USD-TRY?hl=tr'
page=requests.get(url1)

html_page_usd=BeautifulSoup(page.content,"html.parser")

usd=html_page_usd.find("div",class_="YMlKec fxKbKc").getText()
usd=usd.replace(",",".")
usd=float(usd)

url2='https://www.google.com/finance/quote/EUR-TRY?hl=tr'
page2=requests.get(url2)

html_page_eur=BeautifulSoup(page2.content,"html.parser")
eur=html_page_eur.find("div",class_="YMlKec fxKbKc").getText()
eur=eur.replace(",",".")
eur=float(eur)


x=str(datetime.datetime.now())
date=x.split(".")

print(date[0],"itibari ile;\n")
print(f'Anlik dolar kuru: {usd} TL')
print(f'Anlik Euro kuru:  {eur} TL')

while True:
    choose=input("\n\nyapmak istediginiz islem:\n1- USD to TL\n2- TL to USD\n3- EUR to TL\n4- TL to EUR\n")
    if choose=='1':
        amount=input("Donusturmek istediginiz tutari giriniz(USD): ")
        print(amount,"USD =",float(amount)*usd,"TL")
        break
    elif choose=='2':
        amount=input("Donusturmek istediginiz tutari giriniz(TL): ")
        print(amount,"TL =",float(amount)/usd,"USD")
        break
    elif choose=='3':
        amount=input("Donusturmek istediginiz tutari giriniz(EUR: ")
        print(amount,"EUR =",float(amount)*eur,"TL")
        break
    elif choose=='4':
        amount=input("Donusturmek istediginiz tutari giriniz(TL): ")
        print(amount,"TL =",float(amount)/eur,"EUR")
        break
    else:
        print("gecersiz islem")