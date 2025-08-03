from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Firefox()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.ID,"user-name").send_keys("standard_user")
time.sleep(3)
driver.find_element(By.ID,"password").send_keys("secret_sauce")
time.sleep(3)
driver.find_element(By.ID,"login-button").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME,"product_sort_container").send_keys("Price (low to high)")
time.sleep(3)
driver.quit()