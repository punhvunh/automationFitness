from selenium.webdriver.common.by import By


class RestorePasswordPageElementsLocators:
    SEND_TO_EMAIL_BUTTON = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"butt_foot")]'
                                      '//button[contains(.,"Отправить на E-mail")]')

    EMAIL_PLACEHOLDER = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"input_grop")]'
                                   '//input[@placeholder="E-mail"]')

    FILL_IN_THIS_FIELD_ERROR = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"input_grop error")]'
                                          '//p[text()="* Заполните данное поле"]')

    EMAIL_NOT_FOUND_ERROR = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"input_grop error")]'
                                       '//p[text()="* E-mail не найден"]')

    RESTORE_HEADER = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"input_grop")]'
                                '[contains(.,"Для восстановления пароля укажите почту, на которую регистрировались. На эту почту мы вышлем Вам текущие доступы к аккаунту.")]')

    SUCCESS_HEADER = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"input_grop-result")]'
                                '//p[contains(.,"Письмо с доступами отправлено на E-mail")]')

    DISABLED_RESEND_BUTTON = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"butt_foot")]'
                                        '//button[@disabled="disabled"][contains(.,"Повторная отправка через")]')
