"""Módulo de entrada do usuário para controle do cronômetro.

Atalhos:
- s: start
- p: pause
- r: reset
- g: show time elapsed
- Esc: quit
"""

from threading import Event
from stopwatch.stopwatch import Stopwatch
from stopwatch.user_input.display import Display
from stopwatch.user_input.listener import KeyListener

# sppssrasspggqsrssrsrsprsrsp

def main() -> None:
    """Prepara e executa o display e o listener de teclado."""
    stopwatch = Stopwatch()
    stop_event = Event()

    print("\nInício do listener!")
    
    display = Display(stop_event, stopwatch)
    display.start()

    listener = KeyListener(stop_event, stopwatch)
    try:
        listener.run()
    finally:
        # garante que o display seja finalizado ao sair do listener
        stop_event.set()
        display.stop()

    print("\n\nFim do listener!")

if __name__ == "__main__":
    main()

