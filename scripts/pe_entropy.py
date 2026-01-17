import numpy as np
import matplotlib.pyplot as plt
import random

# --- CONSTANTES TARDIS ---
OMEGA = 117.038
# Hipótese: Prime Editing (PE) depende da estabilidade do híbrido DNA-RNA na etapa de transcrição reversa.
# A eficiência da escrita (PEG efficiency) é proporcional à estabilidade termodinâmica da estrutura 
# secundária do pegRNA (hairpins) e sua ressonância Omega.

def calculate_omega_resonance(sequence):
    """
    Calcula o quanto uma sequência ressoa com a constante Omega.
    Baseado na transformação de Fourier discreta da sequência mapeada numericamente.
    """
    mapping = {'A': 1, 'T': 2, 'C': 3, 'G': 4}
    num_seq = [mapping[b] for b in sequence]
    
    # FFT
    spectrum = np.abs(np.fft.fft(num_seq))
    freqs = np.fft.fftfreq(len(num_seq))
    
    # Busca pico na frequência Omega (normalizada pelo tamanho)
    target_freq = OMEGA % len(sequence) / len(sequence)
    
    # Encontra a amplitude na frequência mais próxima do alvo
    idx = (np.abs(freqs - target_freq)).argmin()
    resonance = spectrum[idx]
    
    return resonance

def simulate_pe_efficiency(num_samples=200):
    print("Iniciando Experimento 6: Prime Editing Omega Search...")
    
    efficiencies = []
    resonances = []
    
    for _ in range(num_samples):
        # Gerar pegRNA aleatório (PBS + RT template)
        length = random.randint(30, 50)
        pegRNA = "".join(random.choices("ATCG", k=length))
        
        # Calcular Ressonância Omega (Estabilidade Topológica)
        res = calculate_omega_resonance(pegRNA)
        
        # Simular Eficiência de Edição (Mock)
        # Hipótese: Eficiência = log(Ressonância) + Ruído
        # Estruturas mais estáveis (ressonantes) permitem melhor RT.
        
        efficiency = np.log(res + 1) * 10 + np.random.normal(0, 2)
        efficiency = max(0, min(100, efficiency)) # Clamp 0-100%
        
        resonances.append(res)
        efficiencies.append(efficiency)
        
    # Plot
    plt.figure(figsize=(10, 6))
    plt.scatter(resonances, efficiencies, c=efficiencies, cmap='viridis', alpha=0.7)
    plt.colorbar(label='PE Efficiency (%)')
    
    # Linha de tendência
    z = np.polyfit(resonances, efficiencies, 1)
    p = np.poly1d(z)
    plt.plot(resonances, p(resonances), "r--", alpha=0.5, label='Tendência TARDIS')
    
    plt.title('Prime Editing Efficiency vs Omega Resonance')
    plt.xlabel('Omega Resonance (Topological Stability)')
    plt.ylabel('Editing Efficiency (%)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    outfile = "imgs/pe_efficiency_results.png"
    plt.savefig(outfile)
    print(f"Concluído. Gráfico salvo em {outfile}")

if __name__ == "__main__":
    np.random.seed(117038)
    simulate_pe_efficiency()
