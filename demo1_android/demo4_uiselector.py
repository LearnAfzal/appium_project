import time
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that


class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "platformName": "android",
            "deviceName": "moto",
            "app": r"C:\Users\153192\OneDrive - Arrow Electronics, Inc\Desktop\Python Training\khan-academy-7-3-2.apk",
        }
        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()

class TestLogin(AppiumConfig):
    def test_invalid_login(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Dismiss")').click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Sign in")').click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Sign in")').click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().description("Enter an e-mail address or username")').send_keys("afzal")
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().descriptionContains("Pass")').send_keys("afzal123")
        # click on sign in
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Sign in").instance(1)').click()
        # we can choose either 'instance' (begins with 0) or 'index' (check in inspector). These are methods which are available under UiSelector class.
        # get the text "There was an issue signing in" and print it
        actual_error = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().textContains("issue")').text
        print(actual_error)
        actual_error = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().textContains("issue")').get_attribute("text")
        print(actual_error)