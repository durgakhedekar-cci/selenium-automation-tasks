from page_objects.login_page import LoginPage
from page_objects.task_page import TaskPage


def test_task(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.perform_login('admin', 'admin123')

    task_page = TaskPage(driver)
    task_page.go_to_task_page()

    assert task_page.current_url == "https://login-app-iota.vercel.app/task", "URL is not correct"

    task_page.check_pg_header() == "TASK TRACKER", "title does not match"
    task_page.check_subheader() == "Instructions", "Sub title is wrong"