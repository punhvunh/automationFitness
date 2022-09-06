from generator.genarator import generated_login_data
from locators.login_page_elements_locators import LoginPageElementsLocators
from pages.base_page import BasePage
from locators.main_page_elements_locators import MainPageElementsLocators as MainElementsLocators
from locators.restore_password_page_elements_locators import \
    RestorePasswordPageElementsLocators as RestorePasswordElementsLocators


class RestorePasswordPage(BasePage):
    restore_password_page_locators = RestorePasswordElementsLocators()
    login_page_locators = LoginPageElementsLocators()
    main_page_locators = MainElementsLocators()

    def goes_to_restore_password_page(self):
        self.element_is_visible(self.main_page_locators.LOG_IN_BUTTON).click()
        self.element_is_visible(self.login_page_locators.FORGOT_YOUR_PASSWORD_LINK).click()
        print("\ngoToRestorePasswordPage:success")

    def sees_restore_password_page_elements(self):
        self.element_is_visible(self.login_page_locators.DOMAIN_LOGO)
        self.element_is_visible(self.restore_password_page_locators.RESTORE_HEADER)
        self.element_is_visible(self.restore_password_page_locators.EMAIL_PLACEHOLDER)
        self.element_is_visible(self.restore_password_page_locators.SEND_TO_EMAIL_BUTTON)
        print("\nseesRestorePasswordPageElements:success")

    def sees_error_messages_under_empty_field(self):
        self.element_is_visible(self.restore_password_page_locators.SEND_TO_EMAIL_BUTTON).click()
        self.element_is_visible(self.restore_password_page_locators.FILL_IN_THIS_FIELD_ERROR)
        print("\nseesErrorMessagesUnderEmptyField:success")

    def sees_error_messages_under_field_with_wrong_email(self):
        login_info = next(generated_login_data())
        email = login_info.email
        self.element_is_visible(self.restore_password_page_locators.EMAIL_PLACEHOLDER).send_keys(email)
        self.element_is_visible(self.restore_password_page_locators.SEND_TO_EMAIL_BUTTON).click()
        self.element_is_visible(self.restore_password_page_locators.EMAIL_NOT_FOUND_ERROR)
        print("\nseesErrorMessagesUnderFieldWithWrongEmail:success")

    def sends_new_password_to_correct_email(self):
        input_email = "test@test.test"
        self.element_is_visible(self.restore_password_page_locators.EMAIL_PLACEHOLDER).send_keys(email)
        self.element_is_visible(self.restore_password_page_locators.SEND_TO_EMAIL_BUTTON).click()
        self.element_is_visible(self.restore_password_page_locators.DISABLED_RESEND_BUTTON)
        self.element_is_visible(self.restore_password_page_locators.SUCCESS_HEADER)
        print("\nsendsNewPasswordToCorrectEmail:success")
        return input_email

    def get_output_email(self):
        output_email = self.element_is_present(self.restore_password_page_locators.EMAIL_PLACEHOLDER).get_attribute("value")
        print("\ngetOutPutEmail:success")
        return output_email

