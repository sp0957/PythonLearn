from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://parabank.parasoft.com/parabank/index.htm")
driver.maximize_window()
# driver.find_element(By.NAME,"username").send_keys("HELLOOO")

# driver.find_element(By.NAME,"password").send_keys("IJMMSMDSDKN")

# driver.find_element(By.LINK_TEXT,"Forgot login info?").click()
# aa=driver.find_elements(By.TAG_NAME,"a")
# print(len(aa)) #using len() how many link we can find