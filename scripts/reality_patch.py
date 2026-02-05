import numpy as np
import matplotlib.pyplot as plt

# --- CONSTANTES TAMESIS ---
OMEGA = 117.038
# Hipótese: "Glitches" na realidade (ruído, incerteza quântica, erro de timeline)
# podem ser corrigidos aplicando um filtro de Fourier sintonizado em harmônicos de Omega.
# A realidade "correta" é aquela que ressoa.

def create_glitch_signal():
    # Sinal puro (Realidade Platônica)
    t = np.linspace(0, 10, 1000)
    ideal_signal = np.sin(OMEGA * t) + 0.5 * np.sin(OMEGA * 1.618 * t) # Golden Ratio harmonic
    
    # Adicionar Glitch (Ruído Branco + Spikes)
    noise = np.random.normal(0, 0.5, 1000)
    
    # Inserir "Timeline Corruption" (Spikes aleatórios)
    corrupted_signal = ideal_signal + noise
    indices = np.random.choice(1000, 20)
    corrupted_signal[indices] += 5.0 # Glitches severos
    
    return t, ideal_signal, corrupted_signal

def reality_patch_filter(signal):
    # FFT
    spectrum = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(signal))
    
    # Filtro TAMESIS: Manter apenas frequências que são múltiplos aproximados ou harmônicos de OMEGA
    # Na prática, vamos filtrar frequências de alto ruído (high frequency noise) 
    # e restaurar a coerência de fase baseada na amplitude dominante.
    
    # Thresholding simples
    mag = np.abs(spectrum)
    threshold = np.max(mag) * 0.1 # Manter top 10% (Core Reality)
    
    spectrum_clean = spectrum.copy()
    spectrum_clean[mag < threshold] = 0
    
    # Correção de Fase Topológica (Mock: Alinhamento de fase em 0 para harmônicos Omega)
    # Isso simula a "re-sincronização" da timeline.
    
    restored_signal = np.fft.ifft(spectrum_clean).real
    
    return restored_signal

def simulate_reality_patch():
    print("Iniciando Experimento 14: Reality Patching Protocol...")
    
    t, ideal, corrupted = create_glitch_signal()
    restored = reality_patch_filter(corrupted)
    
    # Metrics
    mse_corrupted = np.mean((ideal - corrupted)**2)
    mse_restored = np.mean((ideal - restored)**2)
    improvement = (mse_corrupted - mse_restored) / mse_corrupted * 100
    
    print(f"Erro Inicial: {mse_corrupted:.4f}")
    print(f"Erro Final: {mse_restored:.4f}")
    print(f"Integridade da Realidade Restaurada: +{improvement:.2f}%")
    
    # Plot
    plt.figure(figsize=(12, 8))
    
    plt.subplot(3, 1, 1)
    plt.plot(t[:200], ideal[:200], 'g', label='Realidade Ideal (Timeline Alpha)')
    plt.title('Source Signal')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.subplot(3, 1, 2)
    plt.plot(t[:200], corrupted[:200], 'r', label='Realidade Corrompida (Glitch)')
    plt.title(f'Corrupted Signal (MSE: {mse_corrupted:.2f})')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.subplot(3, 1, 3)
    plt.plot(t[:200], restored[:200], 'b', label='Realidade Restaurada (Patch Omega)')
    plt.title(f'Restored Signal (Improvement: {improvement:.1f}%)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    outfile = "../imgs/reality_patch_results.png"
    plt.savefig(outfile, dpi=300, bbox_inches="tight")
    print(f"Concluído. Gráfico salvo em {outfile}")

if __name__ == "__main__":
    np.random.seed(117038)
    simulate_reality_patch()
