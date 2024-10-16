from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
# or We can use .classname in CSS_SELECTOR which is "blinkingText"
# driver.find_element(By.CSS_SELECTOR,".blinkingText").click()
WindowsOpened = driver.window_handles
driver.switch_to.window(WindowsOpened[1])
message = driver.find_element(By.CSS_SELECTOR, ".red").text
print(message)
var = message.split("at")[1].strip().split(" ")[0]  # String concept is used here..
# print("The message which I want from the text then I Used split and get it" + " " + var)
driver.close()
driver.switch_to.window(WindowsOpened[0])
driver.find_element(By.ID, "username").send_keys(var)
driver.find_element(By.ID, "password").send_keys(var)
driver.find_element(By.ID, "signInBtn").click()

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)

