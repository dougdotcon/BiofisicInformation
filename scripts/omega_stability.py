import numpy as np
import matplotlib.pyplot as plt
import random

# --- CONSTANTES TARDIS ---
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
    Na física TARDIS, a estrutura topológica impõe correção de erro.
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
            # Em TARDIS real, isso seria um cálculo de invariante de nó (knot theory)
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

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(doses, avg_mutations_random, 'r-o', label='DNA Aleatório (Controle)')
    plt.plot(doses, avg_mutations_omega, 'b-o', label='DNA Omega Ressonante')
    plt.title('Experimento: Resistência à Radiação (Decoerência)')
    plt.xlabel('Dose de Radiação (Entropia Externa)')
    plt.ylabel('Taxa de Mutação Média')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.fill_between(doses, avg_mutations_random, avg_mutations_omega, color='purple', alpha=0.1, label='Proteção Topológica TARDIS')
    
    outfile = "imgs/omega_stability_results.png"
    plt.savefig(outfile)
    print(f"Concluído. Gráfico salvo em {outfile}")

if __name__ == "__main__":
    random.seed(117) # Seed temática
    np.random.seed(117)
    run_experiment()
