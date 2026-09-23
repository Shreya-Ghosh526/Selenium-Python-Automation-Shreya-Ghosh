from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class LoginPage:

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_page_title(self):
        return self.driver.find_element(*self.PRODUCTS_TITLE).text


@given("I open the SauceDemo login page")
def open_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.login_page = LoginPage(context.driver)
    context.login_page.open()
    time.sleep(2)


@when('I login using username "{username}" and password "{password}"')
def login_with_credentials(context, username, password):
    context.login_page.login(username, password)
    time.sleep(2)


@then("I should see the Products page")
def verify_products_page(context):
    assert context.login_page.get_page_title() == "Products"
    context.driver.quit()