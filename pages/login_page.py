from generator.genarator import generated_login_data
from pages.base_page import BasePage
from locators.main_page_elements_locators import MainPageElementsLocators as MainElementsLocators
from locators.login_page_elements_locators import LoginPageElementsLocators as LoginElementsLocators


class LoginPage(BasePage):
    login_page_locators = LoginElementsLocators()
    main_page_locators = MainElementsLocators()

    def sees_login_page_elements(self):
        self.element_is_visible(self.login_page_locators.DOMAIN_LOGO)
        self.element_is_visible(self.login_page_locators.LOGIN_HEADER)
        self.element_is_visible(self.login_page_locators.EMAIL_PLACEHOLDER)
        self.element_is_visible(self.login_page_locators.PASSWORD_PLACEHOLDER)
        self.element_is_visible(self.login_page_locators.LOG_IN_BUTTON)
        self.element_is_visible(self.login_page_locators.FORGOT_YOUR_PASSWORD_LINK)
        print("\nseesLoginPageElements:success")

    def clicks_on_button_log_in_at_main_page(self):
        self.element_is_visible(self.main_page_locators.LOG_IN_BUTTON).click()
        print("\nclicksOnButtonLogInAtMainPage:success")

    def fills_empty_fields_with_right_data(self):
        email = 'test@test.test'
        password = '123456'
        self.element_is_visible(self.login_page_locators.EMAIL_PLACEHOLDER).send_keys(email)
        self.element_is_visible(self.login_page_locators.PASSWORD_PLACEHOLDER).send_keys(password)
        print("fillsEmptyFields:success")

    def clicks_on_button_log_in(self):
        self.element_is_visible(self.login_page_locators.LOG_IN_BUTTON).click()
        print("clicksOnButtonLogIn:success")

    def does_not_see_error_messages_under_fields(self):
        self.element_is_not_visible(self.login_page_locators.ENTER_EMAIL_ERROR)
        self.element_is_not_visible(self.login_page_locators.ENTER_PASSWORD_ERROR)
        print("doesNotSeeErrorMessagesUnderFields:success")

    def sees_error_messages_under_fields(self):
        self.element_is_visible(self.login_page_locators.ENTER_EMAIL_ERROR)
        self.element_is_visible(self.login_page_locators.ENTER_PASSWORD_ERROR)
        print("seesErrorMessagesUnderFields:success")

    def fills_empty_fields_with_wrong_data_and_click_on_button_log_in(self):
        login_info = next(generated_login_data())
        email = login_info.email
        password = login_info.password
        self.element_is_visible(self.login_page_locators.EMAIL_PLACEHOLDER).send_keys(email)
        self.element_is_visible(self.login_page_locators.PASSWORD_PLACEHOLDER).send_keys(password)
        self.clicks_on_button_log_in()
        self.element_is_visible(self.login_page_locators.WRONG_EMAIL_OR_PASSWORD_ERROR)
        print("fillsEmptyFieldsWithWrongDataAndClickOnButtonLogIn:success")
