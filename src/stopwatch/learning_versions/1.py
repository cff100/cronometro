
from datetime import datetime
from pynput import keyboard
import time
import threading

# (Thread Principal)

a = datetime.today()
print(a)

# help(datetime)  # Descrição da classe
# help(datetime.today)  # Descrição do módulo da classe

def numero_threads_ativas():
    n_threads_ativas = threading.active_count()
    print(f"Número de threads ativas: {n_threads_ativas}")

print("ANTES de iniciar o thread secundário:")
numero_threads_ativas()
print("\n")

# Função chamada quando uma tecla é pressionada
def on_press(key):
    try:
        # Imprime o caractere da tecla alfanumérica
        print(f"Tecla alfanumérica {key.char}' pressionada")
    except AttributeError:
        # Imprime a tecla especial (Ctrl, Shift, F1, etc.)
        print(f'Tecla especial {key} pressionada')

# Função chamada quando uma tecla é liberada
def on_release(key):
    print(f'{key} liberada')
    
    # Condição para parar de escutar
    if key == keyboard.Key.esc:
        # Para o listener
        listener.stop()


# Configura e inicia o Listener (thread secundário)
# Ele chama as funções on_press e on_release
listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
listener.start()

print("DURANTE a execução do thread secundário:")
numero_threads_ativas()
print("\n")

# Exemplo para execução na thread principal
for i in range(6):
    print(i)
    time.sleep(1)

# Bloqueia o thread principal e espera o listener terminar
if listener.is_alive():
    print("Esperando a finalização do thread secundário...")
listener.join()

print("\nDEPOIS de finalizar o thread secundário:")
numero_threads_ativas()
print("\n")

print("Listener de teclado encerrado.")



