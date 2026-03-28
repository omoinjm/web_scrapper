from __future__ import annotations

import asyncio
import logging
from typing import Optional
from urllib.parse import urlparse

from web_scrapper.core.crawler import CrawlQueue
from web_scrapper.core.models import CrawlItem
from web_scrapper.core.robots_checker import RobotsTxtChecker
from web_scrapper.core.tracker import ProgressTracker
from web_scrapper.interfaces.renderer import AbstractRenderer
from web_scrapper.interfaces.storage import AbstractStorage

logger = logging.getLogger(__name__)


class SiteArchiver:
    """
    Coordinates the crawl queue, renderer, and storage to archive an entire site.
    """

    def __init__(
        self,
        renderer: AbstractRenderer,
        storage: AbstractStorage,
        root_url: str,
        max_depth: int = 3,
        skip_existing: bool = True,
        fetch_markdown: bool = True,
        respect_robots: bool = False,
    ) -> None:
        self._renderer = renderer
        self._storage = storage
        self.root_url = root_url
        self.max_depth = max_depth
        self._skip_existing = skip_existing
        self._fetch_markdown = fetch_markdown
        self._respect_robots = respect_robots

        parsed = urlparse(root_url)
        self.domain = parsed.netloc

        self._queue = CrawlQueue(root_url=root_url, max_depth=max_depth)
        self._progress = ProgressTracker()
        self._robots_checker: Optional[RobotsTxtChecker] = None

        if self._respect_robots:
            self._robots_checker = RobotsTxtChecker()

    async def run(self) -> ProgressTracker:
        logger.info("Starting archive of %s (max depth=%d)", self.root_url, self.max_depth)
        archive_root = self._storage.get_archive_root(self.domain)
        logger.info("Output directory: %s", archive_root)

        with self._robots_checker if self._robots_checker else asyncio.nullcontext():  # type: ignore[attr-defined]
            async with self._renderer:
                tasks: list[asyncio.Task] = []

                while self._queue or tasks:
                    while self._queue:
                        item = self._queue.pop()
                        
                        # Check robots.txt if enabled
                        if self._robots_checker and not self._robots_checker.is_allowed(item.url):
                            logger.info("⏭  Skipping (robots.txt): %s", item.url)
                            self._progress.skipped += 1
                            continue
                        
                        self._progress.total_queued += 1
                        task = asyncio.create_task(
                            self._process_page(item),
                            name=f"page:{item.url}",
                        )
                        tasks.append(task)

                    if not tasks:
                        break

                    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
                    tasks = list(pending)

                    for task in done:
                        exc = task.exception()
                        if exc:
                            logger.error("Unexpected task failure: %s", exc)

        self._progress.summary()
        return self._progress

    async def _process_page(self, item: CrawlItem) -> None:
        url = item.url
        self._progress.log_status(url)

        if self._skip_existing and self._storage.is_downloaded(url):
            logger.info("⏭  Skipping (already archived): %s", url)
            self._progress.skipped += 1
            return

        logger.info("🌐 Processing [depth=%d]: %s", item.depth, url)

        html: Optional[str] = await self._safe_fetch_html(url)

        # Only enqueue links if HTML was successfully fetched
        if html is not None:
            try:
                new_links = self._queue.enqueue_links(url, html, item.depth)
                if new_links:
                    logger.debug("Discovered %d new links from %s", new_links, url)
            except Exception as exc:
                logger.error("Failed to enqueue links from %s: %s", url, exc)
        else:
            logger.warning("Skipping link extraction for %s due to HTML fetch failure", url)

        pdf_ok = await self._safe_render_pdf(url)
        md_ok = True  # Assume success if markdown is disabled
        
        if self._fetch_markdown:
            md_ok = await self._safe_fetch_markdown(url)

        if pdf_ok and md_ok:
            self._progress.succeeded += 1
            logger.info("✔  Done: %s", url)
        elif pdf_ok or md_ok:
            # Partial success - still count as failed but log what succeeded
            self._progress.failed += 1
            logger.warning("✖  Partial failure for: %s (pdf=%s, md=%s)", url, pdf_ok, md_ok)
        else:
            self._progress.failed += 1
            logger.error("✖  Complete failure for: %s (both PDF and Markdown failed)", url)

    async def _safe_fetch_html(self, url: str) -> Optional[str]:
        try:
            return await self._renderer.fetch_html(url)
        except Exception as exc:
            logger.error("HTML fetch failed for %s: %s", url, exc)
            return None

    async def _safe_render_pdf(self, url: str) -> bool:
        try:
            pdf_bytes = await self._renderer.render_pdf(url)
            self._storage.save_pdf(url, pdf_bytes)
            return True
        except Exception as exc:
            logger.error("PDF render failed for %s: %s", url, exc)
            return False

    async def _safe_fetch_markdown(self, url: str) -> bool:
        try:
            markdown = await self._renderer.fetch_markdown(url)
            self._storage.save_markdown(url, markdown)
            return True
        except Exception as exc:
            logger.error("Markdown fetch failed for %s: %s", url, exc)
            return False
