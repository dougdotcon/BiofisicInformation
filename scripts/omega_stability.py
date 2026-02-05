import numpy as np
import matplotlib.pyplot as plt
import random

# --- CONSTANTES TAMESIS ---
OMEGA = 117.038

def generate_dna_sequence(length=1000, mode='random'):
    """Gera sequências de DNA baseadas no modo selecionado."""
    bases = ['A', 'T', 'C', 'G']
    
    if mode == 'random':
        return "".join(random.choices(bases, k=length))
    
    elif mode == 'omega_resonant':
        # Gera sequência com periodicidade baseada na raiz de Omega
        seq = []
        period = int(np.sqrt(OMEGA)) # ~10.8 -> 11 bases
        pattern = random.choices(bases, k=period)
        
        for i in range(length):
            # Adiciona base do padrão com pequena chance de erro (ruído entrópico)
            if random.random() > 0.05:
                seq.append(pattern[i % period])
            else:
                seq.append(random.choice(bases))
        return "".join(seq)

def simulate_radiation_damage(sequence, radiation_dose=0.1):
    """
    Simula dano por radiação (decoerência).
    Sequências ressonantes devem se 'curar' ou resistir melhor (hipótese).
    Na física TAMESIS, a estrutura topológica impõe correção de erro.
    """
    seq_list = list(sequence)
    mutations = 0
    
    for i in range(len(seq_list)):
        if random.random() < radiation_dose:
            # Dano ocorre
            original = seq_list[i]
            
            # Hipótese: "Cura" topológica
            # Se a vizinhança respeita a geometria Omega, o erro é suprimido
            is_protected = False
            
            # Checagem simplificada de "proteção topológica" (vizinhança consistente)
            # Em TAMESIS real, isso seria um cálculo de invariante de nó (knot theory)
            period = int(np.sqrt(OMEGA))
            if i > period and i < len(seq_list) - period:
                neighbor_consistency = (seq_list[i-period] == original) + (seq_list[i+period] == original)
                if neighbor_consistency > 0:
                    is_protected = True # Ressonância protege a informação
            
            # Se não protegido, muta
            damage_prob = 0.2 if is_protected else 1.0
            
            if random.random() < damage_prob:
                seq_list[i] = random.choice(['A', 'T', 'C', 'G'])
                if seq_list[i] != original:
                    mutations += 1
                
    return "".join(seq_list), mutations

def run_experiment():
    print("Iniciando Experimento 2: Estabilidade Omega...")
    
    n_sequences = 100
    seq_len = 500
    doses = np.linspace(0, 0.5, 20)
    
    avg_mutations_random = []
    avg_mutations_omega = []
    
    for dose in doses:
        muts_rnd = []
        muts_omg = []
        
        for _ in range(n_sequences):
            # Grupo Controle
            seq_rnd = generate_dna_sequence(seq_len, 'random')
            _, m_r = simulate_radiation_damage(seq_rnd, dose)
            muts_rnd.append(m_r)
            
            # Grupo Omega
            seq_omg = generate_dna_sequence(seq_len, 'omega_resonant')
            _, m_o = simulate_radiation_damage(seq_omg, dose)
            muts_omg.append(m_o)
            
        avg_mutations_random.append(np.mean(muts_rnd))
        avg_mutations_omega.append(np.mean(muts_omg))
        print(f"Dose {dose:.2f}: Random={np.mean(muts_rnd):.1f} vs Omega={np.mean(muts_omg):.1f} mutações")

    # Plot - Estilo Publicação Científica
    plt.figure(figsize=(10, 6), dpi=300)
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.size'] = 11
    plt.rcParams['axes.linewidth'] = 1.2
    
    # Plotar com marcadores e linhas profissionais
    plt.plot(doses, avg_mutations_random, 'o-', color='#d62728', linewidth=2.5, 
            markersize=8, markerfacecolor='white', markeredgewidth=2,
            label='Random DNA (Control)', zorder=3)
    plt.plot(doses, avg_mutations_omega, 's-', color='#1f77b4', linewidth=2.5, 
            markersize=8, markerfacecolor='white', markeredgewidth=2,
            label='Ω-Resonant DNA', zorder=3)
    
    # Área de proteção
    plt.fill_between(doses, avg_mutations_random, avg_mutations_omega, 
                    color='#9467bd', alpha=0.2, label='Topological Protection')
    
    plt.title('Radiation Resistance: Topological Protection Effect', 
             fontsize=13, fontweight='bold', pad=15)
    plt.xlabel('Radiation Dose (mutation probability)', fontsize=12)
    plt.ylabel('Average Mutations per 500 bp', fontsize=12)
    plt.legend(frameon=True, shadow=True, fontsize=11, loc='upper left')
    plt.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    
    # Calcular e anotar melhoria percentual
    idx_high = len(doses) * 3 // 4
    improvement = ((avg_mutations_random[idx_high] - avg_mutations_omega[idx_high]) / 
                   avg_mutations_random[idx_high]) * 100
    plt.annotate(f'Protection: ~{improvement:.0f}%\\nat high doses',
                xy=(doses[idx_high], avg_mutations_random[idx_high]),
                xytext=(doses[idx_high]*0.7, avg_mutations_random[idx_high]*0.6),
                bbox=dict(boxstyle='round,pad=0.7', facecolor='wheat', alpha=0.8),
                arrowprops=dict(arrowstyle='->', lw=1.5, color='black'),
                fontsize=10)
    
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    outfile = "../imgs/omega_stability_results.png"
    plt.savefig(outfile, dpi=300, bbox_inches='tight')
    print(f"Concluído. Gráfico salvo em {outfile}")

if __name__ == "__main__":
    random.seed(117) # Seed temática
    np.random.seed(117)
    run_experiment()
