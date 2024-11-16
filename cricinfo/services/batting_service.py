import pandas as pd
import requests
from ..helpers import DataSanatizer
from ..helpers import RequestHelper
from ..match_format import MatchFormat
from ..team import Team

class BattingService:
    """
    For retrieving batting related data from cricinfo
    """

    @staticmethod
    def retrieve_batting_stats(team: Team, match_format: MatchFormat):
        BattingService._validate_request(team, match_format)
        params = BattingService._construct_batting_query_parameters(team=team, match_format=match_format)
        dataframes = []
        tables = BattingService._parse_batting_page(params=params, page=1, dataframes=dataframes)
        num_pages = int(tables[1][0][0].split(' ')[-1])
        for page in range(2, num_pages+1):
            BattingService._parse_batting_page(params=params, page=page, dataframes=dataframes)
        return pd.concat(dataframes, ignore_index=True)

    @staticmethod
    def _construct_batting_query_parameters(team: Team, match_format: MatchFormat) -> dict:
        return {
            RequestHelper.TEAM_PARAMETER.value : team.value,
            RequestHelper.MATCH_FORMAT_PARAMETER.value : match_format.value,
            RequestHelper.TYPE_PARAMETER.value  : RequestHelper.BATTING_TYPE_VALUE.value,
            RequestHelper.TEMPLATE_PARAMETER.value : RequestHelper.TEMPLATE_VALUE.value 
        }
    
    @staticmethod
    def _parse_batting_page(params: dict, page: int, dataframes: list[pd.DataFrame]):
        params[RequestHelper.PAGE_PARAMETER.value] = str(page)
        response = requests.get(RequestHelper.REQUEST_URL.value, headers=RequestHelper.HEADER_MAP(), params=params)
        tables = pd.read_html(response.content)
        dataframes.append(DataSanatizer._clean_nan_column(tables[2]))
        return tables
    
    @staticmethod
    def _validate_request(team, match_format):
        if not isinstance(team, Team):
            raise TypeError(f"Invalid type for team. Expected {Team.__name__}, got {type(team).__name__} instead.")
        
        if not isinstance(match_format, MatchFormat):
            raise TypeError(f"Invalid type for match format. Expected {MatchFormat.__name__}, got {type(match_format).__name__} instead.")