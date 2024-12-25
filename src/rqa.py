import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from pyrqa.time_series import TimeSeries
from pyrqa.settings import Settings
from pyrqa.computation import RQAComputation
from pyrqa.neighbourhood import FixedRadius
from pyrqa.analysis_type import Classic
from pyrqa.metric import EuclideanMetric
import pandas as pd
import random
import os

os.getcwd()

def generate_structured_dna_sequence(length=10000, motif="ACGT", motif_repeat_interval=50, random_ratio=0.5):
    """
    Generate a structured DNA sequence with repeating motifs and random regions.
    
    Args:
        length (int): Total length of the sequence.
        motif (str): The repeating motif to include.
        motif_repeat_interval (int): How often the motif repeats.
        random_ratio (float): Proportion of random bases between motifs (0.0 to 1.0).
    
    Returns:
        str: Generated structured DNA sequence.
    """
    sequence = []
    motif_length = len(motif)
    random_section_length = int(motif_repeat_interval * random_ratio)
    
    while len(sequence) < length:
        # Add the repeating motif
        sequence.append(motif)
        
        # Add a random section
        random_section = ''.join(random.choices("ACGT", k=random_section_length))
        sequence.append(random_section)
    
    # Join the parts and trim to the desired length
    structured_sequence = ''.join(sequence)[:length]
    return structured_sequence

# Generate a structured DNA sequence
structured_dna_sequence = generate_structured_dna_sequence(
    length=1000,
    motif="ACGTACACACATTTA",  # Example repeating motif
    motif_repeat_interval=50,  # Insert motif approximately every 50 bases
    random_ratio=0.5  # 50% of the interval is random
)

# Display the first 200 bases for verification
print("Structured DNA Sequence (first 200 bases):", structured_dna_sequence[:200])

# Optionally save the sequence to a file
with open("structured_dna_sequence_10kb.txt", "w") as file:
    file.write(structured_dna_sequence)



# Function to generate a random DNA sequence of specified length
def generate_random_dna_sequence(length=2000):
    return ''.join(random.choices("ACGT", k=length))

# Generate a 10,000 base pair DNA sequence
random_dna_sequence = generate_random_dna_sequence()

# Display the first 100 bases for verification
print("Random DNA Sequence (first 100 bases):", random_dna_sequence[:100])

# Optionally save the sequence to a file
with open("random_dna_sequence_10kb.txt", "w") as file:
    file.write(random_dna_sequence)


def arrange_states_on_nd_sphere(states, dim, radius=1):
    """
    Arrange states evenly on the surface of an n-dimensional sphere.

    Args:
        states (list of str): The set of states to arrange (e.g., k-mers ['AA', ..., 'TT']).
        dim (int): Number of dimensions for the sphere.
        radius (float): Radius of the sphere.

    Returns:
        dict: Mapping of states to their n-dimensional coordinates.
    """
    n_states = len(states)
    coords = []
    for _ in range(n_states):
        point = np.random.normal(0, 1, dim)
        point /= np.linalg.norm(point)
        coords.append(point * radius)
    return {states[i]: coords[i] for i in range(n_states)}

def generate_kmers(sequence, k, step):
    """
    Generate k-mers from a sequence with a specified step size.

    Args:
        sequence (str): Input sequence (e.g., 'ACGTACGT').
        k (int): Length of k-mers to generate.
        step (int): Step size for generating k-mers.

    Returns:
        list of str: List of k-mers.
    """
    return [sequence[i:i + k] for i in range(0, len(sequence) - k + 1, step)]




def generate_cgr(sequence, states, dim, k):
    """
    Generate a Chaos Game Representation (CGR).

    Args:
        sequence (list of str): The sequence to be analyzed (e.g., k-mers ['A', 'C', 'G', 'T']).
        states (list of str): The set of possible states (e.g., k-mers ['AA', 'AC', ..., 'TT']).
        dim (int): The number of dimensions for the CGR.
        k (float): The fraction to move towards the target state (e.g., 1/2 for halfway).

    Returns:
        np.ndarray: Array of CGR points.
    """
    state_to_coord = arrange_states_on_nd_sphere(states, dim)
    current_position = np.zeros(dim)
    trajectory = [current_position]
    for symbol in sequence:
        if symbol in state_to_coord:
            target = state_to_coord[symbol]
            current_position = current_position + (target - current_position) / k
            trajectory.append(current_position)
    return np.array(trajectory), state_to_coord



from scipy.spatial.distance import cdist

def compute_recurrence_matrix(trajectory, embedding_dimension=2, time_delay=1, radius=0.1):
    """
    Compute the recurrence matrix explicitly using a distance-based approach.

    Args:
        trajectory (np.ndarray): The trajectory data from CGR.
        embedding_dimension (int): The embedding dimension for recurrence.
        time_delay (int): The time delay for embedding.
        radius (float): The neighborhood radius for recurrence detection.

    Returns:
        np.ndarray: The computed recurrence matrix.
    """
    # Ensure the trajectory is in the correct format and type
    #trajectory = trajectory.astype(np.float32).flatten()

    # Create the embedded trajectory
    embedded_trajectory = []
    for i in range(len(trajectory) - (embedding_dimension - 1) * time_delay):
        embedded_point = [
            trajectory[i + j * time_delay]
            for j in range(embedding_dimension)
        ]
        embedded_trajectory.append(embedded_point)
    embedded_trajectory = np.array(embedded_trajectory)

    # Compute pairwise distances
    distances = cdist(embedded_trajectory, embedded_trajectory, metric="euclidean")

    # Apply the radius threshold to create the recurrence matrix
    recurrence_matrix = (distances <= radius).astype(int)

    return recurrence_matrix

def apply_rqa(trajectory, embedding_dimension=2, time_delay=1, radius=0.1):
    """
    Apply Recurrence Quantification Analysis (RQA).

    Args:
        trajectory (np.ndarray): The trajectory data from CGR.
        embedding_dimension (int): The embedding dimension for RQA.
        time_delay (int): The time delay for RQA.
        radius (float): The radius for neighborhood determination.

    Returns:
        dict: RQA results.
    """
    #trajectory = trajectory.astype(np.float16)
    flattened_trajectory = trajectory[:,0] #trajectory.flatten()
    print(flattened_trajectory)
    time_series = TimeSeries(flattened_trajectory, embedding_dimension=embedding_dimension, time_delay=time_delay)
    settings = Settings(
        time_series=time_series,
        neighbourhood=FixedRadius(radius),
        similarity_measure=EuclideanMetric,
        theiler_corrector=1)  
    
    computation = RQAComputation.create(settings)
    result = computation.run()
    recurrence_matrix = compute_recurrence_matrix(flattened_trajectory, embedding_dimension=embedding_dimension, 
                                                    time_delay=time_delay, radius=radius)
    return {
        'Recurrence Rate': result.recurrence_rate,
        'Determinism': result.determinism,
        'Laminarity': result.laminarity,
        'Trapping Time': result.trapping_time,
        'Longest Diagonal Line': result.longest_diagonal_line,
        'points': result.recurrence_points,
        'recurrence_matrix':recurrence_matrix
    }, result

from pyrqa.computation import RPComputation




def plot_recurrence_matrix(recurrence_matrix):
    """
    Plot the recurrence matrix.

    Args:
        result: RQA computation result containing the recurrence matrix.
    """
    plt.figure(figsize=(6, 6))
    plt.imshow(recurrence_matrix, cmap='binary', origin='lower')
    plt.title("Recurrence Plot")
    plt.xlabel("Time")
    plt.ylabel("Time")
    plt.colorbar(label="Recurrence")
    plt.show()

if __name__ == "__main__":
    # Parameters for CGR and RQA
    dim = 2  # 2D CGR
    k = 2  # Fraction of movement (1/k)
    kmer_length = 2  # Dinucleotides
    step_size = 1  # Step size for k-mer generation
    input_sequence = structured_dna_sequence
    # Generate k-mers
    kmers = generate_kmers(input_sequence, kmer_length, step_size)

    # Define states (all possible dinucleotides)
    alphabet = "ACGT"
    states = ["".join(p) for p in product(alphabet, repeat=kmer_length)]

    # Generate CGR
    trajectory, state_coords = generate_cgr(kmers, states, dim, k)

    # Plot the 2D CGR
    fig, ax = plt.subplots()
    #trajectory
    trajectory = np.array(trajectory)
    ax.plot(trajectory[:, 0], trajectory[:, 1], marker='o', label='CGR Trajectory')
    for state, coord in state_coords.items():
        ax.text(coord[0], coord[1], state, fontsize=10)
    ax.set_title("2D Chaos Game Representation")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    plt.legend()
    plt.show()
    # Apply RQA
    rqa_results, rqa_result_obj = apply_rqa(trajectory, embedding_dimension=2, time_delay=1, radius=0.1)
    # Print RQA results
    print("RQA Results:")
    for key, value in rqa_results.items():
        print(f"{key}: {value}")
    # Plot Recurrence Plot
    rmat = pd.DataFrame(rqa_results["recurrence_matrix"])
    rmat.to_csv('recurmat.csv')
    plot_recurrence_matrix(rqa_results['recurrence_matrix'])



 