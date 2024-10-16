import time
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://www.cricbuzz.com/')
driver.maximize_window()
print(driver.title) # It gives you the title of web page.
print(driver.current_url)