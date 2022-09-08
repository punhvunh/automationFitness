from pages.base_page import BasePage
from locators.courses_page_elements_locators import CoursesPageElementsLocators as CoursesElementsLocators
from locators.main_page_elements_locators import MainPageElementsLocators as MainElementsLocators
from locators.login_page_elements_locators import LoginPageElementsLocators as LoginElementsLocators


class CoursesPage(BasePage):
    courses_page_locators = CoursesElementsLocators()
    main_page_locators = MainElementsLocators()
    login_page_locators = LoginElementsLocators()

    def sees_courses_page_elements(self):
        self.element_is_visible(self.main_page_locators.LOG_IN_BUTTON).click()
        email = 'test@test.test'
        password = '123456'
        self.element_is_visible(self.login_page_locators.EMAIL_PLACEHOLDER).send_keys(email)
        self.element_is_visible(self.login_page_locators.PASSWORD_PLACEHOLDER).send_keys(password)
        self.element_is_visible(self.login_page_locators.LOG_IN_BUTTON).click()
        self.element_is_visible(self.login_page_locators.DOMAIN_LOGO)
        self.element_is_visible(self.courses_page_locators.HAMBURGER_BUTTON)
        self.element_is_visible(self.courses_page_locators.SUPER_BOOTY_COURSE)
        self.element_is_visible(self.courses_page_locators.FITNESS_DANCE_COURSE)
        self.element_is_visible(self.courses_page_locators.ON_TH_TWINE_COURSE)
        self.element_is_visible(self.courses_page_locators.FACE_FITNESS_COURSE)
        self.element_is_visible(self.courses_page_locators.POSTURE_COURSE)
        self.element_is_visible(self.courses_page_locators.BURN_FAT_NEW_COURSE)
        self.element_is_visible(self.courses_page_locators.BOXING_COURSE)
        self.element_is_visible(self.courses_page_locators.WILDBERRIES_COURSE)
        self.element_is_visible(self.courses_page_locators.WALKING_COURSE)
        self.element_is_visible(self.courses_page_locators.MEDITATION_COURSE)
        self.element_is_visible(self.courses_page_locators.FINANCIAL_LITERACY_COURSE)
        self.element_is_visible(self.courses_page_locators.SUPER_BOOTY_DESCRIPTION)
        self.element_is_visible(self.courses_page_locators.FITNESS_DANCE_DESCRIPTION)
        self.element_is_visible(self.courses_page_locators.ON_TH_TWINE_DESCRIPTION)
        self.element_is_visible(self.courses_page_locators.FACE_FITNESS_DESCRIPTION)
        self.element_is_visible(self.courses_page_locators.POSTURE_DESCRIPTION)
        self.element_is_visible(self.courses_page_locators.BURN_FAT_NEW_DESCRIPTION)
        self.element_is_visible(self.courses_page_locators.BOXING_DESCRIPTION)
        self.element_is_present(self.courses_page_locators.WILDBERRIES_DESCRIPTION)
        self.element_is_visible(self.courses_page_locators.WALKING_DESCRIPTION)
        self.element_is_visible(self.courses_page_locators.MEDITATION_DESCRIPTION)
        self.element_is_visible(self.courses_page_locators.FINANCIAL_LITERACY_DESCRIPTION)
        print("\nseesCoursesPageElements:success")
