from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    family_checkbox = driver.find_element(
        By.ID,
        "ctl00_mainContent_chk_friendsandfamily"
    )

    family_checkbox.click()

    print(
        "Family and Friends selected:",
        family_checkbox.is_selected()
    )

    assert family_checkbox.is_selected()
    student_checkbox = driver.find_element(
        By.ID,
        "ctl00_mainContent_chk_StudentDiscount"
    )

    student_checkbox.click()

    print(
        "Student selected:",
        student_checkbox.is_selected()
    )

    assert student_checkbox.is_selected()
    country_box = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "autosuggest")
        )
    )

    country_box.send_keys("ind")

    print("Typed 'ind' in Country box.")

    suggestions = wait.until(
        EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, "li.ui-menu-item a")
        )
    )

    print("Number of suggestions:", len(suggestions))

    for suggestion in suggestions:

        print("Suggestion:", suggestion.text)

        if suggestion.text == "India":

            suggestion.click()

            print("India selected successfully.")

            break

    print("\nAssignment 3 completed successfully.")


finally:
    driver.quit()