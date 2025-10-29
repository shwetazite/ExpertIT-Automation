import os
import sys
import pytest

# ✅ Ensure current directory (project root) is in sys.path
sys.path.append(os.path.dirname(__file__))

from utils.driver_factory import get_driver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    driver = get_driver(browser)
    yield driver
    driver.quit()
