# cricinfo

[![Tests](https://github.com/aaraza/cricinfo/actions/workflows/run_test.yml/badge.svg)](https://github.com/aaraza/cricinfo/actions/workflows/run_test.yml)
[![Documentation](https://readthedocs.org/projects/cricinfo/badge/?version=latest)](https://cricinfo.readthedocs.io/en/latest/)
[![PyPI](https://img.shields.io/pypi/v/cricinfo-stats)](https://pypi.org/project/cricinfo-stats/)

Python library for loading cricket [statistics](https://stats.espncricinfo.com/ci/engine/stats/index.html) from [ESPN Cricinfo](https://www.espncricinfo.com) into pandas DataFrames.

- [Documentation](https://cricinfo.readthedocs.io/en/latest/)
- [GitHub](https://github.com/aaraza/cricinfo)
- [PyPI](https://pypi.org/project/cricinfo-stats/)

## Installation

```
pip install cricinfo-stats
```

Requires Python 3.10+.

## Features

- Career batting, bowling, fielding, and all-round statistics for international cricketers.
- Partnership statistics for international cricket teams.
- Aggregated team statistics in international cricket.

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

### Sample Output

```
>>> df.head()
                Player  Mat  Inns    Runs     HS   Ave    SR  100  50  ...
0       Babar Azam (PK)   99   93    3485  122*  46.46  129.0  9  26  ...
1  Mohammad Rizwan (PK)   72   65    2088   88*  38.66  126.0  0  19  ...
```

### Error Handling

`retrieve_stats` may raise:
- `requests.HTTPError` if ESPN Cricinfo is unreachable or returns an error.
- `ValueError` if the response HTML cannot be parsed.

## Supported Teams

| Enum Value | Team |
|---|---|
| `Team.England` | England |
| `Team.Australia` | Australia |
| `Team.SouthAfrica` | South Africa |
| `Team.WestIndies` | West Indies |
| `Team.NewZealand` | New Zealand |
| `Team.India` | India |
| `Team.Pakistan` | Pakistan |
| `Team.SriLanka` | Sri Lanka |
| `Team.Zimbabwe` | Zimbabwe |

Pass `team=None` to retrieve stats for all teams.

## Supported Formats

| Enum Value | Format |
|---|---|
| `MatchFormat.Test` | Test |
| `MatchFormat.ODI` | ODI |
| `MatchFormat.T20I` | T20I |
| `MatchFormat.International` | International (aggregated) |

## Stat Types

| Enum Value | Description |
|---|---|
| `StatType.BATTING` | Career batting statistics |
| `StatType.BOWLING` | Career bowling statistics |
| `StatType.FIELDING` | Career fielding statistics |
| `StatType.ALLROUND` | Career all-round statistics |
| `StatType.PARTNERSHIP` | Partnership statistics |
| `StatType.TEAM` | Team statistics |
| `StatType.AGGREGATE` | Aggregated team statistics |

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

Documentation is hosted on [Read the Docs](https://cricinfo.readthedocs.io/en/latest/) and rebuilds automatically on every push to `main` (configured via `.readthedocs.yaml`). Sphinx pulls docstrings from source using `autodoc`.

To build locally:

```
cd docs/
make clean
make html
```

## Packaging

Update the version in:
1. `setup.py`
2. `docs/source/conf.py`
