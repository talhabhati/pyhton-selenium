from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time

# Firefox
driver = webdriver.Firefox()
# Google
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# Declaration of wait variable and
wait = WebDriverWait(driver, 20)  # Declaration

driver.get('https://www.google.com/intl/en-GB/gmail/about/')
driver.maximize_window()

driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign in').click()
driver.find_element(By.ID, 'identifierId').send_keys("talhacybbhati@gmail.com")

# Next button for verifying your email address
driver.find_element(By.XPATH,
'/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()

action = wait.until(expected_conditions.element_to_be_clickable((By.NAME, 'Passwd')))
action.click()
# Password typing
driver.find_element(By.NAME, 'Passwd').send_keys('33102075tb')
# Nest to login
driver.find_element(By.XPATH,
'/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
print("Login success")

time.sleep(10)