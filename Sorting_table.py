import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
# click on column header
# collect all veggie names -> BrowserSorted veggielist

# and now veggielist and newsortedlist should be equal
# because when you click on column header browser already sort the veggiename this is the functionality on web page already.
browsersortedveggie = []
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
veggiwebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggiwebElements:
    browsersortedveggie.append(ele.text)

# Sort the browsersorted veggielist => newsortedlist
originalbrowserSortedlist = browsersortedveggie.copy()

browsersortedveggie.sort()
assert browsersortedveggie == originalbrowserSortedlist

time.sleep(5)
