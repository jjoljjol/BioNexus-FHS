library(Seurat)
library(ggplot2)

# BioNexus snRNA-seq Preprocessing Pipeline (Intel Optimized)

preprocess_multispecies <- function(counts_dir, species_name) {
  # 1. Ingest Raw Counts
  counts <- Read10X(data.dir = counts_dir)
  obj <- CreateSeuratObject(counts = counts, project = species_name)
  
  # 2. Quality Control (QC)
  # Calibrated for Nuclei (SnRNA-seq)
  obj[["percent.mt"]] <- PercentageFeatureSet(obj, pattern = "^MT-", ignore.case = TRUE)
  obj <- subset(obj, subset = nFeature_RNA > 200 & nFeature_RNA < 2500 & percent.mt < 5)
  
  # 3. Normalization (SCTransform optimized)
  obj <- SCTransform(obj, method = "glmGamPoi", verbose = FALSE)
  
  # 4. Dimensionality Reduction
  obj <- RunPCA(obj, verbose = FALSE)
  
  # Note: UMAP computation is accelerated via oneAPI if configured
  obj <- RunUMAP(obj, dims = 1:30, verbose = FALSE)
  
  return(obj)
}

# Example Usage:
# bovine_obj <- preprocess_multispecies("./data/bovine/", "Bovine")
print("BioNexus Preprocessing Module Loaded.")
