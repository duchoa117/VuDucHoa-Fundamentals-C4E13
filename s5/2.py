numbers = input('Enter your list numbers, seper by space: ')
list_numbers = list(numbers.strip().split())
cout=0
n = input('which number do you want to cout in your list??? ')
for number in list_numbers:
     if number == n:
         cout+=1
if cout < 2:

    print(n, 'appears {0} time in your list.'.format(cout))
else:
    print(n, 'appears {0} times in your list.'.format(cout))
