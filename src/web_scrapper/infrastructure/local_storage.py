from __future__ import annotations

import logging
from pathlib import Path
from urllib.parse import urlparse

from web_scrapper.interfaces.storage import AbstractStorage

logger = logging.getLogger(__name__)

_PDF_FILENAME = "page.pdf"
_MD_FILENAME = "page.md"

class LocalStorage(AbstractStorage):
    """
    Local filesystem implementation of AbstractStorage.
    """

    def __init__(self, output_dir: Path | str = ".") -> None:
        self._output_dir = Path(output_dir).resolve()
        self._output_dir.mkdir(parents=True, exist_ok=True)
        logger.debug("Storage root: %s", self._output_dir)

    def page_dir(self, url: str) -> Path:
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        path_part = parsed.path.strip("/") or "index"

        if parsed.query:
            safe_query = self._sanitise_segment(parsed.query)
            path_part = f"{path_part}_{safe_query}"

        safe_segments = [self._sanitise_segment(seg) for seg in path_part.split("/") if seg]
        relative = Path(domain).joinpath(*safe_segments) if safe_segments else Path(domain) / "index"

        return self._output_dir / relative

    def is_downloaded(self, url: str) -> bool:
        d = self.page_dir(url)
        return (d / _PDF_FILENAME).exists() and (d / _MD_FILENAME).exists()

    def save_pdf(self, url: str, data: bytes) -> Path:
        target = self._ensure_dir(url) / _PDF_FILENAME
        target.write_bytes(data)
        logger.debug("PDF saved: %s", target)
        return target

    def save_markdown(self, url: str, text: str) -> Path:
        target = self._ensure_dir(url) / _MD_FILENAME
        target.write_text(text, encoding="utf-8")
        logger.debug("Markdown saved: %s", target)
        return target

    def get_archive_root(self, domain: str) -> Path:
        return self._output_dir / domain.lower()

    def _ensure_dir(self, url: str) -> Path:
        d = self.page_dir(url)
        d.mkdir(parents=True, exist_ok=True)
        return d

    @staticmethod
    def _sanitise_segment(segment: str) -> str:
        safe_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._~")
        return "".join(c if c in safe_chars else "_" for c in segment)
