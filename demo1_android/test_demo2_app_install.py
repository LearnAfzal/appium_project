import time
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True) # making use of pytest to terminate/quit the session properly
    # if particular line fails then server will stuck in the same point & it will not terminate
    def handle_app_launch(self):
        des_cap = {
            "platformName": "android",
            "deviceName": "moto",
            "app": r"C:\Users\153192\OneDrive - Arrow Electronics, Inc\Desktop\Python Training\khan-academy-7-3-2.apk",
            # "udid":"emulator-5557" # when we need to specifically connect with particular device then we can make use of 'udid'
            # By default it will connect with first device
        }

        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()

class TestAndroidDeviceLocal(AppiumConfig):
    def test_invalid_login(self):
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@content-desc='Enter an e-mail address or username']").send_keys("afzal")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[contains(@content-desc,'Pass')]").send_keys("afzal123")
        # click on sign in
        self.driver.find_element(AppiumBy.XPATH, "(//android.widget.TextView[@text='Sign in'])[2]").click()
        # get the text "There was an issue signing in" and print it
        actual_error = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'issue')]").text
        print(actual_error)
        actual_error = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'issue')]").get_attribute("text")
        print(actual_error)

    def test_invalid_sign_up_email_test(self):
        self.driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Dismiss']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Settings']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign up with email']").click()
        self.driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@content-desc='First name']").send_keys("afzal")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@content-desc='Last name']").send_keys("khan")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Birthday']").click()
        self.driver.find_element(AppiumBy.XPATH, "(//android.widget.EditText[@resource-id='android:id/numberpicker_input'])[1]").click()
        self.driver.find_element(AppiumBy.XPATH,"(//android.widget.EditText[@resource-id='android:id/numberpicker_input'])[1]").clear()
        self.driver.find_element(AppiumBy.XPATH,"(//android.widget.EditText[@resource-id='android:id/numberpicker_input'])[1]").send_keys("Aug")
        #select date
        self.driver.find_element(AppiumBy.XPATH,"(//android.widget.EditText[@resource-id='android:id/numberpicker_input'])[2]").click()
        self.driver.find_element(AppiumBy.XPATH,"(//android.widget.EditText[@resource-id='android:id/numberpicker_input'])[2]").clear()
        self.driver.find_element(AppiumBy.XPATH,"(//android.widget.EditText[@resource-id='android:id/numberpicker_input'])[2]").send_keys("20")
        #select year
        self.driver.find_element(AppiumBy.XPATH,"(//android.widget.EditText[@resource-id='android:id/numberpicker_input'])[3]").click()
        self.driver.find_element(AppiumBy.XPATH,"(//android.widget.EditText[@resource-id='android:id/numberpicker_input'])[3]").clear()
        self.driver.find_element(AppiumBy.XPATH,"(//android.widget.EditText[@resource-id='android:id/numberpicker_input'])[3]").send_keys("1995")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='OK']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@content-desc='Email address']").send_keys("afzal@gmail.com")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@content-desc='Password']").send_keys("afzal123")
        #self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='CREATE']").click()