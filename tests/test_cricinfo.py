from cricinfo import Cricinfo, Team, MatchFormat, StatType


class TestCricinfo:

    def setup_method(self):
        self.team = Team.Pakistan
        self.match_format = MatchFormat.T20I

    def test_retrieve_batting_stats(self):
        df = Cricinfo.retrieve_stats(self.team, self.match_format, StatType.BATTING)
        assert df is not None
        assert df.shape[1] == 15
        assert df.shape[0] > 100

    def test_retrieve_bowling_stats(self):
        df = Cricinfo.retrieve_stats(self.team, self.match_format, StatType.BOWLING)
        assert df is not None
        assert df.shape[1] == 14
        assert df.shape[0] > 100

    def test_retrieve_fielding_stats(self):
        df = Cricinfo.retrieve_stats(self.team, self.match_format, StatType.FIELDING)
        assert df is not None
        assert df.shape[1] == 11
        assert df.shape[0] > 100

    def test_retrieve_allround_stats(self):
        df = Cricinfo.retrieve_stats(self.team, self.match_format, StatType.ALLROUND)
        assert df is not None
        assert df.shape[1] == 14
        assert df.shape[0] > 100

    def test_retrieve_partnership_stats(self):
        df = Cricinfo.retrieve_stats(self.team, self.match_format, StatType.PARTNERSHIP)
        assert df is not None
        assert df.shape[1] == 9
        assert df.shape[0] > 100

    def test_retrieve_team_stats(self):
        df = Cricinfo.retrieve_stats(self.team, self.match_format, StatType.TEAM)
        assert df is not None
        assert df.shape[1] == 13
        assert df.shape[0] == 1

    def test_retrieve_aggregate_stats(self):
        df = Cricinfo.retrieve_stats(self.team, self.match_format, StatType.AGGREGATE)
        assert df is not None
        assert df.shape[1] == 10
        assert df.shape[0] == 1

    def test_retrieve_stats_without_team(self):
        df = Cricinfo.retrieve_stats(None, MatchFormat.Test, StatType.TEAM)
        assert df is not None
        assert df.shape[1] == 13
        assert df.shape[0] >= 13
