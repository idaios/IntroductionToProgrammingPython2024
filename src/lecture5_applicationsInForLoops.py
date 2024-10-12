import time

t0 = time.time()

mylist = []
for i in range(10000000):
    mylist.append(i)
t1 = time.time()
totaltime = t1 - t0
print(f"the total time is {totaltime}")

t0 = time.time()
mylist = list(range(10000000))
t1 = time.time()
print(f"second approach with list {t1 - t0}")
      
t0 = time.time()    
mylist = [i for i in range(10000000)]
t1 = time.time()
print(f"third approach with list comprehension{t1 - t0}")