import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)

# driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("05/30/2023") #mm/dd/yyyy

year=2023
month="June"
date=13
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()#open datepicker

while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if mon==month:
        break;
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()# next Arrow
        # driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click()#previous Arrow
                                                                                         # (you want yo select a 20220)

dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for ele in dates:
    if ele.text==date:
        ele.click()
        break
