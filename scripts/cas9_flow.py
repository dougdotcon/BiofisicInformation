import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# --- CONSTANTES TAMESIS ---
OMEGA = 117.038
# Hipótese: Enzimas como Cas9 são "máquinas de Maxwell" que processam informação.
# A eficiência catalítica depende da topologia da rede de resíduos (aminoácidos).
# O fluxo de informação deve minimizar a entropia de Von Neumann.

def create_protein_network(n_residues=100):
    """
    Cria um grafo representando a proteína.
    Nós = Aminoácidos
    Arestas = Contatos físicos/químicos
    """
    # Modelo Small-World (propriedade comum em proteínas)
    G = nx.watts_strogatz_graph(n_residues, k=6, p=0.1)
    return G

def calculate_information_flow(G):
    """
    Calcula a eficiência do fluxo de informação usando
    Centralidade de Informação e Entropia do Grafo.
    """
    # Espectro do Laplaciano
    L = nx.laplacian_matrix(G).toarray().astype(float)
    eigenvalues = np.linalg.eigvalsh(L)
    
    # Entropia Espectral (Von Neumann)
    # S = - sum(lambda * log(lambda)) (normalizado)
    eigenvalues = eigenvalues[eigenvalues > 1e-10] # Remove zero
    prob = eigenvalues / np.sum(eigenvalues)
    entropy = -np.sum(prob * np.log(prob))
    
    # Eficiência Global 
    efficiency = nx.global_efficiency(G)
    
    return efficiency, entropy

def optimize_cas9_topology(generations=50):
    print("Iniciando Experimento 5: Otimização Topológica da Cas9...")
    
    G = create_protein_network(150) # Modelo simplificado da Cas9
    
    history_eff = []
    history_ent = []
    
    print(f"Otimizando rede de {len(G.nodes)} resíduos por {generations} gerações...")
    
    for gen in range(generations):
        # Mutação: Rewiring (mudança conformacional ou mutação pontual)
        G_mut = G.copy()
        
        # Escolhe aresta para remover e uma para adicionar
        edges = list(G_mut.edges())
        if edges:
            rem_edge = edges[np.random.randint(len(edges))]
            G_mut.remove_edge(*rem_edge)
            
        nodes = list(G_mut.nodes())
        u, v = np.random.choice(nodes, 2, replace=False)
        G_mut.add_edge(u, v)
        
        # Seleção: Critério Omega
        # A natureza busca MAXIMIZAR eficiência e MINIMIZAR entropia (Free Energy Minimization)
        # TAMESIS: Otimização próxima a criticalidade Omega? 
        # Vamos assumir critério simples: E = Efficiency - Entropy
        
        eff_orig, ent_orig = calculate_information_flow(G)
        eff_mut, ent_mut = calculate_information_flow(G_mut)
        
        score_orig = eff_orig * 10 - ent_orig
        score_mut = eff_mut * 10 - ent_mut
        
        if score_mut > score_orig:
            G = G_mut
            history_eff.append(eff_mut)
            history_ent.append(ent_mut)
        else:
            # Metropolis criterion (Temperatura térmica)
            if np.random.random() < 0.1: # Aceita ruim as vezes
                G = G_mut
                history_eff.append(eff_mut)
                history_ent.append(ent_mut)
            else:
                history_eff.append(eff_orig)
                history_ent.append(ent_orig)
                
    # Plot - Estilo Publicação Científica
    plt.figure(figsize=(12, 5), dpi=300)
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.size'] = 11
    plt.rcParams['axes.linewidth'] = 1.2
    
    # Subplot 1: Eficiência
    ax1 = plt.subplot(1, 2, 1)
    ax1.plot(history_eff, color='#1f77b4', linewidth=2.5, label='Network Efficiency')
    ax1.fill_between(range(len(history_eff)), history_eff, 
                    alpha=0.3, color='#1f77b4')
    ax1.set_title('(a) Catalytic Efficiency Evolution', 
                 fontsize=12, fontweight='bold', pad=10)
    ax1.set_xlabel('Optimization Iteration', fontsize=11)
    ax1.set_ylabel('Global Information Flow', fontsize=11)
    ax1.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    
    # Região de convergência
    conv_start = len(history_eff) * 2 // 3
    ax1.axvspan(conv_start, len(history_eff), alpha=0.1, color='green')
    ax1.text(conv_start + 3, min(history_eff) + 0.01, 'Convergence', 
            fontsize=9, style='italic', color='darkgreen')
    
    # Subplot 2: Entropia
    ax2 = plt.subplot(1, 2, 2)
    ax2.plot(history_ent, color='#d62728', linewidth=2.5, label='Von Neumann Entropy')
    ax2.fill_between(range(len(history_ent)), history_ent, 
                    alpha=0.3, color='#d62728')
    ax2.set_title('(b) Entropy Minimization', 
                 fontsize=12, fontweight='bold', pad=10)
    ax2.set_xlabel('Optimization Iteration', fontsize=11)
    ax2.set_ylabel('Spectral Entropy', fontsize=11)
    ax2.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    
    # Linha de tendência
    z = np.polyfit(range(len(history_ent)), history_ent, 2)
    p = np.poly1d(z)
    ax2.plot(range(len(history_ent)), p(range(len(history_ent))), 
            "--", color='black', linewidth=1.5, alpha=0.6, label='Trend')
    ax2.legend(fontsize=9, loc='upper right', frameon=True)
    
    plt.tight_layout()
    outfile = "../imgs/cas9_optimization_results.png"
    plt.savefig(outfile, dpi=300, bbox_inches='tight')
    print(f"Concluído. Gráfico salvo em {outfile}")

if __name__ == "__main__":
    np.random.seed(137) # Fine structure constant seed
    optimize_cas9_topology()
