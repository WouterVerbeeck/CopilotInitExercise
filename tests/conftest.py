import copy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module

BASELINE_ACTIVITIES = copy.deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset global in-memory activities state before and after each test."""
    # Arrange
    app_module.activities = copy.deepcopy(BASELINE_ACTIVITIES)

    # Act
    yield

    # Assert
    app_module.activities = copy.deepcopy(BASELINE_ACTIVITIES)


@pytest.fixture
def client():
    """Provide a FastAPI test client."""
    # Arrange
    app = app_module.app

    # Act
    test_client = TestClient(app)

    # Assert
    return test_client


def pytest_runtest_logreport(report):
    """Show colored status markers for completed test calls."""
    if report.when != "call":
        return

    green = "\033[92m"
    red = "\033[91m"
    reset = "\033[0m"

    if report.passed:
        print(f"{green}\u2713{reset} {report.nodeid}")
        return

    if report.failed:
        print(f"{red}\u2717{reset} {report.nodeid}")
