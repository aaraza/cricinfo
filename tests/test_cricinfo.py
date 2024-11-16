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

    def test_retrive_fielding_stats(self):
        df = Cricinfo.retrieve_fielding_stats(team=self.team, match_format=self.match_format)
        assert df is not None, "Expected dataframe returned from Cricinfo service to not be none."
        assert df.shape[1] == 11, "Expected dataframe for fielding stats to have to have 11 columns."
        assert df.shape[0] > 100, "Expected atleast 100 records returned for sample fielding stat retrieval."
    
    def test_retrive_allround_stats(self):
        df = Cricinfo.retrieve_allround_stats(team=self.team, match_format=self.match_format)
        assert df is not None, "Expected dataframe returned from Cricinfo service to not be none."
        assert df.shape[1] == 14, "Expected dataframe for all-round stats to have to have 14 columns."
        assert df.shape[0] > 100, "Expected atleast 100 records returned for sample all-round stat retrieval."

    def test_retrieve_partnership_stats(self):
        df = Cricinfo.retrieve_partnership_stats(team=self.team, match_format=self.match_format)
        assert df is not None, "Expected dataframe returned from Cricinfo service to not be none."
        assert df.shape[1] == 9, "Expected dataframe for partnership stats to have to have 9 columns."
        assert df.shape[0] > 100, "Expected atleast 100 records returned for sample partnership stat retrieval." 

    def test_retrieve_team_stats(self):
        df = Cricinfo.retrieve_team_stats(team=self.team, match_format=self.match_format)
        assert df is not None, "Expected dataframe returned from Cricinfo service to not be none."
        assert df.shape[1] == 13, "Expected dataframe for team stats to have to have 13 columns."
        assert df.shape[0] == 1, "Expected 1 records returned for sample team stat retrieval."

    def test_retrieve_aggregate_stats(self):
        df = Cricinfo.retrieve_aggregate_stats(team=self.team, match_format=self.match_format)
        assert df is not None, "Expected dataframe returned from Cricinfo service to not be none."
        assert df.shape[1] == 10, "Expected dataframe for aggregate team stats to have to have 10 columns."
        assert df.shape[0] == 1, "Expected 1 records returned for sample team stat retrieval."     