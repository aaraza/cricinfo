import sys
sys.path.append("...")
from cricinfo.helpers.stat_type import StatType
from cricinfo.services.cricinfo_service import CricinfoService
from cricinfo.team import Team
from cricinfo.match_format import MatchFormat
import pytest

class TestCricinfoService:

    def setup_method(self):
        self.team = Team.Pakistan
        self.match_format = MatchFormat.Test

    def test_retrieve_stats(self):
        df = CricinfoService.retrieve_stats(team=self.team, match_format=self.match_format, stats_type=StatType.TEAM)
        assert df is not None, "Expected dataframe returned from Cricinfo service to not be none."
        assert df.shape[1] == 13, "Expected dataframe for team stats to have to have 13 columns."
        assert df.shape[0] == 1, "Expected 1 records returned for sample team stat retrieval."

    def test_retrieve_stats_without_team_filter(self):
        df = CricinfoService.retrieve_stats(team=None, match_format=self.match_format, stats_type=StatType.TEAM)
        assert df is not None, "Expected dataframe returned from Cricinfo service to not be none."
        assert df.shape[1] == 13, "Expected dataframe for team stats to have to have 13 columns."
        assert df.shape[0] >= 13, "Expected 13 records returned for sample team stat retrieval without team filter."

    def test_invalid_team(self):
        stat_type = StatType.BOWLING
        with pytest.raises(TypeError, match="Invalid type for team"):
            CricinfoService.retrieve_stats(team="INVALID_TEAM", match_format=self.match_format, stats_type=stat_type)

    def test_invalid_format(self):
        stat_type = StatType.BOWLING
        with pytest.raises(TypeError, match="Invalid type for match_format"):
            CricinfoService.retrieve_stats(team=self.team, match_format="INVALID_FORMAT", stats_type=stat_type)

    def test_invalid_stats_type(self):
        with pytest.raises(TypeError, match="Invalid type for stats_type"):
            CricinfoService.retrieve_stats(team=self.team, match_format=self.match_format, stats_type="1")