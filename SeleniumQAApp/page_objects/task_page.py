import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TaskPage:
    __task_url = (By.CSS_SELECTOR, "div > a:nth-of-type(2)")
    __header_txt = (By.TAG_NAME, "h4")
    __subheader_txt = (By.TAG_NAME, "h5")
    __span1_text = (By.CSS_SELECTOR, ".border.border-1.d-flex.flex-column.instruction.mt-2.px-4.py-2.rounded > span:nth-of-type(1)")
    __span2_text = (By.CSS_SELECTOR, ".border.border-1.d-flex.flex-column.instruction.mt-2.px-4.py-2.rounded > span:nth-of-type(2)")
    __span3_text = (By.CSS_SELECTOR, ".border.border-1.d-flex.flex-column.instruction.mt-2.px-4.py-2.rounded > span:nth-of-type(3)")
    __span4_text = (By.CSS_SELECTOR, ".border.border-1.d-flex.flex-column.instruction.mt-2.px-4.py-2.rounded > span:nth-of-type(4)")
    __add_task_field = (By.ID, "task-input")
    __add_btn = (By.CSS_SELECTOR, ".btn.btn-primary.col-2.mb-2.ml-2")
    __added_text = (By.CSS_SELECTOR, ".col-10.text-break.wrap")
    __edit_btn = (By.CSS_SELECTOR, "svg:nth-of-type(1) > path")
    __save_btn = (By.CSS_SELECTOR, ".btn.btn-secondary.col-2.mb-2.ml-2")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def current_url(self):
        return self._driver.current_url

    def go_to_task_page(self):
        self._driver.find_element(*self.__task_url).click()

    @property
    def check_pg_header(self) -> str:
        head_text = self._driver.find_element(*self.__header_txt)
        actual_txt = head_text.text
        return actual_txt
    @property
    def check_subheader(self) -> str:
        subhead_text = self._driver.find_element(*self.__subheader_txt)
        actual_text = subhead_text.text
        return actual_text
    @property
    def check_sub_subheader1(self) -> str:
        sub_subheader1_text = self._driver.find_element(*self.__span1_text)
        actual_text1 = sub_subheader1_text.text
        return actual_text1

    @property
    def check_sub_subheader2(self) -> str:
        sub_subheader2_text = self._driver.find_element(*self.__span2_text)
        actual_text2 = sub_subheader2_text.text
        return actual_text2

    @property
    def check_sub_subheader3(self) -> str:
        sub_subheader3_text = self._driver.find_element(*self.__span3_text)
        actual_text3 = sub_subheader3_text.text
        return actual_text3

    @property
    def check_sub_subheader4(self) -> str:
        sub_subheader4_text = self._driver.find_element(*self.__span4_text)
        actual_text4 = sub_subheader4_text.text
        return actual_text4

    def enter_text(self, sometext):
        add_task = self._driver.find_element(*self.__add_task_field)
        add_button = self._driver.find_element(*self.__add_btn)
        add_task.click()
        add_task.clear()
        add_task.send_keys(sometext)
        add_button.click()

    def get_added_text(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__added_text))
        return self._driver.find_element(*self.__added_text).text

    def edit_the_task(self, edittxt):
        edit_button = self._driver.find_element(*self.__edit_btn)
        edit_button.click()
        edit_field = self._driver.find_element(*self.__add_task_field)
        edit_field.click()
        edit_field.clear()
        edit_field.send_keys(edittxt)
        save_button = self._driver.find_element(*self.__save_btn)
        save_button.click()

