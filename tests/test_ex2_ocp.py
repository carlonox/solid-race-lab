"""
Tests for Exercise 2 - Open/Closed Principle (OCP).

Run just this file with:
    pytest tests/test_ex2_ocp.py -v
"""
import random

from exercises import ex2_ocp


def test_car_and_truck_unchanged():
    """Regression check: Car/Truck must keep working exactly as given --
    you should not need to touch them (or Vehicle) to finish this exercise."""
    car = ex2_ocp.Car("C")
    car.move()
    assert car.position == 4

    truck = ex2_ocp.Truck("T")
    truck.move()
    assert truck.position == 2


def test_motorcycle_and_bicycle_are_vehicles():
    assert issubclass(ex2_ocp.Motorcycle, ex2_ocp.Vehicle)
    assert issubclass(ex2_ocp.Bicycle, ex2_ocp.Vehicle)


def test_motorcycle_moves_variably():
    random.seed(42)
    moto = ex2_ocp.Motorcycle("M")
    deltas = []
    for _ in range(15):
        before = moto.position
        moto.move()
        deltas.append(moto.position - before)
    assert all(d > 0 for d in deltas), "Motorcycle must always move forward."
    assert len(set(deltas)) > 1, (
        "Motorcycle should move erratically (varying step sizes), not a fixed amount every tick."
    )


def test_bicycle_gets_slower_over_time():
    bike = ex2_ocp.Bicycle("B")
    deltas = []
    for _ in range(15):
        before = bike.position
        bike.move()
        deltas.append(bike.position - before)

    assert all(d >= 1 for d in deltas), "Bicycle must always move forward (at least 1)."
    early_avg = sum(deltas[:3]) / 3
    late_avg = sum(deltas[-3:]) / 3
    assert late_avg <= early_avg, (
        "Bicycle should tire out: its later steps should not be bigger than its early steps."
    )
