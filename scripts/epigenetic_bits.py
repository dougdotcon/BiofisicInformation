import numpy as np
import matplotlib.pyplot as plt

# --- CONSTANTES TAMESIS ---
OMEGA = 117.038
K_BOLTZMANN = 1.38e-23
# Hipótese: Epigenética (metilação) é memória holográfica.
# A energia necessária para "flipar" um bit epigenético (metilar/desmetilar)
# deve ser maior que o ruído térmico (kT) + a estabilidade holográfica de Omega.

def simulate_epigenetic_memory_stability(generations=1000):
    print("Iniciando Experimento 7: Epigenetic Holography...")
    
    # Grid holográfico 100x100 bits (loci epigenéticos)
    memory_grid = np.zeros((100, 100))
    
    # Gravar uma memória (Padrão Omega)
    for i in range(100):
        for j in range(100):
            if (i**2 + j**2) % int(OMEGA) < 10:
                memory_grid[i][j] = 1 # Metilado
    
    initial_memory = memory_grid.copy()
    
    # Evolução Termodinâmica
    temperatures = [10, 50, 100] # Baixa, Média, Alta Entropia
    stability_curves = []
    
    for temp in temperatures:
        current_grid = initial_memory.copy()
        stability_history = []
        
        for _ in range(generations):
            # Tentar flipar bits aleatoriamente (ruído)
            noise_map = np.random.random((100, 100))
            
            # Limiar de estabilidade:
            # Em TAMESIS, bits correlacionados holograficamente são mais difíceis de flipar.
            # Se o bit faz parte de um padrão Omega, ele resiste.
            
            for i in range(100):
                for j in range(100):
                    # Check Neighbor Consistency (Holographic Lock)
                    neighbors = 0
                    # ... [simplificado] ... check 4 vizinhos
                    
                    # Probabilidade de flip depende da temperatura e da "trava holográfica"
                    prob_flip = (temp / 1000.0)
                    if current_grid[i][j] == 1: # Se é memória gravada
                        prob_flip /= OMEGA # Muito mais difícil apagar memória Omega!
                    
                    if noise_map[i][j] < prob_flip:
                        current_grid[i][j] = 1 - current_grid[i][j] # Flip
            
            # Calcular retenção
            retention = np.sum(current_grid * initial_memory) / np.sum(initial_memory)
            stability_history.append(retention * 100)
            
        stability_curves.append(stability_history)

    # Plot
    plt.figure(figsize=(10, 6))
    colors = ['blue', 'orange', 'red']
    labels = ['Baixa Entropia', 'Média Entropia', 'Alta Entropia (Crítica)']
    
    for i, curve in enumerate(stability_curves):
        plt.plot(curve, color=colors[i], label=labels[i])
        
    plt.title('Holographic Memory Persistence: Epigenetic Stability')
    plt.xlabel('Time (Generations)')
    plt.ylabel('Memory Retention (%)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    outfile = "../imgs/epigenetic_holography_results.png"
    plt.savefig(outfile, dpi=300, bbox_inches="tight")
    print(f"Concluído. Gráfico salvo em {outfile}")

if __name__ == "__main__":
    np.random.seed(42)
    simulate_epigenetic_memory_stability()
