from cricinfo import MatchFormat 

class TestMatchFormats:

    def test_match_formats(self):
        match_formats = [
            "Test",
            "ODI",
            "T20I",
            "International"
        ]
        for match_format in match_formats:
            assert match_format in MatchFormat.__members__