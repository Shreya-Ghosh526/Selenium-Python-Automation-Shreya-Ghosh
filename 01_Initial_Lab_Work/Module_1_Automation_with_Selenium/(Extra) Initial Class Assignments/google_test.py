from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com")

    print("Page Title:", driver.title)

finally:
    driver.quit()