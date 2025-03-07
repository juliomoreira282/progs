import time
from colorama import init, Fore, Style

init(autoreset=True)
def simular_semaforo():
    estados = [
        ("Verde", 45, Fore.GREEN),
        ("Amarelo", 3, Fore.YELLOW),
        ("Vermelho", 45, Fore.RED)
    ]

    while True:
        for cor, duracao, corTerminal in estados:
            print(f"{corTerminal} Semáforo: {cor} - {duracao} segundos{Style.RESET_ALL}")
            time.sleep(duracao)
            print()

if __name__ == "__main__":
    try:
        simular_semaforo()
    except KeyboardInterrupt:
        print("Simulação interrompida pelo usuário.")