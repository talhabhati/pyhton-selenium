from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.google.com/intl/en-GB/gmail/about/")
driver.maximize_window()
time.sleep(0)
driver.find_element(By.PARTIAL_LINK_TEXT,'Sign in').click()
my_mail=driver.find_element(By.ID,"identifierId")
my_mail.send_keys("muhammadtalha42577@gmail.com")
time.sleep(2)
ent=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span').click()
#my_pass=driver.find_element(By.ID,"")
time.sleep(2)
driver.find_element(By.NAME,'Passwd').send_keys('33102075Tb')
time.sleep(5)
driver.quit()