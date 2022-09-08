from pages.base_page import BasePage
from locators.main_page_elements_locators import MainPageElementsLocators as MainElementsLocators
from locators.privacy_policy_page_elements_locators import \
    PrivatePolicyPageElementsLocators as PrivatePolicyElementsLocators
from locators.login_page_elements_locators import LoginPageElementsLocators as LoginElementsLocators


class PrivacyPolicyPage(BasePage):
    main_page_locators = MainElementsLocators()
    login_page_locators = LoginElementsLocators()
    private_policy_page_locators = PrivatePolicyElementsLocators()

    def sees_privacy_policy_elements(self):
        self.element_is_present(self.main_page_locators.REQUISITE_FOOTER)
        self.scroll_to_element(self.main_page_locators.REQUISITE_FOOTER_XPATH)
        print("\nScrolls to requisite footer: success")
        self.element_is_visible(self.main_page_locators.PRIVATE_POLICY_LINK).click()
        self.switch_to_next_tab()
        self.element_is_visible(self.login_page_locators.DOMAIN_LOGO)
        self.element_is_visible(self.private_policy_page_locators.SUPPORT_MAIL_NUMBER_ONE)
        self.element_is_visible(self.private_policy_page_locators.SUPPORT_MAIL_NUMBER_TWO)
        self.element_is_present(self.private_policy_page_locators.SUPPORT_MAIL_NUMBER_THREE)
        self.scroll_to_element(self.private_policy_page_locators.SUPPORT_MAIL_NUMBER_THREE_XPATH)
        print("Scrolls to support mail number three: success")
        self.element_is_visible(self.private_policy_page_locators.PRIVACY_POLICY_LINK)
        self.element_is_visible(self.private_policy_page_locators.SUPPORT_MAIL_NUMBER_THREE)
        print("Sees privacy policy elements: success")


