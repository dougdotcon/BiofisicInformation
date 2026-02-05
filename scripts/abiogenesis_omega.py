import numpy as np
import matplotlib.pyplot as plt

# --- CONSTANTES TAMESIS ---
OMEGA = 117.038
# Hipótese: A Abiogênese (surgimento da vida) é estatisticamente impossível via acaso (Teorema do Macaco Infinito).
# A vida exige um "Atrator Topológico" (Omega) que colapsa a função de onda das possibilidades
# em direção à complexidade funcional.

def simulate_abiogenesis(attempts=1000):
    print("Iniciando Experimento 12: Omega Abiogenesis...")
    
    # Meta: Montar uma proteína funcional simples de 50 resíduos
    target_complexity = 50
    
    # Modelo 1: Acaso (Random Walk)
    # Probabilidade de adicionar o aminoácido correto: 1/20
    # Probabilidade cumulativa = (1/20)^N
    
    # Modelo 2: Atrator Omega (Guided Walk)
    # O universo "quer" criar vida. O campo Omega favorece configurações estáveis.
    # Probabilidade = 1/20 * Omega_Bootstrap
    
    progress_random = []
    progress_omega = []
    
    current_chain_random = 0
    current_chain_omega = 0
    
    for t in range(attempts):
        # 1. Tentativa Aleatória
        # Se acertar, cadeia cresce. Se errar, cadeia quebra (instabilidade).
        if np.random.random() < 0.05: # 1/20
            current_chain_random += 1
        else:
            current_chain_random = 0 # Quebra
            
        # 2. Tentativa Omega
        # O acerto é facilitado pela ressonância
        if np.random.random() < 0.05 * np.log(OMEGA): # Boost de probabilidade
            current_chain_omega += 1
        else:
            # Se errar, a memória holográfica pode "segurar" a estrutura por um tempo
            # Não zera imediatamente, decai.
            current_chain_omega = max(0, current_chain_omega - 1)
            
        progress_random.append(current_chain_random)
        progress_omega.append(current_chain_omega)
        
        if current_chain_omega >= target_complexity:
            print(f"Vida criada (Omega) na iteração {t}!")
            # Manter no gráfico como sucesso
            for _ in range(attempts - t - 1):
                progress_omega.append(target_complexity)
                progress_random.append(current_chain_random) # Random continua falhando
            break
            
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(progress_random, 'r-', alpha=0.5, label='Acaso (Random Chance)')
    plt.plot(progress_omega, 'b-', linewidth=2, label='Atrator Omega (Intelligent Design/Physics)')
    
    plt.axhline(y=target_complexity, color='green', linestyle='--', label='Complexidade Mínima para Vida')
    
    plt.title('Origin of Life: Random Chance vs Omega Attractor')
    plt.xlabel('Iterações (Tempo Cósmico)')
    plt.ylabel('Complexidade do Polímero')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    outfile = "../imgs/abiogenesis_results.png"
    plt.savefig(outfile, dpi=300, bbox_inches="tight")
    print(f"Concluído. Gráfico salvo em {outfile}")

if __name__ == "__main__":
    np.random.seed(117)
    simulate_abiogenesis()
