import numpy as np
import matplotlib.pyplot as plt

# --- CONSTANTES TARDIS ---
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
        
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(coherence_history, 'purple', linewidth=2)
    plt.axvline(x=100, color='gold', linestyle='--', label='Ativação Omega (t=100)')
    
    plt.title('Neural-Genomic Resonance: The Consciousness Interface')
    plt.xlabel('Tempo (ms)')
    plt.ylabel('Coerência de Fase (Sincronicidade)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Annotate
    plt.text(20, 0.2, 'Estado de Vigília (Baixo Acoplamento)', fontsize=10)
    plt.text(110, 0.8, 'Estado Omega (Alta Consciência)', fontsize=10, color='purple', fontweight='bold')
    
    outfile = "imgs/consciousness_resonance_results.png"
    plt.savefig(outfile)
    print(f"Concluído. Gráfico salvo em {outfile}")

if __name__ == "__main__":
    np.random.seed(117)
    simulate_consciousness_resonance()
