from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import os


file_path = os.path.join(
    os.path.dirname(__file__),
    "login_test_data.csv"
)

test_data = pd.read_csv(file_path)

print("Test data loaded successfully.")
print("\nNumber of test cases:", len(test_data))

driver = webdriver.Chrome()

try:
    driver.maximize_window()

    for index, row in test_data.iterrows():

        test_case = row["test_case"]
        username = row["username"]
        password = row["password"]
        expected_result = row["expected_result"]
        expected_error = row["expected_error"]

        print("\n----------------------------------------")
        print("Test Case:", test_case)
        print("Username:", username)
        print("Password:", password)
        print("----------------------------------------")

        driver.get("https://www.saucedemo.com/")

        time.sleep(3)

        username_field = driver.find_element(
            By.ID,
            "user-name"
        )

        password_field = driver.find_element(
            By.NAME,
            "password"
        )

        login_button = driver.find_element(
            By.XPATH,
            "//input[@type='submit' and @value='Login']"
        )

        username_field.send_keys(username)

        print("Username entered.")
        time.sleep(2)

        password_field.send_keys(password)

        print("Password entered.")
        time.sleep(2)

        login_button.click()

        print("Login button clicked.")
        time.sleep(3)

        if expected_result == "success":

            assert "/inventory.html" in driver.current_url

            print("Expected result: Successful login")
            print("Actual result: Login successful")
            print("Test case passed.")

        else:

            error_message = driver.find_element(
                By.CSS_SELECTOR,
                "h3[data-test='error']"
            ).text

            print("Expected error:", expected_error)
            print("Actual error:", error_message)

            assert error_message == expected_error

            print("Validation error matched.")
            print("Test case passed.")

        time.sleep(3)

    print("\n========================================")
    print("All data-driven test cases passed.")
    print("Assignment 8 completed successfully.")
    print("========================================")

    time.sleep(5)

finally:
    driver.quit()