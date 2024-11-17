from .match_format import MatchFormat
from .services.cricinfo_service import CricinfoService
from .helpers.stat_type import StatType
from .team import Team
import pandas as pd

class Cricinfo:
    """
    Loads cricket statistics from ESPN's cricinfo site into Pandas data frames.
    """ 
    @staticmethod
    def retrieve_batting_stats(team: Team, match_format: MatchFormat) -> pd.DataFrame :
        """
        Retrieve the batting statistics for all players in international cricket.

        :param team: Filter stats by team. 
        :type team: Team, :obj:`None`

        :param match_format: Filter stats by format.
        :type match_format: MatchFormat

        :raises TypeError: If Team or MatchFormat do not use the specified type.
        """
        return CricinfoService.retrieve_stats(team, match_format, StatType.BATTING)
    
    @staticmethod
    def retrieve_bowling_stats(team: Team, match_format: MatchFormat) -> pd.DataFrame:
        """
        Retrieve the bowling statistics for all players in international cricket.

        :param team: Filter stats by team. 
        :type team: Team, :obj:`None`

        :param match_format: Filter stats by format.
        :type match_format: MatchFormat

        :raises TypeError: If Team or MatchFormat do not use the specified type.
        """
        return CricinfoService.retrieve_stats(team, match_format, StatType.BOWLING)
    
    @staticmethod
    def retrieve_fielding_stats(team: Team, match_format: MatchFormat) -> pd.DataFrame:
        """
        Retrieve the fielding statistics for all players in international cricket.

        :param team: Filter stats by team. 
        :type team: Team, :obj:`None`

        :param match_format: Filter stats by format.
        :type match_format: MatchFormat

        :raises TypeError: If Team or MatchFormat do not use the specified type.
        """
        return CricinfoService.retrieve_stats(team, match_format, StatType.FIELDING)

    @staticmethod
    def retrieve_allround_stats(team: Team, match_format: MatchFormat) -> pd.DataFrame:
        """
        Retrieve the all-round statistics for all players in international cricket.

        :param team: Filter stats by team. 
        :type team: Team, :obj:`None`

        :param match_format: Filter stats by format.
        :type match_format: MatchFormat

        :raises TypeError: If Team or MatchFormat do not use the specified type.
        """
        return CricinfoService.retrieve_stats(team, match_format, StatType.ALLROUND)

    @staticmethod
    def retrieve_partnership_stats(team: Team, match_format: MatchFormat) -> pd.DataFrame:
        """
        Retrieve the partnership statistics for all partnerships for a given team in international cricket.

        :param team: Filter stats by team. 
        :type team: Team, :obj:`None`

        :param match_format: Filter stats by format.
        :type match_format: MatchFormat

        :raises TypeError: If Team or MatchFormat do not use the specified type.
        """
        return CricinfoService.retrieve_stats(team, match_format, StatType.PARTNERSHIP)

    @staticmethod
    def retrieve_team_stats(team: Team, match_format: MatchFormat) -> pd.DataFrame:
        """
        Retrieve team statistics for a given team in international cricket.

        :param team: Filter stats by team. 
        :type team: Team, :obj:`None`

        :param match_format: Filter stats by format.
        :type match_format: MatchFormat

        :raises TypeError: If Team or MatchFormat do not use the specified type.
        """
        return CricinfoService.retrieve_stats(team, match_format, StatType.TEAM)

    @staticmethod
    def retrieve_aggregate_stats(team: Team, match_format: MatchFormat) -> pd.DataFrame:
        """
        Retrieve aggregated team statistics for a given team in international cricket.

        :param team: Filter stats by team. 
        :type team: Team, :obj:`None`

        :param match_format: Filter stats by format.
        :type match_format: MatchFormat

        :raises TypeError: If Team or MatchFormat do not use the specified type.
        """
        return CricinfoService.retrieve_stats(team, match_format, StatType.AGGREGATE)   