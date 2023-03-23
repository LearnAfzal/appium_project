from appium import webdriver
import time
from selenium.webdriver.common.by import By
des_cap = {
    "platformName": "android",
    "deviceName": "moto",
    "appPackage": "org.khanacademy.android",
    "appActivity": "org.khanacademy.android.ui.library.MainActivity"
}
driver=webdriver.Remote(command_executor="http://localhost:4723/wd/hub",desired_capabilities=des_cap)
driver.implicitly_wait(30)
time.sleep(3)
if len(driver.find_elements(By.XPATH,"//android.widget.TextView[@text='Dismiss']"))>0:
    driver.find_element(By.XPATH, "//android.widget.TextView[@text='Dismiss']").click()
driver.find_element(By.XPATH, "//android.widget.TextView[@text='Sign in']").click()
driver.find_element(By.XPATH, "//android.widget.TextView[@text='Sign in']").click()
driver.quit()