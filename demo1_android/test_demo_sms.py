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
            # "udid":"emulator-5557"
        }
        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()

class TestAndroidDeviceLocal(AppiumConfig):
    def test_list_sms(self):
        time.sleep(5)
        messges = self.driver.execute_script("mobile: listSms", {"max": 1})
        print(messges)
        print(messges["items"])
        print(messges["total"])
        print(messges["items"][0])
        print(messges["items"][0]["body"])

