import requests
from bs4 import BeautifulSoup

url = "https://www.hepsiburada.com/ara?q=laptop"

# Sayfayi cek
response = requests.get(url)

# HTML icerigini ayristir
soup = BeautifulSoup(response.content, "html.parser")

# Laptop isimlerini bul
product_titles = soup.find_all("a", class_="product-title")

# Isimleri ekrana yazdir
for title in product_titles:
    print(title.text.strip())
