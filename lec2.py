from selenium import webdriver

path=r"H:\alnafi all cources\DEV-OPS\python selenium\driver\geckodriver.exe"
driver = webdriver.Firefox(executable_path=path)
driver.get("https://dev.alnafi.com/")
driver.maximize_window()
driver.quit()

