from flask import*
from random import randint
from gmail import GMail, Message
import datetime


app = Flask(__name__)
from models.class_c4e_services import *
import mlab
app.secret_key = "anhquydeptraichoe10diemdi:VVVV"
mlab.connect()
@app.route('/')
def home_page():
    return render_template("index.html")
@app.route('/list_service/<service_gender>')
def all_services(service_gender):
    print(service_gender)
    checked = False
    users = User.objects()
    for user in users:
        if str(user["id"]) in session:
            user = user
            checked = True
    if checked:
        return redirect(url_for('all_services_for_user',user_id = user["id"], service_gender = service_gender))
    else:
        return render_template('all_services.html', services = Service.objects(gender = service_gender))
@app.route('/admin')
def admin():
    services = Service.objects()
    return render_template("admin.html",services = services)
@app.route("/admin/trade_information")
def trade_table():
    trades = Trade.objects()
    return render_template("trade_table.html", trades = trades)
@app.route('/detail/<service_id>')
def detail(service_id):
    checked = False
    users = User.objects()
    for user in users:
        if str(user["id"]) in session:
            user = user
            checked = True
    if checked:
        services = Service.objects(id = service_id)
        return render_template('detail_all_services.html',services = services, user = user )
    else:
        return redirect(url_for('loggin'))
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
            image = form["image"],
            status = form["status"]


        )
        new_service.save()
        return redirect(url_for('index'))
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
                set__image = form["image"],
                set__status = form["status"]

        )
        return redirect(url_for('home_page'))
@app.route('/detail/del/<service_id>')
def delete(service_id):
    services = Service.objects(id = service_id)
    services.delete()
    return redirect(url_for('home_page'))
@app.route("/sign_up", methods = ["GET", "POST"])
def sign_up():
    confirm_username = False
    confirm_email = False
    if request.method == "GET":
        return render_template("sign_up.html")
    elif request.method == "POST":
        form = request.form
        users = User.objects()
        for user in users:
            if form["email"] == user["email"]:
                confirm_email = True
            if form['username'] == user['username']:
                confirm_username = True
        if confirm_email:
            return "Email has been used. Try again"
        elif confirm_username:
            return "Username has been used. Try again"
        else:
            str_password = str(randint(1000,9999))

            new_user = User(
                fullname = form["fullname"],
                email = form["email"],
                username = form["username"],
                password = str_password

            )
            new_user.save()
            users = User.objects(username = form["username"])
            from gmail import GMail, Message
            accept_account = """
            <h1>Accept your Warm winter Account</h1>
<h3><strong>Username: {{username}}</strong></h3>
<h3>Password: {{password}}</h3>
<p>" You can change your password in here :<a href="http://localhost:5000/password_change">http://localhost:5000/password_change</a> "</p>
<p>&nbsp;</p>
<div class="HOEnZb adL">
<div class="im">
<p style="text-align: center;"><strong><em>"Thanks for use our program"</em></strong></p>
</div>
</div>
    """


            accept_account = accept_account.replace('{{username}}',form['username'])
            accept_account = accept_account.replace('{{password}}',str_password)
            gmail = GMail('duchoapc99techkids@gmail.com', 'duchoa119')
            msg = Message('Accept Account', to= form['email'], html= accept_account)
            gmail.send(msg)
            return "Check your Email to Loggin"
@app.route('/loggin',methods = ["GET", "POST"] )
def loggin():
    if request.method == "GET":
        return render_template('loggin.html')
    if request.method == "POST":
        checked = False
        form = request.form
        users = User.objects()
        for user in users:
            if form['username'] == user['username'] and form['password'] == user['password']:
                checked = True

        if checked:
            username_exact = User.objects(username__exact = form["username"])
            session[str(username_exact[0]["id"])] = True

            return redirect(url_for("home_page")) #******************
        else:
            return "Fail"
@app.route("/all_services_for_user/<user_id>/<service_gender>")
def all_services_for_user(user_id,service_gender):
    services = Service.objects(gender = service_gender)

    return render_template('all_services_for_user.html',user_id = user_id, services = services)


@app.route("/get_service/<user>/<service>/<user_id>/<service_id>")
def get_service(user, service, user_id, service_id):
    checked = False
    trades = Trade.objects()
    for trade in trades :
        if user_id == trade['user_id'] and service_id == trade['service_id']:
            checked = True
    if checked:
        return " You have already got this service"
    else:
        now = datetime.datetime.now()

        new_trade = Trade(
            user = user,
            service = service,
            datetime = str(now),
            is_accept = True,
            user_id = user_id,
            service_id = service_id

        )
        new_trade.save()

        return "Already sent"
@app.route("/confirmed/<user_id>/<service_id>")
def confirm(user_id, service_id):
    Trade.objects(service_id = service_id).update(set__is_accept = False)
    Service.objects(id = service_id).update(set__status = "Busy")

    return redirect(url_for('trade_table'))
@app.route("/password_change", methods = ["GET", 'POST'])
def password():
    if request.method == 'GET':
        return render_template('password_change.html')
    elif request.method == "POST":
        form = request.form
        checked = False
        users = User.objects()
        for user in users:
            if user['username'] == form['username'] and user['password'] == form['password']:
                checked = True
        if checked:
            User.objects(username = form['username']).update(set__password = form["new_password"])
            return redirect(url_for('home_page'))
        else:
            return "Wrong. Try again"
@app.route('/logout/<user_id>')
def logout(user_id):
    del session[user_id]
    return redirect(url_for('home_page'))





if __name__ == '__main__':
  app.run(debug=True)
