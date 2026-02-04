# Visual Integrity Proof: Deterministic Agentic Plotting

This directory contains the original Python and R scripts used to generate the figures for the manuscript *"AI-Driven Democratization of Multi-Species Omics for Industrial Cultured Meat Optimization."*

## Methodology

To ensure maximum scientific integrity and prevent "AI Hallucinations," all visualizations were generated using a **Deterministic Agentic Plotting Pipeline**:

1.  **Data Backbone**: Raw transcriptomic matrices (CSV/h5ad) were ingested into the local BioNexus stack.
2.  **Script Generation**: The Antigravity Agent (Claude 3.5 Sonnet) was tasked with writing specific plotting scripts using `matplotlib`, `seaborn`, `Seurat`, and `ggplot2`.
3.  **Recursive Verification**: Scripts were executed and iteratively refined by the agent to ensure pixel-perfect alignment with the underlying data.
4.  **Final Rendering**: The `.png` files included in the submission are the direct output of these scripts.

## Directory Contents

- `plotting_main_figures.py`: The master script for generating Figures 1, 2, 4, and 5.
- `plotting_fhs_diagnostics.R`: R script for Figure 3 (SNR/CSS metrics).
- `plotting_orchestration_v2.py`: The script used for the enhanced Figure 6 schematic and throughput benchmark.

## reproducibility

Researchers can replicate these findings by running the scripts against the processed data available on Zenodo.
