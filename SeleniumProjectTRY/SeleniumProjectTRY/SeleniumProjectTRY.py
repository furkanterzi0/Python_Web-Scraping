from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from getpass import getpass
import time



driver=webdriver.Chrome()

url='https://github.com/login'
driver.get(url)
title1=driver.title


emailBox=driver.find_element(By.ID,"login_field")
emailBox.send_keys("terzifurkan34@gmail.com")

passwordBox=driver.find_element(By.ID,"password")
passwordBox.send_keys("852456furkan")
passwordBox.send_keys(Keys.ENTER)
time.sleep(2)
title2=driver.title

if title1==title2:
    print("--login failed--")
else:
    print("--login successful--")

searchBox=driver.find_element(By.CLASS_NAME,"flex-1")
searchBox.send_keys(Keys.ENTER)
time.sleep(3)
searchBox=driver.find_element(By.ID,"query-builder-test")
searchBox.send_keys("sadik turan")
searchBox.send_keys(Keys.ENTER)
time.sleep(3)

content=driver.find_elements(By.CLASS_NAME,"Box-sc-g0xbh4-0 bItZsX")

for x in content:
    print(x.text)
time.sleep(3)
driver.close()





