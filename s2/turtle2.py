a=int(input(' so canh cua hinh to nhat la ? '))

from turtle import*
speed(-100)

for j in range(3,a+1):
    if j%2==1:
        color('blue')
    else:
        color('red')


    for i in range(j):
        forward(100)
        left(360/j)
mainloop()
# theo nhu yeu cau hinh de bai thi a cho a la 6 nhe :VVV xong a nghich them cho vui
