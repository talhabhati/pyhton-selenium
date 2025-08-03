import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.get('https://www.wikipedia.org/')
driver.maximize_window()
driver.implicitly_wait(5)
#yeh driver ko action k liye ready kiya ha
act=ActionChains(driver)
#yeh wo elelment bnaya ha jis per action karwana ha
dou=driver.find_element(By.XPATH,'//*[@id="js-link-box-fa"]/strong/bdi')
time.sleep(2)
#yeh action ha double click ka
act.double_click(dou).perform()
time.sleep(3)
driver.quit()