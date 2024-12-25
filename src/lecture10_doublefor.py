import random

emot = ['<3', ';)', ':-)', '^_^', ':O', '<(")', '3:-)', '🤩', '😘']
print(emot)

print("")
counter = 0
for i in range(50):
    for j in range(len(emot)):
        counter += 1
        print(emot[j], end=' ')
    if counter % 18 == 0:    
        print("", end="\n")
        #k = random.randint(0, len(emot)-1)
        #print(random.choice(emot), end=' ')
