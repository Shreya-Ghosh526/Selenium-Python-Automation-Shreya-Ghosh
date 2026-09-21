from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get(
        "https://testautomationpractice.blogspot.com/"
        "p/gui-elements-ajax-hidden.html"
    )

    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    load_button = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "loadContent")
        )
    )

    print("Load AJAX Content button found.")

    load_button.click()

    print("Load AJAX Content button clicked.")

   
    wait.until(
        EC.text_to_be_present_in_element(
            (By.ID, "ajaxContent"),
            "AJAX Content Loaded"
        )
    )

    print("Dynamic content is now available.")

    ajax_content = driver.find_element(
        By.ID,
        "ajaxContent"
    )
    print("\nExtracted text:")
    print(ajax_content.text)

finally:
    driver.quit()