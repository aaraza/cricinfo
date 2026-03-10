"""Constants for ESPN Cricinfo HTTP requests."""

BASE_URL = "https://stats.espncricinfo.com/ci/engine/stats/index.html"

PAGE_PARAMETER = "page"
TEAM_PARAMETER = "team"
TEMPLATE_PARAMETER = "template"
TEMPLATE_VALUE = "results"
TYPE_PARAMETER = "type"
MATCH_FORMAT_PARAMETER = "class"

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/87.0.4280.88 Safari/537.36"
)

HEADERS = {"User-Agent": USER_AGENT}
