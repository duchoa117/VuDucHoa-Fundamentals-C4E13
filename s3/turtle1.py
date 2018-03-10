color=['red', 'blue', 'brown', 'yellow', 'gray']
from turtle import*

n=int(input('nhap so canh cua hinh lon nhat??(n>=3) n= '))
speed(-100)


for i in range(3,n+1,1):

    if (i-3)%5==0:
        color('red')
    elif (i-3)%5==1:
        color('blue')
    elif (i-3)%5==2:
        color('brown')
    elif (i-3)%5==3:
        color('yellow')
    elif (i-3)%5==4:
        color('gray')
    for j in range(i):
        forward(100)
        left(360/i)


mainloop()
#n=7
