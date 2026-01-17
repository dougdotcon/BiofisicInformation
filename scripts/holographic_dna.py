import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import entropy

# --- CONSTANTES TARDIS ---
# Hipótese: "Junk DNA" (Regiões não-codificantes) atuam como dissipadores de calor entrópico
# Protegendo os genes codificantes (Regiões codificantes) de flutuações.
# A razão ideal deve obedecer a proporção holográfica.

def generate_genome_segment(size=1000, coding_ratio=0.02):
    """
    Gera um segmento de genoma.
    coding_ratio ~ 2% (similar a humanos)
    """
    genome = np.zeros(size)
    n_coding = int(size * coding_ratio)
    
    # Distribui genes aleatoriamente
    indices = np.random.choice(range(size), n_coding, replace=False)
    genome[indices] = 1 # 1 = Gene Codificante, 0 = Não-codificante ("Junk")
    return genome

def holographic_noise_simulation(genome, intensity=0.1):
    """
    Simula ruído de informação (mutações/erros de transcrição) entrando no sistema.
    O ruído entra pela "borda" (não-codificante) e difunde para o "bulk" (genes).
    """
    size = len(genome)
    damage_map = np.zeros(size)
    
    # Ruído aleatório atinge o genoma
    noise_hits = int(size * intensity)
    hit_indices = np.random.randint(0, size, noise_hits)
    
    for idx in hit_indices:
        # Se bater em região não-codificante (0), o dano é absorvido (dissipado)
        # Se bater em gene (1), o dano é crítico
        
        if genome[idx] == 0:
            # Absorção entrópica: Junk DNA absorve o erro e reorganiza
            damage_map[idx] = 0.1 # Dano leve
        else:
            # Dano funcional crítico
            damage_map[idx] = 1.0 # Crítico
            
    return np.sum(damage_map)

def run_holographic_experiment():
    print("Iniciando Experimento 3: Fronteira Holográfica...")
    
    ratios = np.linspace(0.01, 0.99, 50) # Varia proporção de genes de 1% a 99%
    total_damages = []
    
    # Para cada razão coding/non-coding, testamos a resistência do sistema
    for r in ratios:
        damages = []
        for _ in range(50):
            g = generate_genome_segment(size=1000, coding_ratio=r)
            d = holographic_noise_simulation(g, intensity=0.2)
            damages.append(d)
        total_damages.append(np.mean(damages))
        
    # Análise Teórica TARDIS
    # O ponto ótimo deve ser onde a derivada da entropia é zero?
    # Ou onde o sistema maximiza a informação útil vs ruído.
    
    plt.figure(figsize=(10, 6))
    plt.plot(ratios * 100, total_damages, 'g-')
    plt.axvline(x=2.0, color='r', linestyle='--', label='Humano (~2% coding)')
    plt.axvline(x=98.0, color='b', linestyle='--', label='Bactéria (~90%+ coding)')
    
    plt.title('Holographic Shielding: Role of Non-Coding DNA')
    plt.xlabel('% of Coding Genes (Volume)')
    plt.ylabel('Systemic Damage (Information Loss)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Annotate TARDIS prediction
    plt.annotate('TARDIS Optima (High Complexity)', xy=(2, min(total_damages)+5), xytext=(20, 40),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    
    outfile = "imgs/holographic_dna_results.png"
    plt.savefig(outfile)
    print(f"Concluído. Gráfico salvo em {outfile}")

if __name__ == "__main__":
    np.random.seed(42)
    run_holographic_experiment()
