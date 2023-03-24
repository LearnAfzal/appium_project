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

class TestArts(AppiumConfig):
    def test_himalayas(self):
        if len(self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']")) > 0:
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()
            # id refers to 'resource-id'
        self.driver.find_element(AppiumBy.ID, "org.khanacademy.android:id/tab_bar_button_search").click()
        # ACCESSIBILITY_ID refers to 'content-desc' in android
        # self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Search tab").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Arts and humanities']").click()
        # in native app only the elements which is visible in screen only able to steer -> thats why we require swipe
        time.sleep(5)
        # swipe until //android.widget.TextView[@text='Art of Asia'] presence
        #  self.driver.swipe(902, 1174,924, 794,1)
        # scroll to art of asia and click
        para_dic = {"strategy": AppiumBy.ANDROID_UIAUTOMATOR, "selector": 'UiSelector().text("Art of Asia")'}
        self.driver.execute_script("mobile: scroll", para_dic)
        # above script belongs to mobile commands-> to execute mobile command we required dict
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Art of Asia']").click()
        # scroll to the himalayas and click
        para_dic = {"strategy": AppiumBy.ANDROID_UIAUTOMATOR, "selector": 'UiSelector().textContains("Himala")'}
        self.driver.execute_script("mobile: scroll", para_dic)
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().textContains("Himala")').click()


