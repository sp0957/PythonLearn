import time

from  selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.alert import Alert
from selenium.webdriver import *
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")

driver.find_element(By.ID,"benzradio").click();


select=Select(driver.find_element(By.ID,"carselect"))
select.select_by_value("benz")


select=Select(driver.find_element(By.ID,"multiple-select-example"))
select.select_by_value("peach")
select.select_by_visible_text("Apple")


ss=driver.find_element(By.ID,"mousehover")
s1=driver.find_element(By.XPATH,"//a[text()='Reload']")
act=ActionChains(driver)
act.move_to_element(ss).move_to_element(s1).click().perform()


# driver.find_element(By.ID,"confirmbtn").click();
# aa=Alert(driver.switch_to.alert)
# aa.dismiss()
# time.sleep(1000)

