import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.invalid
def test_invalid_username_login():

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("https://login-app-iota.vercel.app/login")
    time.sleep(2)
    current_url = driver.current_url
    assert current_url == "https://login-app-iota.vercel.app/login", "Default URL should be login"

    user_name = driver.find_element(By.ID, "username_textbox")
    password = driver.find_element(By.ID, "password_textbox")


    login_btn = driver.find_element(By.XPATH,
                                    "/html//div[@id='root']/div[@class='App']/section/div//form//button[@type='submit']")

    user_name.send_keys("adminxyz")

    password.send_keys("admin123")

    login_btn.click()
    # Validate logged in URL
    logging_url = driver.current_url
    assert logging_url == "https://login-app-iota.vercel.app/login", "URL should not change"
    # Validate login message
    error_text = driver.find_element(By.CSS_SELECTOR, ".mb-2.text-center.text-danger")
    error_txt = error_text.text
    assert error_text.is_displayed(), "Error message is not displayed"
    assert error_txt == "Invalid Credentials", "Error message does not match"
    time.sleep(5)
    driver.quit()


@pytest.mark.invalid
def test_invalid_password_login():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("https://login-app-iota.vercel.app/login")
    time.sleep(2)
    current_urls = driver.current_url
    assert current_urls == "https://login-app-iota.vercel.app/login", "Default URL should be login"

    user_names = driver.find_element(By.ID, "username_textbox")
    passwords = driver.find_element(By.ID, "password_textbox")

    login_button = driver.find_element(By.XPATH,
                                       "/html//div[@id='root']/div[@class='App']/section/div//form//button[@type='submit']")

    user_names.send_keys("admin")

    passwords.send_keys("admin12344")

    login_button.click()
    # Validate logged in URL
    login_url = driver.current_url
    assert login_url == "https://login-app-iota.vercel.app/login", "URL should not change"
    # Validate login message
    error_message = driver.find_element(By.CSS_SELECTOR, ".mb-2.text-center.text-danger")
    error_msg = error_message.text
    assert error_message.is_displayed(), "Error message is not displayed"
    assert error_msg == "Invalid Credentials", "Error message does not match"
    time.sleep(5)
    driver.quit()
