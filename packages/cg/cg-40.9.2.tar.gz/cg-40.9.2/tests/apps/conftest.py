"""Fixtures for testing apps"""


import pytest
import requests

from cg.utils.commands import Process


@pytest.fixture
def response():
    """Mock a requests.response object"""

    class MockResponse(requests.Response):
        """Mock requests.response class"""

        def __init__(self):
            pass

        @property
        def ok(self):
            """Mock ok"""
            return False

        @property
        def text(self):
            """Mock text"""
            return "response text"

        @property
        def reason(self):
            """Mock reason"""
            return "response reason"

    return MockResponse()


@pytest.fixture
def mock_process():
    """Fixture returns mock Process class factory"""

    def _mock_process(result_stderr: str, result_stdout: str):
        class MockProcess(Process):
            """Process class with mocked run_command method"""

            def run_command(self, parameters=None):
                """Overrides originial run_command method"""
                self.stdout = result_stdout
                self.stderr = result_stderr

        return MockProcess

    return _mock_process
