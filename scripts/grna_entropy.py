import numpy as np
import matplotlib.pyplot as plt
import random
from difflib import SequenceMatcher

# --- CONSTANTES TARDIS ---
OMEGA = 117.038
# Hipótese: A especificidade do gRNA não é apenas homologia (Hamming), 
# mas "Ressonância de Informação". Off-targets ocorrem quando a 
# "assinatura entrópica" é similar, mesmo com bases diferentes.

def generate_sequence(length=20):
    return "".join(random.choices("ATCG", k=length))

def calculate_entropic_signature(seq):
    """
    Calcula uma 'assinatura' numérica baseada em pesos TARDIS.
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
        
    # Plotting Correlation
    plt.figure(figsize=(10, 6))
    
    # Cor: Vermelho se Hamming baixo (perigo de off-target), Azul se seguro
    colors = ['red' if h <= 5 else 'blue' for h in hamming_scores]
    
    plt.scatter(hamming_scores, entropic_scores, c=colors, alpha=0.6)
    plt.title('Hamming Distance vs Entropic Distance (TARDIS Metric)')
    plt.xlabel('Hamming Distance (Standard Biology)')
    plt.ylabel('Entropic Distance (TARDIS Physics)')
    
    # Destacar a região de "Falso Positivo" ou "Falso Negativo"
    # Hipótese TARDIS: Coisas com Hamming alto (seguro) podem ter Entropia baixa (perigo oculto)
    # ou vice-versa.
    
    plt.axhline(y=10, color='purple', linestyle='--', label='TARDIS Danger Threshold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    outfile = "imgs/grna_specificity_results.png"
    plt.savefig(outfile)
    print(f"Concluído. Gráfico salvo em {outfile}")

if __name__ == "__main__":
    random.seed(42)
    run_grna_experiment()
