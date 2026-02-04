import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def apply_bionexus_style():
    """Applies the BioNexus Premium Design System to Matplotlib/Seaborn."""
    # Theme configuration
    sns.set_theme(style="white", palette="muted")
    
    # Custom color tokens (HSL-inspired)
    BIONEXUS_EMERALD = "#10b981"
    BIONEXUS_DEEP_SLATE = "#0f172a"
    BIONEXUS_ELECTRIC_BLUE = "#3b82f6"
    BIONEXUS_AMETHYST = "#a855f7"
    
    params = {
        'axes.facecolor': '#f8fafc',  # Slate-50 context
        'axes.edgecolor': '#cbd5e1',
        'axes.grid': True,
        'grid.color': '#e2e8f0',
        'grid.linestyle': '--',
        'grid.linewidth': 0.5,
        'axes.labelsize': 12,
        'axes.titlesize': 14,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'font.family': 'sans-serif',
        'font.sans-serif': ['Arial', 'Liberation Sans', 'DejaVu Sans', 'Inter'],
        'legend.frameon': True,
        'legend.facecolor': 'white',
        'legend.edgecolor': '#e2e8f0',
        'savefig.dpi': 300,
        'savefig.bbox': 'tight',
    }
    plt.rcParams.update(params)
    return [BIONEXUS_EMERALD, BIONEXUS_ELECTRIC_BLUE, BIONEXUS_AMETHYST, BIONEXUS_DEEP_SLATE]

def add_glass_effect(ax):
    """Adds a subtle drop shadow/glow effect to plot elements."""
    for patch in ax.patches:
        patch.set_linewidth(1.5)
        patch.set_edgecolor('white')  # Clean border
        patch.set_alpha(0.9)
