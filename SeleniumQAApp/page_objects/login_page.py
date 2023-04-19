
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class LoginPage:
    __url = 'https://login-app-iota.vercel.app/login'
    __username_field = (By.ID, "username_textbox")
    __password_field = (By.ID, "password_textbox")
    __submit_button = (By.XPATH, "/html//div[@id='root']/div[@class='App']/section/div//form//button[@type='submit']")
    __error_label_field = (By.CSS_SELECTOR, ".mb-2.text-center.text-danger")
    __header_txt = (By.XPATH, "/html//div[@id='root']/div[@class='App']/section/div/div//h4[.='Please login to your account']")
    __rightside_header_txt = (By.XPATH, "/html//div[@id='root']/div[@class='App']/section/div//h4[@class='mb-3 text-center text-uppercase']")
    __rightside_sub_text = (By.XPATH, "///p[@innertext>'Selenium is a powerful tool for controlling web browsers thr']")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get(self.__url)

    @property
    def current_url(self):
        return self._driver.current_url

    def perform_login(self, username, password):
        username_data = self._driver.find_element(*self.__username_field)
        password_data = self._driver.find_element(*self.__password_field)
        submit_button_field = self._driver.find_element(*self.__submit_button)

        username_data.send_keys(username)
        password_data.send_keys(password)
        submit_button_field.click()

    @property
    def error_label_text(self)->str:
        error_label = self._driver.find_element(self.__error_label_field)
        actual_text = error_label.text
        return actual_text

    def is_error_label_displayed(self) -> bool:
        error_label = self._driver.find_element(self.__error_label_field)
        return error_label.is_displayed()

    @property
    def get_the_heading(self) -> str:
        header_text = self._driver.find_element(*self.__header_txt)
        actual_txt1 = header_text.text
        return actual_txt1

    @property
    def get_the_heading_rightside(self) -> str:
        header_text_rightside = self._driver.find_element(*self.__rightside_header_txt)
        actual_txt2 = header_text_rightside.text
        return actual_txt2

    # @property
    # def get_the_sub_text_rightside(self) -> str:
    #     sub_text_rightside = self._driver.find_element(*self.get_the_sub_text_rightside)
    #     actual_txt3 = sub_text_rightside.text
    #     return actual_txt3