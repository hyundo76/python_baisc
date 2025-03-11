card = {'name': 'pay', 
        'phone':'445454', 
        'address':'seoul'}

print(card)
card['etc'] = 'dmdkd'
card['etc'] = 'asda'

print(card)

print(card['etc'])

print(card['etc'][2])

del card['etc']

print(card)

print(type(card))

print(len(card))

print('address' in card)

print(card.keys())

for k in card.keys():
    print(k)

for x, y in card.items():
    print(x,y)
print(card.get('address'))