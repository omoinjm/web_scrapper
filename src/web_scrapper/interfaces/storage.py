from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

class AbstractStorage(ABC):
    """
    Interface for filesystem persistence.
    """

    @abstractmethod
    def is_downloaded(self, url: str) -> bool:
        """Return True if the page has already been archived."""
        pass

    @abstractmethod
    def save_pdf(self, url: str, data: bytes) -> Path:
        """Save PDF bytes to storage."""
        pass

    @abstractmethod
    def save_markdown(self, url: str, text: str) -> Path:
        """Save Markdown text to storage."""
        pass

    @abstractmethod
    def get_archive_root(self, domain: str) -> Path:
        """Return the root path of the archive for a given domain."""
        pass
