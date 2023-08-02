import logging

import pytest
import requests

from common.get_test_stat import get_stat
from fixtures.client import ClientApi

logger = logging.getLogger("api")


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="https://petstore.swagger.io",
    )


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--api-url")
    return ClientApi(url=url)


def pytest_terminal_summary(terminalreporter, config):
    """
    Send results to telegram
    """
    # settings
    is_send_grafana = True  # you can add this value in pytest_addoption
    if is_send_grafana:
        # test stat
        passed = get_stat(terminalreporter.stats.get("passed"))
        failed = get_stat(terminalreporter.stats.get("failed"))
        xfailed = get_stat(terminalreporter.stats.get("xfailed"))
        skipped = get_stat(terminalreporter.stats.get("skipped")) + xfailed
        total = passed + xfailed + failed + skipped
        # supabase
        supabase_url = 'your_url'
        supabase_api_key = 'your_api_key'
        headers = {
            "apikey": supabase_api_key,
            "Authorization": f"Bearer {supabase_api_key}",
            "Prefer": "return=representation",
        }
        # send result to supabase
        data_test_result = {
            'total': total,
            'passed': passed,
            'failed': failed,
            'skipped': skipped
        }
        requests.post(url=f'{supabase_url}/rest/v1/test',
                      json=data_test_result,
                      headers=headers)
