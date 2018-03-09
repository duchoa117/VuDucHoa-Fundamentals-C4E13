
import getpass

a = getpass.getpass('the word:')
# phan che tu e tra mang cho chuan

c=list(a)
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
    if enter==a:
        print('Bingo')
        break
    else:
        print('Wrong :((. Try again')
    #by hoa handsome
