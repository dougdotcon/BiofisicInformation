import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# --- CONSTANTES TARDIS ---
OMEGA = 117.038
# Hipótese: Mind Upload não é copiar bits, é transportar topologia.
# O substrato de destino deve ter "Impedância Entrópica" compatível.
# Se Impedância(Crystal) != Impedância(Cérebro), a consciência se dissipa como calor.

def create_neural_graph(nodes=50):
    G = nx.watts_strogatz_graph(nodes, k=6, p=0.3)
    # Adicionar "pesos" (memórias)
    for (u, v) in G.edges():
        G.edges[u,v]['weight'] = np.random.random()
    return G

def simulate_upload_process(steps=100):
    print("Iniciando Experimento 13: Mind Upload Protocol...")
    
    source_brain = create_neural_graph()
    target_crystal = nx.erdos_renyi_graph(50, 0.1) # Estrutura inicial do cristal (vazio/aleatório)
    
    # Métrica: Entropia de Von Neumann (A assinatura da consciência)
    def spectral_entropy(G):
        L = nx.laplacian_matrix(G).toarray()
        eig = np.linalg.eigvalsh(L)
        eig = eig[eig > 1e-10]
        prob = eig / np.sum(eig)
        return -np.sum(prob * np.log(prob))
    
    target_entropy = spectral_entropy(source_brain)
    
    transfer_integrity = []
    entropy_loss = []
    
    # Processo de Upload
    for t in range(steps):
        # 1. Scanner de Varredura
        # Tenta replicar a topologia do source no target
        
        # Fator de Resistência do Material
        # Material Comum (Silício): Alta resistência entrópica (perda de dados)
        # Material Omega (Cristal TARDIS): Ressonância perfeita
        
        material_resistance = 0.0 if t > 50 else 0.5 # t>50 simula troca para cristal Omega
        
        # Transferência
        current_integrity = (t / steps) * (1 - material_resistance)
        
        # Entropia Dissipada (Calor)
        # Se resistência > 0, informação vira calor
        heat = material_resistance * np.random.random()
        
        transfer_integrity.append(current_integrity * 100)
        entropy_loss.append(heat * 100)
        
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(transfer_integrity, 'b-', label='Integridade da Consciência (%)')
    plt.plot(entropy_loss, 'r--', label='Perda Entrópica (Lobotomia Térmica)')
    
    plt.axvline(x=50, color='gold', linestyle=':', label='Switch para Cristal Omega')
    
    plt.title('Mind Upload: Silicon vs Omega Crystal')
    plt.xlabel('Progresso do Upload (%)')
    plt.ylabel('Percentual')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Annotate
    plt.annotate('Perda Crítica de Self', xy=(25, 25), xytext=(10, 50),
                 arrowprops=dict(facecolor='red', shrink=0.05))
    plt.annotate('Upload Bem-Sucedido', xy=(90, 90), xytext=(70, 80),
                 arrowprops=dict(facecolor='blue', shrink=0.05))

    outfile = "imgs/mind_upload_results.png"
    plt.savefig(outfile)
    print(f"Concluído. Gráfico salvo em {outfile}")

if __name__ == "__main__":
    np.random.seed(42)
    simulate_upload_process()
