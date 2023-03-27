import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.login
@pytest.mark.negative
@pytest.mark.parametrize("username,password,expected_error_message",
                         [("adminxyz", "admin123", "Invalid Credentials"),
                          ("admin", "admin12345", "Invalid Credentials"),
                          ("adminsss", "admin12345s", "Invalid Credentials")])
def test_invalid_username_login(driver, username, password, expected_error_message):
    driver.get("https://login-app-iota.vercel.app/login")
    time.sleep(2)
    current_url = driver.current_url
    assert current_url == "https://login-app-iota.vercel.app/login", "Default URL should be login"

    user_name = driver.find_element(By.ID, "username_textbox")

    passwords = driver.find_element(By.ID, "password_textbox")

    login_btn = driver.find_element(By.XPATH,
                                    "/html//div[@id='root']/div[@class='App']/section/div//form//button[@type='submit']")

    user_name.send_keys(username)
    passwords.send_keys(password)
    login_btn.click()
    # # Validate logged in URL
    logging_url = driver.current_url
    assert logging_url == "https://login-app-iota.vercel.app/login", "URL should not change"
    # Validate login message
    error_text = driver.find_element(By.CSS_SELECTOR, ".mb-2.text-center.text-danger")
    error_txt = error_text.text
    assert error_text.is_displayed(), "Error message is not displayed"
    assert error_txt == expected_error_message, "Error message does not match"

