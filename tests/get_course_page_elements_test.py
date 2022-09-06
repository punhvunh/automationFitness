import time

from pages.get_course_page import GetCoursePage


def open_domain(driver):
    main_page = GetCoursePage(driver, 'https://miloetelo.ru')
    main_page.open()
    return main_page


class TestGetCoursePageElements:

    def test_sees_all_elements_in_get_course_window(self, driver):
        get_course_page = open_domain(driver)
        get_course_page.sees_all_elements_in_get_course_window()
        time.sleep(5)

    def test_close_get_course_window(self, driver):
        get_course_page = open_domain(driver)
        get_course_page.closes_get_course_window()
        time.sleep(5)
