from turtle import*
def draw_tym(x,y,len):
    penup()
    setposition(x,y)
    pendown()
    color('black','red')
    begin_fill()
    left(90)
    circle(len,180)
    right(180)
    circle(len,180)
    left(45)
    forward(2*len*2**(1/2))
    left(90)
    forward(2*len*2**(1/2))
    right(45)
    end_fill()
