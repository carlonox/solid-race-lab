"""
Track: a tiny, reusable console animation engine.

This module is provided COMPLETE — you do not need to modify it for any
exercise. It knows nothing about vehicles, professions, or SOLID; it only
knows how to animate a list of "racers" on the terminal.

Contract a racer object must satisfy (a very small, implicit interface):
    racer.name      -> str
    racer.symbol    -> str   (a short string / emoji drawn on the track)
    racer.position  -> int   (distance already travelled, starts at 0)
    racer.move()    -> None  (mutates racer.position; called once per tick)

Anything that satisfies this contract can be raced — that is the whole
point: the engine depends on this small shape, not on any concrete class
(see Exercise 5 — Dependency Inversion Principle).
"""
from __future__ import annotations

import os
import time
from typing import Callable, Iterable, List, Optional, Protocol, runtime_checkable


@runtime_checkable
class Racer(Protocol):
    name: str
    symbol: str
    position: int

    def move(self) -> None: ...


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


class Track:
    """Renders and runs a race for any list of Racer-shaped objects."""

    def __init__(self, length: int = 40, tick_seconds: float = 0.25, animate: bool = True):
        self.length = length
        self.tick_seconds = tick_seconds
        self.animate = animate

    def render(self, racers: Iterable[Racer]) -> None:
        if self.animate:
            clear_screen()
        border = "=" * (self.length + 14)
        print(border)
        for r in racers:
            pos = max(0, min(r.position, self.length))
            lane = (" " * pos) + r.symbol
            print(f"{lane:<{self.length + 2}}| {r.name} ({r.position}m)")
        print(border)

    def run(
        self,
        racers: List[Racer],
        max_ticks: int = 200,
        on_tick: Optional[Callable[[int, List[Racer]], None]] = None,
    ) -> Optional[Racer]:
        """Advances every racer once per tick until one reaches self.length.

        Returns the winning racer, or None if max_ticks was reached first.
        """
        winner: Optional[Racer] = None
        ticks = 0
        while winner is None and ticks < max_ticks:
            for r in racers:
                r.move()
                if r.position < 0:
                    raise RuntimeError(
                        f"{r.name}.move() produced a negative position ({r.position}). "
                        "A racer must never move backwards past the start line — "
                        "see Exercise 3 (LSP)."
                    )
                if r.position >= self.length and winner is None:
                    winner = r
            self.render(racers)
            if on_tick:
                on_tick(ticks, racers)
            if self.animate:
                time.sleep(self.tick_seconds)
            ticks += 1

        if winner:
            print(f"\n🏁 {winner.name} wins the race in {ticks} ticks!\n")
        else:
            print(f"\n⏱  Race stopped after {max_ticks} ticks with no winner.\n")
        return winner
