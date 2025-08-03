import time
from selenium import webdriver
from selenium.webdriver.common.by import  By
driver=webdriver.Chrome()
driver.get('https://m.rediff.com/')
driver.maximize_window()
driver.implicitly_wait(5)
#yeh frame switching huwi jis dusri site ma jana ha us k frame k id diya ha
driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="moneyiframe"]'))
my_nse = driver.find_element(By.XPATH,'//*[@id="nseindex"]')
print(my_nse.text)

time.sleep(2)
driver.quit()
