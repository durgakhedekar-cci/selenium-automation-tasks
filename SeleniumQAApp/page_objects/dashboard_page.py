from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class DashboardPage:
    __logout_link = (By.XPATH, "//div[@id='navbarSupportedContent']//a[@href='/login']")
    __contact_list_header = (By.XPATH, "//h1[text()='Contact List']")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def current_url(self):
        return self._driver.current_url

    def perform_logout(self):
        self._driver.find_element(*self.__logout_link).click()

    def get_contact_title(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__contact_list_header))
        return self._driver.find_element(*self.__contact_list_header).text
