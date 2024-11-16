from cricinfo.helpers.request_helper import RequestHelper

class TestRequestHelper:

    def test_request_header_map(self):
        header_map = RequestHelper.HEADER_MAP()
        assert header_map is not None
        assert len(header_map) >= 1
        assert 'User-Agent' in header_map

    def test_constants(self):
        constants = [
            "PAGE_PARAMETER",
            "TEAM_PARAMETER",
            "TEMPLATE_PARAMETER",
            "TEMPLATE_VALUE",
            "TYPE_PARAMETER",
            "MATCH_FORMAT_PARAMETER",
            "USER_AGENT_PARAMEATER",
            "USER_AGENT_VALUE",
            "REQUEST_URL",
        ]
        for constant in constants:
            assert constant in RequestHelper.__members__