import sys
import os
import re

os.getcwd()
os.chdir("/home/motoo/teaching/2024_2025/python/src/")

# Function to read sequence names from a file
def read_sequence_names(filename):
    names = []
    with open(filename, 'r') as file:
        for line in file:
            names.append(line.strip())
    return names


def geneNamesAssociation(filename):
    pattern = re.compile(r"(NM_[^,]+),([^,]+)")
    geneid = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            match = pattern.match(line)
            if match:
                nmid = match.group(1)
                gid = match.group(2)
                geneid[nmid] = gid
    return geneid

nmassocfile = "/home/motoo/teaching/2024_2025/python/src/nm_affy.txt"
nmassoc = geneNamesAssociation(nmassocfile)

nmassoc


filename = "/home/motoo/teaching/2024_2025/python/src/gene_ids.txt"

mygenes = read_sequence_names(filename)
mygenes



# Function to parse a multiline FASTA file

# ^\s*$

def parse_fasta(fastafile):
    pattern = re.compile(r">(NM_[^_]+)_")
    pattern2 = re.compile(r"[acgtACGTNn-]")
    sequences = {}
    header = None
    sequence_lines = []
    with open(fastafile, 'r') as file:
        for line in file:
            line = line.strip()
            match = pattern.match(line)
            match2 = pattern2.match(line)
            if match:
                mykey = match.group(1)
                sequences[mykey]=""
            elif match2:
                sequences[mykey] += line.upper()
    return sequences


fastafile = "upstream1000.fa"
sequences = parse_fasta(fastafile)
sequences


gidsequences = {}
for k,v in sequences.items():
    newk = nmassoc[k]
    gidsequences[newk] = v

gidsequences

##############
## background
i=0
foreground = {}
for k,v in gidsequences.items():
    i+=1
    if i > 100:
        break
    foreground[k] = v

import random
background = dict(random.sample(list(gidsequences.items()), 1000))

def scanDict(d, k):
    """
    Scans a dictionary of DNA sequences and extracts all substrings (motifs) of length k.

    Parameters:
        d (dict): A dictionary where keys are sequence names and values are DNA sequences.
        k (int): The length of the substrings (motifs) to extract.

    Returns:
        dict: A dictionary where keys are substrings (motifs) and values are the number of occurrences.
    """
    motif_counts = {}

    # Iterate through each sequence in the dictionary
    for seq_name, sequence in d.items():
        # Slide through the sequence to extract substrings of length k
        for i in range(len(sequence) - k + 1):
            motif = sequence[i:i + k]
            # Increment the count of the motif in the motif_counts dictionary
            if motif in motif_counts:
                motif_counts[motif] += 1
            else:
                motif_counts[motif] = 1

    return motif_counts


fgdMotifs = scanDict(foreground, k=8)
bgdMotifs = scanDict(background, k=8)


def getFET(foregroundMotifs, backgroundMotifs):
    a1 = 0
    a2 = 0
    b1 = 0
    b2 = 0
    for m,v in fgdMotifs.items():
            contingency_table  = [[3]]

fgdMotifs
bgdMotifs


'''
            if header:
                sequences[header] = "".join(sequence_lines)
            header = line[1:]  # Remove the '>'
            sequence_lines = []
        else:
            sequence_lines.append(line)

    if header:
        sequences[header] = "".join(sequence_lines)

    return sequences

    '''

# Function to filter sequences based on the names file
def filter_fasta(input_fasta, output_fasta, names_file):
    # Read the names to be selected
    sequence_names = read_sequence_names(names_file)

    # Parse the input FASTA file
    with open(input_fasta, 'r') as infile:
        sequences = parse_fasta(infile)

    # Write the filtered sequences to the output file
    with open(output_fasta, 'w') as outfile:
        for header, sequence in sequences.items():
            if header in sequence_names:
                outfile.write(f">{header}\n")
                outfile.write(f"{sequence}\n")

# Main function to handle command-line arguments
def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <input_fasta> <names_file> <output_fasta>")
        sys.exit(1)

    input_fasta = sys.argv[1]
    names_file = sys.argv[2]
    output_fasta = sys.argv[3]

    filter_fasta(input_fasta, output_fasta, names_file)

if __name__ == "__main__":
    main()
