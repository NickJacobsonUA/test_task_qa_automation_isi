import random

from data.data import GenInfo
from faker import Faker

fake = Faker('en_US')
Faker.seed()


def generated_data():
    yield GenInfo(
        firstname= 'Autotester',
        lastname= fake.last_name(),
        username=f'Auto_{fake.user_name()}',
        temperature_from=random.randint(1,50),
        temperature_to=random.randint(51, 104),
        id_number=f'Auto_{random.randint(10000,100000)}',
        email = fake.email(),
        address = fake.street_address(),
        mobile=fake.msisdn(),
        password = '000000',
        universal='autotest',
        year=random.randint(1995,2023),
    )