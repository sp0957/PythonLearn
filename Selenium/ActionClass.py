import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://jqueryui.com/slider/")
driver.switch_to.frame(0)

act=ActionChains(driver)
#slider
slider=driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
print(slider.location) #{'x': -1, 'y': 4}
act.drag_and_drop_by_offset(slider,344,0).perform()
time.sleep(5)
