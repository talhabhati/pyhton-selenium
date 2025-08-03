from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')
driver.maximize_window()
em=driver.find_element(By.ID,"Email")
em.clear()
time.sleep(1)
em.send_keys("admin@yourstore.com")
pas=driver.find_element(By.ID,'Password')
pas.clear()
time.sleep(1)
pas.send_keys("admin")
#button ka khuch nhi mila tu Xpath dal diya
driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button').click()
time.sleep(4)
#yeh order ma jana k liye click kiya ha
driver.find_element(By.XPATH,'/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[3]/a').click()
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[3]/ul/li[1]/a').click()
time.sleep(3)
#jitna ab is page ma check boxes ha sara x ma store huga phr loop ma aik aik kar k un pe click huga
x=driver.find_elements(By.CLASS_NAME, 'checkboxGroups')
for i in x:
    i.click()
    time.sleep(2)
print("total check boxes are ",len(x))
time.sleep(5)