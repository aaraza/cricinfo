from cricinfo import Team

class TestTeam:

    def test_teams(self):
        teams = [
            "England",
            "Australia",
            "SouthAfrica",
            "WestIndies",
            "NewZealand",
            "India",
            "Pakistan",
            "SriLanka",
            "Zimbawe"
        ]
        for team in teams:
            assert team in Team.__members__