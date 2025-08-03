import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
driver=webdriver.Chrome()
driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.CLASS_NAME,'signinbtn').click()
alert_handle = Alert(driver)
print(alert_handle.text)

time.sleep(3)
driver.quit()