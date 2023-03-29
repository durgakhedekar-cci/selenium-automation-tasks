from datetime import time

import pytest
from selenium.webdriver.common.by import By

from conftest import driver
from page_objects.login_page import LoginPage


@pytest.mark.login
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.perform_login('admin', 'admin123')

    # Validate logged in URL
    logging_url = driver.current_url
    assert logging_url == "https://login-app-iota.vercel.app/dashboard", "URL should not change"

    # # Validate login message
    # header_text = driver.find_element(By.XPATH, "//h1[text()='Contact List']")
    # login_text = header_text.text
    # assert header_text.is_displayed(), "Contact List message not displayed "
    # assert login_text == "Contact List", "Contact List text does not match"

    driver.quit()


@pytest.mark.login
def test_logout(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.perform_login('admin', 'admin123')

    logged_url = driver.current_url
    assert logged_url == "https://login-app-iota.vercel.app/dashboard", "URL should not change"

    logout_btn = driver.find_element(By.XPATH, "//div[@id='navbarSupportedContent']//a[@href='/login']")
    logout_btn.click()
    driver.quit()
