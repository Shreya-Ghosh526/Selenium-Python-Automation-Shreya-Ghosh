from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:

    driver.maximize_window()

    driver.get("https://testautomationpractice.blogspot.com/")
    time.sleep(3)

    name = driver.find_element(By.ID, "name")
    name.send_keys("Shreya Ghosh")
    print("Name entered.")
    time.sleep(1)

    email = driver.find_element(By.ID, "email")
    email.send_keys("shreya@example.com")
    print("Email entered.")
    time.sleep(1)

    phone = driver.find_element(By.ID, "phone")
    phone.send_keys("9876543210")
    print("Phone number entered.")
    time.sleep(1)


    address = driver.find_element(By.ID, "textarea")
    address.send_keys("Kolkata, West Bengal")
    print("Address entered.")
    time.sleep(1)

    male = driver.find_element(By.ID, "male")
    male.click()
    print("Male selected.")
    time.sleep(1)
    monday = driver.find_element(By.ID, "monday")
    monday.click()
    print("Monday selected.")
    time.sleep(1)

    print("Form filling completed successfully.")

    time.sleep(5)

finally:
    driver.quit()