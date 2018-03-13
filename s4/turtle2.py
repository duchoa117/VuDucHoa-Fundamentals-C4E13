from turtle import*
color('blue')
speed(-100)
a=0
right(150)
for i in range(50):
    a+=1
    for i in range(4):
        forward(200-4*a)
        right(90)
    right(10)
mainloop()
