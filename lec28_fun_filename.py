import time as t
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import *      #date and time ka module impotr kiya ha
da=date.today()
# aj ki date ko month name din aur year ma likh aga
dat=da.strftime("%B_%d_%y")
print(dat)
#functoin bnaay ha ju screen shot lega
def file_name_date():
    mypath=os.getcwd() + "//"     #current working directory k sath / lagaiga
    filename=mypath + t.asctime().replace(":","_")+".png"    #pehla folder phr file ka name aur extention de ha
    driver.save_screenshot(filename)

driver = webdriver.Firefox()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
driver.implicitly_wait(10)
my_email = driver.find_element(By.ID,'user-name')
my_pass = driver.find_element(By.ID,'password')
#email aur password wali jaga pe colour aur border badlega
driver.execute_script("arguments[0].setAttribute('style','background: yellow; border:2px solid red;');",my_email)
driver.execute_script("arguments[0].setAttribute('style','background: yellow; border:2px solid red;');",my_pass)
#yeh file_name_date function ko call kiya ha jo screen shot lega
file_name_date()
driver.quit()
