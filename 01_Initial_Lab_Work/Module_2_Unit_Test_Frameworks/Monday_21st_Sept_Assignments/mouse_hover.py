from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

try:
    driver.maximize_window()
    driver.get("https://testautomationpractice.blogspot.com/")
    time.sleep(3)

    point_me = driver.find_element(
        By.XPATH, "//button[normalize-space()='Point Me']"
    )

    actions = ActionChains(driver)
    actions.move_to_element(point_me).perform()

    print("Mouse moved over the Point Me button.")
    time.sleep(3)

    mobiles = driver.find_element(
        By.XPATH, "//a[normalize-space()='Mobiles']"
    )

    mobiles.click()

    print("Mobiles option clicked successfully.")
    time.sleep(5)

    print("Mouse hover operation completed successfully.")

finally:
    driver.quit()