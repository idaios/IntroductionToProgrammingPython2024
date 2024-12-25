import requests

def get_gene_coordinates(gene_name, species="human"):
    """
    Fetch the genomic coordinates for a gene by its common name using UCSC Table Browser.
    
    Args:
        gene_name (str): The common name of the gene (e.g., "BRCA2").
        species (str): The species name (default is "human").
    
    Returns:
        tuple: (chromosome, start, end, strand)
    """
    url = f"https://api.genome.ucsc.edu/getData/track?genome={species}&track=knownGene&table=knownGene"
    params = {
        "filter": f"geneName={gene_name}",
        "format": "json"
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        gene_info = data['gene']
        chromosome = gene_info['chrom']
        start = gene_info['txStart']
        end = gene_info['txEnd']
        strand = gene_info['strand']
        return chromosome, start, end, strand
    else:
        raise Exception(f"Error fetching gene coordinates: {response.status_code}")

def fetch_upstream_sequence(chromosome, start, end, strand, flank_length=1000, species="human"):
    """
    Fetch the upstream sequence of a gene from UCSC based on its coordinates.
    
    Args:
        chromosome (str): Chromosome name (e.g., "chr13").
        start (int): Start position of the gene.
        end (int): End position of the gene.
        strand (int): Strand of the gene (1 for "+" and -1 for "-").
        flank_length (int): Length of the upstream region to fetch.
        species (str): The species name (default is "human").
    
    Returns:
        str: The upstream sequence.
    """
    # Calculate the upstream region
    if strand == 1:  # "+" strand
        upstream_start = max(1, start - flank_length)
        upstream_end = start
    elif strand == -1:  # "-" strand
        upstream_start = end
        upstream_end = end + flank_length
    
    # Fetch the sequence from UCSC
    url = f"https://api.genome.ucsc.edu/getData/sequence?genome={species}&chrom={chromosome}&start={upstream_start}&end={upstream_end}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Error fetching upstream sequence: {response.status_code}")

# Example usage
gene_name = "BRCA2"  # Example gene common name
species = "human"

# Step 1: Get gene coordinates
chromosome, start, end, strand = get_gene_coordinates(gene_name, species)

# Step 2: Fetch the upstream sequence
upstream_sequence = fetch_upstream_sequence(chromosome, start, end, strand, flank_length=1000)

print(f"Upstream sequence for {gene_name}: {upstream_sequence}")
