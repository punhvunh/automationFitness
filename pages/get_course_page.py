from locators.main_page_elements_locators import MainPageElementsLocators
from pages.base_page import BasePage
from locators.get_course_page_elements_locators import GetCoursePageElementsLocators as GetCourseElementsLocators


class GetCoursePage(BasePage):
    get_course_page_locators = GetCourseElementsLocators()
    main_page_locators = MainPageElementsLocators()

    def sees_all_elements_in_get_course_window(self):
        self.element_is_visible(self.main_page_locators.GET_BUTTON).click()
        print("\nclicksGetButton:success")
        self.element_is_visible(self.main_page_locators.LEAVE_A_REQUEST_BUTTON).click()
        print("\nclicksLeaveARequestButton:success")
        self.element_is_visible(self.get_course_page_locators.CLOSE_BUTTON)
        print("\nseesCloseButton:success")
        self.element_is_visible(self.get_course_page_locators.NEXT_BUTTON)
        print("\nseesNextButton:success")
        self.element_is_visible(self.get_course_page_locators.ENTER_YOUR_EMAIL_PLACEHOLDER)
        print("\nseesEnterYourEmailPlaceholder:success")
        # self.element_is_visible(self.get_course_page_locators.GET_COURSE_WINDOW)
        # print("\nseesGetCourseWindow:success")

    def close_get_course_window(self):
        self.element_is_visible(self.main_page_locators.GET_BUTTON).click()
        print("\nclicksGetButton:success")
        self.element_is_visible(self.main_page_locators.LEAVE_A_REQUEST_BUTTON).click()
        print("\nclicksLeaveARequestButton:success")
        self.element_is_visible(self.get_course_page_locators.CLOSE_BUTTON).click()
        print("\nclicksCloseButton:success")