from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
driver=webdriver.Chrome()

url='https://github.com/'
driver.get(url)

searchInput=driver.find_element(By.NAME,"q")
time.sleep(2)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(3)
result=driver.find_elements(By.CSS_SELECTOR, 'a.v-align-middle')

for e in result:
    print(e.text)



driver.close()