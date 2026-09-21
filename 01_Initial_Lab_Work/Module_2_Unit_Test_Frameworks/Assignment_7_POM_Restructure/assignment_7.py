from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class LoginPage:

    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (
        By.XPATH,
        "//input[@type='submit' and @value='Login']"
    )

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        time.sleep(3)

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        print("Username entered using POM.")
        time.sleep(3)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        print("Password entered using POM.")
        time.sleep(3)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        print("Login button clicked.")
        time.sleep(5)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()


class DashboardPage:

    INVENTORY_CONTAINER = (By.ID, "inventory_container")

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.current_url

    def is_inventory_page_displayed(self):
        time.sleep(3)
        return self.driver.find_element(
            *self.INVENTORY_CONTAINER
        ).is_displayed()


driver = webdriver.Chrome()

try:
    driver.maximize_window()

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    print("Opening SauceDemo login page...")
    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    print("Checking dashboard...")

    assert "/inventory.html" in dashboard_page.get_current_url()

    assert dashboard_page.is_inventory_page_displayed()

    print("Login successful!")
    print("Current URL:", dashboard_page.get_current_url())
    print("Dashboard displayed successfully.")
    print("Assignment 7 completed successfully.")

    time.sleep(5)

finally:
    driver.quit()