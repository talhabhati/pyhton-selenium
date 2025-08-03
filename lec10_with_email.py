from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#For Firefox
driver = webdriver.Firefox()
driver.implicitly_wait(10)
#For Google
#driver = webdriver.Chrome()

driver.get('https://www.google.com/intl/en-GB/gmail/about/')
driver.maximize_window()

driver.find_element(By.PARTIAL_LINK_TEXT,'Sign in').click()
driver.find_element(By.ID,'identifierId').send_keys("talhabhati@gmail.com")

#Next button for verifying your email address
driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
#Password typing
driver.find_element(By.NAME,'Passwd').send_keys('1234!@')

#Next to login
driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
print("Login success")