import time

from pages.offer_agreement_page import OfferAgreementPage


def open_domain(driver):
    main_page = OfferAgreementPage(driver, 'https://miloetelo.ru')
    main_page.open()
    return main_page


class TestOfferAgreementPageElements:

    def test_sees_offer_agreement_elements(self, driver):
        offer_agreement_page = open_domain(driver)
        offer_agreement_page.sees_offer_agreement_elements()
        time.sleep(5)
