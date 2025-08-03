from selenium import webdriver

from selenium.webdriver.common.by import By
import time

#Firefox
#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

#Google
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.google.com/intl/en-GB/gmail/about/')
driver.maximize_window()

driver.find_element(By.PARTIAL_LINK_TEXT,'Sign in').click()
driver.find_element(By.ID,'identifierId').send_keys("talhabhati@gmail.com")

#Next button for verifying your email address
driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()

#Password typing
driver.find_element(By.NAME,'Passwd').send_keys('1234@!')

time.sleep(0.3)
#Nest to login
driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
print("Login success")

time.sleep(30)