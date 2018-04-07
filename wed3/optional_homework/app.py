from flask import *
app = Flask(__name__)
from pymongo import MongoClient
MongoClient_uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'
client = MongoClient(MongoClient_uri)
db = client.get_default_database()
river = db['river']
# all_rivers = rivers.find()


@app.route('/')
def river_table():
    all_rivers = river.find()
    return render_template('river_table.html', all_rivers = all_rivers)

if __name__ == '__main__':
  app.run(debug=True)
