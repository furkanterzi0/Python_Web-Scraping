
html_doc="""
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>This is a Heading</h1>
<h1>This is assdas Heading</h1>
<div class="1"> 
<p>asdadsa</p
</div>
<p>This is a paragraph.</p>

</body>
</html>
"""
from bs4 import BeautifulSoup


soup=BeautifulSoup(html_doc,'html.parser')

result=soup.prettify()#prettify=guzellestirme
result=soup.title
result=soup.head
result=soup.body

result=soup.title.string
result=soup.h1.string

result=soup.find_all('h1')#liste seklinde
result=soup.find_all('h1')[1]
result=soup.find_all('div')[0]
result=soup.find_all('div')[0].p

result=soup.div.findChildren()


print(result)
