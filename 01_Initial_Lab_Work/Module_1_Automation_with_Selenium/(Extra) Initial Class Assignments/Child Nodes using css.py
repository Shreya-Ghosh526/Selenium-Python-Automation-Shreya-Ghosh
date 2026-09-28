'''Assignment 4: Child Nodes Using CSS

Question: Identify and locate child/nested web elements using 
CSS child selectors and interact with the required elements.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open the Chrome browser
driver = webdriver.Chrome()

try:
    # Open the practice website
    driver.get("https://testautomationpractice.blogspot.com/")

    # Maximize the browser window
    driver.maximize_window()

    time.sleep(2)

    # Locate the Submit button inside Section 1
    # "div > button" means button is a direct child of the div
    submit_button = driver.find_element(
        By.CSS_SELECTOR,
        "#section1 > button"
    )

    # Click the button
    submit_button.click()

    print("Submit button was located and clicked successfully.")

    time.sleep(5)

finally:
    # Close the browser
    driver.quit()