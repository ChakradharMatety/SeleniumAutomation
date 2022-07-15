from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
from selenium.webdriver.common.by import By


# driver = webdriver.Chrome(executable_path="C:\\Users\\dell\\Downloads\\chromedriver.exe")
# s=Service("C:\\Users\\dell\\Downloads\\geckodriver.exe")

@allure.severity(allure.severity_level.NORMAL)
class TestHRM:

    @allure.severity(allure.severity_level.MINOR)
    def test_logo(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        status = self.driver.find_element(By.XPATH, "//div[@id='divLogo']//img").is_displayed()
        assert status is True
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        if self.driver.title=="India":
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="login Page", attachment_type=AttachmentType.PNG)
            assert False

        self.driver.close()
        # self.driver.find_element(By.ID, "btnLogin").click()
