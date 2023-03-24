import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# this file will have code for arrange only
@pytest.fixture
def driver():
    # open the browser
    print("Creating driver for chrome browser")
    browser_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield browser_driver
    print("Closing driver for chrome browser")
    browser_driver.quit()
