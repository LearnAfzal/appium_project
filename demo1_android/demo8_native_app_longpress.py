import time
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions.android.nativekey import AndroidKey
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

class TestAdvanceCode(AppiumConfig):
    def test_tap_using_coordinates(self):
        if len(self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']")) > 0:
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()
        self.driver.find_element(AppiumBy.ID, "org.khanacademy.android:id/tab_bar_button_search").click()
        action=TouchAction(self.driver)
        action.tap(x=900,y=900,count=5).perform()
        time.sleep(5)

    def test_tap_using_webelements(self):
        if len(self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']")) > 0:
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()
        self.driver.find_element(AppiumBy.ID, "org.khanacademy.android:id/tab_bar_button_search").click()
        action = TouchAction(self.driver)
        action.tap(self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Arts and humanities']"),count=10).perform()
        #first of all it will take the coordinates/location of given locator & tap 10 times using the coordinates
        time.sleep(5)

    def test_long_press_coordinates(self):
        action = TouchAction(self.driver)
        action.long_press(x=330, y=1102,
                          duration=1000).perform()

    def test_long_press_webelements(self):
        time.sleep(2)
        self.driver.press_keycode(AndroidKey.HOME)
        time.sleep(2)
        self.driver.swipe(902, 1174, 902, 794, 1000)
        action = TouchAction(self.driver)
        action.long_press(self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'Khan')]"),
                          duration=1000).perform()
        self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'App in')]").click()

    # logics for press and move to
    def test_press(self):
        action = TouchAction(self.driver)
        action.press(100, 100).wait(1000).move_to(200, 200).release()


    