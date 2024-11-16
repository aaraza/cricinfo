from .match_format import MatchFormat
from .services import BattingService
from .team import Team

class Cricinfo:
    """
    Library for querying/loading cricket stats from espncricinfo.com info Pandas DataFrames.
    """ 
    @staticmethod
    def retrieve_batting_stats(team: Team, match_format: MatchFormat):
        """
        Retrieve the batting statistics for all players that have played
        internationally for a given team.

        :param team: The team for whose player's statistics will be retrieved. :class:`Team`.
        :type team: Team

        :param match_format: The format for which the statistics will be retrieved. :class:`MatchFormat`.
        :type match_format: MatchFormat

        :raises TypeError: If Team or MatchFormat parameters are not of the enum types provided in this library.
        """
        return BattingService.retrieve_batting_stats(team, match_format)