"""A tribute to Douglas Adams. Don't panic."""

from enum import IntEnum

__all__ = [
    "DeepThought",
    "TheAnswerToLifeTheUniverseAndEverything",
]

__version__ = "0.1.0"


class DeepThought(IntEnum):
    """7.5 million years of compute. You're welcome."""

    TheAnswerToLifeTheUniverseAndEverything = 42


TheAnswerToLifeTheUniverseAndEverything = DeepThought.TheAnswerToLifeTheUniverseAndEverything
