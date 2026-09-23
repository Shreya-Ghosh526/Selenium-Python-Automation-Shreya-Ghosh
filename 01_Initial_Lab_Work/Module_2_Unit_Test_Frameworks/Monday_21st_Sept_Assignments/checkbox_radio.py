from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    time.sleep(3)

    radio2 = driver.find_element(By.XPATH, "//input[@value='radio2']")
    radio2.click()

    print("Radio Button 2 selected.")
    time.sleep(3)

    assert radio2.is_selected()
    print("Radio Button 2 selection verified.")

    checkbox1 = driver.find_element(By.XPATH, "//input[@value='option1']")
    checkbox2 = driver.find_element(By.XPATH, "//input[@value='option2']")

    checkbox1.click()
    print("Checkbox Option 1 selected.")
    time.sleep(2)

    checkbox2.click()
    print("Checkbox Option 2 selected.")
    time.sleep(3)

    assert checkbox1.is_selected()
    assert checkbox2.is_selected()

    print("Checkbox selections verified.")
    print("Checkbox and RadioButton operation completed successfully.")

    time.sleep(5)

finally:
    driver.quit()