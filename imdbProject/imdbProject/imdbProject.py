from re import X
import requests
from bs4 import BeautifulSoup
url='https://www.imdb.com/chart/top/'
htmlContent=requests.get(url).content
html=BeautifulSoup(htmlContent,'html.parser')

allNames=html.find("tbody",{"class":"lister-list"}).find_all("tr",limit=25)
count=1
print('TOP RATED MOVIES:\n')
for x in allNames:
    p=x.find("td",{"class": "titleColumn"}).find("a").text
    print(f'{count}. : {p}')
    count+=1



