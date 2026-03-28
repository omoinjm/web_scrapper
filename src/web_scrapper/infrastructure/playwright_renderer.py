from __future__ import annotations

import asyncio
import logging
from typing import Optional

import httpx
from playwright.async_api import (
    Browser,
    BrowserContext,
    Page,
    Playwright,
    async_playwright,
)

from web_scrapper.interfaces.renderer import AbstractRenderer

logger = logging.getLogger(__name__)

_DEFAULT_TIMEOUT_MS: int = 30_000
_DEFAULT_HTTP_TIMEOUT: float = 30.0
_JINA_BASE_URL: str = "https://r.jina.ai"
_PDF_OPTIONS: dict = {
    "format": "A4",
    "print_background": True,
    "margin": {"top": "1cm", "right": "1cm", "bottom": "1cm", "left": "1cm"},
}


class PlaywrightRenderer(AbstractRenderer):
    """
    Playwright-based implementation of the AbstractRenderer.
    
    Uses a semaphore to limit concurrent browser context creation and prevent
    Chromium from crashing under heavy load.
    """

    def __init__(
        self,
        delay: float = 1.0,
        max_retries: int = 3,
        concurrency: int = 5,
        timeout_ms: int = _DEFAULT_TIMEOUT_MS,
        http_timeout: float = _DEFAULT_HTTP_TIMEOUT,
    ) -> None:
        self.delay = delay
        self.max_retries = max_retries
        self.timeout_ms = timeout_ms
        self.http_timeout = http_timeout
        # Semaphore limits concurrent browser operations (context + page creation)
        self._semaphore = asyncio.Semaphore(concurrency)
        self._playwright: Optional[Playwright] = None
        self._browser: Optional[Browser] = None
        self._http_client: Optional[httpx.AsyncClient] = None

    async def start(self) -> None:
        self._playwright = await async_playwright().start()
        self._browser = await self._playwright.chromium.launch(
            headless=True,
            args=[
                "--disable-gpu",
                "--disable-dev-shm-usage",
                "--no-sandbox",
            ],
        )
        self._http_client = httpx.AsyncClient(
            timeout=self.http_timeout,
            follow_redirects=True,
            headers={"User-Agent": "Mozilla/5.0 (compatible; WebArchiver/1.0)"},
        )
        logger.info("Playwright browser started.")

    async def stop(self) -> None:
        if self._http_client:
            await self._http_client.aclose()
        if self._browser:
            await self._browser.close()
        if self._playwright:
            await self._playwright.stop()
        logger.info("Playwright browser stopped.")

    async def render_pdf(self, url: str) -> bytes:
        return await self._with_retry(self._render_pdf_once, url, label="PDF")

    async def fetch_html(self, url: str) -> str:
        return await self._with_retry(self._fetch_html_once, url, label="HTML")

    async def fetch_markdown(self, url: str) -> str:
        jina_url = f"{_JINA_BASE_URL}/{url}"
        return await self._with_retry(self._fetch_text_once, jina_url, label="Markdown")

    async def _render_pdf_once(self, url: str) -> bytes:
        assert self._browser is not None, "Browser not started"
        context: Optional[BrowserContext] = None
        page: Optional[Page] = None
        try:
            # Create context and page under semaphore protection
            context = await self._browser.new_context()
            page = await context.new_page()
            await page.goto(url, wait_until="networkidle", timeout=self.timeout_ms)
            pdf_bytes: bytes = await page.pdf(**_PDF_OPTIONS)
            return pdf_bytes
        except Exception:
            # Clean up page/context on failure
            if page is not None:
                await page.close()
            if context is not None:
                await context.close()
            raise

    async def _fetch_html_once(self, url: str) -> str:
        assert self._http_client is not None, "HTTP client not started"
        response = await self._http_client.get(url)
        response.raise_for_status()
        return response.text

    async def _fetch_text_once(self, url: str) -> str:
        assert self._http_client is not None, "HTTP client not started"
        response = await self._http_client.get(url)
        response.raise_for_status()
        return response.text

    async def _with_retry(self, coro_fn, url: str, label: str = "request"):
        async with self._semaphore:
            last_exc: Optional[Exception] = None
            for attempt in range(1, self.max_retries + 1):
                try:
                    result = await coro_fn(url)
                    if self.delay > 0:
                        await asyncio.sleep(self.delay)
                    return result
                except Exception as exc:
                    last_exc = exc
                    wait = 2 ** (attempt - 1)
                    logger.warning(
                        "%s attempt %d/%d failed for %s — %s. Retrying in %ds…",
                        label, attempt, self.max_retries, url, exc, wait,
                    )
                    await asyncio.sleep(wait)
            raise RuntimeError(f"All {self.max_retries} {label} attempts failed for {url}") from last_exc
