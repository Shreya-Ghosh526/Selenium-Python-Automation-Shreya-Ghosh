from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()


    table = driver.find_element(
        By.XPATH,
        "//table[.//th[normalize-space()='BookName']]"
    )

    print("Web table found successfully.")

    headers = table.find_elements(By.TAG_NAME, "th")

    header_names = []

    for header in headers:
        header_names.append(header.text.strip())

    print("\nTable Headers:")
    print(header_names)
    price_index = header_names.index("Price")

    print("Price column index:", price_index)
    rows = table.find_elements(By.TAG_NAME, "tr")

    print("\nTotal rows including header:", len(rows))
    target_book = "Learn Java"
    book_found = False

    for row in rows[1:]:

        cells = row.find_elements(By.TAG_NAME, "td")

        if len(cells) == 0:
            continue
        row_data = []

        for cell in cells:
            row_data.append(cell.text.strip())

        print("Row:", row_data)

        # Match the BookName
        if row_data[0] == target_book:

            book_found = True

            price = row_data[price_index]

            print("\n--------------------------------")
            print("Target Book:", target_book)
            print("Price:", price)
            print("--------------------------------")

            break
    assert book_found, f"{target_book} was not found."

    print("\nAssignment 5 completed successfully.")

finally:
    driver.quit()