from enum import Enum


class StatType(Enum):
    """The type of statistics to retrieve."""
    BATTING = "batting"
    BOWLING = "bowling"
    FIELDING = "fielding"
    ALLROUND = "allround"
    PARTNERSHIP = "fow"
    TEAM = "team"
    AGGREGATE = "aggregate"
