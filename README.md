# cricinfo

Library for loading cricket [stats](https://stats.espncricinfo.com/ci/engine/stats/index.html) from https://www.espncricinfo.com into pandas dataframes.

# Features

1. Career batting stats for all players of a given team in international cricket by format or aggregated.
2. Career bowling stats for all players of a given team in international cricket by format or aggregated.

## Teams Supported
```
England
Australia
SouthAfrica
WestIndies
NewZealand
India
Pakistan
SriLanka
Zimbawe
```

## Formats Supported
```
TEST
ODI
T20I
International
```

## Sample Usage
```
from cricinfo import Cricinfo
from cricinfo import MatchFormat
from cricinfo import Team

Cricinfo.retrieve_batting_stats(team=Team.Pakistan, match_format=MatchFormat.Test)
```