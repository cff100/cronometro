import pytest
import time

from stopwatch.stopwatch import Stopwatch


def test_initial_state():

    t = Stopwatch()
    assert t.start_time is None
    assert t.elapsed == 0
    assert t.is_running is False
    assert t.get_time_elapsed() == 0


def test_start_and_get_time_elapsed(monkeypatch):

    t = Stopwatch()

    monkeypatch.setattr(time, "time", lambda: 1000.0)
    t.start()
    assert t.is_running is True
    assert t.start_time == 1000.0

    monkeypatch.setattr(time, "time", lambda: 1005.2)
    assert pytest.approx(t.get_time_elapsed(), rel=1e-6) == 5.2


def test_pause_accumulates_and_stops(monkeypatch):

    t = Stopwatch()

    monkeypatch.setattr(time, "time", lambda: 1000.0)
    t.start()

    monkeypatch.setattr(time, "time", lambda: 1003.0)
    t.pause()
    assert t.is_running is False
    assert pytest.approx(t.elapsed, rel=1e-6) == 3.0
    assert pytest.approx(t.get_time_elapsed(), rel=1e-6) == 3.0

    # Advance the clock: get_time_elapsed and elapsed shouldn't change when it's not running
    monkeypatch.setattr(time, "time", lambda: 1006.0)
    assert pytest.approx(t.elapsed, rel=1e-6) == 3.0
    assert pytest.approx(t.get_time_elapsed(), rel=1e-6) == 3.0


def test_reset_clears_state(monkeypatch):

    t = Stopwatch()

    monkeypatch.setattr(time, "time", lambda: 2000.0)
    t.start()
    monkeypatch.setattr(time, "time", lambda: 2004.5)
    t.pause()

    t.reset()
    assert t.start_time is None
    assert t.elapsed == 0
    assert t.is_running is False
    assert t.get_time_elapsed() == 0


def test_start_two_in_a_row(monkeypatch):

    t = Stopwatch()
    monkeypatch.setattr(time, "time", lambda: 3000.0)
    t.start()

    # Calling start() again shouldn't change start_time
    monkeypatch.setattr(time, "time", lambda: 3001.0)
    t.start()
    assert t.start_time == 3000.0



def test_pause_without_start_does_nothing(monkeypatch):

    t = Stopwatch()

    t.pause()
    assert t.start_time is None
    assert t.elapsed == 0
    assert t.is_running is False
