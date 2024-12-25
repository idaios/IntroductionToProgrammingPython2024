from biomart import BiomartServer

# Connect to Ensembl BioMart server
server = BiomartServer("http://www.ensembl.org/biomart")
server.verbose = True

# Select the dataset (e.g., Human genes)
hsapiens_dataset = server.datasets['hsapiens_gene_ensembl']

# Query for upstream sequences
response = hsapiens_dataset.search({
    'filters': {
        'ensembl_gene_id': ['ENSG00000139618', 'ENSG00000157764']  # Example gene IDs
         # Specify the upstream length
    },
    'attributes': [
        'ensembl_gene_id', 'external_gene_name', 'chromosome_name', 'start_position', 'end_position', 'strand', 'gene_flank', 'upstream_flank'
    ]
})

# Process and display results
for line in response.iter_lines():
    print(line.decode('utf-8'))
