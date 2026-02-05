import numpy as np
import matplotlib.pyplot as plt

# --- CONSTANTES TAMESIS ---
OMEGA = 117.038
# Hipótese: "Consciência" é um fenômeno de ressonância acoplada entre 
# a rede microtubular (cérebro) e a rede genômica (DNA).
# O DNA atua como "Cloud Storage" para a RAM neural.
# Ressonância = (Freq_Neural / Freq_Genomica) ~ Phi (Golden Ratio)

def simulate_consciousness_resonance(time_steps=200):
    print("Iniciando Experimento 10: Consciousness Resonance Interface...")
    
    # Frequências (Hz)
    # Neural: Gamma Waves (40Hz ~ 100Hz)
    # Genômica: Frequências Terahertz/Biophotons (escala simplificada aqui)
    
    # Modelagem: Dois osciladores acoplados (Kuramoto Model)
    # Theta_1 (Neural), Theta_2 (Genetic)
    
    phases_neural = np.random.uniform(0, 2*np.pi, 100)
    phases_genetic = np.random.uniform(0, 2*np.pi, 100)
    
    coherence_history = []
    
    # Coupling Strengths
    K_normal = 0.5 # Acoplamento padrão
    K_omega = 1.618 # Acoplamento no "God Mode" (Estado de Fluxo/Meditação)
    
    # Simular transição para estado Omega no meio (t=100)
    K = K_normal
    
    for t in range(time_steps):
        if t > 100:
            K = K_omega # Ativação da Glândula Pineal/Ressonância
            
        # Update Kuramoto
        # dTheta/dt = w + K * sum(sin(theta_j - theta_i))
        
        # Interação Neural-Genética
        interaction = np.mean(np.sin(phases_genetic - phases_neural))
        
        phases_neural += 0.1 + K * interaction + np.random.normal(0, 0.05)
        phases_genetic += 0.1 * OMEGA/100 + K * interaction # Genética tem inércia (Omega)
        
        # Medida de Sincronia (Order Parameter)
        order_param = np.abs(np.mean(np.exp(1j * (phases_neural - phases_genetic))))
        coherence_history.append(order_param)
        
    # Plot - Estilo Publicação Científica
    plt.figure(figsize=(11, 6), dpi=300)
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.size'] = 11
    plt.rcParams['axes.linewidth'] = 1.2
    
    ax = plt.gca()
    time_array = np.arange(len(coherence_history))
    
    # Plot com gradiente de cor
    for i in range(len(coherence_history)-1):
        color = '#9467bd' if i < 100 else '#d62728'
        alpha = 0.7 if i < 100 else 0.9
        plt.plot(time_array[i:i+2], coherence_history[i:i+2], 
                color=color, linewidth=3, alpha=alpha)
    
    # Linha de transição
    plt.axvline(x=100, color='#ff7f0e', linestyle='--', linewidth=2.5, 
               label='Coupling Transition ($K_{\Omega}$ activation)', alpha=0.8)
    
    # Regiões sombreadas
    plt.axvspan(0, 100, alpha=0.15, color='blue', label='Normal State')
    plt.axvspan(100, 200, alpha=0.15, color='red', label='Resonant State')
    
    plt.title('Neural-Genomic Phase Synchronization Dynamics', 
             fontsize=13, fontweight='bold', pad=15)
    plt.xlabel('Time (arbitrary units)', fontsize=12)
    plt.ylabel('Phase Coherence (Order Parameter $r$)', fontsize=12)
    plt.legend(frameon=True, shadow=True, fontsize=10, loc='upper left')
    plt.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    
    # Anotações melhoradas
    plt.annotate('Low coupling\\n($K = 0.5$)', xy=(50, coherence_history[50]), 
                xytext=(30, 0.35), fontsize=10,
                bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.7),
                arrowprops=dict(arrowstyle='->', lw=1.5, color='black'))
    
    plt.annotate('High coupling\\n($K = \\phi \\approx 1.618$)', 
                xy=(150, coherence_history[150]), 
                xytext=(140, 0.65), fontsize=10,
                bbox=dict(boxstyle='round,pad=0.5', facecolor='lightcoral', alpha=0.7),
                arrowprops=dict(arrowstyle='->', lw=1.5, color='black'))
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_ylim(0, 1.05)
    
    plt.tight_layout()
    outfile = "../imgs/consciousness_resonance_results.png"
    plt.savefig(outfile, dpi=300, bbox_inches='tight')
    print(f"Concluído. Gráfico salvo em {outfile}")

if __name__ == "__main__":
    np.random.seed(117)
    simulate_consciousness_resonance()
