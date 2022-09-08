from pages.base_page import BasePage
from locators.main_page_elements_locators import MainPageElementsLocators as MainElementsLocators


class MainPage(BasePage):
    main_page_locators = MainElementsLocators()

    def sees_url(self):
        self.element_is_visible(self.main_page_locators.URL_TEXT)
        print("\nSees url: success")

    def sees_logic_of_support_button(self):
        self.element_is_visible(self.main_page_locators.SUPPORT_BUTTON_LOGIC)
        print("\nSees logic of support button: success")

    def sees_cost_and_period_of_silver_course(self):
        self.element_is_present(self.main_page_locators.SILVER_COURSE_PERIOD)
        self.scroll_to_element(self.main_page_locators.SILVER_COURSE_PERIOD_XPATH)
        print("\nScrolls to silver course period: success")
        self.element_is_visible(self.main_page_locators.SILVER_COURSE_NAME)
        self.element_is_visible(self.main_page_locators.SILVER_COURSE_COST)
        self.element_is_visible(self.main_page_locators.SILVER_COURSE_PERIOD)
        print("Sees cost and period of silver course: success")

    def sees_requisites_and_links(self):
        self.element_is_present(self.main_page_locators.REQUISITE_FOOTER)
        self.scroll_to_element(self.main_page_locators.REQUISITE_FOOTER_XPATH)
        print("\nScrolls to requisite footer: success")
        self.element_is_visible(self.main_page_locators.REQUISITE_FOOTER)
        self.element_is_visible(self.main_page_locators.REQUISITE_FOOTER)
        self.element_is_visible(self.main_page_locators.PRIVATE_POLICY_LINK)
        self.element_is_visible(self.main_page_locators.OFFER_AGREEMENT_LINK)
        self.element_is_visible(self.main_page_locators.HOW_TO_UNSUBSCRIBE_LINK)
        print("Sees requisites and links: success")
