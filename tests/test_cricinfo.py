from cricinfo import Cricinfo
from cricinfo import Team
from cricinfo import MatchFormat

class TestCricInfo:

    def setup_method(self):
        self.team = Team.Pakistan
        self.match_format = MatchFormat.T20I

    def test_retrieve_batting_stats(self):
        df = Cricinfo.retrieve_batting_stats(team=self.team, match_format=self.match_format)
        assert df is not None, "Expected dataframe returned from Cricinfo service to not be none."
        assert df.shape[1] == 15, "Expected dataframe for batting stats to have to have 15 columns."
        assert df.shape[0] > 100, "Expected atleast 100 records returned for sample batting stat retrieval."

    def test_retrieve_bowling_stats(self):
        df = Cricinfo.retrieve_bowling_stats(team=self.team, match_format=self.match_format)
        assert df is not None, "Expected dataframe returned from Cricinfo service to not be none."
        assert df.shape[1] == 14, "Expected dataframe for bowling stats to have to have 14 columns."
        assert df.shape[0] > 100, "Expected atleast 100 records returned for sample bowling stat retrieval." 