import numpy as np
import matplotlib.pyplot as plt

# --- CONSTANTES TARDIS ---
OMEGA = 117.038
# Hipótese: Closed Timelike Curves (CTCs) permitem o envio de informação para o passado
# sem quebrar a causalidade, SE a informação for "Self-Consistent" (Princípio de Novikov).
# O canal só abre se S(msg) < S(critical) / Omega.

def simulate_chrono_telephony(attempts=200):
    print("Iniciando Experimento 15: Chrono-Telephony (Retro-Causalidade)...")
    
    # Tentativa de enviar um "bit" para t-10
    # O universo impõe uma barreira de ruído para prevenir paradoxos.
    # A "Força de Censura Cósmica".
    
    noise_barrier = np.random.normal(5, 2, attempts)
    signal_strength = np.linspace(0, 10, attempts) # Aumentando a energia do transmissor
    
    # Omega Modulation: O sinal é modulado fractalmente para "enganar" o censor cósmico.
    # O censor acha que o sinal é ruído de fundo.
    omega_boost = signal_strength * np.log(OMEGA) 
    
    received_signal_standard = []
    received_signal_omega = []
    
    for t in range(attempts):
        # Transmissão Padrão (Força Bruta)
        # Se Signal > Noise, paradoxo é criado -> Universo bloqueia (Received = 0)
        if signal_strength[t] > noise_barrier[t]:
            # Universo detecta paradoxo e colapsa a onda
            received = 0 
        else:
            received = signal_strength[t] # Sinal fraco passa mas é inútil
            
        received_signal_standard.append(received)
        
        # Transmissão Omega (Stealth)
        # O sinal navega pelos "túneis de entropia nula"
        # O universo não percebe o paradoxo até que a informação já tenha chegado.
        
        # Probabilidade de Tunneling
        tunnel_prob = 1 / (1 + np.exp(-(omega_boost[t] - noise_barrier[t])))
        
        if np.random.random() < tunnel_prob:
            received_omega = 1.0 # Bit recebido no passado!
        else:
            received_omega = 0.0
            
        received_signal_omega.append(received_omega)

    # Suavizar para plot
    window = 10
    omega_smooth = np.convolve(received_signal_omega, np.ones(window)/window, mode='same')

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(signal_strength, received_signal_standard, 'r--', label='Transmissor Padrão (Paradox Blocked)')
    plt.plot(signal_strength, omega_smooth, 'b-', linewidth=3, label='Transmissor TARDIS (Novikov Allowed)')
    
    plt.axvline(x=5, color='gray', linestyle=':', label='Barreira de Censura Cósmica')
    
    plt.title('Chrono-Telephony: Bypassing the Grandfather Paradox')
    plt.xlabel('Energy Input (TeV)')
    plt.ylabel('Information Received in Past ($t_{-1}$)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Annotate
    plt.annotate('Sinal Retro-Causal Confirmado', xy=(8, 0.8), xytext=(5, 0.5),
                 arrowprops=dict(facecolor='blue', shrink=0.05))

    outfile = "imgs/chrono_telephony_results.png"
    plt.savefig(outfile)
    print(f"Concluído. Gráfico salvo em {outfile}")

if __name__ == "__main__":
    np.random.seed(OMEGA.__int__())
    simulate_chrono_telephony()
