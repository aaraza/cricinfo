from cricinfo import StatType


class TestStatType:

    def test_stat_types(self):
        stat_types = [
            "BATTING",
            "BOWLING",
            "FIELDING",
            "ALLROUND",
            "PARTNERSHIP",
            "TEAM",
            "AGGREGATE",
        ]
        for stat_type in stat_types:
            assert stat_type in StatType.__members__
