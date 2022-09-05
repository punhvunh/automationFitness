from selenium.webdriver.common.by import By


class GetCoursePageElementsLocators:
    CLOSE_BUTTON = (By.XPATH, '//div[contains(@class,"modal-content")]//button[contains(@class,"close")]//span')

    NEXT_BUTTON = (By.XPATH, '//div[contains(@class,"modal-content")]//button[contains(@class,"bubbly-button")]'
                             '[text()="Далее"]')

    ENTER_YOUR_EMAIL_PLACEHOLDER = (By.XPATH, '//div[contains(@class,"modal-content")]'
                                              '//input[@placeholder="Введите ваш email"]')

    GET_COURSE_WINDOW = (By.XPATH, '//div[contains(@class,"modal-content")]//div[contains(@class,"modal-body")]' 
                                   '//h4[contains(.,"Получите фитнес-курса + ПП меню")]')
