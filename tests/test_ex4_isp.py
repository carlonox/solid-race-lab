"""
Tests for Exercise 4 - Interface Segregation Principle (ISP).

Run just this file with:
    pytest tests/test_ex4_isp.py -v
"""
from exercises import ex4_isp


def test_small_focused_interfaces_exist():
    for iface, method in [
        (ex4_isp.Movable, "move"),
        (ex4_isp.Refuelable, "refuel"),
        (ex4_isp.Flyable, "fly"),
        (ex4_isp.Pedalable, "pedal_harder"),
    ]:
        assert iface.__abstractmethods__ == frozenset({method}), (
            f"{iface.__name__} should declare exactly one abstract method: {method}."
        )


def test_gas_car_only_implements_relevant_interfaces():
    assert not hasattr(ex4_isp.GasCar, "fly"), "GasCar should not be forced to implement fly()."
    assert not hasattr(ex4_isp.GasCar, "pedal_harder"), (
        "GasCar should not be forced to implement pedal_harder()."
    )
    car = ex4_isp.GasCar("Racer")
    car.move()
    car.refuel()


def test_bicycle_only_implements_relevant_interfaces():
    assert not hasattr(ex4_isp.Bicycle, "refuel"), (
        "Bicycle should not be forced to implement refuel()."
    )
    assert not hasattr(ex4_isp.Bicycle, "fly"), "Bicycle should not be forced to implement fly()."
    bike = ex4_isp.Bicycle("Pedal Pete")
    bike.move()
    bike.pedal_harder()


def test_drone_exists_and_only_implements_relevant_interfaces():
    assert hasattr(ex4_isp, "Drone"), "Add a Drone class that can move() and fly()."
    assert not hasattr(ex4_isp.Drone, "refuel"), "Drone should not be forced to implement refuel()."
    assert not hasattr(ex4_isp.Drone, "pedal_harder"), (
        "Drone should not be forced to implement pedal_harder()."
    )
    drone = ex4_isp.Drone("Sky Scout")
    drone.move()
    drone.fly()
    assert issubclass(ex4_isp.Drone, ex4_isp.Movable)
    assert issubclass(ex4_isp.Drone, ex4_isp.Flyable)
