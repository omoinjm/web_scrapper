from __future__ import annotations

import logging
from urllib.parse import urlparse, urlunparse
from urllib.robotparser import RobotFileParser

import httpx

logger = logging.getLogger(__name__)


class RobotsTxtChecker:
    """
    Checks URLs against a site's robots.txt rules.
    
    Fetches and caches robots.txt per domain, allowing efficient
    compliance checking during crawling.
    """

    def __init__(self, http_timeout: float = 10.0) -> None:
        self.http_timeout = http_timeout
        self._parsers: dict[str, RobotFileParser] = {}
        self._http_client: httpx.Client | None = None

    def __enter__(self) -> RobotsTxtChecker:
        self._http_client = httpx.Client(timeout=self.http_timeout)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if self._http_client:
            self._http_client.close()

    def _get_domain(self, url: str) -> str:
        """Extract the domain (scheme + netloc) from a URL."""
        parsed = urlparse(url)
        return urlunparse((parsed.scheme, parsed.netloc, "", "", "", ""))

    def _fetch_robots(self, domain: str) -> RobotFileParser:
        """Fetch and parse robots.txt for a domain."""
        robots_url = f"{domain}/robots.txt"
        parser = RobotFileParser()
        
        if self._http_client is None:
            logger.warning("HTTP client not initialized, allowing all URLs")
            parser.set_url(robots_url)
            return parser
        
        try:
            response = self._http_client.get(robots_url)
            if response.status_code == 200:
                parser.parse(response.text.splitlines())
            elif response.status_code == 404:
                logger.debug("No robots.txt found for %s, allowing all URLs", domain)
            else:
                logger.warning(
                    "Unexpected status %d for robots.txt at %s",
                    response.status_code, domain
                )
        except httpx.RequestError as exc:
            logger.warning("Failed to fetch robots.txt for %s: %s", domain, exc)
        
        parser.set_url(robots_url)
        return parser

    def get_parser(self, url: str) -> RobotFileParser:
        """Get or create the RobotFileParser for a URL's domain."""
        domain = self._get_domain(url)
        if domain not in self._parsers:
            self._parsers[domain] = self._fetch_robots(domain)
        return self._parsers[domain]

    def can_fetch(self, url: str, user_agent: str = "*") -> bool:
        """Check if a URL can be fetched according to robots.txt rules."""
        parser = self.get_parser(url)
        if not parser.mtime():
            # robots.txt was not fetched or empty, allow all
            return True
        try:
            return parser.can_fetch(user_agent, url)
        except Exception:
            # Parse error, be permissive
            return True

    def is_allowed(self, url: str, user_agent: str = "*") -> bool:
        """Alias for can_fetch for clearer semantics."""
        return self.can_fetch(url, user_agent)
