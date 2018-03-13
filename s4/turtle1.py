from turtle import*
n=int(input('How many squares do you want? '))
speed(-100)
color('blue')

for i in range(n):
    for j in range(4):
        forward(100)
        left(90)
    left(360/n)

mainloop()
