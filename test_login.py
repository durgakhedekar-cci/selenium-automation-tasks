import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.login
def test_valid_login():
# open the browser
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # Navigate to Site URL
    driver.get("https://login-app-iota.vercel.app/login")
    time.sleep(2)
    # Validate if default URL is pointing to login route
    current_url = driver.current_url
    assert current_url == "https://login-app-iota.vercel.app/login", "Default URL should be login"
    # locate username element
    user_name = driver.find_element(By.ID, "username_textbox")
    # locate password element
    password = driver.find_element(By.ID, "password_textbox")
    # locate Login button
    login_btn = driver.find_element(By.XPATH,
                                    "/html//div[@id='root']/div[@class='App']/section/div//form//button[@type='submit']")
    # enter Valid username
    user_name.send_keys("admin")
    # enter valid password
    password.send_keys("admin123")
    # click on login button
    login_btn.click()
    # Validate logged in URL
    logged_url = driver.current_url
    assert logged_url == "https://login-app-iota.vercel.app/about", "Default logged URL is about"
    # Validate login message
    header_text = driver.find_element(By.TAG_NAME, "h1")
    login_txt = header_text.text
    assert header_text.is_displayed(), "Welcome message not displayed "
    assert login_txt == "Welcome to Selenium Learning Group", "Welcome text does not match"

    time.sleep(5)
    driver.quit()
