"""Pytest configuration and shared fixtures."""

import pytest


@pytest.fixture(autouse=True)
def configure_async():
    """Configure asyncio for all tests."""
    pass
