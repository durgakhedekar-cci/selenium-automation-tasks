import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class TestCasesPage:
    __testcase_url = (By.CSS_SELECTOR, "div > a:nth-of-type(4)")
    __collapase_btn_tc1 = (By.CSS_SELECTOR, "h2#flush-headingOne > .accordion-button.collapsed")
    __expand_btn_tc1 = (By.CSS_SELECTOR, "h2#flush-headingOne > .accordion-button")
    __collapse_btn_tc2 = (By.CSS_SELECTOR, "h2#flush-headingTwo > .accordion-button.collapsed")
    __expand_btn_tc2 = (By.CSS_SELECTOR, "h2#flush-headingTwo > .accordion-button")
    __collapse_btn_tc3 = (By.CSS_SELECTOR, "h2#flush-headingThree > .accordion-button.collapsed")
    __expand_btn_tc3 = (By.CSS_SELECTOR, "h2#flush-headingThree > .accordion-button")
    __collapse_btn_tc4 = (By.CSS_SELECTOR, "h2#flush-headingFour > .accordion-button.collapsed")
    __expand_btn_tc4 = (By.CSS_SELECTOR, "h2#flush-headingFour > .accordion-button")
    __tc1_inside_text = (By.XPATH, "//div[@id='flush-collapseOne']/div[@class='accordion-body px-5']")
    __tc2_inside_text = (By.XPATH, "//div[@id='flush-collapseTwo']/div[@class='accordion-body px-5']")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get(self.__url)

    @property
    def current_url(self):
        return self._driver.current_url

    def go_to_testcase_page(self):
        self._driver.find_element(*self.__testcase_url).click()

    def check_collapse_expand_tc1(self):
        element = self._driver.find_element(*self.__collapase_btn_tc1)
        self._driver.execute_script("arguments[0].click();", element)
        element1 = self._driver.find_element(*self.__expand_btn_tc1)
        self._driver.execute_script("arguments[0].click();", element1)

    def check_collapse_expand_tc2(self):
        element2 = self._driver.find_element(*self.__collapse_btn_tc2)
        self._driver.execute_script("arguments[0].click();", element2)
        element3 = self._driver.find_element(*self.__expand_btn_tc2)
        self._driver.execute_script("arguments[0].click();", element3)

    def check_collapse_expand_tc3(self):
        element4 = self._driver.find_element(*self.__collapse_btn_tc3)
        self._driver.execute_script("arguments[0].click();", element4)
        element5 = self._driver.find_element(*self.__expand_btn_tc3)
        self._driver.execute_script("arguments[0].click();", element5)

    def check_collapse_expand_tc4(self):
        element = self._driver.find_element(*self.__collapse_btn_tc4)
        self._driver.execute_script("arguments[0].click();", element)
        element1 = self._driver.find_element(*self.__expand_btn_tc4)
        self._driver.execute_script("arguments[0].click();", element1)

    @property
    def get_text_tc1(self) -> str:
        text_tc1 = self._driver.find_element(*self.__expand_btn_tc1)
        txt_tc1 = text_tc1.text
        return txt_tc1

    @property
    def get_inside_text_tc1(self) -> str:
        open_tc1 = self._driver.find_element(*self.__collapase_btn_tc1)
        open_tc1.click()
        inside_tc1_text = self._driver.find_element(*self.__tc1_inside_text)
        inside_tc1_txt = inside_tc1_text.text
        return inside_tc1_txt

    @property
    def get_text_tc2(self) -> str:
        text_tc2 = self._driver.find_element(*self.__expand_btn_tc2)
        txt_tc2 = text_tc2.text
        return txt_tc2

    @property
    def get_inside_text_tc2(self) -> str:
        open_tc2 = self._driver.find_element(*self.__collapse_btn_tc2)
        open_tc2.click()
        inside_tc2_text = self._driver.find_element(*self.__tc2_inside_text)
        inside_tc2_txt = inside_tc2_text.text
        return inside_tc2_txt

    @property
    def get_text_tc3(self) -> str:
        text_tc3 = self._driver.find_element(*self.__expand_btn_tc3)
        txt_tc3 = text_tc3.text
        return txt_tc3

    @property
    def get_text_tc4(self) -> str:
        text_tc4 = self._driver.find_element(*self.__expand_btn_tc4)
        txt_tc4 = text_tc4.text
        return txt_tc4

