from selenium import webdriver
import time

driver=webdriver.Chrome()
url='https://www.youtube.com/'
driver.get(url)
time.sleep(2)
driver.maximize_window()
driver.save_screenshot("youtube.png")


print(driver.title)

url2='https://www.instagram.com/'
driver.get(url2)
time.sleep(2)

driver.back()
driver.forward()
time.sleep(2)
driver.close()
