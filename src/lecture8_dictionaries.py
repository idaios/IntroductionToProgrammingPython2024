bathmoi = {'giorgos':10, 'antonis':7, 'maria':10, 'katerina':9, 'eleni':10, 'manolis':8}
print(bathmoi)

v = bathmoi['antonis']
print(v)

#v = bathmoi['katerina']
#print(v)

v = bathmoi.get('katerina', -1)
print(v)


for k in bathmoi.keys():
    print(f"Η βαθμολογία του {k} είναι {bathmoi[k]}")

v = 0
for i in bathmoi.values():
    v += i
mo = v/len(bathmoi)
print(mo)

print(f"max degree is {max(bathmoi.values())}")

print(set(bathmoi.values()))

for i,j in bathmoi.items():
    print(f"Η βαθμολογια για τον {i} ειναι {j}")