"""
Tests for Exercise 3 - Liskov Substitution Principle (LSP).

Run just this file with:
    pytest tests/test_ex3_lsp.py -v
"""
from exercises import ex3_lsp


def test_unreliable_car_is_a_vehicle():
    assert issubclass(ex3_lsp.UnreliableCar, ex3_lsp.Vehicle)


def test_unreliable_car_never_moves_backwards_or_raises():
    car = ex3_lsp.UnreliableCar("Shaky Sam")
    last = car.position
    for _ in range(300):
        car.move()  # must never raise
        assert car.position >= last, (
            "A Vehicle must never move backwards -- that breaks substitutability (LSP). "
            "Model 'unreliability' as staying in place, not rolling back or throwing."
        )
        last = car.position


def test_track_can_run_a_full_race_without_crashing():
    """Integration check: Track's own LSP guard (position must never go
    negative) must never fire for this exercise's vehicles."""
    from engine.track import Track

    vehicles = [ex3_lsp.SteadyCar("Rex"), ex3_lsp.UnreliableCar("Sam")]
    track = Track(length=60, tick_seconds=0, animate=False)
    winner = track.run(vehicles, max_ticks=500)
    assert winner is not None
