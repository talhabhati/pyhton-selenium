from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://m.cricbuzz.com/cricket-stats/icc-rankings/men/batting")
driver.maximize_window()
rows=driver.find_elements(By.XPATH,'/html/body/div/main/div[2]/div[1]/div/div/div[2]/div[2]/div[1]')
column=driver.find_elements(By.XPATH,'/html/body/div/main/div[2]/div[1]/div/div/div[2]/div[1]')
print(len(rows))
print(len(column))
time.sleep(3)
driver.quit()