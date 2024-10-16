from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.LINK_TEXT, "Shop").click()
productlist = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for product in productlist:
    ProductName = product.find_element(By.XPATH, "div/h4/a").text
    if ProductName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()  # regular expression

driver.find_element(By.XPATH, "//tbody/tr[3]/td[5]").click()
driver.find_element(By.ID, "country").send_keys("Ind")
# Important to understand this concept...
wait = WebDriverWait(driver, 10)
from selenium.webdriver.support import expected_conditions

wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class = 'checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "[type = 'submit']").click()
successText = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success! Thank you!" in successText
driver.close()

# It is a small project to understand the basics of Selenium. Thankyou!
