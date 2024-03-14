from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from getpass import getpass

driver=webdriver.Chrome()


def instagramLogIn(username,passwordd):
    driver.get('https://www.instagram.com/')
    time.sleep(2)
    usernameBox=driver.find_element(By.NAME,"username")
    usernameBox.send_keys(username)
    passwordBox=driver.find_element(By.NAME,"password")
    passwordBox.send_keys(passwordd)

    passwordBox.send_keys(Keys.ENTER)

    #saveBox=driver.find_element(By.CLASS_NAME,"_ac8f")
    #saveBox.send_keys(Keys.ENTER)
    

    time.sleep(100)

    

username=input('usarname: ')
password=getpass('password: ')
instagramLogIn(username,password)

driver.close()
