from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class ContactPage:
    __contact_url = (By.XPATH, "//div[@id='navbarSupportedContent']//a[@href='/contact']")
    __add_contacts_text = (By.XPATH, "/html//div[@id='root']//div[@role='button']/div[@class='text-uppercase']")
    __plus_btn = (By.CSS_SELECTOR, ".fs-2.pointer-event > path:nth-of-type(1)")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get(self.__url)

    @property
    def current_url(self):
        return self._driver.current_url


    def go_to_contact_pg(self):
        self._driver.find_element(*self.__contact_url).click()

    @property
    def get_the_heading(self) -> str:
        header_text = self._driver.find_element(*self.__add_contacts_text)
        actual_txt = header_text.text
        return actual_txt

    def click_plus_button(self):
        self._driver.find_element(*self.__plus_btn).click()

