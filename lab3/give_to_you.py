

tym = int(input("How many tyms do you want??? "))
from turtle import*
from draw_tym import draw_tym
speed(0)
# color('blue')

for i in range(tym):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_tym(x, y, length)
# mainloop()
# color('blue')
# penup()
# setposition(-200,200)
# pendown()
# forward(21)
# penup()
# setposition(-193,207)
# pendown()
# right(90)
# forward(17)
# penup()
# setposition(-186,207)
# pendown()
# forward(17)
mainloop()
