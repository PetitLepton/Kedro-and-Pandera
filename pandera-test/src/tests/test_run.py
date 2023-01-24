"""This module contains an example test.

Tests should be placed in ``src/tests``, in modules that mirror your
project's structure, and in files named test_*.py. They are simply
functions
named ``test_*`` which test a unit of logic.

To run the tests, run ``kedro test`` from the project root directory.
"""

# Built-in
from pathlib import Path

# Third-party
import pytest
from kedro.framework.context import KedroContext


@pytest.fixture
def project_context():  # type: ignore
    return KedroContext(package_name="pandera_test", project_path=Path.cwd())


# The tests below are here for the demonstration purpose
# and should be replaced with the ones testing the project
# functionality
class TestProjectContext:
    def test_project_path(self, project_context):  # type: ignore
        assert project_context.project_path == Path.cwd()
