from cricinfo.helpers import StatType
from cricinfo.services import CricinfoService
from cricinfo import Team
from cricinfo import MatchFormat

class TestCricinfoService:

    def setup_method(self):
        self.team = Team.Pakistan
        self.match_format = MatchFormat.T20I

    def test_retrieve_stats_batting(self):
        stat_type = StatType.BATTING
        df = CricinfoService.retrieve_stats(team=self.team, match_format=self.match_format, stats_type=stat_type)
        assert df is not None, f"Expected dataframe returned from Cricinfo service to not be none."
        assert df.shape[1] == 15, f"Expected dataframe for batting stats to have to have 15 columns."
        assert df.shape[0] > 100, f"Expected atleast 100 records returned for sample batting stat retrieval."

    def test_retrieve_stats_bowling(self):
        stat_type = StatType.BOWLING
        df = CricinfoService.retrieve_stats(team=self.team, match_format=self.match_format, stats_type=stat_type)
        assert df is not None, f"Expected dataframe returned from Cricinfo service to not be none."
        assert df.shape[1] == 14, f"Expected dataframe for bowling stats to have to have 14 columns."
        assert df.shape[0] > 100, f"Expected atleast 100 records returned for sample bowling stat retrieval." 