from datetime import time
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



def login_logout():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://login-app-iota.vercel.app/login")
    time.sleep(2)

    username = driver.find_element(By.ID, "username_textbox")
    username.send_keys("admin")

    password = driver.find_element(By.ID, "password_textbox")
    password.send_keys("admin123")

    Login_btn = driver.find_element(By.XPATH,
                                    "/html//div[@id='root']/div[@class='App']/section/div//form//button[@type='submit']")
    Login_btn.click()
    time.sleep(2)

    logout_btn = driver.find_element(By.XPATH, "//div[@id='navbarSupportedContent']//a[@href='/login']")
    logout_btn.click()

    current_url = driver.current_url
    assert current_url == "https://login-app-iota.vercel.app/login", "Default URL is login"

    time.sleep(5)
    driver.quit()


