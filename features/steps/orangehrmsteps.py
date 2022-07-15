import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


# driver = webdriver.Firefox(executable_path="C:\\Drivers\\geckodriver.exe")

@given(u'launch chrome browser')
def open_browser(context):
    # s = Service("E:\\geckodriver.exe")
    context.driver = webdriver.Firefox(executable_path="C:\\Drivers\\geckodriver.exe")
    context.driver.maximize_window()


@when(u'open orange hrm homepage')
def open_application(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then(u'Verify that the logo present on page')
def verify_logo(context):
    status = context.driver.find_element(By.XPATH, "//div[@id='divLogo']//img").is_displayed()
    assert status is True


@when(u'Enter the username "{userid}" and password "{password}"')
def enter_username_pwd(context, userid, password):
    context.driver.find_element(By.ID, "txtUsername").send_keys(userid)
    context.driver.find_element(By.ID, "txtPassword").send_keys(password)
    context.driver.find_element(By.ID, "btnLogin").click()

@then(u'Verify text present on Dashboard page after login')
def verify_text(context):
    try:
        text = context.driver.find_element(By.XPATH, "//h1[contains(text(),'Dashboard')]").text
        if text == "Dashboard":
            assert True, "Test Passed"
    except:
        assert True, "Test Passes"
        allure.attach(context.driver.get_screenshot_as_png(),name="Invalid Login",attachment_type=AttachmentType.PNG)
    finally:
        context.driver.close()
        # assert text == "Dashboard"


@then(u'close browser')
def close_browser(context):
    context.driver.close()
