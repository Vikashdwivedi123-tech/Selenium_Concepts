import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# service_obj = Service("C:/Users/Dell/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
# driver = webdriver.Chrome(service = service_obj)
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("ind")
countries = driver.find_elements(By.CSS_SELECTOR,"Li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if(country.text == "India"):
        country.click()
        break
time.sleep(10)
# It is not selecting india but don't know why...
assert driver.get(By.ID,"autosuggest").get_attribute("value") == "India"