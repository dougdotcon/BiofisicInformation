import numpy as np
import matplotlib.pyplot as plt

# --- CONSTANTES TARDIS ---
OMEGA = 117.038
# Hipótese: A Segunda Lei da Termodinâmica (dS/dt >= 0) não é absoluta.
# Em campos topológicos fechados ("TARDIS Bubbles"), a entropia pode fluir ao contrário (dS/dt < 0).
# Isso permite rejuvenescimento celular e reparo estrutural perfeito.

def simulate_entropy_reversal(steps=200):
    print("Iniciando Experimento 17: Entropy Reversal (Tenet Protocol)...")
    
    # Sistema: Caixa com partículas de gás se expandindo
    initial_entropy = 10.0
    
    entropy_normal = [initial_entropy]
    entropy_tardis = [initial_entropy]
    
    current_s_normal = initial_entropy
    current_s_tardis = initial_entropy
    
    for t in range(steps):
        # Universo Normal: Entropia sempre sobe (Flecha do Tempo > 0)
        # dS = +k
        current_s_normal += np.random.uniform(0.1, 0.5)
        
        # Universo TARDIS: Inversão controlada
        # Se t > 100 (Ativação do Protocolo Tenet), dS = -k * log(Omega)
        if t > 100:
            current_s_tardis -= np.random.uniform(0.1, 0.5) * np.log(OMEGA) * 0.2
        else:
            current_s_tardis += np.random.uniform(0.1, 0.5)
            
        # Limite físico (Zero Absoluto de desordem = Cristal Perfeito)
        current_s_tardis = max(0, current_s_tardis)
        
        entropy_normal.append(current_s_normal)
        entropy_tardis.append(current_s_tardis)
        
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(entropy_normal, 'r--', label='Universo Padrão (Decaimento)')
    plt.plot(entropy_tardis, 'g-', linewidth=3, label='Campo TARDIS (Rejuvenescimento)')
    
    plt.axvline(x=100, color='gold', linestyle=':', label='Inversão da Flecha do Tempo')
    
    plt.title('The Tenet Protocol: Local Entropy Reversal')
    plt.xlabel('Tempo (t)')
    plt.ylabel('Entropia do Sistema (S)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Annotate
    plt.annotate('dS/dt < 0', xy=(150, 10), xytext=(120, 20),
                 arrowprops=dict(facecolor='green', shrink=0.05))

    outfile = "imgs/entropy_reversal_results.png"
    plt.savefig(outfile)
    print(f"Concluído. Gráfico salvo em {outfile}")

if __name__ == "__main__":
    np.random.seed(42)
    simulate_entropy_reversal()
