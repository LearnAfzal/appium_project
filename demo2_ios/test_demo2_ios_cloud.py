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
            "app": "bs://444bd0308813ae0dc236f8cd461c02d3afa7901d",
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

class TestSampleApp(AppiumIosConfig):
    def test_text_box(self):
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='Text']").click()
        #in ios type=tagname & in android class=tagname
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='Text Input']").send_keys("Hello")
        self.driver.find_element(AppiumBy.XPATH,"(//XCUIElementTypeButton[@name='UI Elements'])[1]").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='Alert']").click()
        alert_msg=self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='This is a native alert.']").text
        assert_that(alert_msg).is_equal_to("This is a native alert.")
        self.driver.find_element(AppiumBy.XPATH, "(//XCUIElementTypeOther[@name='Horizontal scroll bar, 1 page'])[2]").click()
        time.sleep(5)
