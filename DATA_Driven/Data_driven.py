import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from DATA_Driven import XLUtils

driver=webdriver.Chrome()
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india/fixed-deposit-calculator-SBI-BSB001.html")
# driver.switch_to.alert.dismiss()
driver.maximize_window()
driver.implicitly_wait(10)

file="D://sahil_learn//Automation_Testing_Python//ALL_DATA.xlsx"
rows=XLUtils.getRows(file,"Sheet1")
time.sleep(77)
for r in range(2,rows+1):
    #reading data from excel
    pric=XLUtils.readData(file,"Sheet1",r,1)
    rateofinterest = XLUtils.readData(file, "Sheet1", r, 2)
    per1=XLUtils.readData(file,"Sheet1",r,3)
    per2 = XLUtils.readData(file, "Sheet1", r, 4)
    fer = XLUtils.readData(file, "Sheet1", r, 5)
    exp_mvalue=XLUtils.readData(file,"Sheet1",r,6)
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(pric)
    driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(rateofinterest)
    driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(per1)
    perdrp=Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
    perdrp.select_by_visible_text(per2)
    ferdrp = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
    ferdrp.select_by_visible_text(fer)
    time.sleep(5)
    driver.find_element(By.XPATH,"/html[1]/body[1]/div[6]/div[2]/div[1]/div[5]/div[1]/div[1]/div[3]/form[1]/div[2]/a[1]/img[1]").click()
    #validation
    act_mvalue=driver.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text
    if float(exp_mvalue)==float(act_mvalue):
        print("Test Is Pass")
        XLUtils.writeData(file,"Sheet1",r,8,"Passed")
        XLUtils.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("Test IS failed")
        XLUtils.writeData(file,"Sheet1",r,8,"Failed")
        XLUtils.fillRedColor(file,"Sheet1",r,8)
    driver.find_element(By.XPATH,"//img[@class='PL5']").click()
    time.sleep(4)
