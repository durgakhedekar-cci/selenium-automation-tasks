import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# this file will have code for arrange only
@pytest.fixture
def driver():
    # open the browser
    print("Creating driver for chrome browser")
    # browser_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # browser_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    browser_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    yield browser_driver
    print("Closing driver for chrome browser")
    browser_driver.quit()





