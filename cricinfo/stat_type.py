from enum import Enum


class StatType(Enum):
    """The type of statistics to retrieve.

    Each type corresponds to a different statistics table on ESPN Cricinfo:

    - ``BATTING``, ``BOWLING``, ``FIELDING``, ``ALLROUND``: Career player statistics.
    - ``PARTNERSHIP``: Partnership records for a team.
    - ``TEAM``: Overall team records.
    - ``AGGREGATE``: Aggregated team statistics across matches.
    """
    BATTING = "batting"
    BOWLING = "bowling"
    FIELDING = "fielding"
    ALLROUND = "allround"
    PARTNERSHIP = "fow"
    TEAM = "team"
    AGGREGATE = "aggregate"
