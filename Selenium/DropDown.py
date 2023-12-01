import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

conty=Select(driver.find_element(By.ID,"country"))
# conty.select_by_index(7)
# #all option in deopdown  how capture
alll=conty.options
print(len(alll))
driver.switch_to.frame()
