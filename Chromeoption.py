# with the help of chrome option we can set the behaviour of browser while invoking.
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--start-maximized")
chrome_option.add_argument("headless")
chrome_option.add_argument("--ignore_certificate-errors")
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
