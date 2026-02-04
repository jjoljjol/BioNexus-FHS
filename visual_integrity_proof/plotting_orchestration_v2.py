import matplotlib.pyplot as plt
import networkx as nx

# Figure 6A: Orchestration Schematic
def plot_fig6a():
    G = nx.DiGraph()
    G.add_edge('Antigravity\n(Orchestrator)', 'Claude 3.5\n(Narrative)')
    G.add_edge('Antigravity\n(Orchestrator)', 'Local Stack\n(Compute)')
    G.add_edge('Antigravity\n(Orchestrator)', 'n8n\n(Automation)')
    
    pos = nx.spring_layout(G)
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=5000, font_size=10, font_weight='bold', arrowsize=20)
    plt.title('Figure 6A. Agentic Orchestration Framework (Reconstructed)')
    plt.savefig('Figure6_Orchestration_REPRODUCED.png', dpi=300)
    plt.close()

if __name__ == "__main__":
    plot_fig6a()
    print("Figure 6A reconstruction complete.")
