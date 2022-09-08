from selenium.webdriver.common.by import By


class MainPageElementsLocators:

    REQUISITE_FOOTER_XPATH = '//div[contains(@class,"row")]//div[@class="footer_requisites" and normalize-space()="ИП ' \
                             'Чиняев Алексей Евгеньевич, ИНН 650502931989 Краснодарский край, Сочи г, Абрикосовая ул, ' \
                             '17а, 59"] '

    SILVER_COURSE_PERIOD_XPATH = '//div[contains(@class,"row")]//div[contains(@class,"prise_one silver")]//span[' \
                                 'contains(@class,"name_summ")][.="за 1 день, далее 978 RUB за 3 дня"] '

    LEAVE_A_REQUEST_BUTTON_XPATH = '(//div[contains(@class,"row")]//a[contains(@class,"bubbly-button")][text(' \
                                   ')="Оставить заявку"])[3]'

    URL_TEXT = (By.XPATH, '//div[contains(@class,"row")]//header//div[contains(@class,"box_h1")]'
                          '//a[text()="miloetelo.ru"]')

    SUPPORT_BUTTON_LOGIC = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"btn_wrapper")]'
                                      '//a[contains(@class,"btn_support")][@href="mailto:support@miloetelo.ru"]')

    SILVER_COURSE_NAME = (By.XPATH, '(//div[contains(@class,"row")]//div[contains(@class,"prise_one silver")]'
                                    '//div[contains(@class,"prise_name")]//h3[text()="silver"])[1]')

    SILVER_COURSE_COST = (By.XPATH, '(//div[contains(@class,"row")]//div[contains(@class,"prise_one silver")]'
                                    '//div[contains(@class,"summ")]//span[text()="1 RUB"])[1]')

    SILVER_COURSE_PERIOD = (By.XPATH, SILVER_COURSE_PERIOD_XPATH)

    GET_BUTTON = (By.XPATH, '//div[contains(@class,"row")]//a[contains(@class,"bubbly-button")][text()="Получить"]')

    LOG_IN_BUTTON = (By.XPATH, '//div[contains(@class,"log_in")]//a')

    LEAVE_A_REQUEST_BUTTON = (By.XPATH, '(//div[contains(@class,"row")]//a[contains(@class,"bubbly-button")]'
                                        '[text()="Оставить заявку"])[3]')

    REQUISITE_FOOTER = (By.XPATH, REQUISITE_FOOTER_XPATH)

    PRIVATE_POLICY_LINK = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"foot_link")]'
                                      '//a[text()="Политика конфиденциальности"]')

    OFFER_AGREEMENT_LINK = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"foot_link")]'
                                      '//a[text()="Договор оферты"]')

    HOW_TO_UNSUBSCRIBE_LINK = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"foot_link")]'
                                         '//a[text()="Как отписаться"]')


