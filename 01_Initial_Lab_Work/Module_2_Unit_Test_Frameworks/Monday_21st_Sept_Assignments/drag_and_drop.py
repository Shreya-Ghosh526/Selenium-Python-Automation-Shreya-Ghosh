from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

try:
    driver.maximize_window()
    driver.get("https://testautomationpractice.blogspot.com/")
    time.sleep(3)

    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")

    print("Source and target elements located.")
    time.sleep(2)

    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()

    print("Drag and drop performed successfully.")
    time.sleep(5)

finally:
    driver.quit()