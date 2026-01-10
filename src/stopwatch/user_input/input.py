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
from stopwatch.display import Display
from stopwatch.user_input.listener import KeyListener

# psrsgpgspgsg

def main() -> None:
    """Prepara e executa o display e o listener de teclado."""
    stopwatch = Stopwatch()
    stop_event = Event()

    print("\nInício do listener!")
    
    display = Display(stop_event, stopwatch)
    display.start()

    listener = KeyListener(stop_event, stopwatch, display)
    try:
        listener.run()
    finally:
        stop_event.set()
        display.stop()

    print("\n\nFim do listener!\n")

if __name__ == "__main__":
    main()

