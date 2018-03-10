item=['T-Shirt', 'Sweater']
while True:
    choice=input('welcome to our shop, what do you want (C, R, U, D) ? ')

    if choice=='R':

        print('Our items: ',end='')
        print(*item, sep=', ')
    elif choice=='C':
        newitem=input('Enter new item: ')
        item.append(newitem)
        print('Our items: ', end='')
        print(*item, sep=', ')
    elif choice=='U':
        update=int(input('Update position?                   '))
        newitem=input('New item? ')
        item[update-1]=newitem
        print('Our items: ',end='')
        print(*item, sep=', ')
    elif choice=='D':
        delete=int(input('Delete position? '))
        item.pop(delete-1)
        print('Our items: ',end='')
        print(*item, sep=', ')
    else:
        print('Wrong enter')
        # choice=input('Try again ')
        print('Try again')
