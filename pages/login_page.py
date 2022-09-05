from generator.genarator import generated_login_data
from pages.base_page import BasePage
from locators.main_page_elements_locators import MainPageElementsLocators as MainElementsLocators
from locators.login_page_elements_locators import LoginPageElementsLocators as LoginElementsLocators


class LoginPage(BasePage):
    login_page_locators = LoginElementsLocators()
    main_page_locators = MainElementsLocators()

    def sees_login_page_elements(self):
        self.element_is_visible(self.login_page_locators.DOMAIN_LOGO)
        self.element_is_visible(self.login_page_locators.HEADER_LOGIN)
        self.element_is_visible(self.login_page_locators.PLACEHOLDER_EMAIL)
        self.element_is_visible(self.login_page_locators.PLACEHOLDER_PASSWORD)
        self.element_is_visible(self.login_page_locators.BUTTON_LOG_IN)
        self.element_is_visible(self.login_page_locators.LINK_FORGOT_YOUR_PASSWORD)

    def clicks_on_button_log_in_at_main_page(self):
        self.element_is_visible(self.main_page_locators.LOG_IN_BUTTON).click()
        print("\nclickOnButtonLogInAtMainPage:success")

    def fills_empty_fields_with_right_data(self):
        email = 'test@test.test'
        password = '123456'
        self.element_is_visible(self.login_page_locators.PLACEHOLDER_EMAIL).send_keys(email)
        self.element_is_visible(self.login_page_locators.PLACEHOLDER_PASSWORD).send_keys(password)
        print("fillsEmptyFields:success")

    def clicks_on_button_log_in(self):
        self.element_is_visible(self.login_page_locators.BUTTON_LOG_IN).click()
        print("clicksOnButtonLogIn:success")

    def does_not_error_messages_under_fields(self):
        self.element_is_not_visible(self.login_page_locators.ERROR_UNDER_FIELD_EMAIL)
        self.element_is_not_visible(self.login_page_locators.ERROR_UNDER_FIELD_PASSWORD)
        print("doesNotSeeErrorMessagesUnderFields:success")

    def sees_error_messages_under_fields(self):
        self.element_is_visible(self.login_page_locators.ERROR_UNDER_FIELD_EMAIL)
        self.element_is_visible(self.login_page_locators.ERROR_UNDER_FIELD_PASSWORD)
        print("seesErrorMessagesUnderFields:success")

    def fills_empty_fields_with_wrong_data_and_click_on_button_log_in(self):
        login_info = next(generated_login_data())
        email = login_info.email
        password = login_info.password
        self.element_is_visible(self.login_page_locators.PLACEHOLDER_EMAIL).send_keys(email)
        self.element_is_visible(self.login_page_locators.PLACEHOLDER_PASSWORD).send_keys(password)
        self.clicks_on_button_log_in()
        self.element_is_visible(self.login_page_locators.GENERAL_ERROR_UNDER_FIELD_PASSWORD)
        print("fillsEmptyFieldsWithWrongDataAndClickOnButtonLogIn:success")
