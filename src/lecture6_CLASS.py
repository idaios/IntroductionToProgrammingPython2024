import time
x = list(range(10))
print(x)

z = 0
mesox = sum(x)/len(x)
for i in x:
    z = z + (i-mesox)**2
z = z/len(x)

print(z)

z = 0
for i in range(10):
    z = z + (x[i]-mesox)**2
z = z/len(x)
print(z)

z = []
for i in x:
    z.append((i-mesox)**2)

v = sum(z)/len(z)
print(v)


x = list(range(10,100,2))
print(x)


### megales listes
'''
t0 = time.time()
x = list(range(0, 60000000, 2))
t1 = time.time()
print(f"time1: {t1 - t0}")

t0 = time.time()
x = [ 2*i for i in range(30000000) ]
t1 = time.time()
print(f"time2: {t1 - t0}")
'''

### logikes metablites/ logikes praxeis

a = 10

## >, <, >=, <=, ==, !=

a = 10000
x = (a < 100)
y = True

## and or 
## x and y
bb = (x or y) or  False

x = 7


x = 4

if (x % 2) == 0:
    print(f"x is a multiple of 2: {x}")
if (x % 3) == 0:
    print(f"x is a multiple of 3: {x}")
if( ((x %2) != 0) and ( (x % 3) != 0 ) ):
    print(f"x is not a multiple of 2 or 3: {x}")
