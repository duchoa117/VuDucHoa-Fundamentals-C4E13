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
    status = StringField()

class User(Document):
    fullname = StringField()
    email = StringField()
    username = StringField()
    password = StringField()

class Trade(Document):
    user = StringField()
    service = StringField()
    datetime = StringField()
    is_accept = BooleanField()
    user_id = StringField()
    service_id = StringField()
