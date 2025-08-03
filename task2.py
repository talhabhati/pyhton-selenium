from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://dev.alnafi.com/")
driver.maximize_window()
time.sleep(2)
le=driver.find_elements(By.TAG_NAME,"option")
print(len(le))     # le ki tadad nikali ha
driver.quit()