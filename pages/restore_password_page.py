from pages.base_page import BasePage
from locators.restore_password_page_elements_locators import \
    RestorePasswordPageElementsLocators as RestorePasswordElementsLocators


class MainPage(BasePage):
    restore_password_page_locators = RestorePasswordElementsLocators()
