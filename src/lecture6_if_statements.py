
a = list(range(10))

for i in a:
    if i > 5:
        print(f"Number {i} is greater than 5")
    elif i == 5:
        print(f"Number {i} is equal to 5")
    else:
        print(f"Number {i} is less than 5")



mylist = [9,1,0,-1,7,14,56]
for i in mylist:
    if i not in a:
        print(f"Number {i} is not in list a:{a}")
    else:
        print(f"Number {i} is  in list a:{a}")