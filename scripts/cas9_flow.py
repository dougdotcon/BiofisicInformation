import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# --- CONSTANTES TARDIS ---
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
        # TARDIS: Otimização próxima a criticalidade Omega? 
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
                
    # Plot
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(history_eff, 'b-')
    plt.title('Evolução da Eficiência Catalítica (Informacional)')
    plt.xlabel('Iteração (Mutação)')
    plt.ylabel('Eficiência Global da Rede')
    plt.grid(True, alpha=0.3)
    
    plt.subplot(1, 2, 2)
    plt.plot(history_ent, 'r-')
    plt.title('Minimização da Entropia de Von Neumann')
    plt.xlabel('Iteração')
    plt.ylabel('Entropia Espectral')
    plt.grid(True, alpha=0.3)
    
    outfile = "imgs/cas9_optimization_results.png"
    plt.savefig(outfile)
    print(f"Concluído. Gráfico salvo em {outfile}")

if __name__ == "__main__":
    np.random.seed(137) # Fine structure constant seed
    optimize_cas9_topology()
