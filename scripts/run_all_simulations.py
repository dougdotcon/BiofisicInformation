"""
Script para rodar todas as simulações e gerar gráficos melhorados
"""
import subprocess
import sys
import os

# Lista de todos os scripts de simulação
scripts = [
    "entropic_dna.py",
    "omega_stability.py",
    "holographic_dna.py",
    "grna_entropy.py",
    "cas9_flow.py",
    "pe_entropy.py",
    "epigenetic_bits.py",
    "base_editing_thermo.py",
    "population_omega.py",
    "consciousness_resonance.py",
    "viral_tardis.py",
    "abiogenesis_omega.py",
    "mind_upload_sim.py",
    "reality_patch.py",
    "chrono_telephony.py",
    "multiverse_map.py",
    "entropy_reversal.py"
]

def run_script(script_name):
    """Executa um script e captura saída"""
    print(f"\n{'='*60}")
    print(f"Executando: {script_name}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(
            [sys.executable, script_name],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        print(result.stdout)
        if result.stderr:
            print(f"Avisos/Erros: {result.stderr}")
        
        if result.returncode == 0:
            print(f"✓ {script_name} concluído com sucesso")
            return True
        else:
            print(f"✗ {script_name} falhou com código {result.returncode}")
            return False
    except subprocess.TimeoutExpired:
        print(f"✗ {script_name} excedeu o tempo limite de 60s")
        return False
    except Exception as e:
        print(f"✗ Erro ao executar {script_name}: {e}")
        return False

if __name__ == "__main__":
    print("="*60)
    print("RODANDO TODAS AS SIMULAÇÕES")
    print("="*60)
    
    # Criar diretório de imagens se não existir
    if not os.path.exists("../imgs"):
        os.makedirs("../imgs")
        print("Diretório 'imgs' criado")
    
    success_count = 0
    failed_scripts = []
    
    for script in scripts:
        if os.path.exists(script):
            if run_script(script):
                success_count += 1
            else:
                failed_scripts.append(script)
        else:
            print(f"✗ Arquivo {script} não encontrado")
            failed_scripts.append(script)
    
    # Resumo final
    print("\n" + "="*60)
    print("RESUMO")
    print("="*60)
    print(f"Total de scripts: {len(scripts)}")
    print(f"Executados com sucesso: {success_count}")
    print(f"Falharam: {len(failed_scripts)}")
    
    if failed_scripts:
        print("\nScripts que falharam:")
        for script in failed_scripts:
            print(f"  - {script}")
    
    print("\n✓ Processamento concluído!")
    print("Verifique a pasta 'imgs' para os gráficos gerados.")
