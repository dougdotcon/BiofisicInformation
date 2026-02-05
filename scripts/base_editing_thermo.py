import numpy as np
import matplotlib.pyplot as plt

# --- CONSTANTES TAMESIS ---
OMEGA = 117.038
# Hipótese: Base Editing (C->T) é uma transição de tunelamento quântico.
# Ao contrário do Cas9 (que rasga a topologia -> DSB), o BE apenas rotaciona a informação.
# Delta S (Entropia) do BE deve ser logarítmicamente menor que Cas9.

def simulate_editing_thermodynamics():
    print("Iniciando Experimento 8: Base Editing Thermodynamics...")
    
    # Energias de ativação (hipotéticas, em unidades kT)
    # DSB (Cas9) = Alta barreira, rompimento topológico crítico
    E_dsb = 50.0 
    
    # Base Editing = Rotação de bit (Deaminação)
    E_be = 15.0
    
    # Simulação de Monte Carlo para taxa de sucesso no tempo
    time_steps = np.linspace(0, 100, 200)
    
    # Probabilidade de transição: P = exp(-DeltaE / kT) * Omega_Factor
    # Omega_Factor: BE preserva a estrutura holográfica (fator > 1), Cas9 rompe (fator < 1)
    
    success_rate_cas9 = []
    success_rate_be = []
    
    entropy_generated_cas9 = []
    entropy_generated_be = []
    
    for t in time_steps:
        # Rate equation: dN/dt = k * (N0 - N)
        # k ~ exp(-E)
        
        k_cas9 = np.exp(-E_dsb / 20.0) * (1.0 / np.sqrt(OMEGA)) # Penalidade topológica
        k_be = np.exp(-E_be / 20.0) * np.sqrt(OMEGA) # Bônus topológico
        
        # Cumulative success (Saturação em 100%)
        p_cas9 = 1 - np.exp(-k_cas9 * t)
        p_be = 1 - np.exp(-k_be * t)
        
        success_rate_cas9.append(p_cas9 * 100)
        success_rate_be.append(p_be * 100)
        
        # Entropia gerada (Desperdício de energia/dano colateral)
        # S ~ Probabilidade * Energia Dissipada
        entropy_generated_cas9.append(p_cas9 * E_dsb * OMEGA) # DSB gera muito calor entrópico
        entropy_generated_be.append(p_be * E_be)
        
    # Plot
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    ax1.set_xlabel('Time (Simulation Steps)')
    ax1.set_ylabel('Editing Efficiency (%)', color='tab:blue')
    ax1.plot(time_steps, success_rate_cas9,  color='tab:blue', linestyle='--', label='Cas9 (DSB)')
    ax1.plot(time_steps, success_rate_be, color='tab:blue', linewidth=2, label='Base Editor (Quantum Tunneling)')
    ax1.tick_params(axis='y', labelcolor='tab:blue')
    ax1.legend(loc='upper left')
    
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    ax2.set_ylabel('Collateral Entropy (Information Loss)', color='tab:red')  
    ax2.plot(time_steps, entropy_generated_cas9, color='tab:red', linestyle='--', label='Cas9 Entropy')
    ax2.plot(time_steps, entropy_generated_be, color='tab:red', linewidth=2, label='BE Entropy')
    ax2.tick_params(axis='y', labelcolor='tab:red')
    # ax2.legend(loc='upper right')
    
    plt.title('Thermodynamic Comparison: Cas9 vs Base Editing')
    fig.tight_layout()  
    plt.grid(True, alpha=0.3)
    
    outfile = "../imgs/base_editing_thermo_results.png"
    plt.savefig(outfile, dpi=300, bbox_inches="tight")
    print(f"Concluído. Gráfico salvo em {outfile}")

if __name__ == "__main__":
    np.random.seed(137)
    simulate_editing_thermodynamics()
