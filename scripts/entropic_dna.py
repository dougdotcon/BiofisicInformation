import numpy as np
import random
import matplotlib.pyplot as plt
from Bio.Seq import Seq
from collections import Counter

# --- CONSTANTES TAMESIS ---
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
    
    print(f"Iniciando simulação TAMESIS com {generations} gerações...")
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
    
    # Plotar Resultados - Estilo Publicação Científica
    plt.figure(figsize=(12, 5), dpi=300)
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.linewidth'] = 1.2
    
    ax1 = plt.subplot(1, 2, 1)
    ax1.plot(stab, color='#1f77b4', linewidth=2.5, label='Ω Resonance')
    ax1.fill_between(range(len(stab)), np.array(stab) * 0.95, np.array(stab) * 1.05, 
                     alpha=0.2, color='#1f77b4')
    ax1.set_title('(a) Stability Evolution', fontsize=12, fontweight='bold', pad=10)
    ax1.set_xlabel('Generation', fontsize=11)
    ax1.set_ylabel('Ω Resonance (a.u.)', fontsize=11)
    ax1.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    
    # Linha de convergência
    final_avg = np.mean(stab[-20:])
    ax1.axhline(y=final_avg, color='gray', linestyle=':', linewidth=1.5, alpha=0.7)
    ax1.text(20, final_avg*1.05, f'Convergence: {final_avg:.1f}', fontsize=9, style='italic')
    
    ax2 = plt.subplot(1, 2, 2)
    ax2.plot(ent, color='#d62728', linewidth=2.5, label='Shannon Entropy')
    ax2.fill_between(range(len(ent)), np.array(ent) * 0.95, np.array(ent) * 1.05, 
                     alpha=0.2, color='#d62728')
    ax2.set_title('(b) Entropic Optimization', fontsize=12, fontweight='bold', pad=10)
    ax2.set_xlabel('Generation', fontsize=11)
    ax2.set_ylabel('Shannon Entropy (bits)', fontsize=11)
    ax2.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    
    # Anotação de seleção
    mid_point = len(ent) // 2
    ax2.annotate('Selection pressure', xy=(mid_point, ent[mid_point]), 
                xytext=(mid_point+30, ent[mid_point]+0.15),
                arrowprops=dict(arrowstyle='->', color='black', lw=1),
                fontsize=9)
    
    plt.tight_layout()
    plt.savefig('../imgs/tardis_evolution_plot.png', dpi=300, bbox_inches='tight')
    print("Simulação concluída. Gráfico salvo como '../imgs/tardis_evolution_plot.png'.")
    plt.close()

