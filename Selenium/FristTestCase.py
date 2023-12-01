import time

from  selenium import webdriver
from  selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By

# ser_obj=service("D:\sahil_learn\Automation Testing Python\chromedriver_win32\chromedriver.exe")
#
# driver=webdriver.Chrome(service=ser_obj)
driver=webdriver.Chrome()

driver.get("https://careercenter.tops-int.com/")
driver.find_element(By.ID,"mobile").send_keys("9081812583")
time.sleep(5)
driver.find_element(By.NAME,"user_password").send_keys("9081812583")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@value='Login' and @type='submit']").click()
time.sleep(5)
driver.implicitly_wait(1,7 )
webdriverWait()
print(driver.title)

time.sleep(10)
print(driver.current_url)
time.sleep(10)
print(driver.page_source)
time.sleep(10)
act_title=driver.title
exp_title="TOPS Career Center - Welcome to TOPS Technologies"
if act_title==exp_title:
    print("Test is Pass")
else:
    print("Test is Failed")
time.sleep(10)
driver.close()