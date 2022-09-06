from selenium.webdriver.common.by import By


class LoginPageElementsLocators:

    DOMAIN_LOGO = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"text-center")]'
                             '//a[contains(.,"miloetelo.ru")]')

    LOGIN_HEADER = (By.XPATH, '//div[contains(@class,"row")]//a[text()="Войти"]')

    EMAIL_PLACEHOLDER = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"input_grop")]'
                                   '//input[@placeholder="E-mail"]')

    PASSWORD_PLACEHOLDER = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"input_grop")]'
                                      '//input[@placeholder="Пароль"]')

    LOG_IN_BUTTON = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"col-12")]//button[text()="Войти"]')

    ENTER_EMAIL_ERROR = (By.XPATH, '//div[contains(@class,"row")]'
                                   '//div[contains(@class,"input_grop error ")]//p[text()="*Введите e-mail"]')

    ENTER_PASSWORD_ERROR = (By.XPATH, '//div[contains(@class,"row")]'
                                      '//div[contains(@class,"input_grop error")]//p[text()="*Введите пароль"]')

    WRONG_EMAIL_OR_PASSWORD_ERROR = (By.XPATH, '//div[contains(@class,"row")]'
                                               '//div[contains(@class,"input_grop error")]'
                                               '//p[text()="*Неверный e-mail или пароль"]')

    FORGOT_YOUR_PASSWORD_LINK = (By.XPATH, '//div[contains(@class,"row")]//a[text()="Забыли пароль"]')
