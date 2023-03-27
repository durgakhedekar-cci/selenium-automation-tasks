from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class LoginPage:
    __url = 'https://login-app-iota.vercel.app/login'
    __username_field = (By.ID, "username_textbox")
    __password_field = (By.ID, "password_textbox")
    __submit_button = (By.XPATH, "/html//div[@id='root']/div[@class='App']/section/div//form//button[@type='submit']")

    def __init__(self, driver:WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get(self.__url)

    @property
    def current_url(self):
        return self._driver.current_url

