# Import pacakges
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# open the browser
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Navigate to the URL
driver.get("https://duckduckgo.com/")
time.sleep(3)
# Search for the textbox on the webpage
search_textbox = driver.find_element(By.ID, 'search_form_input_homepage')

# Enter search text in the textbox

search_textbox.send_keys("Selenium")

# Locate the search button

search_button = driver.find_element(By.ID, 'search_button_homepage')
# Click on the search button

search_button.click()
time.sleep(5)

# View result
driver.close()
