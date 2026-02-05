"""
Script para atualizar todos os caminhos de imagem dos scripts restantes
"""
import os
import glob

# Lista de scripts para atualizar
scripts_to_update = [
    'holographic_dna.py',
    'pe_entropy.py',
    'epigenetic_bits.py',
    'base_editing_thermo.py',
    'population_omega.py',
    'viral_tardis.py',
    'abiogenesis_omega.py',
    'mind_upload_sim.py',
    'reality_patch.py',
    'chrono_telephony.py',
    'multiverse_map.py',
    'entropy_reversal.py'
]

for script in scripts_to_update:
    if os.path.exists(script):
        with open(script, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Atualizar caminhos das imagens
        content = content.replace('plt.savefig("imgs/', 'plt.savefig("../imgs/')
        content = content.replace("plt.savefig('imgs/", "plt.savefig('../imgs/")
        content = content.replace('outfile = "imgs/', 'outfile = "../imgs/')
        content = content.replace("outfile = 'imgs/", "outfile = '../imgs/")
        
        # Adicionar DPI e bbox_inches se não existir
        if 'dpi=300' not in content:
            content = content.replace('.savefig(outfile)', '.savefig(outfile, dpi=300, bbox_inches="tight")')
            content = content.replace('.savefig("..', '.savefig("..').replace(')"', '", dpi=300, bbox_inches="tight")')
        
        with open(script, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ {script} atualizado")
    else:
        print(f"✗ {script} não encontrado")

print("\nTodos os scripts foram atualizados!")
