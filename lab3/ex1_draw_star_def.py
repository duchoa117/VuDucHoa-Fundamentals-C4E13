from turtle import*
def draw_star(x,y,len):
    penup()
    setposition(x,y)
    pendown()
    for i in range(5):
        forward(len)
        right(144)
