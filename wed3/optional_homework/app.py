from flask import *
app = Flask(__name__)
from models.c4e import River
import mlab
mlab.connect()


@app.route('/')
def river_table():

    all_rivers = River.objects(continent = "Africa")
    return render_template('afica_river_table.html', all_rivers = all_rivers)
@app.route('/ALL_rivers_in_‘S. America’_continent_with_length_less_than_1000_km')
def America_lt_100_river():
    all_rivers = River.objects(continent = 'S. America',length__lt = 1000)
    return render_template('a_river.html', all_rivers = all_rivers)


if __name__ == '__main__':
  app.run(debug=True)
