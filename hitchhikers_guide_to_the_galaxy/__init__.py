"""A tribute to Douglas Adams. Don't panic."""

from enum import IntEnum

__all__ = [
    "TheAnswerToLifeTheUniverseAndEverything",
    "Answer",
]

__version__ = "0.1.0"


class TheAnswerToLifeTheUniverseAndEverything(IntEnum):
    """The Answer. Yes, that one. Seed responsibly."""

    FORTY_TWO = 42


Answer = TheAnswerToLifeTheUniverseAndEverything
