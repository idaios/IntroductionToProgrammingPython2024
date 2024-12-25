import random
alphabet = ['A', 'C', 'G', 'T']
n = 20000
dna_list = [random.choice(alphabet) for i in range(n)]
dna = ''.join(dna_list)
print(dna)

d = {}
for i in range(len(dna)-5):
    w = dna[i:(i+6)]
    if w in d.keys():
        d[w] += 1
    else:
        d[w] = 1

print(len(d))

print(d.values())
print(sum(d.values())/len(d))
 