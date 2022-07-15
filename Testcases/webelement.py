from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s=Service("C:\\Users\\dell\\Downloads\\geckodriver.exe")
driver=webdriver.Firefox(service=s)
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
# driver.find_element_by_name("txtUsername").send_keys("Hello")
# driver.find_element_by_id("txtPassword").send_keys("password")
driver.find_element(By.NAME,"txtUsername").send_keys("Hello")
driver.find_element(By.ID,"txtPassword").send_keys("password")
driver.find_element(By.XPATH,"//input[@id='btnLogin']").click()
driver.close()
