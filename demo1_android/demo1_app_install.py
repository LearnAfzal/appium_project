from appium import webdriver
import time
from selenium.webdriver.common.by import By
des_cap = {
    "platformName": "android",
    "deviceName": "moto",
    "app": r"C:\Users\153192\OneDrive - Arrow Electronics, Inc\Desktop\Python Training\khan-academy-7-3-2.apk" # we are requesting the server to install this apk
}

driver=webdriver.Remote(command_executor="http://localhost:4723/wd/hub",desired_capabilities=des_cap) # this local host address we are fetching from the Remote class
driver.implicitly_wait(30)
time.sleep(3)
if len(driver.find_elements(By.XPATH,"//android.widget.TextView[@text='Dismiss']"))>0:
    driver.find_element(By.XPATH, "//android.widget.TextView[@text='Dismiss']").click()
driver.find_element(By.XPATH, "//android.widget.TextView[@text='Sign in']").click()
driver.find_element(By.XPATH, "//android.widget.TextView[@text='Sign in']").click()
driver.find_element(By.XPATH, "//android.widget.EditText[@text='Enter an e-mail address or username']").send_keys("afzal")
driver.find_element(By.XPATH, "//android.widget.EditText[@text='Password']").send_keys("afzal@123")
driver.find_element(By.XPATH, "//android.widget.TextView[@text='Sign in'][2]").click()
actual_error=driver.find_element(By.XPATH, "//android.widget.TextView[@text='There was an issue signing in']").text
print(actual_error)
actual_error=driver.find_element(By.XPATH, "//android.widget.TextView[@text='There was an issue signing in']").get_attribute("text")
print(actual_error)
time.sleep(5)

