name=input('Your name? ')
listsize=[]
print('Hello', name, ".let's make your sheep sizes list" )
cout=int(input('How many sizes do you want?? '))
for i in range(cout):
    # if end!= 'End':
        size=input('Enter size: ')
        listsize.append(size)
print('Your sheep sizes list: ', end='')
print(*listsize, sep=', ')
int_listsize=[int(x) for x in listsize]
# print(int_listsize)
max= int_listsize[0]
for j in range(cout):
    if max<=int_listsize[j]:
        max = int_listsize[j]
print('Now your biggest sheep has size', max, "let's shear it :))")
# choice=input("You wanna sheart it ??(if yes-enter'Y', no-enter'N') ")
while True:
    choice=input("You wanna sheart it ??(if yes-enter'Y', no-enter'N') ")
    if choice=='Y':
        str_max=str(max)
        listsize[listsize.index(str_max)]='8'
        print('After shearing, here is your flock: ', end='')
        print(*listsize, sep=', ')
        break
    elif choice=='N':
        print("You haven't sheared it yet")
        choice=input('shear it now ? ')
    else:
        print('Wrong enter')
        print('Try again')

month=int(input('How many months have been passed(After month always shear)?? '))
for m in range(month-1):
    int_listsize=[int(x) for x in listsize]
    for k in range(cout):
        int_listsize[k]= int_listsize[k]+50
        listsize[k]=str(int_listsize[k])
    int_listsize=[int(x) for x in listsize]
    maxx= int_listsize[0]

    print('Month',m+1,':')
    print('One month has passed, now here is you flock:')
    print(*listsize,sep=', ')
    for m in range(cout):
        if maxx<=int_listsize[m]:
            maxx = int_listsize[m]
    str_maxx=str(maxx)
    listsize[listsize.index(str_maxx)]='8'
    print('Now your biggest sheep has size', maxx, "let's shear it :))")
    print('After shearing, here is your flock: ')
    print(*listsize, sep=', ')
int_listsize=[int(x) for x in listsize]
for n in range(cout):
    int_listsize[n]= int_listsize[n]+50
    listsize[n]=str(int_listsize[n])
int_listsize=[int(x) for x in listsize]
maxx= int_listsize[0]

print('Month',month,':')
print('One month has passed, now here is you flock:')
print(*listsize,sep=', ')
for m in range(cout):
    if maxx<=int_listsize[m]:
        maxx = int_listsize[m]
str_maxx=str(maxx)
print('Now your biggest sheep has size', maxx)
# int_listsize(int(x) for x in listsize)
add=0
for n in range(cout):
    add=add+ int_listsize[n]
print('Your flock has size in total: ', add)
print('You would get ',add," * 2$ = ", add*2,'*',sep='')
