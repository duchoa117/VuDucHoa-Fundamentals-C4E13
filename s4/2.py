number=int(input('Enter the number: '))
# print(number)
listnumber=list(str(number))
newlistnumber=[]
Updated=[]
cout=0
a=len(listnumber)
b=3
# print(listnumber)
if number<0:
    b=4
while len(listnumber)//3!=0 and len(listnumber)>b:
    newlistnumber.append(listnumber[len(listnumber)-1])
    newlistnumber.append(listnumber[len(listnumber)-2])
    newlistnumber.append(listnumber[len(listnumber)-3])
        # cout+=3
    newlistnumber.append(',')
    listnumber.remove(listnumber[a-cout-1])
    listnumber.remove(listnumber[a-cout-2])
    listnumber.remove(listnumber[a-cout-3])
    cout+=3
    # print(newlistnumber)
    # print(listnumber)
while len(listnumber)!=0:
    newlistnumber.append(listnumber[len(listnumber)-1])
    listnumber.remove(listnumber[len(listnumber)-1])
# print(*newlistnumber)
for i in range(len(newlistnumber)):
    Updated.append(newlistnumber[len(newlistnumber)-1-i])
print('Updated: ',*Updated, sep='')
