from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TaskPage:
    __task_url = (By.CSS_SELECTOR, "div > a:nth-of-type(2)")
    __header_txt = (By.TAG_NAME, "h4")
    __subheader_txt = (By.TAG_NAME, "h5")
    __span1_text = (
    By.CSS_SELECTOR, ".border.border-1.d-flex.flex-column.instruction.mt-2.px-4.py-2.rounded > span:nth-of-type(1)")
    __span2_text = (
    By.CSS_SELECTOR, ".border.border-1.d-flex.flex-column.instruction.mt-2.px-4.py-2.rounded > span:nth-of-type(2)")
    __span3_text = (
    By.CSS_SELECTOR, ".border.border-1.d-flex.flex-column.instruction.mt-2.px-4.py-2.rounded > span:nth-of-type(3)")
    __span4_text = (
    By.CSS_SELECTOR, ".border.border-1.d-flex.flex-column.instruction.mt-2.px-4.py-2.rounded > span:nth-of-type(4)")
    __add_task_field = (By.ID, "task-input")
    __add_btn = (By.CSS_SELECTOR, ".btn.btn-primary.col-2.mb-2.ml-2")
    __added_text = (By.CSS_SELECTOR, ".col-10.text-break.wrap")
    __text_present = (By.CSS_SELECTOR, "input#task-input")
    __edit_btn = (By.CSS_SELECTOR, "svg:nth-of-type(1) > path")
    __save_btn = (By.CSS_SELECTOR, ".btn.btn-secondary.col-2.mb-2.ml-2")
    __delete_btn = (By.CSS_SELECTOR, "svg:nth-of-type(3) > path")
    __strike_button = (By.CSS_SELECTOR, "svg:nth-of-type(2) > path")
    __strike_txt = (By.CSS_SELECTOR, ".col-10.task-done.text-break.wrap")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get(self.__url)

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
        # add_task.clear()
        add_task.send_keys(sometext)
        add_button.click()

    def get_added_text(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__added_text))
        return self._driver.find_element(*self.__added_text).text

    @property
    def check_mandatory_field(self) -> str:
        click_textfield = self._driver.find_element(*self.__add_task_field)
        click_textfield.click()
        click_add_button_field = self._driver.find_element(*self.__add_btn)
        click_add_button_field.click()
        alert = self._driver.switch_to.alert
        popup_txt = alert.text
        alert.accept()
        return popup_txt


    @property
    def get_text_from_textbox(self) -> str:
        get_txt = self._driver.find_element(*self.__text_present)
        actual_txt5 = get_txt.get_attribute('value')
        return actual_txt5

    @property
    def get_placeholder_text(self) -> str:
        placeholder_txt = self._driver.find_element(*self.__text_present)
        placeholder_txt.clear()
        actual_txt6 = placeholder_txt.get_attribute('placeholder')
        return actual_txt6

    def edit_the_task(self, edittxt):
        edit_button = self._driver.find_element(*self.__edit_btn)
        edit_button.click()
        edit_field = self._driver.find_element(*self.__add_task_field)
        edit_field.click()
        edit_field.clear()
        edit_field.send_keys(edittxt)
        save_button = self._driver.find_element(*self.__save_btn)
        save_button.click()

    def delete_the_task(self):
        delete_button = self._driver.find_element(*self.__delete_btn)
        delete_button.click()

    def is_deleted_text_displayed(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(e.invisibility_of_element_located(self.__added_text))

    def stike_through(self):
        strike_btn = self._driver.find_element(*self.__strike_button)
        strike_btn.click()
        strike_text = self._driver.find_element(*self.__strike_txt)
        #this is to check if strike through cannot be seen
        #self._driver.execute_script("arguments[0].style.textDecoration = 'none';", strike_text)
        actual_txt7 = strike_text.value_of_css_property('text-decoration')

        if 'line-through' in actual_txt7:
            print("I can see the strike-through text")
            return True
        else:
            print("I cannot see the strike-through text")
            return False