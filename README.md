# cricinfo

Library for loading cricket [stats](https://stats.espncricinfo.com/ci/engine/stats/index.html) from https://www.espncricinfo.com into pandas dataframes.

- [Documentation](https://cricinfo.readthedocs.io/en/latest/)
- [GitHub](https://github.com/aaraza/cricinfo)
- [PyPi](https://pypi.org/project/cricinfo-stats/): `pip install cricinfo-stats`

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

df = Cricinfo.retrieve_batting_stats(team=Team.Pakistan, match_format=MatchFormat.Test)
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

### Documentation
```
cp README.md docs/source/README.md
cd docs/
make clean
make html
```

## Packaging

Update version for the library as well as the docs:
1. `setup.py`
2. `docs\source\conf.py`