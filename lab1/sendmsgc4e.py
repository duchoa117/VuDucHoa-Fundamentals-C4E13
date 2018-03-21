from pymongo import MongoClient
client_uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'
client = MongoClient(client_uri)
db = client.get_default_database()
posts = db['posts']
new_post = {
    'title':'Anonymous',
    'author': 'From hell',
    'content':'Hello world....My...home.!'
}
posts.insert_one(new_post)
