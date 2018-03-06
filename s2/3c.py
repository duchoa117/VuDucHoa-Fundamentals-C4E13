a=int( input(' nhap n '))
for i in range(1, a+1):
    # print(*range(i, i*a, i))
    for j in range(i, i*(a+1), i):
        if 0==j//10:
            print(j, end=' '*(3))
        else:
            for b in range(1,a):
                if 1<=j//(10**b)<10:
                    print(j, end=' '*(3-b))
    print()
# tổng quat e muon sua 4>>> a :)))
