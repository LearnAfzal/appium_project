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
            "app": r"C:\Users\153192\OneDrive - Arrow Electronics, Inc\Desktop\Python Training\com.bsl.hyundai_2021-08-09.apk",
        }
        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()

class TestVirtualAndroidDevice(AppiumConfig):
    def test_register(self):
        while len(self.driver.find_elements(AppiumBy.XPATH, "//android.widget.Button[@text='Don’t allow']"))>0:
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Don’t allow']").click()
        #self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Don’t allow']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='SIGN UP!']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Name*']").send_keys("afzal")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Mobile Number*']").send_keys("9876543210")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Email ID*']").send_keys("afzal@gmail.com")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Password*']").send_keys("afzal123")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Confirm Password*']").send_keys("afzal123")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.CheckBox[@resource-id='com.bsl.hyundai:id/checkAcceptTermsCondition']").click()
        # click on Register
        #self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Register']").click()

        



