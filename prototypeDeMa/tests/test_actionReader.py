"""Module for testing the behavior of actionReader.py"""

import pytest
import prototypeDeMa.actionReader as AR


@pytest.fixture
def newActionReader():
    """Create a new ActionReader"""

    actionReader = AR.ActionReader()
    return actionReader


def test_actionReaderExists(newActionReader):
    """For testing purposes"""

    assert newActionReader is not None, "The ActionReader doesn't exist!"
