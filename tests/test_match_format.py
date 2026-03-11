from cricinfo import MatchFormat


class TestMatchFormat:

    def test_match_formats(self):
        formats = [
            "Test",
            "ODI",
            "T20I",
            "International",
        ]
        for fmt in formats:
            assert fmt in MatchFormat.__members__
