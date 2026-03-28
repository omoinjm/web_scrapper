from __future__ import annotations

import logging
import time

logger = logging.getLogger(__name__)

class ProgressTracker:
    """Simple in-memory progress tracker logged at each step."""

    def __init__(self) -> None:
        self.total_queued: int = 0
        self.succeeded: int = 0
        self.skipped: int = 0
        self.failed: int = 0
        self._start: float = time.monotonic()

    @property
    def processed(self) -> int:
        return self.succeeded + self.skipped + self.failed

    def elapsed(self) -> str:
        secs = int(time.monotonic() - self._start)
        return f"{secs // 60}m{secs % 60:02d}s"

    def log_status(self, current_url: str) -> None:
        logger.info(
            "[%s] ✔ %d succeeded | ⏭ %d skipped | ✖ %d failed | queued ~%d — %s",
            self.elapsed(),
            self.succeeded,
            self.skipped,
            self.failed,
            self.total_queued - self.processed,
            current_url,
        )

    def summary(self) -> None:
        logger.info(
            "Crawl complete in %s — %d succeeded, %d skipped, %d failed, %d total unique URLs discovered.",
            self.elapsed(),
            self.succeeded,
            self.skipped,
            self.failed,
            self.total_queued,
        )
