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

    contact_page.click_plus_minus_button()

    assert contact_page.get_first_name_field == "First name", "Text is incorrect"
    assert contact_page.get_last_name_field == "Last name", "Text is incorrect"
    assert contact_page.get_email_field == "Email address", "Text is incorrect"
    assert contact_page.get_phone_field() == "Phone Number", "Text is incorrect"
    assert contact_page.get_address_field == "Address", "Text is incorrect"
    assert contact_page.get_submit_field_text == "Submit", "Text is incorrect"

    assert contact_page.get_placeholder_text_fn == "Enter first name", "The placeholder text is incorrect"
    assert contact_page.get_placeholder_text_ln == "Enter last name", "The placeholder text is incorrect"
    assert contact_page.get_placeholder_text_email == "Enter email", "The placeholder text is incorrect"
    assert contact_page.get_placeholder_text_phone == "Enter phone number", "The placeholder text is incorrect"
    assert contact_page.get_placeholder_text_address == "Enter adress", "The placeholder text is incorrect"
    time.sleep(5)

    assert contact_page.get_table_field_name == "Name", "The column field name is incorrect"
    assert contact_page.get_table_field_email == "Email", "The column field name is incorrect"
    assert contact_page.get_table_field_phone == "Phone Number", "The column field name is incorrect"
    assert contact_page.get_table_field_address == "Address", "The column field name is incorrect"

    #contact_page.enter_text_in_fields('Test', 'Test1', 'test@test.com','1234567890', 'Ponda')
    time.sleep(5)
