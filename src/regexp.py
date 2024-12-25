import re

mystr = "the black cat climbed the red tree"
pattern = re.compile('ATG[ACGT]*ACGT')

# Test strings
sequence = "ATGCTAGATGATGACGTTTTATGAAA"

matches = pattern.findall(sequence)
print(f"Matches found: {matches}")
patstr = 'cat'

pattern=re.compile(patstr)

print(pattern.search(mystr))


if pattern.search(mystr):
    print(f"String \"{mystr}\" contains the pattern: --  {patstr}")



####################

dna = "ACCACACAGATATCACAGAGACCCACACACAGGAGATTTATAGACACACA"
patstr = "ATCAC[ACGT]GGGAC[AT]"
pat = re.compile(patstr)

if pat.search(dna):
    print(f"{patstr} exists in {dna}")


## start of the string
dna = "ACCACACAGATATCACAGAGACCCACACACAGGAGATTTATAGACACACA"
patstr = "ACCACACA"
pat = re.compile(patstr)

if pat.match(dna):
    print(f"{patstr} is in the beginning  of {dna}")



##############

import re

# Pattern to match a DNA sequence starting with 'ATG'
pattern = re.compile("ATG")

# Test strings
sequences = ["ATGCTAG", "CTGATG", "ATGTTT"]

for seq in sequences:
    match = pattern.match(seq)
    if match:
        print(f"'{seq}' starts with 'ATG'.")
    else:
        print(f"'{seq}' does not start with 'ATG'.")

################

# Pattern to find 'ATG' anywhere in the sequence
pattern = re.compile('ATG')

# Test strings
sequences = ["ATGCTAG", "CTGATG", "TTTATGAAA"]

for seq in sequences:
    pat = pattern.search(seq)
    if pat:
        print(f"'ATG' found in '{seq}' at position {pat.start()}.")
    else:
        print(f"'ATG' not found in '{seq}'.")

########

# Pattern to find all occurrences of 'ATG'


###########

# Pattern to find 'ATG' and return detailed information
pattern = re.compile(r'ATG')

# Test string
sequence = "ATGCTAGATGATGTTTATGAAA"

matches = pattern.finditer(sequence)
print(matches)
for match in matches:
    print(match)
    print(f"'ATG' found at position {match.start()}-{match.end()} in '{sequence}'.")


# Pattern to split the sequence at 'ATG'
pattern = re.compile(r'ATG')

# Test string
sequence = "ATGCTAGATGATGTTTATGAAA"

split_result = pattern.split(sequence)
print(f"Split result: {split_result}")


################

# Pattern to replace 'ATG' with 'XXX'
##############

import re

# DNA sequence
sequence = "ACGATGCTTTAAACGGGAGGGTAA"

# Regex with capturing groups to extract codons (three nucleotides)
pattern = re.compile(r'([A]+)C([G]+)')

# Find all codons
matches = pattern.findall(sequence)

# Print the results
for match in matches:
    print(f"first motif is  found: {match[1]}")



import re

# DNA sequence
sequence = "ACGATGCTTTAAACGGGAGGGTAA"

# Regex with capturing groups to extract codons (three nucleotides)
pattern = re.compile(r'([A]+)C([G]+)')

# Find all codons
match = pattern.search(sequence)

# Print the results
for match in matches:
    print(match.group(1))