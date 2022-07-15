import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

s=Service("C:\\Users\\dell\\Downloads\\geckodriver.exe")
driver=webdriver.Firefox(service=s)
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
driver.implicitly_wait(10)
parentwindow=driver.current_window_handle
# print(parentwindow)
driver.find_element(By.XPATH,"//img[@alt='LinkedIn OrangeHRM group']").click()
windowids=driver.window_handles
print(len(windowids))
for ids in windowids:
    print(ids[0])
    driver.switch_to.window(ids)
    print(driver.title)