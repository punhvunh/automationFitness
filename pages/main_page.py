from pages.base_page import BasePage
from locators.main_page_elements_locators import MainPageElementsLocators as MainElementsLocators


class MainPage(BasePage):
    locators = MainElementsLocators()

    def sees_url(self):
        self.element_is_visible(self.locators.URL_TEXT)
        print("\nseesUrl:success")

    def sees_logic_of_support_button(self):
        self.element_is_visible(self.locators.SUPPORT_BUTTON_LOGIC)
        print("\nseesLogicOfSupportButton:success")

    def sees_name_of_silver_course(self):
        self.element_are_visible(self.locators.SILVER_COURSE_NAME)
        print("\nseesNameOfSilverCourse:success")

    def sees_cost_of_silver_course(self):
        self.element_are_visible(self.locators.SILVER_COURSE_COST)
        print("\nseesCostOfSilverCourse:success")

    def sees_period_of_silver_course(self):
        self.element_are_visible(self.locators.SILVER_COURSE_COST)
        print("\nseesPeriodOfSilverCourse:success")

    def go_to_silver_course_name(self):
        self.go_to_element(self.locators.SILVER_COURSE_NAME)
        print("\ngoToSilverCourseName:success")
