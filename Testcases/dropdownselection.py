import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

s=Service("C:\\Users\\dell\\Downloads\\geckodriver.exe")
driver=webdriver.Firefox(service=s)
driver.get("https://facebook.com")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT,"Create New Account").click()
ele=driver.find_element(By.ID,"month")
Select(ele).select_by_index(3)
time.sleep(2)
Select(ele).select_by_visible_text("Oct")
time.sleep(2)
Select(ele).select_by_value("6")

ddlist=Select(ele).options

print(len(ddlist))
for values in ddlist:
    print(values.text)

eles=driver.find_elements(By.XPATH,"//select[@id='month']/option")
for i in range(len(eles)):
    print(eles[i].text)
    if eles[i].text=="Sep":
        eles[i].click()



