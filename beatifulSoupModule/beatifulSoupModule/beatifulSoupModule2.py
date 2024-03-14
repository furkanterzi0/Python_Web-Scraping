html_doc="""
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>This is a Heading</h1>
<div class="1"> 
<p>asdadsa</p
</div>
<p>This is a paragraph.</p>

</body>
</html>
"""
from bs4 import BeautifulSoup



soup=BeautifulSoup(htnl_doc,'html.parser')

result=soup.prettify()
print(result)
