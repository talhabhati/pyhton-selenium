import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("https://www.wikipedia.org/")
driver.maximize_window()
time.sleep(2)
#Tag name option se search ki sari optoins find_elements k through sari le variable ma store huwi h
le=driver.find_elements(By.TAG_NAME,"option")
print(len(le))     # le ki tadad nikali ha
for i in le:
    print("language is", i.text, "and it's value is ",i.get_attribute("lang"))
driver.quit()
