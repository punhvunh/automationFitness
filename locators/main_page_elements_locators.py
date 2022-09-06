from selenium.webdriver.common.by import By


class MainPageElementsLocators:

    URL_TEXT = (By.XPATH, '//div[contains(@class,"row")]//header//div[contains(@class,"box_h1")]'
                          '//a[text()="miloetelo.ru"]')

    SUPPORT_BUTTON_LOGIC = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"btn_wrapper")]'
                                      '//a[contains(@class,"btn_support")][@href="mailto:support@miloetelo.ru"]')

    SILVER_COURSE_NAME = (By.XPATH, '(//div[contains(@class,"row")]//div[contains(@class,"prise_one silver")]'
                                    '//div[contains(@class,"prise_name")]//h3[text()="silver"])[1]')

    SILVER_COURSE_COST = (By.XPATH, '(//div[contains(@class,"row")]//div[contains(@class,"prise_one silver")]'
                                    '//div[contains(@class,"summ")]//span[text()="1 RUB"])[1]')

    SILVER_COURSE_PERIOD = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"prise_one silver")]'
                                      '//span[contains(@class,"name_summ")][.="за 1 день, далее 978 RUB за 3 дня"]')

    GET_BUTTON = (By.XPATH, '//div[contains(@class,"row")]//a[contains(@class,"bubbly-button")][text()="Получить"]')

    LOG_IN_BUTTON = (By.XPATH, '//div[contains(@class,"log_in")]//a')

    LEAVE_A_REQUEST_BUTTON = (By.XPATH, '(//div[contains(@class,"row")]//a[contains(@class,"bubbly-button")]'
                                        '[text()="Оставить заявку"])[3]')
