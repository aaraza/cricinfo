from enum import Enum

class RequestHelper(Enum):
    """
    Constants used when making HTTP requests to cricinfo
    """

    PAGE_PARAMETER = "page"
    TEAM_PARAMETER = "team"
    TEMPLATE_PARAMETER = "template"
    TEMPLATE_VALUE = "results"
    TYPE_PARAMETER = "type"
    MATCH_FORMAT_PARAMETER = "class"
    USER_AGENT_PARAMEATER = "User-Agent"
    USER_AGENT_VALUE = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    REQUEST_URL='https://stats.espncricinfo.com/ci/engine/stats/index.html'

    @classmethod
    def HEADER_MAP(cls):
        """
        Populates the User Agent Header
        """
        return {cls.USER_AGENT_PARAMEATER.value : cls.USER_AGENT_VALUE.value}
