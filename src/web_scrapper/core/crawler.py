from __future__ import annotations

import logging
from collections import deque
from urllib.parse import urljoin, urlparse, urlunparse

from bs4 import BeautifulSoup
from web_scrapper.core.models import CrawlItem

logger = logging.getLogger(__name__)

_IGNORED_SCHEMES = frozenset({"mailto", "tel", "javascript", "data", "ftp", "ftps"})

class CrawlQueue:
    """
    BFS-based crawl queue that tracks visited URLs and enforces max depth.
    """

    def __init__(self, root_url: str, max_depth: int = 3) -> None:
        self.root_url = root_url
        self.max_depth = max_depth
        self.visited: set[str] = set()
        self._queue: deque[CrawlItem] = deque()

        parsed = urlparse(self.root_url)
        self.domain: str = parsed.netloc
        normalised = self.normalise_url(self.root_url)
        self._queue.append(CrawlItem(url=normalised, depth=0))
        self.visited.add(normalised)

    def __len__(self) -> int:
        return len(self._queue)

    def __bool__(self) -> bool:
        return bool(self._queue)

    def pop(self) -> CrawlItem:
        return self._queue.popleft()

    def enqueue_links(self, base_url: str, html: str, current_depth: int) -> int:
        if current_depth >= self.max_depth:
            return 0

        soup = BeautifulSoup(html, "html.parser")
        added = 0

        for tag in soup.find_all("a", href=True):
            href: str = tag["href"].strip()
            if not href:
                continue

            absolute = urljoin(base_url, href)
            parsed = urlparse(absolute)

            if parsed.scheme in _IGNORED_SCHEMES or parsed.scheme not in ("http", "https"):
                continue

            if self._bare_domain(parsed.netloc) != self._bare_domain(self.domain):
                logger.debug("External link skipped: %s", absolute)
                continue

            normalised = self.normalise_url(absolute)

            if normalised in self.visited:
                continue

            self.visited.add(normalised)
            self._queue.append(CrawlItem(url=normalised, depth=current_depth + 1))
            added += 1
            logger.debug("Queued [depth=%d]: %s", current_depth + 1, normalised)

        return added

    @staticmethod
    def normalise_url(url: str) -> str:
        p = urlparse(url)
        path = p.path.rstrip("/") or "/"
        return urlunparse((
            p.scheme.lower(),
            p.netloc.lower(),
            path,
            p.params,
            p.query,
            "",
        ))

    @staticmethod
    def _bare_domain(netloc: str) -> str:
        """Strip 'www.' prefix from domain (Python 3.8 compatible)."""
        netloc = netloc.lower()
        if netloc.startswith("www."):
            return netloc[4:]
        return netloc
