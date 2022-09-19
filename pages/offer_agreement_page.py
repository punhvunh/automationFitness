from pages.base_page import BasePage
from locators.main_page_elements_locators import MainPageElementsLocators as MainElementsLocators
from locators.login_page_elements_locators import LoginPageElementsLocators as LoginElementsLocators
from locators.offer_agreement_page_elements_locators import OfferAgreementPageElementsLocators


class OfferAgreementPage(BasePage):
    main_page_locators = MainElementsLocators()
    login_page_locators = LoginElementsLocators()
    offer_agreement_page_locators = OfferAgreementPageElementsLocators()

    def sees_offer_agreement_elements(self):
        self.element_is_present(self.main_page_locators.REQUISITE_FOOTER)
        self.scroll_to_element(self.main_page_locators.REQUISITE_FOOTER_XPATH)
        print("\nScrolls to requisite footer: success")
        self.element_is_visible(self.main_page_locators.OFFER_AGREEMENT_LINK).click()
        self.switch_to_next_tab()
        self.element_is_visible(self.login_page_locators.DOMAIN_LOGO)
        self.element_is_visible(self.offer_agreement_page_locators.IP_AND_NUMBER_ONE)
        self.element_is_visible(self.offer_agreement_page_locators.OFFER_AGREEMENT_LINK_NUMBER_ONE)
        self.element_is_visible(self.offer_agreement_page_locators.MAIN_DOMAIN_NUMBER_ONE)
        self.element_is_visible(self.offer_agreement_page_locators.MAIN_DOMAIN_NUMBER_TWO)
        self.element_is_visible(self.offer_agreement_page_locators.IP_AND_NUMBER_TWO)
        self.scroll_to_element(self.offer_agreement_page_locators.OFFER_AGREEMENT_LINK_NUMBER_TWO_XPATH)
        print("Scrolls to offer agreement link nuber two: success")
        self.element_is_visible(self.offer_agreement_page_locators.OFFER_AGREEMENT_LINK_NUMBER_TWO)
        self.element_is_visible(self.offer_agreement_page_locators.SUBSCRIPTION_LINK)
        self.element_is_visible(self.offer_agreement_page_locators.SUPPORT_LINK)
        self.scroll_to_element(self.offer_agreement_page_locators.CART_LINK_XPATH)
        print("Scrolls to cart link: success")
        self.element_is_visible(self.offer_agreement_page_locators.CART_LINK)
        self.scroll_to_element(self.offer_agreement_page_locators.SUPPORT_EMAIL_XPATH)
        print("Scrolls to support email: success")
        self.element_is_visible(self.offer_agreement_page_locators.SUPPORT_EMAIL)
        self.element_is_visible(self.offer_agreement_page_locators.IP_AND_NUMBER_AND_ADDRESS)

