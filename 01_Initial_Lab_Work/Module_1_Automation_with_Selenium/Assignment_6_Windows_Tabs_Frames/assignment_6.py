from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get(
        "https://www.selenium.dev/selenium/web/"
        "window_switching_tests/page_with_frame.html"
    )

    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    print("Practice page opened successfully.")

    main_window = driver.current_window_handle

    print("Main window handle stored.")
    iframe = wait.until(
        EC.presence_of_element_located(
            (By.NAME, "myframe")
        )
    )

    driver.switch_to.frame(iframe)

    print("Switched to iframe successfully.")
    iframe_text = driver.find_element(
        By.TAG_NAME,
        "body"
    ).text

    print("Text inside iframe:")
    print(iframe_text)

    driver.switch_to.default_content()

    print("Switched back to main page.")

    open_window = driver.find_element(
        By.LINK_TEXT,
        "Open new window"
    )

    open_window.click()

    print("Open new window link clicked.")

    wait.until(
        EC.number_of_windows_to_be(2)
    )

    print(
        "Number of browser windows:",
        len(driver.window_handles)
    )

    for window in driver.window_handles:

        if window != main_window:

            driver.switch_to.window(window)

            break

    print("Switched to new window successfully.")

    new_window_title = driver.title

    print("New window title:", new_window_title)


    driver.close()

    print("New window closed successfully.")


    driver.switch_to.window(main_window)

    print("Switched back to main window.")

    print("Main window title:", driver.title)

    print("\nAssignment 6 completed successfully.")

finally:
    driver.quit()