"""
Tests for Exercise 1 - Single Responsibility Principle (SRP).

Run just this file with:
    pytest tests/test_ex1_srp.py -v
"""
import contextlib
import io

from exercises import ex1_srp


def test_car_move_does_not_print():
    car = ex1_srp.Car("Test", 5)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        car.move()
    assert buf.getvalue() == "", (
        "Car.move() should not print anything -- rendering belongs to Track (SRP)."
    )


def test_car_move_only_updates_position():
    car = ex1_srp.Car("Test", 7)
    car.move()
    assert car.position == 7
    car.move()
    assert car.position == 14


def test_car_move_does_not_touch_disk(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    car = ex1_srp.Car("Test", 5)
    car.move()
    assert list(tmp_path.iterdir()) == [], (
        "Car.move() should not write files -- logging is RaceLogger's job (SRP)."
    )


def test_race_logger_exists():
    assert hasattr(ex1_srp, "RaceLogger"), (
        "Create a RaceLogger class responsible for recording and saving results."
    )


def test_race_logger_records_and_saves(tmp_path):
    logger = ex1_srp.RaceLogger()
    car = ex1_srp.Car("Test", 5)
    car.move()
    logger.record(tick=0, racers=[car])
    assert len(logger.entries) == 1

    out_file = tmp_path / "log.txt"
    logger.save(str(out_file))
    assert out_file.exists()
    assert out_file.read_text().strip() != ""


def test_main_runs_end_to_end(tmp_path, monkeypatch):
    """Smoke test: the whole exercise should still run a full race."""
    monkeypatch.chdir(tmp_path)
    from engine import track as track_module

    monkeypatch.setattr(track_module.Track, "render", lambda self, racers: None)
    monkeypatch.setattr(track_module.time, "sleep", lambda *_: None)

    ex1_srp.main()
    assert (tmp_path / "race_log.txt").exists()
