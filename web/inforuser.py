from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<nameofuser>')
def infor_user(nameofuser):
    list_user = [
        {
        'user': 'Tokuda',
        'nickname':'Anh hùng đóng gạch thời kì đổi mới',
        'gender': 1,
        'hobbies':'Giúp đỡ phụ nữ người già và trẻ em',
        },
        {
        'user': 'Nene',
        'nickname': 'Vợ quốc dân',
        'gender': 0,
        'hobbies': "Thả thính",
        },
        {
        'user':'Dinh Quy',
        'nickname': 'Anh trai quốc dân',
        'gender': 1,
        'hobbies': 'Luôn luôn lắng nghe luôn luôn chia sẻ :)))',
        }
    ]
    T_F = False
    for u in list_user:
        if u['user'] == nameofuser:

            T_F = True
            break
    if T_F:
        return render_template('inforuser.html',user = u)
    else:
        return "User not found"


if __name__ == '__main__':
  app.run(debug=True)
