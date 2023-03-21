import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://creativecapsule.greythr.com/")
time.sleep(2)

login_name = driver.find_element(By.NAME, "username")
login_name.send_keys("username")

password = driver.find_element(By.ID, "password")
password.send_keys("password")
time.sleep(2)
login_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]")
login_btn.click()

time.sleep(5)
