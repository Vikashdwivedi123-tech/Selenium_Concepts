import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/client/auth/login")
# driver.find_element(By.LINK_TEXT,"Forgot password").click()
driver.get("https://rahulshettyacademy.com/angularpractice/")

# Static drop-down- Select class is used for select tag for the static dropdown.
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
# dropdown.select_by_visible_text("Male")
dropdown.select_by_index(1)  # 0 index -> Male & 1 index -> Female

time.sleep(8)