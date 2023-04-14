import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class TestCasesPage:
    __testcase_url = (By.CSS_SELECTOR, "div > a:nth-of-type(4)")
    __expand_btn_tc1 = (By.CSS_SELECTOR, "h2#flush-headingOne > .accordion-button.collapsed")
    __collapse_btn_tc1 = (By.CSS_SELECTOR, "h2#flush-headingOne > .accordion-button")


    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get(self.__url)

    @property
    def current_url(self):
        return self._driver.current_url

    def go_to_testcase_page(self):
        self._driver.find_element(*self.__testcase_url).click()

    def check_collapse_expand_TC1(self):
        expand_btn = self._driver.find_element(*self.__expand_btn_tc1)
        expand_btn.click()
        collapse_btn = self._driver.find_element(*self.__collapse_btn_tc1)
        collapse_btn.click()


