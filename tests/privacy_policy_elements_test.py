import time

from pages.privacy_policy_page import PrivacyPolicyPage


def open_domain(driver):
    main_page = PrivacyPolicyPage(driver, 'https://miloetelo.ru')
    main_page.open()
    return main_page


class TestPrivatePolicyPageElements:

    def test_sees_privacy_policy_elements(self, driver):
        private_policy_page = open_domain(driver)
        private_policy_page.sees_privacy_policy_elements()
        time.sleep(5)
