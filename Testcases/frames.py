import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

s=Service("C:\\Users\\dell\\Downloads\\geckodriver.exe")
driver=webdriver.Firefox(service=s)
driver.get("https://www.redbus.in")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//i[contains(@id,'profile')]").click()
driver.find_element(By.ID,"signInLink").click()
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='modalIframe']"))
driver.find_element(By.XPATH,"//span[text()='Sign in with Google']").click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.element_to_be_clickable(By.ID,"signInLink")).click()