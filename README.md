# BioNexus-FHS: Information-Theoretic Distillation for Multi-Species Omics

BioNexus-FHS is a computationally accessible bioinformatics framework designed for the industrial scale-up of cultured meat. It leverages the **Functional Hub Scoring (FHS)** algorithm to resolve genomic complexity and identify high-fidelity cell lines across diverse livestock species (Bovine, Porcine, Piscine).

## Key Features
- **Information-Theoretic Feature Selection**: Identifies regulatory hubs (e.g., *THRSP*, *KLF4*) by maximizing Information Gain.
- **Functional Paralog Distillation (FPD)**: Resolves biological noise from duplicate genes (e.g., *pax7a/b*).
- **Intel® XPU Acceleration**: Optimized for high-performance execution on portable hardware using oneAPI and IPEX.

## Architecture
- `fhs_distillation.py`: Core Python implementation for the FHS algorithm.
- `snrna_preproc_intel.R`: Scalable preprocessing pipeline built on Seurat v5.0.

## Installation & Setup
1. **Configure Environment**:
   ```bash
   source /opt/intel/oneapi/setvars.sh
   export USE_XPU=1
   ```
2. **Install Dependencies**:
   ```bash
   pip install torch intel-extension-for-pytorch
   Rscript -e "install.packages('Seurat')"
   ```

## Citation
If you use this framework in your research, please cite:
*Park, J. (2026). AI-Driven Multi-Species Omics for Industrial Cultured Meat Optimization. Nature Communications (In Preparation).*

## License
This project is licensed under the **MIT License**.
