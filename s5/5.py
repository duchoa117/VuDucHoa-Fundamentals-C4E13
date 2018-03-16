prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3

}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15

}
total = 0
for key in prices:
    # for value in stock.values():
        print(key)
        print('price:', prices[key], '$')
        print('stock:', stock[key])
        money = prices[key]*stock[key]
        print('Money can get:',money, '$')
        total += money
print('Total:', total,'$')
