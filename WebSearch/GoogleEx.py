import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.google.com/")
print(driver.title)
time.sleep(3)

search_text = driver.find_element(By.XPATH, "/html/body//form[@role='search']//div[@class='A8SBwf']//div[@class='a4bIc']/input[@role='combobox']")
search_text.send_keys("Selenium")

search_btn = driver.find_element(By.XPATH, "/html/body//form[@role='search']//div[@class='A8SBwf']/div[@class='FPdoLc lJ9FBc']/center/input[@role='button']")

search_btn.click()
time.sleep(3)