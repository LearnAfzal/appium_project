import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

des_cap = {
    # Set URL of the application under test
    "app": "bs://444bd0308813ae0dc236f8cd461c02d3afa7901d",
    # Specify device and os_version for testing
    "deviceName": "iPhone XS",
    "platformVersion": "12",
    # Set other BrowserStack capabilities
    "bstack:options": {
        "userName": "afzalkhan_fBk9r8",
        "accessKey": "agpswdnzU4xzGzR8GnnF",
        "projectName": "First Python project",
        "buildName": "browserstack-build-1",
        "sessionName": "BStack first_test"
    }
}

driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", desired_capabilities=des_cap)
driver.implicitly_wait(30)
print(driver.page_source)
time.sleep(5)
driver.quit() #terminate it properly without any fail
