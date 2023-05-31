import time
from telnetlib import EC

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from tabulate import tabulate
from selenium.webdriver.support import expected_conditions as E


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
    __placeholder_fn_field = (By.ID, "name_textbox")
    __placeholder_ln_field = (By.NAME, "lastName")
    __placeholder_email_field = (By.ID, "email_textbox")
    __placeholder_phone_field = (By.ID, "phone_textbox")
    __placeholder_address_field = (By.ID, "message_textbox")
    __fn_input_field = (By.ID, "name_textbox")
    __ln_input_field = (By.XPATH, "/html//div[@id='root']/div[@class='App']//form/div[1]/div[2]/input[@id='name_textbox']")
    __email_input_field = (By.ID, "email_textbox")
    __phone_input_field = (By.ID, "phone_textbox")
    __address_input_field = (By.ID, "message_textbox")
    __submit_button = (By.XPATH, "/html//div[@id='root']/div[@class='App']//form//button[@type='submit']")
    __table_field_name = (By.XPATH, "/html//div[@id='root']/div[@class='App']//table[@class='table']//th[.='Name']")
    __table_field_email = (By.XPATH, "/html//div[@id='root']/div[@class='App']//table[@class='table']//th[.='Email']")
    __table_field_phone = (By.XPATH, "/html//div[@id='root']/div[@class='App']//table[@class='table']//th[.='Phone Number']")
    __table_field_address = (By.XPATH, "/html//div[@id='root']/div[@class='App']//table[@class='table']//th[.='Address']")
    #__table_row_data = (By.XPATH, "//table/tbody/tr")
    __table_row_data = (By.XPATH, "/html//div[@id='root']/div[@class='App']//table[@class='table']//th")
    #__table_col_data = (By.XPATH, "//table/tbody/tr[1]/td")
    __table_col_data = (By.XPATH, "//table[@class='table']//tbody/tr/td[1]")
    #__table_data = (By.XPATH, "//tr[' + str(i) + ']/td[' + str(j) + ']")
    __table_data = (By.XPATH, "/html//div[@id='root']/div/div/div/div[2]")

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
        # self._driver.find_element(*self.__plus_btn).click()

    @property
    def get_first_name_field(self) -> str:
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

    @property
    def get_placeholder_text_fn(self) -> str:
        placeholder_txt_fn = self._driver.find_element(*self.__placeholder_fn_field)
        actual_txt = placeholder_txt_fn.get_attribute('placeholder')
        return actual_txt

    @property
    def get_placeholder_text_ln(self) -> str:
        placeholder_txt_ln = self._driver.find_element(*self.__placeholder_ln_field)
        actual_txt1 = placeholder_txt_ln.get_attribute('placeholder')
        return actual_txt1

    @property
    def get_placeholder_text_email(self) -> str:
        placeholder_txt_email = self._driver.find_element(*self.__placeholder_email_field)
        actual_txt2 = placeholder_txt_email.get_attribute('placeholder')
        return actual_txt2

    @property
    def get_placeholder_text_phone(self) -> str:
        placeholder_txt_phone = self._driver.find_element(*self.__placeholder_phone_field)
        actual_txt3 = placeholder_txt_phone.get_attribute('placeholder')
        return actual_txt3

    @property
    def get_placeholder_text_address(self) -> str:
        placeholder_txt_address = self._driver.find_element(*self.__placeholder_address_field)
        actual_txt4 = placeholder_txt_address.get_attribute('placeholder')
        return actual_txt4

    @property
    def get_table_field_name(self) -> str:
        table_text1 = self._driver.find_element(*self.__table_field_name)
        table_txt1 = table_text1.text
        return table_txt1

    @property
    def get_table_field_email(self) -> str:
        table_text2 = self._driver.find_element(*self.__table_field_email)
        table_txt2 = table_text2.text
        return table_txt2

    @property
    def get_table_field_phone(self) -> str:
        table_text3 = self._driver.find_element(*self.__table_field_phone)
        table_txt3 = table_text3.text
        return table_txt3

    @property
    def get_table_field_address(self) -> str:
        table_text4 = self._driver.find_element(*self.__table_field_address)
        table_txt4 = table_text4.text
        return table_txt4

    def enter_text_in_fields(self, fname, lname, email, phone, address):
        add_fn = self._driver.find_element(*self.__fn_input_field)
        add_fn.click()
        add_fn.send_keys(fname)
        add_ln = self._driver.find_element(*self.__ln_input_field)
        add_ln.click()
        add_ln.send_keys(lname)
        add_email = self._driver.find_element(*self.__email_input_field)
        add_email.click()
        add_email.send_keys(email)
        add_phone = self._driver.find_element(*self.__phone_input_field)
        add_phone.click()
        add_phone.send_keys(phone)
        add_address = self._driver.find_element(*self.__address_input_field)
        add_address.click()
        add_address.send_keys(address)
        submit_btn = self._driver.find_element(*self.__submit_button)
        submit_btn.click()

    def check_mandatory_field_fn(self):
        fn_error_msg = self._driver.find_element(*self.__fn_input_field).get_attribute("validationMessage")
        return fn_error_msg

    def check_mandatory_field_ln(self):
        fill_fn = self._driver.find_element(*self.__fn_input_field)
        fill_fn.send_keys('Test')
        ln_error_msg = self._driver.find_element(*self.__ln_input_field).get_attribute("validationMessage")
        fill_fn.clear()
        return ln_error_msg

    def get_table_data(self):
        wait = WebDriverWait(self._driver, 10)

        rows = wait.until(E.presence_of_all_elements_located(self.__table_row_data))
        r = len(rows)

        column = wait.until(E.presence_of_all_elements_located(self.__table_col_data))
        c = len(column)

        element = []
        for i in range(1, r):
            row_data = []
            for j in range(1, c):
                get_txt = wait.until(E.visibility_of_element_located(self.__table_data))
                get_txt_text = get_txt.text
                row_data.append(get_txt_text)
            element.append(row_data)

        headers = [cell.text for cell in rows[0].find_elements(By.XPATH, "./td")]
        print("The following data is shown from the table:")
        print(tabulate(element, headers=headers, tablefmt="grid"))


