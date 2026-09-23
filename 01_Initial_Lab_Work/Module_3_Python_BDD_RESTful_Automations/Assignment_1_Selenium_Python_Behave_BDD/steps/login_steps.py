from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given("I open the SauceDemo website")
def open_website(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.saucedemo.com/")
    time.sleep(2)


@when("I enter valid username and password")
def enter_credentials(context):
    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(1)


@when("I click the login button")
def click_login(context):
    context.driver.find_element(By.ID, "login-button").click()
    time.sleep(2)


@then("I should see the products page")
def verify_products_page(context):
    title = context.driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products"
    context.driver.quit()