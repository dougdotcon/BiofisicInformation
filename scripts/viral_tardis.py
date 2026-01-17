import numpy as np
import matplotlib.pyplot as plt

# --- CONSTANTES TARDIS ---
OMEGA = 117.038
# Hipótese: Vírus são pacotes de alta entropia.
# Um genoma protegido por uma "Barreira TARDIS" (sequências fractais de alta complexidade)
# dissipa a energia do vírus antes que ele consiga se integrar.
# É um "Firewall Biológico".

def simulate_viral_infection(generations=100):
    print("Iniciando Experimento 11: Viral TARDIS Shield...")
    
    # Carga Viral (Entropia Externa)
    viral_load = np.linspace(0, 10, generations) # Carga aumenta exponencialmente
    
    # Resistência dos Sistemas
    # Sistema Natural (Linear): Defesa química limitada
    resistance_natural = 5.0
    
    # Sistema TARDIS (Exponencial): Defesa topológica fractal
    # Capacidade de dissipação escala com log(Omega)
    resistance_tardis = 5.0 * np.log(OMEGA) 
    
    health_natural = []
    health_tardis = []
    
    current_health_nat = 100
    current_health_tar = 100
    
    for v in viral_load:
        # Dano = Carga - Resistência
        # Se Carga > Resistência, dano ocorre.
        
        damage_nat = max(0, (v**2) - resistance_natural) # Vírus escala quadrático vs imunidade linear
        damage_tar = max(0, (v**2) - resistance_tardis)  # Vírus vs imunidade logaritmica aumentada
        
        current_health_nat -= damage_nat
        current_health_tar -= damage_tar
        
        health_natural.append(max(0, current_health_nat))
        health_tardis.append(max(0, current_health_tar))
        
    # Plot
    plt.figure(figsize=(10, 6))
    
    plt.plot(health_natural, 'r--', label='Imunidade Biológica Padrão')
    plt.fill_between(range(len(health_natural)), health_natural, color='red', alpha=0.1)
    
    plt.plot(health_tardis, 'b-', linewidth=3, label='Escudo TARDIS (Fractal)')
    plt.fill_between(range(len(health_tardis)), health_tardis, color='blue', alpha=0.1)
    
    plt.axhline(y=0, color='black', linestyle='-')
    
    plt.title('Viral Infection Survival: Standard vs TARDIS Shield')
    plt.xlabel('Viral Cycle (Load Increase)')
    plt.ylabel('System Integrity (%)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Annotate Collapse
    if 0 in health_natural:
        collapse_idx = health_natural.index(0)
        plt.annotate('Colapso Sistêmico', xy=(collapse_idx, 0), xytext=(collapse_idx-20, 20),
                     arrowprops=dict(facecolor='red', shrink=0.05))

    outfile = "imgs/viral_tardis_results.png"
    plt.savefig(outfile)
    print(f"Concluído. Gráfico salvo em {outfile}")

if __name__ == "__main__":
    simulate_viral_infection()
