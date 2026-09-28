'''Assignment 1: Web Element Identification

Identify and locate different web elements on a given webpage using:

1. By.ID
2. By.NAME
3. By.TAG_NAME
4. By.LINK_TEXT
5. By.CLASS_NAME'''



from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Open the Chrome browser
driver = webdriver.Chrome()

try:

    # Open the Test Automation Practice website
    driver.get("https://testautomationpractice.blogspot.com/")

    # Maximize the browser window
    driver.maximize_window()

    # Wait for the webpage to load
    time.sleep(2)


    # =========================================================
    # 1. LOCATE ELEMENT USING ID
    # =========================================================

    # Locate the Name field using its ID attribute
    name = driver.find_element(By.ID, "name")

    # Enter text into the Name field
    name.send_keys("Shreya")

    print("1. Element located using ID")


    # =========================================================
    # 2. LOCATE ELEMENT USING NAME
    # =========================================================

    # Locate the gender radio buttons using their NAME attribute
    gender = driver.find_elements(By.NAME, "gender")

    # Select the Female radio button
    # gender[0] = Male
    # gender[1] = Female
    gender[1].click()

    print("2. Female radio button selected using NAME")


    # =========================================================
    # 3. LOCATE ELEMENT USING TAG NAME
    # =========================================================

    # Locate the first HTML element having the <input> tag
    input_element = driver.find_element(By.TAG_NAME, "input")

    print("3. Element located using TAG_NAME")


    # =========================================================
    # 4. LOCATE ELEMENT USING LINK TEXT
    # =========================================================
    # Locate the Apple link using its visible text
    apple = driver.find_element(By.LINK_TEXT, "Apple")

    print("4. Element located using LINK_TEXT")
    


    # =========================================================
    # 5. LOCATE ELEMENT USING CLASS NAME
    # =========================================================

    # Locate the first element having the class "form-group"
    form_group = driver.find_element(By.CLASS_NAME, "form-group")

    print("5. Element located using CLASS_NAME")


    # Keep the browser open for 4 seconds
    time.sleep(4)


finally:

    # Close the browser
    driver.quit()