from selenium.webdriver.common.by import By


class OfferAgreementPageElementsLocators:
    OFFER_AGREEMENT_LINK_NUMBER_TWO_XPATH = '(//div[contains(@class,"row")]//a[' \
                                            '@href="https://miloetelo.ru/about/oferta/"])[2] '

    CART_LINK_XPATH = '//div[contains(@class,"row")]//a[@href="https://miloetelo.ru/my/cart/"]'

    SUPPORT_EMAIL_XPATH = '//div[contains(@class,"row")]//a[@href="mailto:support@miloetelo.ru"][text(' \
                          ')="support@miloetelo.ru"]'

    OFFER_AGREEMENT_LINK_NUMBER_ONE = (
        By.XPATH, '(//div[contains(@class,"row")]//a[@href="https://miloetelo.ru/about/oferta/"])[1]')

    OFFER_AGREEMENT_LINK_NUMBER_TWO = (
        By.XPATH, OFFER_AGREEMENT_LINK_NUMBER_TWO_XPATH)

    MAIN_DOMAIN_NUMBER_ONE = (
        By.XPATH, '(//div[contains(@class,"row")]//a[@href="https://miloetelo.ru"])[1]')

    MAIN_DOMAIN_NUMBER_TWO = (
        By.XPATH, '(//div[contains(@class,"row")]//a[@href="https://miloetelo.ru"])[2]')

    SUPPORT_LINK = (By.XPATH, '//div[contains(@class,"row")]//a[@href="https://miloetelo.ru/about/support/"]')

    SUBSCRIPTION_LINK = (By.XPATH, '//div[contains(@class,"row")]//a[@href="https://miloetelo.ru/my/subscription/"]')

    CART_LINK = (By.XPATH, CART_LINK_XPATH)

    SUPPORT_EMAIL = (By.XPATH, SUPPORT_EMAIL_XPATH)

    IP_AND_NUMBER_ONE = (By.XPATH,
                         '//div[contains(@class,"row")]//div[contains(@class,"col-12 ")]//div[contains(@class,'
                         '"col-12")][contains(normalize-space(),"Настоящая Публичная Оферта (далее по тексту – '
                         '«Оферта») является официальным публичным предложением ИП Чиняев Алексей Евгеньевич, '
                         'ИНН 650502931989")]')

    IP_AND_NUMBER_TWO = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"col-12 ")]//div[contains('
                                   '@class,"col-12")][contains(normalize-space(),"Исполнитель – ИП Чиняев Алексей '
                                   'Евгеньевич, ИНН 650502931989")]')

    IP_AND_NUMBER_AND_ADDRESS = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"col-12 ")][contains('
                                           'normalize-space()," 9. Реквизиты Исполнителя: ИП Чиняев Алексей '
                                           'Евгеньевич ИНН 650502931989 Российская Федерация, Краснодарский край, '
                                           'Сочи г, Абрикосовая ул, 17а, 59")]')
