# Import pacakges
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


# open the browser
driver = webdriver.Chrome(ChromeDriverManager().install())

# Navigate to the URL
driver.get("https://duckduckgo.com/")
time.sleep(3)
# Search for the textbox on the webpage
search_textbox = driver.find_element_by_id('search_form_input_homepage')

# Enter search text in the textbox

search_textbox.send_keys("Selenium")

# Locate the search button

search_button = driver.find_element_by_id('search_button_homepage')
# Click on the search button

search_button.click()
time.sleep(5)

# View result
driver.close()
