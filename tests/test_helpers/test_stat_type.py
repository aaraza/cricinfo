from cricinfo.helpers.stat_type import StatType

class TestStatType:

    def test_constants(self):
        stat_types = ["BATTING", "BOWLING"]
        for stat_type in stat_types:
            assert stat_type in StatType.__members__