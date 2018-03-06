print('hi')
a=int(input('your hight(cm)=  '))
b=int(input('your weight(kg)= '))
c=a/100
BMI=b/(c*c)
print('your BMI = ',BMI )
if BMI<16:
    print('Severely underweight')
elif 16<=BMI<18.5:
    print('Underweight')
elif 18.5<= BMI<25:
    print('Normal')
elif 25<= BMI<30:
    print('Overweight')
else:
    print('Obese')
