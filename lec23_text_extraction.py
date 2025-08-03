import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://m.rediff.com/')
driver.maximize_window()
driver.implicitly_wait(5)
my_news=driver.find_element(By.ID,'/html/body/div[6]/div[34]/h3')
time.sleep(3)
print(my_news.text)
driver.quit()