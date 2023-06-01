import pytest
from page_objects.about_page import AboutPage
from page_objects.dashboard_page import DashboardPage
from page_objects.login_page import LoginPage


@pytest.mark.contact
def test_dashboard_pg(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.perform_login('admin', 'admin123')

    dashboard_page = DashboardPage(driver)
    assert dashboard_page.current_url == "https://login-app-iota.vercel.app/dashboard", "URL is not correct"
    assert dashboard_page.get_contact_title() == "Contact List", "Header does not match"
    dashboard_page.get_table_data()
