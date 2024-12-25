import re

def count_kmers(sequence, k):
    """
    Count all substrings (k-mers) of length k in a sequence.
    
    Args:
        sequence (str): DNA or protein sequence.
        k (int): Length of the substrings.
    
    Returns:
        dict: A dictionary with substrings as keys and their counts as values.
    """
    kmer_counts = {}
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i + k]
        if kmer in kmer_counts:
            kmer_counts[kmer] += 1
        else:
            kmer_counts[kmer] = 1
    return kmer_counts

def process_fasta(file_path, k):
    """
    Process a FASTA file and count all k-mers in its sequences.
    
    Args:
        file_path (str): Path to the FASTA file.
        k (int): Length of the substrings (k-mers).
    
    Returns:
        dict: Combined counts of k-mers across all sequences.
    """
    header_pattern = re.compile(r'^>')  # Regular expression for FASTA headers
    combined_counts = {}
    with open(file_path, 'r') as file:
        sequence = ""
        for line in file:
            line = line.strip()
            if header_pattern.match(line):  # Match lines starting with '>'
                if sequence:  # Process the previous sequence
                    kmer_counts = count_kmers(sequence, k)
                    for kmer, count in kmer_counts.items():
                        if kmer in combined_counts:
                            combined_counts[kmer] += count
                        else:
                            combined_counts[kmer] = count
                    sequence = ""  # Reset for the next sequence
            else:
                sequence += line  # Append to the current sequence
        # Process the last sequence
        if sequence:
            kmer_counts = count_kmers(sequence, k)
            for kmer, count in kmer_counts.items():
                if kmer in combined_counts:
                    combined_counts[kmer] += count
                else:
                    combined_counts[kmer] = count
    return combined_counts

# Example Usage
file_path = "example.fasta"  # Replace with your FASTA file path
k = 5
kmer_counts = process_fasta(file_path, k)

# Print the results
for kmer, count in sorted(kmer_counts.items()):
    print(f"{kmer}: {count}")
