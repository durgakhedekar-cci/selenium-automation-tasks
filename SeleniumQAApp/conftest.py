import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture
# @pytest.fixture(params=["chrome", "firefox", "edge"])
def driver(request):
    browser = request.config.getoption("--browser")
    # browser = request.param
    # Open Browser
    print(f"Creating driver for {browser} browser")
    if browser == "chrome":
        browser_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        browser_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "edge":
        browser_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise TypeError(f"Expected browser to be chrome,firefox,edge got {browser}")
    #browser_driver.implicitly_wait(10)
    yield browser_driver
    print(f"Closing driver for {browser} browser")
    browser_driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", help="proivide browser as chrome,edge or firefox")
