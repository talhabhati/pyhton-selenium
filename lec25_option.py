import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
fire_options= Options()
fire_options.add_argument('--headless')
driver = webdriver.Chrome(options=fire_options)
driver.get('https://alnafi.com/')
driver.maximize_window()
driver.implicitly_wait(3)
print(driver.title)

time.sleep(5)
driver.quit()