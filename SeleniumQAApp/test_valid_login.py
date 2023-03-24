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
    logging_url = driver.current_url
    assert logging_url == "https://login-app-iota.vercel.app/dashboard", "URL should not change"

    # Validate login message
    time.sleep(3)
    header_text = driver.find_element(By.XPATH, "//h1[text()='Contact List']")
    login_text = header_text.text
    assert header_text.is_displayed(), "Contact List message not displayed "
    assert login_text == "Contact List", "Contact List text does not match"

    time.sleep(5)
    driver.quit()
