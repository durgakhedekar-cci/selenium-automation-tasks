import requests
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class AboutPage:
    __contact_pg_url = (By.XPATH, "//div[@id='navbarSupportedContent']//a[@href='/about']")
    __header_txt = (By.TAG_NAME, "h1")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def current_url(self):
        return self._driver.current_url

    def navigate_to_about(self):
        self._driver.find_element(*self.__contact_pg_url).click()

    @property
    def header_text_data(self) -> str:
        head_text = self._driver.find_element(*self.__header_txt)
        actual_txt = head_text.text
        return actual_txt

    def is_header_text_displayed(self) -> bool:
        try:
            head_txt = self._driver.find_element(*self.__header_txt)
        except NoSuchElementException as e:
            print("\nElement Not Found")
            return False
        return True
