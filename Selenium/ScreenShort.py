import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
# driver.save_screenshot("C:\\Users\\JENIS\\PycharmProjects\\pythonProject\\Selenium\\.dmo.png")
driver.get_screenshot_as_file("C:\\Users\\JENIS\\PycharmProjects\\pythonProject\\Selenium\\.dmo.png")