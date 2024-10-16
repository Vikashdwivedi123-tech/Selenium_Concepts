import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Webdriver is a class present inside the selenium.
# Selenium doesn't invoke directly the chrome browser. In between this term play an important role.
# Chrome driver service - It invoke the chrome browser firstly it checks the version.
# For every chrome browser version there is chrome driver service for the specific version.
# driver = webdriver.Chrome() # driver is the object of chrome class.
# driver.get('https://www.youtube.com/') # Enter the url which you want to hit by the browser.

# Problem - If selenium is not able to find the driver of a version you are using for the browser then 'Service()' class is the way to solev it.
# It takes the path of a driver as a string.

service_obj = Service("C:/Users/Dell/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get('https://www.youtube.com/')

time.sleep(2)  # It is using to see the behaviour of selenium.