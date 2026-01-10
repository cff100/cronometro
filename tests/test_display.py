import time

from threading import Event
from stopwatch.display import Display
from stopwatch.stopwatch import Stopwatch


def test_show_time_prints_current_elapsed(monkeypatch, capsys):
    sw = Stopwatch()
    # Simula tempo inicial e tempo após 3.25s
    monkeypatch.setattr(time, "time", lambda: 1000.0)
    sw.start()

    monkeypatch.setattr(time, "time", lambda: 1003.25)
    disp = Display(Event(), sw)
    disp.show_time()

    captured = capsys.readouterr()
    assert "Tempo decorrido: 3.25 s" in captured.out
