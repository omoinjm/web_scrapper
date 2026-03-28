"""Interfaces module exports."""

from web_scrapper.interfaces.renderer import AbstractRenderer
from web_scrapper.interfaces.storage import AbstractStorage

__all__ = [
    "AbstractRenderer",
    "AbstractStorage",
]
