import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import *      #date and time ka module impotr kiya ha
da=date.today()
# aj ki date ko month name din aur year ma likh aga
dat=da.strftime("%B_%d_%Y")
print(dat)
driver = webdriver.Firefox()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
driver.implicitly_wait(10)
my_email = driver.find_element(By.ID,'user-name')
my_pass = driver.find_element(By.ID,'password')
#email aur password wali jaga pe colour aur border badlega
driver.execute_script("arguments[0].setAttribute('style','background: yellow; border:2px solid red;');",my_email)
driver.execute_script("arguments[0].setAttribute('style','background: yellow; border:2px solid red;');",my_pass)
#yeh file ko date ka name de ker store karega
driver.save_screenshot(fr'H:\alnafi all cources\DEV-OPS\python selenium\images\{dat}.png')
driver.quit()
