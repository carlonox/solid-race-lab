"""
Tests for Exercise 5 - Dependency Inversion Principle (DIP).

Run just this file with:
    pytest tests/test_ex5_dip.py -v
"""
import inspect

from exercises import ex5_dip


class _FakeRacer:
    """A minimal Racer test double -- deliberately NOT SportsCar/DeliveryVan/
    RocketSled, to prove Race doesn't secretly depend on any of them."""

    symbol = "*"

    def __init__(self, name, step):
        self.name = name
        self.position = 0
        self._step = step

    def move(self):
        self.position += self._step


def test_race_constructor_accepts_racers_from_outside():
    sig = inspect.signature(ex5_dip.Race.__init__)
    params = [p for p in sig.parameters if p != "self"]
    assert params, (
        "Race.__init__ should accept the list of racers as a parameter "
        "instead of constructing vehicles itself."
    )


def test_race_does_not_hardcode_its_roster():
    fake_roster = [_FakeRacer("X", 5), _FakeRacer("Y", 7)]
    race = ex5_dip.Race(fake_roster)
    assert race.racers is fake_roster, (
        "Race should store exactly the racers it was given, not build its own."
    )


def test_race_runs_with_an_arbitrary_roster():
    from engine.track import Track

    fake_roster = [_FakeRacer("X", 9), _FakeRacer("Y", 7)]
    race = ex5_dip.Race(fake_roster, track=Track(length=20, tick_seconds=0, animate=False))
    winner = race.start()
    assert winner in fake_roster


def test_race_works_with_two_different_rosters_unmodified():
    from engine.track import Track

    roster_a = [_FakeRacer("A1", 5), _FakeRacer("A2", 4)]
    roster_b = [_FakeRacer("B1", 3), _FakeRacer("B2", 3), _FakeRacer("B3", 6)]

    for roster in (roster_a, roster_b):
        race = ex5_dip.Race(roster, track=Track(length=15, tick_seconds=0, animate=False))
        winner = race.start()
        assert winner in roster
