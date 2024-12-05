from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")  # 'mce_0_ifr is the frame id, or you can write the frame name as well. 
driver.find_element(By.ID, "tinymce").clear()  # It clear the all text present at the location.
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate frame")

driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)
