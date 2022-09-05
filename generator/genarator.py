from data.data import LoginData
from faker import Faker

faker_en = Faker('en_US')


def generated_login_data():
    yield LoginData(
        email=faker_en.email(),
        password=faker_en.password()
    )
