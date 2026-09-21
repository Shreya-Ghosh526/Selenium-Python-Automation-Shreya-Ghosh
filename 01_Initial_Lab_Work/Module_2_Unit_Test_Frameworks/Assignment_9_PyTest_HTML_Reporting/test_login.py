from selenium.webdriver.common.by import By
import time


def test_valid_login(driver):

    driver.get("https://www.saucedemo.com/")

    time.sleep(2)

    username = driver.find_element(
        By.ID,
        "user-name"
    )

    password = driver.find_element(
        By.NAME,
        "password"
    )

    login_button = driver.find_element(
        By.XPATH,
        "//input[@type='submit' and @value='Login']"
    )

    username.send_keys("standard_user")
    time.sleep(1)

    password.send_keys("secret_sauce")
    time.sleep(1)

    login_button.click()
    time.sleep(3)

    assert "/inventory.html" in driver.current_url

    print("Valid login test passed.")


def test_login_page_title(driver):

    driver.get("https://www.saucedemo.com/")

    time.sleep(3)

    assert "Swag Labs" in driver.title

    print("Login page title test passed.")