name=input('Your full name: ')
namelower=name.lower()
namelist=namelower.strip().split(' ')
c=0
# print(namelist)
n=len(namelist)
for j in range(n):
    for m in range(n-c):
        if namelist[m]=='':
            namelist.remove(namelist[m])
            c+=1
            break
# print(namelist)
print('Updated: ',end='')
for i in range(len(namelist)):
    word=list(namelist[i])
    word[0]=word[0].upper()
    print(*word ,sep='', end=' ')
print()
