import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)
#in multiple checjbox you want select only particular then try this logic
checkboxes=driver.find_elements(By.XPATH,"//input[@class='form-check-input' and @type='checkbox']")
time.sleep(5)
for checkbox in checkboxes:
     weekname=checkbox.get_attribute("id")
     if weekname =="tuesday":
        checkbox.click()
time.sleep(10)