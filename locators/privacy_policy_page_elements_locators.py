from selenium.webdriver.common.by import By


class PrivatePolicyPageElementsLocators:

    SUPPORT_MAIL_NUMBER_THREE_XPATH = '(//div[contains(@class,"row")]//p//a[@href="mailto:support@miloetelo.ru"])[3]'

    SUPPORT_MAIL_NUMBER_ONE = (By.XPATH, '(//div[contains(@class,"row")]//p//a[@href="mailto:support@miloetelo.ru"])[1]')

    SUPPORT_MAIL_NUMBER_TWO = (By.XPATH, '(//div[contains(@class,"row")]//p//a[@href="mailto:support@miloetelo.ru"])[2]')

    SUPPORT_MAIL_NUMBER_THREE = (By.XPATH, SUPPORT_MAIL_NUMBER_THREE_XPATH)

    PRIVACY_POLICY_LINK = (By.XPATH, '//div[contains(@class,"row")]//p//a[@href="https://miloetelo.ru/about/privacy/"]')
