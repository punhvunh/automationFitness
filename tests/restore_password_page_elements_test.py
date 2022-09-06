import time

from pages.restore_password_page import RestorePasswordPage


def open_domain(driver):
    main_page = RestorePasswordPage(driver, 'https://miloetelo.ru')
    main_page.open()
    return main_page


class TestRestorePasswordPageElements:

    def test_restore_password_page_elements(self, driver):
        restore_password_page = open_domain(driver)
        restore_password_page.goes_to_restore_password_page()
        restore_password_page.sees_restore_password_page_elements()
        time.sleep(5)

    def test_restore_password_page_with_empty_fields(self, driver):
        restore_password_page = open_domain(driver)
        restore_password_page.goes_to_restore_password_page()
        restore_password_page.sees_error_messages_under_empty_field()
        time.sleep(5)

    def test_restore_password_page_with_wrong_email(self, driver):
        restore_password_page = open_domain(driver)
        restore_password_page.goes_to_restore_password_page()
        restore_password_page.sees_error_messages_under_field_with_wrong_email()
        time.sleep(5)

    def test_restore_password_page_with_correct_email(self, driver):
        restore_password_page = open_domain(driver)
        restore_password_page.goes_to_restore_password_page()
        restore_password_page.sends_new_password_to_correct_email()
        time.sleep(5)
