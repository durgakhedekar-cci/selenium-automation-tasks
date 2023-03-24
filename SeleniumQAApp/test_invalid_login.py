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


@pytest.mark.invalid
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

# def test_invalid_password_login():
#     driver.get("https://login-app-iota.vercel.app/login")
#     time.sleep(2)
#     current_urls = driver.current_url
#     assert current_urls == "https://login-app-iota.vercel.app/login", "Default URL should be login"
#
#     user_names = driver.find_element(By.ID, "username_textbox")
#     passwords = driver.find_element(By.ID, "password_textbox")
#
#     login_button = driver.find_element(By.XPATH,
#                                        "/html//div[@id='root']/div[@class='App']/section/div//form//button[@type='submit']")
#
#     user_names.send_keys("admin")
#
#     passwords.send_keys("admin2365")
#
#     login_button.click()
#     # Validate logged in URL
#     login_url = driver.current_url
#     assert login_url == "https://login-app-iota.vercel.app/login", "URL should not change"
#
#     # Validate login message
#     error_message = driver.find_element(By.CSS_SELECTOR, ".mb-2.text-center.text-danger")
#     error_msg = error_message.text
#     assert error_message.is_displayed(), "Error message is not displayed"
#     assert error_msg == "Invalid Credentials", "Error message does not match"
