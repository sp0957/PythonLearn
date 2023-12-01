# we need to install Requests package Through file --> setting  --> ProjectInterepreter --> +-->Requests
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("https://careercenter.tops-int.com/")
driver.maximize_window()
alllink=driver.find_elements(By.TAG_NAME,"a")
cont=0
time.sleep(5)
for link in alllink:
    url=link.get_attribute('href')
    try:
        time.sleep(3)
        res=requests.head(url)
    except requests.exceptions.RequestException as e:
        continue
    if res.status_code>=400:
        print(url ,"is broken link")
        cont += 1
    else:
        print(url ,"is valid link")
print("totel number of broken link is" ,cont)