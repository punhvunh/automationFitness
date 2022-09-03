from data.data import LoginData
from faker import Faker

faker_ru = Faker('ru_Ru')


def generated_login_data():
    yield LoginData(
        email=faker_ru.email(),
        password=faker_ru.password()
    )
