
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    # open the browser
    print("Creating driver for chrome browser")
    browser_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield browser_driver
    print("Closing driver for chrome browser")
    browser_driver.quit()