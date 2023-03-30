import pytest
from selenium.webdriver.common.by import By

from page_objects.dashboard_page import DashboardPage
from page_objects.login_page import LoginPage


@pytest.mark.login
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.perform_login('admin', 'admin123')

    # Validate logged in URL
    logging_url = driver.current_url
    assert logging_url == "https://login-app-iota.vercel.app/dashboard", "URL should not change"


@pytest.mark.login
def test_logout(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.perform_login('admin', 'admin123')

    dashboard_page = DashboardPage(driver)
    assert dashboard_page.current_url == "https://login-app-iota.vercel.app/dashboard", "URL should not change"

    assert dashboard_page.get_contact_title() == "Contact List", "title does not match 'Contact List'"

    dashboard_page.perform_logout()
    assert dashboard_page.current_url == "https://login-app-iota.vercel.app/login"

