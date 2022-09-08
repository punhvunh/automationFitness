import time

from pages.courses_page import CoursesPage


def open_domain(driver):
    main_page = CoursesPage(driver, 'https://miloetelo.ru')
    main_page.open()
    return main_page


class TestCoursesPage:

    def test_courses_page_elements(self, driver):
        courses_page = open_domain(driver)
        courses_page.sees_courses_page_elements()
        time.sleep(5)
