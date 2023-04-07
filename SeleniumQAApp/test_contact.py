import time

from page_objects.contact_page import ContactPage
from page_objects.login_page import LoginPage


def test_contact(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.perform_login('admin', 'admin123')

    contact_page = ContactPage(driver)
    contact_page.go_to_contact_pg()

    assert contact_page.current_url == "https://login-app-iota.vercel.app/contact", "URL is not correct"
    assert contact_page.get_the_heading == "ADD CONTACTS", " The heading is incorrect"

    contact_page.click_plus_button()

