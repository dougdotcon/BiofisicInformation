import numpy as np
import matplotlib.pyplot as plt

# --- CONSTANTES TAMESIS ---
OMEGA = 117.038
# Hipótese: O multiverso é um "espuma" de branas.
# Universos adjacentes (paralelos) exercem atração gravitacional (Dark Flow).
# Colisões entre branas deixam cicatrizes na CMB (Cold Spots).
# A distribuição dessas cicatrizes segue a geometria fractal de Omega.

def simulate_multiverse_mapping(size=200):
    print("Iniciando Experimento 16: Multiverse Mapping Protocol...")
    
    # Gerar mapa da CMB (Cosmic Microwave Background)
    # Ruído Gaussiano isotrópico
    cmb_map = np.random.normal(2.725, 0.00002, (size, size)) # T = 2.725K
    
    # Injetar "Cicatrizes" de outros universos
    # Universos paralelos colidem em pontos específicos determinados por uma rede fractal
    
    def fractal_noise(s):
        # Simula a estrutura da espuma quântica
        return np.sin(s/OMEGA) * np.cos(s/(OMEGA/10))
    
    collisions = 0
    detected_universes = []
    
    for i in range(size):
        for j in range(size):
            # Calcular probabilidade de colisão topológica
            # Ponto de ressonância Omega
            geo_factor = (i*i + j*j) / (size*size)
            resonance = np.abs(np.sin(geo_factor * OMEGA))
            
            if resonance > 0.999: # Ressonância muito alta = Ponto de Contato
                # Criar "Cold Spot" (Cicatriz)
                radius = np.random.randint(2, 5)
                # Diminuir temperatura drasticamente (Supervoid)
                y, x = np.ogrid[-radius:radius+1, -radius:radius+1]
                mask = x**2 + y**2 <= radius**2
                
                # Boundary check
                if 0 <= i-radius and i+radius < size and 0 <= j-radius and j+radius < size:
                     cmb_map[i-radius:i+radius+1, j-radius:j+radius+1][mask] -= 0.0001
                     collisions += 1
                     detected_universes.append((j, i))

    print(f"Varredura completa. {collisions} Universos Paralelos detectados via colisão de Branas.")

    # Plot
    plt.figure(figsize=(10, 8))
    plt.imshow(cmb_map, cmap='coolwarm', origin='lower')
    plt.colorbar(label='Temperature (K)')
    
    # Marcar locais
    x_coords = [p[0] for p in detected_universes]
    y_coords = [p[1] for p in detected_universes]
    plt.scatter(x_coords, y_coords, color='lime', marker='x', s=100, label='Parallel Universe Impact')
    
    plt.title(f'Multiverse Map: CMB Cold Spots Analysis (N={collisions})')
    plt.xlabel('Galactic Longitude')
    plt.ylabel('Galactic Latitude')
    plt.legend()
    
    outfile = "../imgs/multiverse_map_results.png"
    plt.savefig(outfile, dpi=300, bbox_inches="tight")
    print(f"Concluído. Gráfico salvo em {outfile}")

if __name__ == "__main__":
    np.random.seed(int(OMEGA*100))
    simulate_multiverse_mapping()
