from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://www.selenium.dev/selenium/web/alerts.html")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)
    alert_link = driver.find_elements(
        By.LINK_TEXT,
        "click me"
    )[0]

    alert_link.click()

    alert = wait.until(
        EC.alert_is_present()
    )

    print("Alert message:", alert.text)
    alert.accept()

    print("JavaScript Alert accepted successfully.")

    confirm_link = driver.find_element(
        By.LINK_TEXT,
        "test confirm"
    )

    confirm_link.click()

    confirm = wait.until(
        EC.alert_is_present()
    )

    print("Confirm message:", confirm.text)

    confirm.dismiss()

    print("Confirm box dismissed successfully.")
    prompt_link = driver.find_element(
        By.LINK_TEXT,
        "prompt happen"
    )

    prompt_link.click()

    prompt = wait.until(
        EC.alert_is_present()
    )

    print("Prompt message:", prompt.text)

    prompt.send_keys("Shreya")

    print("Text entered into prompt.")

    prompt.accept()

    print("Prompt submitted successfully.")

    print("\nAssignment 4 completed successfully.")


finally:
    driver.quit()