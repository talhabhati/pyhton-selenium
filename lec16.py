import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
def is_elements_avail(tag_name):
    try:
        driver.find_element(By.TAG_NAME,"tag_name")
        return True
    except NoSuchElementException:
        return False
print(is_elements_avail('talha123'))
print(is_elements_avail('a'))
