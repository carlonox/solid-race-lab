"""
Exercise 4 - Interface Segregation Principle (ISP)

VehicleActions below is a single "fat" interface that forces every
vehicle to implement actions that make no sense for it: a GasCar has no
pedals, a Bicycle has no engine or wings, and neither can fly. Both are
forced to implement fly() (and other irrelevant methods) with an
"I can't do that" stub -- a classic ISP violation.

YOUR TASK:
  1. Replace the one fat `VehicleActions` interface with several small,
     focused ones: `Movable` (move), `Refuelable` (refuel), `Flyable`
     (fly), `Pedalable` (pedal_harder) -- each with exactly ONE abstract
     method.
  2. Make GasCar implement only Movable + Refuelable, and Bicycle only
     Movable + Pedalable. Remove their now-unnecessary
     NotImplementedError stubs entirely.
  3. Add a new `Drone` class that implements Movable + Flyable (move()
     and fly()) -- and nothing else. It should NOT be forced to
     implement refuel() or pedal_harder().

Run it to see the race once Drone exists:
    python -m exercises.ex4_isp

Check your work:
    pytest tests/test_ex4_isp.py -v
"""
from abc import ABC, abstractmethod

from engine.track import Track


class VehicleActions(ABC):
    """VIOLATION (on purpose): one fat interface forces every vehicle to
    implement actions that don't apply to it. Split this into smaller
    interfaces (see the module docstring) instead of using this class.
    """

    @abstractmethod
    def move(self) -> None: ...

    @abstractmethod
    def refuel(self) -> None: ...

    @abstractmethod
    def fly(self) -> None: ...

    @abstractmethod
    def pedal_harder(self) -> None: ...


# TODO(ISP): define Movable, Refuelable, Flyable and Pedalable here,
# each with exactly one abstract method, and delete VehicleActions above
# once nothing uses it any more.


class GasCar(VehicleActions):
    symbol = "\U0001F697"

    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        self.position += 4

    def refuel(self):
        print(f"{self.name} refuels at the gas station.")

    def fly(self):
        # TODO(ISP): once GasCar only implements the interfaces it needs,
        # this method (and the one below) should not need to exist.
        raise NotImplementedError("Cars can't fly!")

    def pedal_harder(self):
        raise NotImplementedError("Cars don't have pedals!")


class Bicycle(VehicleActions):
    symbol = "\U0001F6B2"

    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        self.position += 3

    def refuel(self):
        # TODO(ISP): Bicycle shouldn't need to implement this at all.
        raise NotImplementedError("Bicycles don't use fuel!")

    def fly(self):
        raise NotImplementedError("Bicycles can't fly!")

    def pedal_harder(self):
        self.position += 1
        print(f"{self.name}'s rider pedals harder!")


# TODO(ISP): add a Drone class here (Movable + Flyable only).


def main():
    vehicles = [GasCar("Racer"), Bicycle("Pedal Pete")]
    # TODO(ISP): once Drone exists, add Drone("Sky Scout") to the race.
    Track(length=30).run(vehicles)


if __name__ == "__main__":
    main()
