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
        print("\nSees login page elements: success")

    def clicks_on_button_log_in_at_main_page(self):
        self.element_is_visible(self.main_page_locators.LOG_IN_BUTTON).click()
        print("\nClicks on button log in at main page: success")

    def fills_empty_fields_with_correct_data(self):
        email = 'test@test.test'
        password = '123456'
        self.element_is_visible(self.login_page_locators.EMAIL_PLACEHOLDER).send_keys(email)
        self.element_is_visible(self.login_page_locators.PASSWORD_PLACEHOLDER).send_keys(password)
        print("Fills empty fields: success")

    def clicks_on_button_log_in(self):
        self.element_is_visible(self.login_page_locators.LOG_IN_BUTTON).click()
        print("Clicks on button log in: success")

    def does_not_see_error_messages_under_fields(self):
        self.element_is_not_visible(self.login_page_locators.ENTER_EMAIL_ERROR)
        self.element_is_not_visible(self.login_page_locators.ENTER_PASSWORD_ERROR)
        print("Does not see error messages under fields: success")

    def sees_error_messages_under_fields(self):
        self.element_is_visible(self.login_page_locators.ENTER_EMAIL_ERROR)
        self.element_is_visible(self.login_page_locators.ENTER_PASSWORD_ERROR)
        print("Sees error messages under fields: success")

    def fills_empty_fields_with_wrong_data_and_click_on_button_log_in(self):
        login_info = next(generated_login_data())
        input_email = login_info.email
        input_password = login_info.password
        self.element_is_visible(self.login_page_locators.EMAIL_PLACEHOLDER).send_keys(input_email)
        self.element_is_visible(self.login_page_locators.PASSWORD_PLACEHOLDER).send_keys(input_password)
        self.clicks_on_button_log_in()
        self.element_is_visible(self.login_page_locators.WRONG_EMAIL_OR_PASSWORD_ERROR)
        print("Fills empty fields with wrong data and click on button log in: success")
        return input_email, input_password

    def get_output_email_and_output_password(self):
        output_email = self.element_is_present(self.login_page_locators.EMAIL_PLACEHOLDER).get_attribute("value")
        output_password = self.element_is_present(self.login_page_locators.PASSWORD_PLACEHOLDER).get_attribute("value")
        print("Get output email and output password: success")
        return output_email, output_password
