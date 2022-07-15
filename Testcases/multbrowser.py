from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service("C:\\Users\\dell\\Downloads\\geckodriver")
driver=webdriver.Firefox(service=s)
driver.get("http://learn-automation.com")
driver.maximize_window()
# driver.close()

s=Service("E:\\Drivers\\chromedriver")
driver=webdriver.Chrome(service=s)
driver.get("http://learn-automation.com")
driver.maximize_window()