from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class CrawlItem:
    """Represents a single URL to be processed at a given depth."""
    url: str
    depth: int
