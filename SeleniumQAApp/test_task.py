import time

from page_objects.login_page import LoginPage
from page_objects.task_page import TaskPage


def test_task(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.perform_login('admin', 'admin123')

    task_page = TaskPage(driver)
    task_page.go_to_task_page()

    assert task_page.current_url == "https://login-app-iota.vercel.app/task", "URL is not correct"

    assert task_page.check_pg_header == "TASK TRACKER", "title does not match"
    assert task_page.check_subheader == "Instructions", "Sub title is wrong"
    assert task_page.check_sub_subheader1 == "- Add -> Add New Tasks", "Sub sub heading does not match"
    assert task_page.check_sub_subheader2 == "- Edit -> Edit existing task", "Sub sub heading does not match"
    assert task_page.check_sub_subheader3 == "- Done -> If task is completed", "Sub sub heading does not match"
    assert task_page.check_sub_subheader4 == "- Delete -> If you want to delete task", "Sub sub heading does not match"

    assert task_page.get_text_from_textbox == "Fill today's time sheet", "the text is not correct"
    assert task_page.get_placeholder_text == "Add your task", "the text is incorrect"

    task_page.enter_text('Test')
    task_page.get_added_text()

    task_page.edit_the_task('Test123')

    task_page.strike_text()

    task_page.delete_the_task()
    task_page.is_deleted_text_displayed()





