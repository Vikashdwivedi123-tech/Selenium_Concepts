import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
my_name = 'Vikash'
driver.find_element(By.ID, "name").send_keys(my_name)
driver.find_element(By.ID, "alertbtn").click()

alert = driver.switch_to.alert
alertText = alert.text
print(alertText)

assert my_name in alertText  # Here I am doing validation of my name in the popup text.
alert.accept()  # It will click on Ok button present in popup.
# alert.dismiss() # It will click on cancel button present in popup
time.sleep(5)