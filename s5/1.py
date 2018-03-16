inventory = {
    'gold' : 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
print(inventory)
print('*'*147)

inventory['pocket'] = [ 'seashell', 'strange berry', 'lint']
print(inventory)
print('*'*147)
inventory['backpack'].remove('dagger')
print(inventory)
print('*'*147)

inventory['gold']+=50
print(inventory)
print('*'*147)
