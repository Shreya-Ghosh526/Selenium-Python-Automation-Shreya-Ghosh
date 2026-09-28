from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

# Click first checkbox - Option1
driver.find_element(By.ID, "checkBoxOption1").click()

time.sleep(5)

driver.quit()