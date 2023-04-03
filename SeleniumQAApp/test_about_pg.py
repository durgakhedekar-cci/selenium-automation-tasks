import pytest
from page_objects.about_page import AboutPage
from page_objects.login_page import LoginPage


@pytest.mark.contact
def test_about_pg(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.perform_login('admin', 'admin123')

    about_page = AboutPage(driver)
    about_page.navigate_to_about()
    assert about_page.current_url == "https://login-app-iota.vercel.app/about", "URL is not correct"

    assert about_page.is_header_text_displayed() == True

    about_page.header_text_data == "Welcome to Selenium Learning Group", "title does not match"

    #contact_page.is_header_text_displayed()
