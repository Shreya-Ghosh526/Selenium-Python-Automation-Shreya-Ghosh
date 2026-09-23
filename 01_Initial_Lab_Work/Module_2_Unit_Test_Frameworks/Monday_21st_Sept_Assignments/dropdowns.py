from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

try:
    driver.maximize_window()

    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    time.sleep(3)
    dropdown_element = driver.find_element(By.ID, "dropdown-class-example")
    dropdown = Select(dropdown_element)
    dropdown.select_by_visible_text("Option2")

    print("Option 2 selected successfully.")
    time.sleep(3)

    dropdown.select_by_visible_text("Option3")

    print("Option 3 selected successfully.")
    time.sleep(3)

    dropdown.select_by_visible_text("Option1")

    print("Option 1 selected successfully.")
    time.sleep(3)

    print("Dropdown testing completed successfully.")

    time.sleep(5)

finally:
    driver.quit()