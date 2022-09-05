from selenium.webdriver.common.by import By


class LoginPageElementsLocators:
    DOMAIN_LOGO = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"text-center")]'
                             '//a[contains(.,"miloetelo.ru")]')

    HEADER_LOGIN = (By.XPATH, '//div[contains(@class,"row")]//a[text()="Войти"]')

    PLACEHOLDER_EMAIL = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"input_grop")]'
                                   '//input[@placeholder="E-mail"]')

    PLACEHOLDER_PASSWORD = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"input_grop")]'
                                      '//input[@placeholder="Пароль"]')

    BUTTON_LOG_IN = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"col-12")]//button[text()="Войти"]')

    ERROR_UNDER_FIELD_EMAIL = (By.XPATH, '//div[contains(@class,"row")]'
                                         '//div[contains(@class,"input_grop error ")]//p[text()="*Введите e-mail"]')

    ERROR_UNDER_FIELD_PASSWORD = (By.XPATH, '//div[contains(@class,"row")]'
                                            '//div[contains(@class,"input_grop error")]//p[text()="*Введите пароль"]')

    GENERAL_ERROR_UNDER_FIELD_PASSWORD = (By.XPATH, '//div[contains(@class,"row")]'
                                                    '//div[contains(@class,"input_grop error")]'
                                                    '//p[text()="*Неверный e-mail или пароль"]')

    LINK_FORGOT_YOUR_PASSWORD = (By.XPATH, '//div[contains(@class,"row")]//a[text()="Забыли пароль"]')
