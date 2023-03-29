import time

import pytest
from selenium.webdriver.common.by import By

from page_objects.login_page import LoginPage



@pytest.mark.negative
@pytest.mark.parametrize("username,password,expected_error_message",
                         [("adminxyz", "admin123", "Invalid Credentials"),
                          ("admin", "admin12345", "Invalid Credentials"),
                          ("adminsss", "admin12345s", "Invalid Credentials")])
def test_invalid_username_login_p(driver, username, password, expected_error_message):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.perform_login(username, password)

    assert login_page.current_url == "https://login-app-iota.vercel.app/login", "URL should not change"
    #assert login_page.is_error_label_displayed(), "Error message is not displayed"
    #assert login_page.error_label_text == expected_error_message, "Error message not displayed"
