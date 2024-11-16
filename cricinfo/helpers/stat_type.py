from enum import Enum

class StatType(Enum):
    BATTING = "batting"
    BOWLING = "bowling"
    FIELDING = "fielding"
    ALLROUND = "allround"
    PARTNERSHIP = "fow"
    TEAM = "team"
    AGGREGATE = "aggregate"