import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

s=Service("C:\\Users\\dell\\Downloads\\geckodriver.exe")
driver=webdriver.Firefox(service=s)
driver.get("https://www.redbus.in")
driver.maximize_window()
driver.implicitly_wait(10)
ele=driver.find_element(By.XPATH,"//span[contains(text(),'SUPERHIT')]")

acc=ActionChains(driver)
acc.move_to_element(ele).perform()

