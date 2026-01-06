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

def display_time(stop_event: Event, stopwatch: Stopwatch) -> None:
    while not stop_event.is_set():
        if stopwatch.is_running:
            elapsed = stopwatch.get_time_elapsed()
            print(f"\r\033[KTime elapsed: {elapsed:.2f} s", end="")
        time.sleep(0.1)
        


def run_listener(stop_event: Event, stopwatch: Stopwatch) -> None:
    def on_press(key):
        try:
            c = key.char.lower()
        except AttributeError:
            if key == keyboard.Key.esc:
                stop_event.set()
                listener.stop()
            return

        if c == "s":
            stopwatch.start()
        elif c == "p":
            stopwatch.pause()
        elif c == "r":
            stopwatch.reset()
            print(f"\r\033[KTime elapsed: {stopwatch.elapsed:.2f} s", end="")
        elif c == "g":
            print(f"\nTime obtained: {stopwatch.get_time_elapsed():.2f} s")
        else:
            print("\nKey not accepted.")

    with keyboard.Listener(on_press=on_press) as listener:
        print("\nInício do listener!")
        listener.join()
        print("\nFim do listener!")
#srasrspsrsrsrspsgspsgrssrpgggggggssrsrspspgsgsraspwpsrspsfr

def main():
    stopwatch = Stopwatch()        
    stop_event = Event()

    display_thread = Thread(
        target=display_time,
        args=(stop_event, stopwatch),
        daemon=True
    )
    display_thread.start()

    run_listener(stop_event, stopwatch)

if __name__ == "__main__":
    main()

