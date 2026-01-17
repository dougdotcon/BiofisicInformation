import numpy as np
import random
import matplotlib.pyplot as plt
from Bio.Seq import Seq
from collections import Counter

# --- CONSTANTES TARDIS ---
OMEGA = 117.038
ALPHA = 0.47
BOLTZMANN_K = 1.38e-23  # (J/K) - Simbólico aqui, usamos unidades naturais
TEMP_UNRUH = OMEGA / (2 * np.pi)  # Temperatura teórica de "agitação" informacional

def calculate_shannon_entropy(sequence):
    """Calcula a entropia de Shannon de uma sequência de DNA."""
    if not sequence:
        return 0
    counts = Counter(sequence)
    total = len(sequence)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * np.log2(p)
    return entropy

def calculate_omega_resonance(sequence):
    """
    Calcula o quão 'ressonante' a sequência é com a constante Omega.
    Hipótese: Sequências com periodicidade φ ligada a Omega são mais estáveis.
    """
    # Transformar sequência em sinal numérico (A=1, T=2, C=3, G=4)
    mapping = {'A': 1, 'T': 2, 'C': 3, 'G': 4}
    numeric_signal = np.array([mapping.get(b, 0) for b in sequence])
    
    # FFT para análise espectral
    spectrum = np.fft.fft(numeric_signal)
    freqs = np.fft.fftfreq(len(numeric_signal))
    
    # Procurar picos em frequências harmônicas de Omega (simplificado)
    # Omega scale fundamental: 1/117, 1/sqrt(117), etc.
    target_freq = 1.0 / np.sqrt(OMEGA)
    
    # Encontrar a frequência mais próxima no espectro
    idx = (np.abs(freqs - target_freq)).argmin()
    resonance_amplitude = np.abs(spectrum[idx])
    
    return resonance_amplitude

def entropic_mutation(sequence, temperature=TEMP_UNRUH):
    """
    Aplica mutação baseada em probabilidade termodinâmica.
    Sequências com alta 'estabilidade Omega' resistem mais.
    """
    bases = ['A', 'T', 'C', 'G']
    seq_list = list(sequence)
    mutated = False
    
    # Estabilidade local (placeholder para cálculo topológico mais complexo)
    stability = calculate_omega_resonance(sequence) * 0.1
    
    # Probabilidade de mutação decai com estabilidade
    mutation_prob = np.exp(-stability / temperature) * 0.05 # Taxa base ajustável
    
    indices = range(len(seq_list))
    # Escolher 1 posição aleatória para tentar mutar
    idx = random.choice(indices)
    
    if random.random() < mutation_prob:
        original = seq_list[idx]
        new_base = random.choice([b for b in bases if b != original])
        seq_list[idx] = new_base
        mutated = True
        
    return "".join(seq_list), mutated

def simulation_evolution(generations=100, sequences=None):
    """Roda a simulação evolutiva."""
    if sequences is None:
        # Gerar sequências iniciais aleatórias
        sequences = ["".join(random.choices("ATCG", k=50)) for _ in range(10)]
    
    history_entropy = []
    history_stability = []
    
    print(f"Iniciando simulação TARDIS com {generations} gerações...")
    print(f"Temperatura do sistema (Unruh): {TEMP_UNRUH:.2f}")
    
    current_pop = sequences
    
    for gen in range(generations):
        next_pop = []
        gen_entropies = []
        gen_stabilities = []
        
        for seq in current_pop:
            # 1. Mutação entrópica
            new_seq, did_mutate = entropic_mutation(seq)
            
            # 2. Seleção (Otimização Entrópica)
            # Hipótese: Natureza seleciona quem minimiza variação de entropia brusca (estabilidade)
            # Mas aqui vamos simplificar: selecionamos quem tem MAIOR ressonância Omega
            
            curr_stab = calculate_omega_resonance(new_seq)
            
            # Pressão seletiva
            if did_mutate and curr_stab < calculate_omega_resonance(seq):
                # Mutação ruim (perdeu ressonância), chance de morrer
                if random.random() > 0.3: # 70% chance de rejeitar mutação ruim
                    next_pop.append(seq)
                else:
                    next_pop.append(new_seq)
            else:
                next_pop.append(new_seq)
                
            gen_entropies.append(calculate_shannon_entropy(new_seq))
            gen_stabilities.append(curr_stab)
            
        current_pop = next_pop
        history_entropy.append(np.mean(gen_entropies))
        history_stability.append(np.mean(gen_stabilities))
        
        if gen % 10 == 0:
            print(f"Gen {gen}: Estabilidade Média = {np.mean(gen_stabilities):.4f}")
            
    return history_stability, history_entropy

if __name__ == "__main__":
    # Setup inicial
    random.seed(42)
    np.random.seed(42)
    
    # Rodar Simulação
    stab, ent = simulation_evolution(generations=200)
    
    # Plotar Resultados
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(stab, color='purple', label='Ressonância Omega')
    plt.title('Evolução da Estabilidade TARDIS')
    plt.xlabel('Geração')
    plt.ylabel('Ressonância (Estabilidade)')
    plt.grid(True, alpha=0.3)
    
    plt.subplot(1, 2, 2)
    plt.plot(ent, color='cyan', label='Entropia de Shannon')
    plt.title('Evolução da Entropia de Informação')
    plt.xlabel('Geração')
    plt.ylabel('Bits')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('tardis_evolution_plot.png')
    print("Simulação concluída. Gráfico salvo como 'tardis_evolution_plot.png'.")
