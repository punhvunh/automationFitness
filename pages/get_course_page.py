from selenium.webdriver import Keys

from locators.main_page_elements_locators import MainPageElementsLocators
from pages.base_page import BasePage
from locators.get_course_page_elements_locators import GetCoursePageElementsLocators as GetCourseElementsLocators


class GetCoursePage(BasePage):
    get_course_page_locators = GetCourseElementsLocators()
    main_page_locators = MainPageElementsLocators()

    def sees_all_elements_in_get_course_window(self):
        self.element_is_present(self.main_page_locators.LEAVE_A_REQUEST_BUTTON)
        self.scroll_to_element(self.main_page_locators.LEAVE_A_REQUEST_BUTTON_XPATH)
        print("\nScrolls to leave a request button:success")
        self.element_is_visible(self.main_page_locators.LEAVE_A_REQUEST_BUTTON).click()
        self.element_is_visible(self.get_course_page_locators.CLOSE_BUTTON)
        self.element_is_visible(self.get_course_page_locators.NEXT_BUTTON)
        self.element_is_visible(self.get_course_page_locators.ENTER_YOUR_EMAIL_PLACEHOLDER)
        self.element_is_visible(self.get_course_page_locators.GET_COURSE_WINDOW)
        print("Sees all elements in Get course window:success")

    def closes_get_course_window(self):
        self.element_is_present(self.main_page_locators.LEAVE_A_REQUEST_BUTTON)
        self.scroll_to_element(self.main_page_locators.LEAVE_A_REQUEST_BUTTON_XPATH)
        print("\nScrolls to leave a request button:success")
        self.element_is_visible(self.main_page_locators.LEAVE_A_REQUEST_BUTTON).click()
        self.element_is_visible(self.get_course_page_locators.GET_COURSE_WINDOW)
        self.element_is_visible(self.get_course_page_locators.CLOSE_BUTTON).click()
        self.element_is_not_visible(self.get_course_page_locators.GET_COURSE_WINDOW)
        print("Closes get course window:success")
