from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<int:weight>/<int:height>')
def bmi(weight,height):
    h_met = height/100
    BMI = weight/(h_met*h_met)
    if BMI<16:
        infor = 'Severely underweight'
    elif 16<=BMI<18.5:
        infor = 'Underweight'
    elif 18.5<= BMI<25:
        infor = 'Normal'
    elif 25<= BMI<30:
        infor = 'Overweight'
    else:
        infor = 'Obese'
    return "BMI= " + str(BMI) + "   You are: " + infor



if __name__ == '__main__':
  app.run( debug=True)
