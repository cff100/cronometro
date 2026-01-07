"""Módulo responsável pela exibição do tempo do cronômetro."""

import time
from threading import Event, Thread
from stopwatch.stopwatch import Stopwatch
from stopwatch.user_input.listener import KeyListener

class Display:
    def __init__(self, stop_event: Event, stopwatch: Stopwatch, interval: float = 0.1):
        self.stop_event = stop_event
        self.stopwatch = stopwatch
        self.interval = interval
        self._thread = Thread(target=self._run, daemon=True)

    def _run(self) -> None:

        while not self.stop_event.is_set():
            if self.stopwatch.is_running:
                elapsed = self.stopwatch.get_time_elapsed()
                print(f"\r\033[KTime elapsed: {elapsed:.2f} s", end="")

            else:
                print(f"\r\033[KTime elapsed: {self.stopwatch.elapsed:.2f} s", end="")
                pass
            time.sleep(self.interval)


    def start(self) -> None:
        self._thread.start()

    def stop(self, timeout: float = 1.0) -> None:
        # garante que o loop terminará e aguarda a thread terminar
        self.stop_event.set()
        self._thread.join(timeout)
