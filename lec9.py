from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
#yeh website access hugi chrome pe
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(2)   #5 sec ka delay dala ga
#yeh username k variable bnaya ha




driver.quit()