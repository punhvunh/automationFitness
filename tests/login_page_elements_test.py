import time

from pages.login_page import LoginPage


def open_domain(driver):
    main_page = LoginPage(driver, 'https://miloetelo.ru')
    main_page.open()
    return main_page


class TestLoginPage:

    def test_login_page_elements(self, driver):
        login_page = open_domain(driver)
        login_page.clicks_on_button_log_in_at_main_page()
        login_page.sees_login_page_elements()
        time.sleep(5)

    def test_login_page_with_correct_data(self, driver):
        login_page = open_domain(driver)
        login_page.clicks_on_button_log_in_at_main_page()
        login_page.fills_empty_fields_with_correct_data()
        login_page.clicks_on_button_log_in()
        time.sleep(5)

    def test_login_page_with_empty_fields(self, driver):
        login_page = open_domain(driver)
        login_page.clicks_on_button_log_in_at_main_page()
        login_page.does_not_see_error_messages_under_fields()
        login_page.clicks_on_button_log_in()
        login_page.sees_error_messages_under_fields()
        time.sleep(5)

    def test_login_page_with_wrong_data(self, driver):
        login_page = open_domain(driver)
        login_page.clicks_on_button_log_in_at_main_page()
        input_email, input_password = login_page.fills_empty_fields_with_wrong_data_and_click_on_button_log_in()
        output_email, output_password = login_page.get_output_email_and_output_password()
        assert input_email == output_email
        assert input_password == output_password
        time.sleep(5)
