import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

#Static Table
noOfRowss=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
noOfColum=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr[1]/th"))
#read specific row& column data = Master in selenium
data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text
# print(data)
# for r in range(2,noOfRowss+1): #2 min starting with 2th line
#     for c in range(1,noOfColum+1):#1 min starting with 1th line
#         data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data,end='                ')
#     print()

#read only based on condtion
for r in range(2,noOfRowss):
    authName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[2]").text
    if authName=="Mukesh":
        bookname=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]").text
        price=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print(bookname       ,price,         bookname)
    print()
driver.close()