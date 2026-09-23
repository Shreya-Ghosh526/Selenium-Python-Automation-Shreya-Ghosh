from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
    driver.maximize_window()
    driver.get("https://testautomationpractice.blogspot.com/")
    time.sleep(3)

    name = driver.find_element(By.ID, "name")

    name.send_keys("Shreya")
    print("Name entered.")
    time.sleep(2)

    name.send_keys(Keys.CONTROL, "a")
    print("Text selected using Ctrl+A.")
    time.sleep(2)

    name.send_keys("Shreya Ghosh")
    print("New text entered.")
    time.sleep(2)

    name.send_keys(Keys.TAB)
    print("TAB key pressed.")
    time.sleep(3)

    print("Keyboard actions completed successfully.")

    time.sleep(5)

finally:
    driver.quit()