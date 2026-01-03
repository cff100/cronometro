"""Módulo de entrada do usuário para controle do cronômetro.

Atalhos:
- s: start
- p: pause
- r: reset
- g: show time elapsed
- Esc: quit
"""

import time
from threading import Event, Thread
from pynput import keyboard

from stopwatch.stopwatch import Stopwatch

def display_time(stop_event: Event, sw: Stopwatch) -> None:
    while not stop_event.is_set():
        if sw.is_running:
            elapsed = sw.get_time_elapsed()
            print(f"\rTime elapsed: {elapsed:6.2f} s", end="", flush=True)
        time.sleep(0.1)
        


def run_listener(stop_event: Event, sw: Stopwatch) -> None:
    def on_press(key):
        try:
            c = key.char.lower()
        except AttributeError:
            if key == keyboard.Key.esc:
                stop_event.set()
                listener.stop()
            return

        if c == "s":
            sw.start()
        elif c == "p":
            sw.pause()
        elif c == "r":
            sw.reset()
            print("\rTime elapsed:   0.00 s", end="", flush=True)
        elif c == "g":
            print(f"\nTime elapsed: {sw.get_time_elapsed():.2f} s")
        else:
            print("\nKey not accepted.")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def main():
    sw = Stopwatch()        
    stop_event = Event()

    display_thread = Thread(
        target=display_time,
        args=(stop_event, sw),
        daemon=True
    )
    display_thread.start()

    run_listener(stop_event, sw)

if __name__ == "__main__":
    main()

