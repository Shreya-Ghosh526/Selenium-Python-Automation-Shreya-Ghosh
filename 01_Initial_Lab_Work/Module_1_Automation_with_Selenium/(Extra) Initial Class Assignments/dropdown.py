from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

# Find the dropdown
dropdown = Select(driver.find_element(By.ID, "dropdown-class-example"))

# Select an option
dropdown.select_by_visible_text("Option2")

time.sleep(5)

driver.quit()