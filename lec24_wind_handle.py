import time
from selenium import webdriver
from selenium.webdriver.common.by import  By
driver=webdriver.Chrome()
driver.get('https://alnafi.com/')
driver.maximize_window()
driver.implicitly_wait(2)
#us link pe click karwaya ha ju kisi dosre site pe le kar jaiga
driver.find_element(By.XPATH,'//*[@id="footer-section"]/div/div[3]/div[2]/a[2]/svg').click()
#yeh open windows show karega
win=driver.window_handles
print(win)
time.sleep(2)
driver.quit()
