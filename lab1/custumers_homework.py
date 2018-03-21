from pymongo import MongoClient
MongoClient_uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'
client = MongoClient(MongoClient_uri)
db = client.get_default_database()
customers = db['customers']
all_refs = customers.find()
refs = []
for r in all_refs:
     refs.append(r['ref'])
     # print(refs)
ref_events = 0
ref_wom = 0
ref_ads = 0
for i in range(len(refs)):
    if refs[i] == 'events':
        ref_events += 1
    if refs[i] == 'wom':
        ref_wom += 1
    if refs[i] == 'ads':
        ref_ads += 1
print('ads:',ref_ads)
print('wom:',ref_wom)
print('ads:', ref_ads)


import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot
labels = ['events', 'wom', 'ads']
values = [1, 2, 2]
pyplot.pie(values, labels = labels )
pyplot.axis('equal')
pyplot.show()
