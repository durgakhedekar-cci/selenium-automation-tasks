from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class ContactPage:
    __contact_url = (By.XPATH, "//div[@id='navbarSupportedContent']//a[@href='/contact']")
    __add_contacts_text = (By.XPATH, "/html//div[@id='root']//div[@role='button']/div[@class='text-uppercase']")
    __plus_btn = (By.CSS_SELECTOR, ".fs-2.pointer-event > path:nth-of-type(1)")
    __first_name_field = (By.XPATH, "/html//div[@id='root']/div[@class='App']//form//label[.='First name']")
    __last_name_field = (By.XPATH, "/html//div[@id='root']/div[@class='App']//form//label[.='Last name']")
    __email_field = (By.XPATH, "/html//div[@id='root']/div[@class='App']//form//label[.='Email address']")
    __phone_number_field = (By.XPATH, "/html//div[@id='root']/div[@class='App']//form//label[.='Phone Number']")
    __address_field = (By.XPATH, "/html//div[@id='root']/div[@class='App']//form//label[.='Address']")
    __submit_btn_text = (By.XPATH, "/html//div[@id='root']/div[@class='App']//form//button[@type='submit']")

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

    def click_plus_minus_button(self):
        self._driver.find_element(*self.__plus_btn).click()
        #self._driver.find_element(*self.__plus_btn).click()

    @property
    def get_first_name_field(self) ->str:
        fn_txt = self._driver.find_element(*self.__first_name_field)
        first_name_text = fn_txt.text
        return first_name_text

    @property
    def get_last_name_field(self) -> str:
        ln_txt = self._driver.find_element(*self.__last_name_field)
        last_name_text = ln_txt.text
        return last_name_text

    @property
    def get_email_field(self) -> str:
        email_txt = self._driver.find_element(*self.__email_field)
        email_text = email_txt.text
        return email_text

    def get_phone_field(self):
        phone_num = self._driver.find_element(*self.__phone_number_field)
        ph_no = phone_num.text
        return ph_no

    @property
    def get_address_field(self) -> str:
        address_txt = self._driver.find_element(*self.__address_field)
        address_text = address_txt.text
        return address_text

    @property
    def get_submit_field_text(self) -> str:
        submit_txt = self._driver.find_element(*self.__submit_btn_text)
        submit_text = submit_txt.text
        return submit_text
