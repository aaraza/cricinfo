from io import StringIO

import pandas as pd
import requests

from .helpers.constants import (
    BASE_URL,
    HEADERS,
    MATCH_FORMAT_PARAMETER,
    PAGE_PARAMETER,
    TEAM_PARAMETER,
    TEMPLATE_PARAMETER,
    TEMPLATE_VALUE,
    TYPE_PARAMETER,
)
from .helpers.data_sanitizer import clean_nan_column
from .match_format import MatchFormat
from .stat_type import StatType
from .team import Team


class Cricinfo:
    """Loads cricket statistics from ESPN Cricinfo into pandas DataFrames.

    Example::

        from cricinfo import Cricinfo, Team, MatchFormat, StatType

        df = Cricinfo.retrieve_stats(
            team=Team.Pakistan,
            match_format=MatchFormat.T20I,
            stat_type=StatType.BATTING,
        )
    """

    @staticmethod
    def retrieve_stats(
        team: Team | None,
        match_format: MatchFormat,
        stat_type: StatType,
    ) -> pd.DataFrame:
        """Retrieve statistics from ESPN Cricinfo.

        :param team: Filter by team, or ``None`` for all teams.
        :param match_format: The match format to filter by.
        :param stat_type: The type of statistics to retrieve.
        :returns: A DataFrame containing the requested statistics.
        :raises requests.HTTPError: If the HTTP request fails.
        :raises ValueError: If the response cannot be parsed.
        """
        params = Cricinfo._build_params(team, match_format, stat_type)
        dataframes = []

        tables = Cricinfo._fetch_page(params, page=1)
        dataframes.append(clean_nan_column(tables[2]))

        num_pages = Cricinfo._parse_page_count(tables)
        for page in range(2, num_pages + 1):
            tables = Cricinfo._fetch_page(params, page)
            dataframes.append(clean_nan_column(tables[2]))

        return pd.concat(dataframes, ignore_index=True)

    @staticmethod
    def _build_params(team, match_format, stat_type):
        params = {
            MATCH_FORMAT_PARAMETER: match_format.value,
            TYPE_PARAMETER: stat_type.value,
            TEMPLATE_PARAMETER: TEMPLATE_VALUE,
        }
        if team is not None:
            params[TEAM_PARAMETER] = team.value
        return params

    @staticmethod
    def _fetch_page(params, page):
        params[PAGE_PARAMETER] = str(page)
        response = requests.get(BASE_URL, headers=HEADERS, params=params)
        response.raise_for_status()

        tables = pd.read_html(StringIO(response.text))
        if len(tables) < 3:
            raise ValueError(
                f"Expected at least 3 tables in response, got {len(tables)}. "
                "The ESPN Cricinfo page structure may have changed."
            )
        return tables

    @staticmethod
    def _parse_page_count(tables):
        try:
            return int(tables[1][0][0].split()[-1])
        except (IndexError, ValueError, KeyError) as e:
            raise ValueError(
                "Could not determine page count from response. "
                "The ESPN Cricinfo page structure may have changed."
            ) from e
