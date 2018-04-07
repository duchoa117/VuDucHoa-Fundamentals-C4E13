from mongoengine import*
class Service(Document):
    image = StringField()
    gender = IntField()
    name = StringField()
    yob = IntField()
    height = IntField()
    phone_number = StringField()
    address = StringField()
    description = StringField()
    measurements = ListField()
