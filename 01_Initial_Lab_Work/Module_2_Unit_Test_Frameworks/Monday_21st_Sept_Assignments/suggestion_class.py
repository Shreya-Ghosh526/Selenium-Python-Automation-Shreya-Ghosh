from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.maximize_window()

    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    time.sleep(3)

    country = driver.find_element(By.ID, "autocomplete")

    country.send_keys("Ind")
    print("Typed 'Ind' in the suggestion box.")
    time.sleep(3)

    suggestions = driver.find_elements(
        By.CSS_SELECTOR,
        "li.ui-menu-item"
    )

    print("Suggestions displayed:")

    for suggestion in suggestions:
        print(suggestion.text)

        if suggestion.text == "India":
            suggestion.click()
            print("India selected successfully.")
            break

    time.sleep(5)

    print("Suggestion class operation completed successfully.")

finally:
    driver.quit()