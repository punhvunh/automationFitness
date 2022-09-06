import time

from pages.main_page import MainPage


def open_domain(driver):
    main_page = MainPage(driver, 'https://miloetelo.ru')
    main_page.open()
    return main_page


class TestMainPageElements:

    def test_sees_url(self, driver):
        main_page = open_domain(driver)
        main_page.sees_url()
        time.sleep(5)

    def test_sees_logic_of_support_button(self, driver):
        main_page = open_domain(driver)
        main_page.sees_logic_of_support_button()
        time.sleep(5)

    def test_sees_cost_and_period_of_silver_course(self, driver):
        main_page = open_domain(driver)
        main_page.sees_cost_and_period_of_silver_course()
        time.sleep(5)

