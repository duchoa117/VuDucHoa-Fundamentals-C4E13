import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds125053.mlab.com:25053/warn_winter

host = "ds125053.mlab.com"
port = 25053
db_name = "warn_winter"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
