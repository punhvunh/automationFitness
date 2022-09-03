import time

from pages.get_course_page import GetCoursePage


def open_domain(driver):
    get_course_page = GetCoursePage(driver, 'https://miloetelo.ru')
    get_course_page.open()
    return get_course_page


class TestMainPageElements:

    def test_sees_all_elements_in_get_course_window(self, driver):
        get_course_page = open_domain(driver)
        get_course_page.sees_all_elements_in_get_course_window()
        time.sleep(5)
