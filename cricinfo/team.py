from enum import Enum


class Team(Enum):
    """Filter statistics by team.

    Pass ``None`` to retrieve stats for all teams.
    """
    England = "1"
    Australia = "2"
    SouthAfrica = "3"
    WestIndies = "4"
    NewZealand = "5"
    India = "6"
    Pakistan = "7"
    SriLanka = "8"
    Zimbabwe = "9"
