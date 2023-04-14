import time

from page_objects.contact_page import ContactPage
from page_objects.login_page import LoginPage
from page_objects.testcases_page import TestCasesPage


def test_testcases(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.perform_login('admin', 'admin123')

    testcase_page = TestCasesPage(driver)
    testcase_page.go_to_testcase_page()

    assert testcase_page.current_url == "https://login-app-iota.vercel.app/test-cases", "URL is not correct"
    testcase_page.check_collapse_expand_TC1()