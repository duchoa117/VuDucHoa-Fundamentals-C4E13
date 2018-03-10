from turtle import*
n=int(input('nhap n'))
for i in range(n):
    # if (i)%5==0:
    # color('red', 'red')
    # filling()
    # elif (i)%5==1:
    #     color('blue','blue')
    # elif (i)%5==2:
    #     color('brown','red')
    # elif (i)%5==3:
    #     color('yellow','red')
    # elif (i)%5==4:
    #     color('gray', 'red')
    begin_fill()
    if (i)%5==0:
        color('red', 'red')
    # filling()
    elif (i)%5==1:
        color('blue','blue')
    elif (i)%5==2:
        color('brown','brown')
    elif (i)%5==3:
        color('yellow','yellow')
    elif (i)%5==4:
        color('gray', 'gray')
    for j in range(2):
        forward(100)
        right(90)
        forward(200)
        right(90)

    end_fill()
    forward(100)

    # left(90)

mainloop()
