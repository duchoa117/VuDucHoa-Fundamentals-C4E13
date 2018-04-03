from models.classes import Service
from faker import Faker
fake = Faker()
from random import randint, choice
import mlab_warm_winter
for i in range(100):
    name_fake = fake.name()
    mlab_warm_winter.connect()
    new_service = Service(
        name = name_fake,
        gender = choice([0,1]),
        email = name_fake + str(randint(0,100))+"@gmail.com",
        phone_number = fake.phone_number(),
        job = fake.job(),
        company = fake.company(),
        contacted = choice(["Busy","free"])
    )
    new_service.save()
