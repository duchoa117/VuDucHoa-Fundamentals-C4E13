a=int(input('nhap n'))
for i in range(1, a+1):
    if i%2==1:

        for j in range(1,a+1):
            if j%2==1:
                print('1', end=' ')
            else:
                print('0', end=' ')
    else:
        for j in range(1, a+1):
            if j%2==1:
                print('0', end=' ')
            else:
                print('1', end=' ')
    print()
