import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get('https://www.wikipedia.org/')
driver.maximize_window()
driver.implicitly_wait(10)

actions = ActionChains(driver)
#is code ma wo point ha jha pe right click karna ha
my_path = driver.find_element(By.XPATH,'//*[@id="js-link-box-es"]/strong')
time.sleep(1)
actions.context_click(my_path).perform()     #yeh right click wala action huwa ha

time.sleep(5)
driver.quit()