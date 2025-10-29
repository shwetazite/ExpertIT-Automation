import pytest
from utils.driver_factory import get_driver

def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode")

@pytest.fixture
def driver(request):
    headless = request.config.getoption("--headless")
    driver = get_driver(headless=headless)
    yield driver
    driver.quit()
