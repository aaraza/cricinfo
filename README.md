# cricinfo

Library for loading cricket [stats](https://stats.espncricinfo.com/ci/engine/stats/index.html) from https://www.espncricinfo.com into pandas dataframes.

## Features

1. Career batting/bowling/fielding/all-round statistics for international cricketers.
2. Statistics for all partnerships in international cricket for a given team.
3. Aggregated statitics for teams in international cricket.

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

## Code Quality
Run test and lint commands from the root of this repo.

### Testing
```
coverage run -m pytest -v -s
coverage report -m
```

### Linting
`ruff check .`

[![Coverage Status](coverage.svg)](https://github.com/aaraza/cricinfo)