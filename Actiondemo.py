# import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
driver.maximize_window()
action = ActionChains(driver)  # driver is an argument and action is an object.
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform() # It is used for right click.
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform() # difference in last funcn.It will click on reload
# time.sleep(10)