
from datetime import datetime
from pynput import keyboard

# (Thread Principal)

# Função chamada quando uma tecla é pressionada
def on_press(key):

    if key == keyboard.Key.space:
        agora = datetime.now()
        print(agora)
    else:
        print("Precione a tecla 'space' para printar o tempo")

# Função chamada quando uma tecla é liberada
def on_release(key):

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

listener.join() # Esperando a finalização do thread secundário


print("Listener de teclado encerrado.")

                      

       