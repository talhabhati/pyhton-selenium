from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
#yeh website access hugi chrome pe
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(2)   #5 sec ka delay dala ga
#yeh username k variable bnaya ha
my_user=driver.find_element(By.ID,"user-name")
my_user.send_keys("standard_user")   #yeh value enter ki ha user k liye
time.sleep(5)
#yeh password k variable set kiya ha
my_pass=driver.find_element(By.ID,"password")
my_pass.send_keys("secret_sauce") # yeh password ki value enter ki ha

#yeh login button k variable bnaya ha
my_login=driver.find_element(By.ID,"login-button")
my_login.click()        #login button pe click karwaya ha
driver.quit()