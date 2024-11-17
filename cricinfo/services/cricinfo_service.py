import pandas as pd
import requests
from ..helpers.data_sanitizer import DataSanatizer
from ..helpers.request_helper import RequestHelper
from ..helpers.stat_type import StatType
from ..match_format import MatchFormat
from ..team import Team

class CricinfoService:
    @staticmethod
    def retrieve_stats(team: Team, match_format: MatchFormat, stats_type: StatType) -> pd.DataFrame:
        CricinfoService._validate_request(team, match_format, stats_type)
        params = CricinfoService._construct_query_parameters(team=team, match_format=match_format, stats_type=stats_type)
        dataframes = []
        tables = CricinfoService._parse_page(params=params, page=1, dataframes=dataframes)
        num_pages = int(tables[1][0][0].split(' ')[-1])
        for page in range(2, num_pages+1):
            CricinfoService._parse_page(params=params, page=page, dataframes=dataframes)
        return pd.concat(dataframes, ignore_index=True)

    @staticmethod
    def _construct_query_parameters(team: Team, match_format: MatchFormat, stats_type: StatType) -> dict:
        params = {
            RequestHelper.MATCH_FORMAT_PARAMETER.value : match_format.value,
            RequestHelper.TYPE_PARAMETER.value  : stats_type.value,
            RequestHelper.TEMPLATE_PARAMETER.value : RequestHelper.TEMPLATE_VALUE.value 
        }
        if team is not None:
            params[RequestHelper.TEAM_PARAMETER.value] = team.value
        return params
    
    @staticmethod
    def _parse_page(params: dict, page: int, dataframes: list[pd.DataFrame]):
        params[RequestHelper.PAGE_PARAMETER.value] = str(page)
        response = requests.get(RequestHelper.REQUEST_URL.value, headers=RequestHelper.HEADER_MAP(), params=params)
        tables = pd.read_html(response.content)
        dataframes.append(DataSanatizer._clean_nan_column(tables[2]))
        return tables
    
    @staticmethod
    def _validate_request(team, match_format, stats_type):
        if team is not None and not isinstance(team, Team):
            raise TypeError(f"Invalid type for team. Expected {Team.__name__}, got {type(team).__name__} instead.")
        
        if not isinstance(match_format, MatchFormat):
            raise TypeError(f"Invalid type for match_format. Expected {MatchFormat.__name__}, got {type(match_format).__name__} instead.")
        
        if not isinstance(stats_type, StatType):
            raise TypeError(f"Invalid type for stats_type. Expected {StatType.__name__}, got {type(stats_type).__name__} instead.")