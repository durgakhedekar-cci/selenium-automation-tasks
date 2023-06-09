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
    testcase_page.check_collapse_expand_tc1()
    testcase_page.check_collapse_expand_tc2()
    testcase_page.check_collapse_expand_tc3()
    testcase_page.check_collapse_expand_tc4()

    assert testcase_page.get_text_tc1 == "Test 1 : A user with valid credentials should able to Login successfully\nURL : https://login-app-iota.vercel.app/login", "The text is incorrect"
    assert testcase_page.get_inside_text_tc1 == ('1. Open Browser\n' '2. Navigate to Site URL\n' '3. Validate if default URL is pointing to login route\n'
                                                '4. Locate username element\n'
                                                '5. Locate password element\n'
                                                '6. Locate Login button\n'
                                                '7. Enter Valid username\n'
                                                '8. Enter valid password\n'
                                                '9. Click on login button\n'
                                                '10. Validate logged in URL\n'
                                                '11. Validate login message'), "The text is incorrect"

    assert testcase_page.get_text_tc2 == "Test 2 : A user with valid credentials should able to Login successfully and logout successfully\nURL : https://login-app-iota.vercel.app/login", "The text is incorrect"
    assert testcase_page.get_inside_text_tc2 == ('1. Open Browser\n' '2. Navigate to Site URL\n' '3. Validate if default URL is pointing to login route\n'
                                                '4. Locate username element\n'
                                                '5. Locate password element\n'
                                                '6. Locate Login button\n'
                                                '7. Enter Valid username\n'
                                                '8. Enter valid password\n'
                                                '9. Click on login button\n'
                                                '10. Validate logged in URL\n'
                                                '11. Validate login message\n'
                                                '12. Locate logout menu/button\n'
                                                '13. Click on logout button\n'
                                                '14. Validate that login page URL is displayed'), "The text is incorrect"

    assert testcase_page.get_text_tc3 == "Test 3 : A user with invalid username should not be able to Login\nURL : https://login-app-iota.vercel.app/login" , "The text is incorrect"


    assert testcase_page.get_text_tc4 == "Test 4 : A user with invalid password should not be able to Login\nURL : https://login-app-iota.vercel.app/login", "The text is incorrect"