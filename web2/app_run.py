from flask import Flask, render_template
import mlab_warm_winter
from models.classes import Service
app = Flask(__name__)

mlab_warm_winter.connect()
@app.route('/')
def trangchu():
    return render_template('tt.html')
@app.route('/search/')
def search_all():
    get_services = Service.objects()
    return render_template('service.html', all_services = get_services)
@app.route('/search/<gender>')
def search(gender):
    all_services = Service.objects(gender = gender,contacted = "free")[:10]
    return render_template("service.html",all_services = all_services)


if __name__ == '__main__':
  app.run(debug=True)
