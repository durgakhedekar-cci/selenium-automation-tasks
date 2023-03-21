import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.negativeTCs
def test_login_invalid_username():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://login-app-iota.vercel.app/login")
    time.sleep(2)

    username = driver.find_element(By.ID, "username_textbox")
    username.send_keys("ddrfff")

    password = driver.find_element(By.ID, "password_textbox")
    password.send_keys("admin123")

    Login_btn = driver.find_element(By.XPATH,
                                    "/html//div[@id='root']/div[@class='App']/section/div//form//button[@type='submit']")
    Login_btn.click()

    error_text = driver.find_element(By.CSS_SELECTOR, ".mb-2.text-center.text-danger")
    error_txt = error_text.text
    assert error_text.is_displayed(), "Error message is not displayed"
    assert error_txt == "Invalid Credentials", "Error message does not match"
    time.sleep(2)
