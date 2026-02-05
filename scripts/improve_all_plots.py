"""
Script para melhorar todos os gráficos com estilo de publicação científica
"""
import os
import re

# Estilo padrão para todos os gráficos
PLOT_STYLE_HEADER = """
# Configuração de estilo para publicação científica
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']
plt.rcParams['font.size'] = 10
plt.rcParams['axes.linewidth'] = 1.2
plt.rcParams['grid.alpha'] = 0.3
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.linewidth'] = 0.5
"""

def improve_entropic_dna():
    """Melhora o script entropic_dna.py"""
    filepath = "entropic_dna.py"
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Substituir a seção de plot
    plot_section = """
    # Plotar Resultados - Estilo Publicação
    plt.figure(figsize=(12, 5), dpi=300)
    
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
    
    # Convergência
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
    
    plt.tight_layout()
    plt.savefig('imgs/tardis_evolution_plot.png', dpi=300, bbox_inches='tight')
    print("Simulação concluída. Gráfico salvo como 'imgs/tardis_evolution_plot.png'.")
    plt.close()
"""
    
    # Encontrar e substituir a seção de plot
    pattern = r'# Plotar Resultados.*?plt\.savefig\(.*?\).*?print\(.*?\)'
    content = re.sub(pattern, plot_section.strip(), content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ {filepath} atualizado")

if __name__ == "__main__":
    print("Melhorando scripts de visualização...")
    print("=" * 50)
    
    improve_entropic_dna()
    
    print("=" * 50)
    print("Concluído! Execute cada script para gerar os gráficos melhorados.")
