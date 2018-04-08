from flask import*
app = Flask(__name__)
from models.class_c4e_services import Service
import mlab
mlab.connect()

@app.route('/')
def all_services():
    services = Service.objects()
    return render_template('all_services.html',services = services)
@app.route('/admin')
def admin():
    services = Service.objects()
    return render_template("admin.html",services = services)
@app.route('/detail/<service_id>')
def detail(service_id):
    print(service_id)
    services = Service.objects(id = service_id)
    return render_template('detail_all_services.html',services = services)
@app.route('/create',methods = ["GET", "POST"])
def create():
    if request.method == "GET":

        return render_template('create.html')
    elif request.method == "POST":
        form = request.form
        new_service = Service(
            name = form["name"],
            gender = int(form["gender"]),
            yob = form['yob'],
            height = form['height'],
            phone_number = form['phone_number'],
            address = form["address"],
            description = form["description"],
            measurements = [form["m_1"], form["m_2"], form["m_3"]],
            image = form["image"]


        )
        new_service.save()
        return redirect(url_for('all_services'))
@app.route('/detail/fix/<service_id>', methods = ["GET", "POST"])
def fix(service_id):
    services = Service.objects(id = service_id)
    if request.method == "GET":
        return render_template("fix.html",services = services)
    elif request.method == 'POST':
        form = request.form
        services.update(
                set__name = form["name"],
                gender = int(form["gender"]),
                set__yob = form['yob'],
                set__height = form['height'],
                set__phone_number = form['phone_number'],
                set__address = form["address"],
                set__description = form["description"],
                set__measurements = [form["m_1"], form["m_2"], form["m_3"]],
                set__image = form["image"]

        )
        return redirect(url_for('all_services'))
@app.route('/detail/del/<service_id>')
def delete(service_id):
    services = Service.objects(id = service_id)
    services.delete()
    return redirect(url_for('all_services'))





if __name__ == '__main__':
  app.run(debug=True)
