import re
import os

os.getcwd()
os.chdir("/home/motoo/teaching/2024_2025/python/src")


# Compile the regex pattern for matching the header (sequence name after '>')
pattern = re.compile(r'^>(\S+)')
emptyseq = re.compile(r'^\s+$')
sequence = {}
# Open the FASTA file (replace 'your_file.fasta' with the actual file path)
with open('output1_100.fa', 'r') as fasta_file:
    # Initialize an empty list to store sequence names
    sequence_names = []
    
    # Read the file line by line
    for line in fasta_file:
        line = line.strip()
        # Match the compiled pattern against each line
        match = pattern.match(line)
        isempty = emptyseq.match(line)
        # If the pattern matches, extract and store the sequence name
        if match:
            seqname = match.group(1)
            sequence_names.append(seqname)
        elif not isempty:
            line = re.sub(r"-", "", line)
            print(line)
            line = line.upper()
            sequence[seqname] = line

# Print the list of sequence names
print(sequence)


## Let's put this into a function

def readFasta(filename):
    sequence = {}
    # Open the FASTA file (replace 'your_file.fasta' with the actual file path)
    with open('output1_100.fa', 'r') as fasta_file:
    # Initialize an empty list to store sequence names
        sequence_names = []
    
        # Read the file line by line
        for line in fasta_file:
            line = line.strip()
            # Match the compiled pattern against each line
            match = pattern.match(line)
            isempty = emptyseq.match(line)
            # If the pattern matches, extract and store the sequence name
            if match:
                seqname = match.group(1)
                sequence_names.append(seqname)
            elif not isempty:
                line = re.sub(r"-", "", line)
                line = line.upper()
                sequence[seqname] = line
    return(sequence)




seqs = readFasta("output1_100.fa")
print(seqs)


def getkmers(d, x=5):
    kmer = {}
    for name, seq in d.items():
        for i in range(len(seq)-x + 1):
            subseq = seq[i:(i+x)]
            if subseq in kmer.keys():
                kmer[subseq]+=1
            else:
                kmer[subseq] = 1
    return(kmer)

seqmers = getkmers(seqs, 7)

seqmers