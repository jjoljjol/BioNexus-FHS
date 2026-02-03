import numpy as np
import pandas as pd
from scipy.stats import entropy
import torch

def calculate_information_gain(data, clusters):
    """
    Calculates Information Gain for each variable across clusters.
    """
    def shannon_entropy(labels):
        _, counts = np.unique(labels, return_counts=True)
        return entropy(counts, base=2)

    base_entropy = shannon_entropy(clusters)
    values, counts = np.unique(data, return_counts=True)
    weighted_entropy = 0
    for v, c in zip(values, counts):
        weighted_entropy += (c / len(data)) * shannon_entropy(clusters[data == v])
    
    return base_entropy - weighted_entropy

class FHSDistiller:
    def __init__(self, device='xpu'): # Default to Intel XPU
        self.device = device
        if device == 'xpu':
            import intel_extension_for_pytorch as ipex
            
    def distill_paralogs(self, expression_matrix, hub_genes):
        """
        Implementation of Functional Paralog Distillation (FPD).
        Calculates Functional Identity Score (S) based on connectivity to known hubs.
        """
        # Convert to tensor for IPEX acceleration
        matrix_t = torch.tensor(expression_matrix.values).to(self.device).float()
        hubs_t = torch.tensor(hub_genes.values).to(self.device).float()
        
        # Calculate correlation via matrix multiplication
        # Simplified logic for demonstration
        scores = torch.mm(matrix_t.T, hubs_t)
        return scores.cpu().numpy()

if __name__ == "__main__":
    print("BioNexus FHS Distiller Core Module Loaded.")
