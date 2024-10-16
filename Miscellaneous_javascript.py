import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
# document.body.scrooHeight it dynamically select the bottom height of the page.
# How to take screenshot using python..
driver.get_screenshot_as_file("screenshot.png")

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument(
    "headless")  # pass the code without opening chrome yow will not see this at front end it will execute at back end.
chrome_option.add_argument("--ignore-certificate-errors")

time.sleep(10)