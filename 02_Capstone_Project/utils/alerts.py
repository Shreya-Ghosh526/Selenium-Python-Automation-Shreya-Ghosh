from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException


def handle_javascript_alert(driver):
    try:
        alert = driver.switch_to.alert
        message = alert.text
        alert.accept()
        return message
    except NoAlertPresentException:
        return None


def handle_added_popup(driver):
    wait = WebDriverWait(driver, 10)

    popup = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'modal-content')]")
        )
    )

    popup_text = popup.text

    view_cart = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'modal-content')]"
                "//u[contains(text(),'View Cart')]"
            )
        )
    )

    view_cart.click()

    return popup_text