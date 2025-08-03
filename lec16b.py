from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
def avail(att,name):
    if len(driver.find_elements(by=att,value=name)) == 0:
            return False
    else:
            return True
print(avail(By.XPATH,"/html/body/div/div/div[2]"))
print(avail(By.TAG_NAME,"a"))
print(avail(By.TAG_NAME,"div"))
print(avail(By.TAG_NAME,"html"))
print(avail(By.TAG_NAME,"script"))
print(avail(By.TAG_NAME,"input"))