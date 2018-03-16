big = int(input('How many pair of big rabbit? '))
small= int(input('How many pair of small rabbit?? '))
moth = int(input('How many moth have passed? '))
for i in range(1,moth+1):
    print('Moth {0}:'.format(i))
    small_1= small
    big_1= big
    big = big + small_1
    small= big_1
    print(big, 'pair(s) of big rabbit')
    print(small, 'pair(s) of small rabbit')
    print('Được',big + small, 'cặp đôi hạnh phúc và không ai FA như a Quý :))')
