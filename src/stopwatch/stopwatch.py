
import time

class Stopwatch():

    def __init__(self) -> None:
        self.start_time = None
        self.elapsed = 0
        self.running = False

    def start(self) -> None:
        if not self.running:
            self.start_time = time.time()
            self.running = True

    def pause(self) -> None:
        if self.start_time is not None and self.running:
            self.elapsed += time.time() - self.start_time
            self.running = False
            # When pausing, we clear star_time to avoid reusing an old timestamp.
            self.start_time = None

    def reset(self) -> None:
        self.start_time = None
        self.elapsed = 0
        self.running = False

    def get_time_elapsed(self) -> float:
        if self.running and self.start_time is not None:
            return self.elapsed + (time.time() - self.start_time)
        else:
            return self.elapsed