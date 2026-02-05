import numpy as np
import matplotlib.pyplot as plt

# --- CONSTANTES TAMESIS ---
OMEGA = 117.038
# Hipótese: Vírus são pacotes de alta entropia.
# Um genoma protegido por uma "Barreira TAMESIS" (sequências fractais de alta complexidade)
# dissipa a energia do vírus antes que ele consiga se integrar.
# É um "Firewall Biológico".

def simulate_viral_infection(generations=100):
    print("Iniciando Experimento 11: Viral TAMESIS Shield...")
    
    # Carga Viral (Entropia Externa)
    viral_load = np.linspace(0, 10, generations) # Carga aumenta exponencialmente
    
    # Resistência dos Sistemas
    # Sistema Natural (Linear): Defesa química limitada
    resistance_natural = 5.0
    
    # Sistema TAMESIS (Exponencial): Defesa topológica fractal
    # Capacidade de dissipação escala com log(Omega)
    resistance_TAMESIS = 5.0 * np.log(OMEGA) 
    
    health_natural = []
    health_TAMESIS = []
    
    current_health_nat = 100
    current_health_tar = 100
    
    for v in viral_load:
        # Dano = Carga - Resistência
        # Se Carga > Resistência, dano ocorre.
        
        damage_nat = max(0, (v**2) - resistance_natural) # Vírus escala quadrático vs imunidade linear
        damage_tar = max(0, (v**2) - resistance_TAMESIS)  # Vírus vs imunidade logaritmica aumentada
        
        current_health_nat -= damage_nat
        current_health_tar -= damage_tar
        
        health_natural.append(max(0, current_health_nat))
        health_TAMESIS.append(max(0, current_health_tar))
        
    # Plot
    plt.figure(figsize=(10, 6))
    
    plt.plot(health_natural, 'r--', label='Imunidade Biológica Padrão')
    plt.fill_between(range(len(health_natural)), health_natural, color='red', alpha=0.1)
    
    plt.plot(health_TAMESIS, 'b-', linewidth=3, label='Escudo TAMESIS (Fractal)')
    plt.fill_between(range(len(health_TAMESIS)), health_TAMESIS, color='blue', alpha=0.1)
    
    plt.axhline(y=0, color='black', linestyle='-')
    
    plt.title('Viral Infection Survival: Standard vs TAMESIS Shield')
    plt.xlabel('Viral Cycle (Load Increase)')
    plt.ylabel('System Integrity (%)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Annotate Collapse
    if 0 in health_natural:
        collapse_idx = health_natural.index(0)
        plt.annotate('Colapso Sistêmico', xy=(collapse_idx, 0), xytext=(collapse_idx-20, 20),
                     arrowprops=dict(facecolor='red', shrink=0.05))

    outfile = "../imgs/viral_TAMESIS_results.png"
    plt.savefig(outfile, dpi=300, bbox_inches="tight")
    print(f"Concluído. Gráfico salvo em {outfile}")

if __name__ == "__main__":
    simulate_viral_infection()
