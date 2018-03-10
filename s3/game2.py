
# import getpass
#
# a = getpass.getpass('the word:')
# phan che tu e tra mang cho chuan
word=[]
x=int(input('How many words do you want? '))
for m in range(x):
    y=input('the word: ')
    word.append(y)
# make list word
t=0
while t!=x:
    from random import randint
    z=randint(0,x-1-t)
    c=list(word[z])

    newlist=[]
    from random import choice

    cout=len(c)

    while True:
        while len(newlist)!=cout:
            random_c= choice(c)
            c.remove(random_c)
            newlist.append(random_c)
        print(*newlist)
        enter=input('what is this word?? ')
        if enter==word[z]:
            print('Bingo')
            word.remove(word[z])
            t+=1
            print()
            break
        else:
            print('Wrong :((. Try again')
print('You win ')
    #by hoa handsome
