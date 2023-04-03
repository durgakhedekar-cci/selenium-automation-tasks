from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TaskPage:

    __task_url = (By.CSS_SELECTOR, "div > a:nth-of-type(2)")
    __header_txt = (By.TAG_NAME,"h4")
    __subheader_txt = (By.TAG_NAME,"h5")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def current_url(self):
        return self._driver.current_url

    def go_to_task_page(self):
        self._driver.find_element(*self.__task_url).click()

    def check_pg_header(self):
        head_text = self._driver.find_element(*self.__header_txt)
        actual_txt = head_text.text
        return actual_txt

    def check_subheader(self):
        subhead_text = self._driver.find_element(*self.__subheader_txt)
        actual_text = subhead_text.text
        return actual_text

