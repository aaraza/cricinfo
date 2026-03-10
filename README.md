# cricinfo

Python library for loading cricket [statistics](https://stats.espncricinfo.com/ci/engine/stats/index.html) from [ESPN Cricinfo](https://www.espncricinfo.com) into pandas DataFrames.

- [Documentation](https://cricinfo.readthedocs.io/en/latest/)
- [GitHub](https://github.com/aaraza/cricinfo)
- [PyPI](https://pypi.org/project/cricinfo-stats/): `pip install cricinfo-stats`

## Features

- Career batting, bowling, fielding, and all-round statistics for international cricketers.
- Partnership statistics for international cricket teams.
- Aggregated team statistics in international cricket.

## Supported Teams

- England
- Australia
- South Africa
- West Indies
- New Zealand
- India
- Pakistan
- Sri Lanka
- Zimbabwe

## Supported Formats

- Test
- ODI
- T20I
- International

## Usage

```python
from cricinfo import Cricinfo, Team, MatchFormat, StatType

# Retrieve batting stats for Pakistan in T20Is
df = Cricinfo.retrieve_stats(
    team=Team.Pakistan,
    match_format=MatchFormat.T20I,
    stat_type=StatType.BATTING,
)

# Retrieve team stats across all teams in Tests
df = Cricinfo.retrieve_stats(
    team=None,
    match_format=MatchFormat.Test,
    stat_type=StatType.TEAM,
)
```

## Stat Types

| StatType | Description |
|---|---|
| `BATTING` | Career batting statistics |
| `BOWLING` | Career bowling statistics |
| `FIELDING` | Career fielding statistics |
| `ALLROUND` | Career all-round statistics |
| `PARTNERSHIP` | Partnership statistics |
| `TEAM` | Team statistics |
| `AGGREGATE` | Aggregated team statistics |

## Development

### Testing

```
coverage run -m pytest -v -s
coverage report -m
```

### Linting

```
ruff check .
```

### Documentation

```
cp README.md docs/source/README.md
cd docs/
make clean
make html
```

## Packaging

Update the version in:
1. `setup.py`
2. `docs/source/conf.py`
