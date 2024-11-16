from cricinfo.helpers import StatType
from cricinfo.services import CricinfoService
from cricinfo import Team
from cricinfo import MatchFormat
import pytest

class TestCricinfoService:

    def setup_method(self):
        self.team = Team.Pakistan
        self.match_format = MatchFormat.T20I

    def test_retrieve_stats(self):
        stat_type = StatType.BATTING
        df = CricinfoService.retrieve_stats(team=self.team, match_format=self.match_format, stats_type=stat_type)
        assert df is not None, "Expected dataframe returned from Cricinfo service to not be none."
        assert df.shape[1] == 15, "Expected dataframe for batting stats to have to have 15 columns."
        assert df.shape[0] > 100, "Expected atleast 100 records returned for sample batting stat retrieval."

    def test_invalid_team(self):
        stat_type = StatType.BOWLING
        with pytest.raises(TypeError, match="Invalid type for team"):
            CricinfoService.retrieve_stats(team="INVALID_TEAM", match_format=self.match_format, stats_type=stat_type)

    def test_invalid_format(self):
        stat_type = StatType.BOWLING
        with pytest.raises(TypeError, match="Invalid type for match_format"):
            CricinfoService.retrieve_stats(team=Team.Pakistan, match_format="INVALID_FORMAT", stats_type=stat_type)

    def test_invalid_stats_type(self):
        with pytest.raises(TypeError, match="Invalid type for stats_type"):
            CricinfoService.retrieve_stats(team=Team.Pakistan, match_format=self.match_format, stats_type="1")