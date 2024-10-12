import time


x0 = time.time()
mylist = []
for i in range(1,30000001):
    mylist.append(i)
x1 = time.time()

print(f"total time 1 is {x1-x0}")

x0 = time.time()
mylist = []
for i in range(1,10000001):
    mylist.append(i)
x1 = time.time()
print(f"total time 2 is {x1-x0}")
