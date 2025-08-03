
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#path= Service(r"H:\alnafi all cources\DEV-OPS\python selenium\driver\chromedriver.exe")
driver= webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com")
driver.maximize_window()
driver.quit()