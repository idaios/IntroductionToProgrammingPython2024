bathmoi = {'giorgos':8, 'antonis':7, 'maria':10, 'katerina':9, 'eleni':10, 'manolis':8}
print(bathmoi['giorgos'])

bathmoi['konstantina'] = 6
print(bathmoi)
bathmoi['konstantina'] = 6.5
print(bathmoi)


print(bathmoi)


print(bathmoi.get('despoina',-1))


print(bathmoi)


for i,j in bathmoi.items():
    print(f"the mark of {i} is {j}")



