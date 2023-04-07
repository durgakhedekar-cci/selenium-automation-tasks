import time

from page_objects.contact_page import ContactPage
from page_objects.login_page import LoginPage


def test_contact(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.perform_login('admin', 'admin123')

    contact_page = ContactPage(driver)
    contact_page.go_to_contact_pg()
    time.sleep(2)

