import time
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that

des_cap = {
        "platformName": "android",
        "deviceName": "moto",
        "app": r"C:\Users\153192\OneDrive - Arrow Electronics, Inc\Desktop\Python Training\com.bsl.hyundai_2021-08-09.apk",
    }
driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
driver.implicitly_wait(30)
time.sleep(5)