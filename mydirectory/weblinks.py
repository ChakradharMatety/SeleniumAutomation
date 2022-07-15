from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://login.yahoo.com/?.src=ym&pspid=159600001&activity=mail-direct&.lang=en-US&.intl=us&.done=https%3A%2F%2Fmail.yahoo.com%2Fd")
driver.maximize_window()
driver.implicitly_wait(10)

linkslist = driver.find_elements(By.XPATH,"//a")
print(len(linkslist))
parentwindow=driver.current_window_handle
for i in len(linkslist):
    linkslist[i].text
    linkslist[2].click()
    windowids=driver.window_handles
    for ids in windowids:
        print(ids)
        driver.switch_to.window(ids)
        print(driver.title)
    windowid=driver.current_window_handle
    driver.switch_to.window(windowid)
    pagetitle=driver.title
    if pagetitle=="Yahoo Sign UP":
        print("switched to yahoo sign up page")
    else:
        print("Not switched to Yahoo sign up page")

driver.switch_to.window(parentwindow)
driver.close()
driver.quit()






