"""Módulo que encapsula o listener de teclado."""

from threading import Event
from pynput import keyboard
from stopwatch.stopwatch import Stopwatch
from stopwatch.display import Display


class KeyListener:
    def __init__(self, stop_event: Event, stopwatch: Stopwatch, display: Display):
        self.stop_event = stop_event
        self.stopwatch = stopwatch
        self.display = display
        self._listener = keyboard.Listener(on_press=self._on_press)

    def _on_press(self, key):
        try:
            c = key.char.lower()
        except AttributeError:
            if key == keyboard.Key.esc:
                self.stop_event.set()
                self._listener.stop()
            return

        if c == "s":
            self.stopwatch.start()
        elif c == "p":
            self.stopwatch.pause()
        elif c == "r":
            self.stopwatch.reset()
        elif c == "g":
            self.display.show_time()
        else:
            print("\nKey not accepted.")

    def run(self) -> None:
        with self._listener as listener:
            listener.join()
        
