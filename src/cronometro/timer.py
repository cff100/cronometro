
import time

class Timer():

    def __init__(self) -> None:
        self.start_time = None
        self.elapsed = 0
        self.running = False

    def start(self) -> None:
        if not self.running:
            self.start_time = time.time()
            self.running = True

    def pause(self) -> None:
        if self.start_time != None and not self.running:
            self.elapsed += time.time() - self.start_time
            self.running = False

    def reset(self) -> None:
        self.start_time = None
        self.elapsed = 0
        self.running = False

    def get_time_elapsed(self):
        if self.running and self.start_time != None:
            return self.elapsed + (time.time() - self.start_time)
        else:
            return self.elapsed