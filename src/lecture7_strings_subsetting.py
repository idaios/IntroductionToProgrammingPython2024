
## we can represent DNA as a string
dna = "ACACGTGACAATGCATGCACAGGGATGGA"

## many things that apply on lists, they apply on strings as well
print(dna[0])
print(dna[10])
print(dna[-1])
print(dna[0:10])
print(len(dna))

## now let's find all ATGS in a string
numberofATGS = 0
positionsATGS = []
## search for a motif
for i in range(len(dna)-3):
    if dna[i:(i+3)] == "ATG":
        numberofATGS +=1 # numberofATGS = numberofATGS + 1
        positionsATGS.append(i)

print(f"I found {numberofATGS} ATGs")

if numberofATGS > 0:
    print(f"Their positions are {positionsATGS}")


#examples with functions on strings
x = dna.count("ATG")
print(x)

# the first index of the ATG location
x = dna.find("ATG")
print(x)
x = dna.index("ATG")
print(x)


astring = 'hello'
#astring[0] = 'H'
print(astring)

newstring = 'H'
newstring = newstring + astring[1:]
print(newstring)

newstring2 = astring.capitalize()
print(newstring2)