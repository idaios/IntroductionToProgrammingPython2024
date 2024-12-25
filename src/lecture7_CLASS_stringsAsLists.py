a = "ACGATGAATGATAACCGGGTTGA"
## MIKOS
print(len(a))

print(a.count("A"))
print(a.find("ATG"))
print(a.index("ATG"))

## 1. count all atg, 
# 2. if any, put in a list their positions

atgpositions = []
atgcount = 0
#tgg 0, 0... range(0, len("tgg")-3+1)
s = a.count("ATG") ## swsto
for i in range(len(a)-2):
    ## for i in a:
    if a[i:(i+3)] == "ATG":
        atgpositions.append(i)
        atgcount += 1 ## atgcount = atgcount + 1

print(f"I found {atgcount} ATGs")

if atgcount > 0:
    print(f"The positions are {atgpositions}")


## substring in string

fs = "ACCG"
ss = "CCG"

if fs in a:
    print(f"I found {fs} in {a}")
elif ss in a:
    print(f"I didn't find {fs} but i got  {ss} in {a}")
else:
    print(f"I didn't find {ss} in {a}")

print(a)
print(a[0:10:2])

x = ""
for i in range(10):
    x = x + "A"
print(x)

b = a[::-1]
print(b)


rc = []
for i in b:
    if i == 'A':
        rc.append('T')
    elif i == 'T':
        rc.append('A')
    elif i == "C":
        rc.append('G')
    else:
        rc.append('C')

print(''.join(rc))

print(a)


# GCAACCC...12