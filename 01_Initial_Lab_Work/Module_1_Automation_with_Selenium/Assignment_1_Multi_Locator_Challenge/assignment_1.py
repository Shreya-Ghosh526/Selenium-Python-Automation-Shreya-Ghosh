from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

try:

    driver.get("https://www.saucedemo.com/")

    driver.maximize_window()

    time.sleep(2)

    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    print("Username entered using By.ID")
    time.sleep(2)
    password = driver.find_element(By.NAME, "password")
    password.send_keys("secret_sauce")

    print("Password entered using By.NAME")
    time.sleep(2)
    login_button = driver.find_element(
        By.XPATH, "//input[@type='submit' and @value='Login']"
    )

    print("Login button located using By.XPATH")
    time.sleep(2)

    login_button.click()

    print("Login button clicked")
    time.sleep(3)
    assert "/inventory.html" in driver.current_url

    print("Login successful!")
    print("Current URL:", driver.current_url)
    print("Assignment 1 completed successfully.")

    time.sleep(3)

finally:
    driver.quit()