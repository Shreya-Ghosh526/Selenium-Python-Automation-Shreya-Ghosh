import pytest
from selenium import webdriver
import os


@pytest.fixture
def driver(request):

    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    report = getattr(request.node, "rep_call", None)

    if report and report.failed:

        os.makedirs("screenshots", exist_ok=True)

        screenshot_path = os.path.join(
            "screenshots",
            f"{request.node.name}.png"
        )

        driver.save_screenshot(screenshot_path)

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)