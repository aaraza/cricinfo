from enum import Enum

class MatchFormat(Enum):
    """
    Statistics can be filtered by the format of the match.
    International aggregates the stats from the 3 formats.
    """
    Test = '1'
    ODI = '2'
    T20I = '3'
    International = '11'