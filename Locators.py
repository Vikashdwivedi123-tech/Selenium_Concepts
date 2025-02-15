import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

# These are the different locators that selenium provide -
# Id, Xpath, CSSSelectors, Classname, name, LinkText
# Using these locators we can identify the elements on the web page.
from selenium.webdriver.common.by import By

driver.find_element(By.NAME, "email").send_keys("vikash@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Vikash@123")
driver.find_element(By.ID, "exampleCheck1").click()

# If you want to create Xpath for any element then syntax will be like this
# Xpath-  //tagname[@attribute = 'value'] ->Ex: input[@type='submit']

driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

# CSS-  tagname[attribute = 'value'] or #Id or .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Vikash Dwivedi")

# driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Hellovikash")


time.sleep(5)
