import time
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that


class AppiumIosConfig:
    @pytest.fixture(scope="function", autouse=True)
    def launch_app(self):
        des_cap = {
            # Set URL of the application under test
            "app": "bs://5e87b40d6b82aa456649c72090c4ad337837adb9",
            # Specify device and os_version for testing
            "deviceName": "iPhone 11 Pro",
            "platformVersion": "13",
            # Set other BrowserStack capabilities
            "bstack:options": {
                "userName": "afzalkhan_fBk9r8",
                "accessKey": "agpswdnzU4xzGzR8GnnF",
                "projectName": "First Python project",
                "buildName": "browserstack-build-1-ios",
                "sessionName": "BStack first_test-ios"
            }
        }

        self.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()

class TestSauceApp(AppiumIosConfig):
    def test_invalid_login(self):
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='test-Username']").send_keys("John")
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeSecureTextField[@name='test-Password']").send_keys("John123")
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-LOGIN']").click()
        alert_msg = self.driver.find_element(AppiumBy.XPATH,
                                             "//XCUIElementTypeStaticText[contains(@name,'Username and password do not match')]").text
        assert_that(alert_msg).is_equal_to("Username and password do not match any user in this service.")