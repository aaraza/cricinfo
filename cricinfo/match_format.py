from enum import Enum


class MatchFormat(Enum):
    """Filter statistics by match format.

    ``International`` aggregates stats across Test, ODI, and T20I.
    """
    Test = "1"
    ODI = "2"
    T20I = "3"
    International = "11"
