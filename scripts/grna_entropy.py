import numpy as np
import matplotlib.pyplot as plt
import random
from difflib import SequenceMatcher

# --- CONSTANTES TAMESIS ---
OMEGA = 117.038
# Hipótese: A especificidade do gRNA não é apenas homologia (Hamming), 
# mas "Ressonância de Informação". Off-targets ocorrem quando a 
# "assinatura entrópica" é similar, mesmo com bases diferentes.

def generate_sequence(length=20):
    return "".join(random.choices("ATCG", k=length))

def calculate_entropic_signature(seq):
    """
    Calcula uma 'assinatura' numérica baseada em pesos TAMESIS.
    A=1, T=Omega^0.1, C=Omega^0.2, G=Omega^0.3 (hipotético)
    """
    mapping = {
        'A': 1.0, 
        'T': OMEGA**0.1, 
        'C': OMEGA**0.2, 
        'G': OMEGA**0.3
    }
    vals = [mapping[b] for b in seq]
    # Assinatura é a soma ponderada pela posição (topologia)
    signature = sum(v * (i+1)**0.5 for i, v in enumerate(vals))
    return signature

def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def entropic_distance(s1, s2):
    sig1 = calculate_entropic_signature(s1)
    sig2 = calculate_entropic_signature(s2)
    return abs(sig1 - sig2)

def run_grna_experiment():
    print("Iniciando Experimento 4: gRNA Entropic Specificity...")
    
    target = generate_sequence(20)
    print(f"Alvo: {target}")
    
    # Gerar 1000 sequências aleatórias (potenciais off-targets)
    genome_fragments = [generate_sequence(20) for _ in range(1000)]
    
    # Adicionar alguns off-targets "reais" (com poucas mutações)
    for _ in range(10):
        mutant = list(target)
        # 2 ou 3 mutações
        for _ in range(3):
            mutant[random.randint(0, 19)] = random.choice("ATCG")
        genome_fragments.append("".join(mutant))
        
    hamming_scores = []
    entropic_scores = []
    
    for frag in genome_fragments:
        h_dist = hamming_distance(target, frag)
        e_dist = entropic_distance(target, frag)
        
        hamming_scores.append(h_dist)
        entropic_scores.append(e_dist)
        
    # Plotting Correlation - Estilo Publicação Científica
    plt.figure(figsize=(10, 7), dpi=300)
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.size'] = 11
    plt.rcParams['axes.linewidth'] = 1.2
    
    # Normalizar escores entrópicos
    entropic_norm = np.array(entropic_scores) / np.max(entropic_scores) * 20
    
    # Classificar pontos por risco
    high_risk = [(h, e) for h, e in zip(hamming_scores, entropic_norm) if h <= 5 and e <= 10]
    cryptic_risk = [(h, e) for h, e in zip(hamming_scores, entropic_norm) if h > 5 and e <= 10]
    safe = [(h, e) for h, e in zip(hamming_scores, entropic_norm) if e > 10]
    
    # Plot com diferentes categorias
    if high_risk:
        hr_h, hr_e = zip(*high_risk)
        plt.scatter(hr_h, hr_e, c='#d62728', s=80, alpha=0.7, 
                   edgecolors='darkred', linewidth=1.5, label='High Risk (Low Hamming)', zorder=3)
    if cryptic_risk:
        cr_h, cr_e = zip(*cryptic_risk)
        plt.scatter(cr_h, cr_e, c='#ff7f0e', s=80, alpha=0.7, 
                   edgecolors='darkorange', linewidth=1.5, 
                   label='Cryptic Off-targets', marker='^', zorder=3)
    if safe:
        s_h, s_e = zip(*safe)
        plt.scatter(s_h, s_e, c='#1f77b4', s=50, alpha=0.5, 
                   edgecolors='navy', linewidth=1, label='Safe Targets', zorder=2)
    
    plt.title('Off-Target Prediction: Hamming vs. Entropic Distance', 
             fontsize=13, fontweight='bold', pad=15)
    plt.xlabel('Hamming Distance (sequence dissimilarity)', fontsize=12)
    plt.ylabel('Entropic Distance (normalized)', fontsize=12)
    
    # Linhas de threshold
    plt.axhline(y=10, color='#9467bd', linestyle='--', linewidth=2.5, 
               label='Entropic Threshold', alpha=0.8, zorder=1)
    plt.axvline(x=5, color='gray', linestyle=':', linewidth=2, alpha=0.6, zorder=1)
    
    # Zona de perigo
    plt.fill_between([0, 5], 0, 10, alpha=0.15, color='purple', label='Danger Zone', zorder=0)
    
    # Anotações
    plt.text(2.5, 5, 'Known\\nOff-targets', ha='center', fontsize=10, 
            weight='bold', color='darkred')
    plt.text(10, 5, 'Cryptic\\n(Missed)', ha='center', fontsize=9, 
            style='italic', color='darkorange')
    
    plt.legend(frameon=True, shadow=True, fontsize=10, loc='upper right')
    plt.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlim(-0.5, 20)
    ax.set_ylim(-1, 22)
    
    plt.tight_layout()
    outfile = "../imgs/grna_specificity_results.png"
    plt.savefig(outfile, dpi=300, bbox_inches='tight')
    print(f"Concluído. Gráfico salvo em {outfile}")

if __name__ == "__main__":
    random.seed(42)
    run_grna_experiment()
