import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("https://www.wikipedia.org/")
driver.maximize_window()
time.sleep(2)
my_select = driver.find_element(By.ID,"searchLanguage")
sel = Select(my_select)
sel.select_by_value('ja')  #japanese language k liye ja value di ha
time.sleep(5)
driver.quit()