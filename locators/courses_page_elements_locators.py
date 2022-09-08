from selenium.webdriver.common.by import By


class CoursesPageElementsLocators:

    HAMBURGER_BUTTON = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"hamburger")]')

    SUPER_BOOTY_COURSE = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"course_desc")]'
                                    '//h4[text()="Суперпопа"]')

    FITNESS_DANCE_COURSE = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"course_desc")]'
                                      '//h4[text()="Фитнес танцы"]')

    ON_TH_TWINE_COURSE = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"course_desc")]'
                                    '//h4[text()="На шпагат"]')

    FACE_FITNESS_COURSE = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"course_desc")]'
                                     '//h4[text()="Фейсфитнес"]')

    POSTURE_COURSE = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"course_desc")]'
                                '//h4[text()="Осанка"]')

    BURN_FAT_NEW_COURSE = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"course_desc")]'
                                     '//h4[text()="ЖгиЖир NEW"]')

    BOXING_COURSE = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"course_desc")]'
                               '//h4[text()="Boxing"]')

    WILDBERRIES_COURSE = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"course_desc")]'
                                    '//h4[text()="Wildberries"]')

    WALKING_COURSE = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"course_desc")]'
                                '//h4[text()="Ходьба"]')

    MEDITATION_COURSE = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"course_desc")]'
                                   '//h4[text()="Медитация"]')

    FINANCIAL_LITERACY_COURSE = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"course_desc")]'
                                           '//h4[text()="Финансовая грамотность"]')

    SUPER_BOOTY_DESCRIPTION = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"course_desc")]'
                                         '//p[text()="Прорабатываем ягодицы и общий тонус тела"]')

    FITNESS_DANCE_DESCRIPTION = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"course_desc")]'
                                           '//p[text()="Учимся танцевать"]')

    ON_TH_TWINE_DESCRIPTION = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"course_desc")]'
                                         '//p[text()="Работаем над растяжкой и садимся на шпагат"]')

    FACE_FITNESS_DESCRIPTION = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"course_desc")]'
                                          '//p[text()="Здоровое и красивое лицо, шея, зона декольте"]')

    POSTURE_DESCRIPTION = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"course_desc")]'
                                     '//p[text()="Прорабатываем мышцы спины и шеи для правильной осанки"]')

    BURN_FAT_NEW_DESCRIPTION = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"course_desc")]'
                                          '//p[text()="Избавляемся от 3-5 кг за счет безопасных нагрузок"]')

    BOXING_DESCRIPTION = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"course_desc")]'
                                    '//p[text()="Система тренировок по боксу: проработка силовой выносливости"]')

    WILDBERRIES_DESCRIPTION = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"course_desc")]'
                                         '//p[contains(., "Учимся зарабатывать на крупнейшем маркетплейсе")]')

    WALKING_DESCRIPTION = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"course_desc")]'
                                     '//p[text()="Учимся ходить правильно и с пользой"]')

    MEDITATION_DESCRIPTION = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"course_desc")]'
                                        '//p[text()="Учимся жить в гармонии с собой и миром"]')

    FINANCIAL_LITERACY_DESCRIPTION = (By.XPATH, '//div[contains(@class,"row")]//div[contains(@class,"course_desc")]'
                                                '//p[text()="Учимся зарабатывать и управлять собственными финансами"]')
