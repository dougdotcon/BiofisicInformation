import numpy as np
import matplotlib.pyplot as plt

# --- CONSTANTES TARDIS ---
OMEGA = 117.038
# Hipótese: Populações com genoma "Omega-Ressonante" possuem Vantagem Fitness Topológica (TFA).
# TFA = 1.618 (Golden Ratio) * log(Omega).
# Elas devem dominar o nicho ecológico não pela força (energia), mas pela eficiência (informação).

def simulate_population_dynamics(generations=200):
    print("Iniciando Experimento 9: Dinâmica Populacional Omega...")
    
    # Populações Iniciais
    pop_random = 500
    pop_omega = 10 # Começam em minoria absoluta!
    
    capacity = 1000 # Capacidade do ecossistema
    
    history_random = [pop_random]
    history_omega = [pop_omega]
    
    # Taxas de Reprodução (r) e Morte (d)
    # Random: Alta energia, alto desperdício (Estratégia r)
    r_random = 0.8
    d_random = 0.3 # Morrem fácil por entropia
    
    # Omega: Baixa energia, alta eficiência (Estratégia K-informacional)
    r_omega = 0.4 # Reproduzem devagar (complexidade)
    d_omega = 0.05 # Quase imortais (baixa entropia)
    
    for t in range(generations):
        # Competição por recursos (Modelo Lotka-Volterra simplificado)
        total_pop = pop_random + pop_omega
        pressure = total_pop / capacity
        
        # O "Omega Shield" protege contra a pressão ambiental
        # Random sofre muito com a pressão (falta de recursos = morte)
        # Omega sofre menos (eficiência metabólica)
        
        # Updates
        # Delta = (Nascimentos * (1-Pressão)) - (Mortes * Pressão_Entrópica)
        
        d_pop_random = (pop_random * r_random * (1 - pressure)) - (pop_random * d_random * (1 + pressure * 2))
        d_pop_omega = (pop_omega * r_omega * (1 - pressure)) - (pop_omega * d_omega * (1 + pressure * 0.5))
        
        pop_random += d_pop_random
        pop_omega += d_pop_omega
        
        # Limites
        pop_random = max(0, pop_random)
        pop_omega = max(0, pop_omega)
        
        history_random.append(pop_random)
        history_omega.append(pop_omega)
        
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(history_random, 'r--', label='Espécie Padrão (Alta Entropia)')
    plt.plot(history_omega, 'b-', linewidth=3, label='Espécie Omega (Eficiente)')
    
    plt.title('Substituição Populacional: A Vitória da Informação')
    plt.xlabel('Gerações')
    plt.ylabel('Indivíduos')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Anotação do "Crossover"
    crossover = np.argwhere(np.array(history_omega) > np.array(history_random))
    if len(crossover) > 0:
        idx = crossover[0][0]
        plt.annotate('Singularidade Omega', xy=(idx, history_omega[idx]), xytext=(idx+20, history_omega[idx]+100),
                     arrowprops=dict(facecolor='black', shrink=0.05))
    
    outfile = "imgs/population_omega_results.png"
    plt.savefig(outfile)
    print(f"Concluído. Gráfico salvo em {outfile}")

if __name__ == "__main__":
    np.random.seed(42)
    simulate_population_dynamics()
