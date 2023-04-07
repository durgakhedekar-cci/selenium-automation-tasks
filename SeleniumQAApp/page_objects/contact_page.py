from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class ContactPage():
    __contact_url = (By.XPATH, "//div[@id='navbarSupportedContent']//a[@href='/contact']")


    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get(self.__url)

    @property
    def current_url(self):
        return self._driver.current_url

    def go_to_contact_pg(self):
        self._driver.find_element(*self.__contact_url).click()

