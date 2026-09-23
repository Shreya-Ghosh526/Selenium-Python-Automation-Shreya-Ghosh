import json
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.screenshots import capture_screenshot
from utils.alerts import handle_javascript_alert, handle_added_popup


with open("config/test_data.json", "r") as file:
    data = json.load(file)


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


def test_purchase_product(driver):

    wait = WebDriverWait(driver, 15)

    driver.get(data["url"])

    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(text(),'Signup / Login')]")
        )
    )

    capture_screenshot(driver, "01_home_page")

    driver.find_element(
        By.XPATH,
        "//a[contains(text(),'Signup / Login')]"
    ).click()

    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(),'Login to your account')]")
        )
    )

    driver.find_element(
        By.NAME,
        "email"
    ).send_keys(data["email"])

    driver.find_element(
        By.NAME,
        "password"
    ).send_keys(data["password"])

    driver.find_element(
        By.XPATH,
        "//button[contains(text(),'Login')]"
    ).click()

    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(text(),'Logged in as')]")
        )
    )

    capture_screenshot(driver, "02_logged_in")

    driver.get(data["url"] + "view_cart")

    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "cart_info")
        )
    )

    remove_buttons = driver.find_elements(
        By.CSS_SELECTOR,
        "a.cart_quantity_delete"
    )

    for button in remove_buttons:
        try:
            button.click()
            wait.until(EC.staleness_of(button))
        except Exception:
            pass

    capture_screenshot(driver, "03_cart_cleared")

    driver.find_element(
        By.XPATH,
        "//a[contains(text(),'Products')]"
    ).click()

    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(),'All Products')]")
        )
    )

    capture_screenshot(driver, "04_products_page")

    search_box = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "search_product")
        )
    )

    search_box.send_keys(data["product"])

    driver.find_element(
        By.ID,
        "submit_search"
    ).click()

    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(),'Searched Products')]")
        )
    )

    product = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                f"//div[contains(@class,'productinfo')]"
                f"//p[normalize-space()='{data['product']}']"
            )
        )
    )

    assert product.is_displayed()

    capture_screenshot(driver, "05_product_search")

    product_card = product.find_element(
        By.XPATH,
        "./ancestor::div[contains(@class,'product-image-wrapper')]"
    )

    view_product = product_card.find_element(
        By.XPATH,
        ".//a[contains(text(),'View Product')]"
    )

    driver.execute_script(
        "arguments[0].click();",
        view_product
    )

    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "quantity")
        )
    )

    capture_screenshot(driver, "06_product_details")

    quantity = driver.find_element(
        By.ID,
        "quantity"
    )

    quantity.clear()
    quantity.send_keys(str(data["quantity"]))

    assert quantity.get_attribute("value") == str(data["quantity"])

    add_to_cart = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.cart")
        )
    )

    add_to_cart.click()

    alert_text = handle_javascript_alert(driver)

    if alert_text:
        print("JavaScript Alert:", alert_text)
    else:
        popup_text = handle_added_popup(driver)
        print("HTML Popup:", popup_text)

    capture_screenshot(driver, "07_product_added")

    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "cart_info")
        )
    )

    capture_screenshot(driver, "08_cart")

    cart_product = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                f"//td[contains(@class,'cart_description')]"
                f"//a[normalize-space()='{data['product']}']"
            )
        )
    )

    assert cart_product.is_displayed()

    cart_quantity = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                f"//td[contains(@class,'cart_description')]"
                f"//a[normalize-space()='{data['product']}']"
                f"/ancestor::tr"
                f"//td[contains(@class,'cart_quantity')]//button"
            )
        )
    )

    assert cart_quantity.text == str(data["quantity"])

    capture_screenshot(driver, "09_final_cart")