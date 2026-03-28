"""Tests for the PlaywrightRenderer component."""

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest

from web_scrapper.infrastructure.playwright_renderer import PlaywrightRenderer


class TestPlaywrightRenderer:
    """Tests for the PlaywrightRenderer class."""

    @pytest.fixture
    def renderer(self):
        """Create a PlaywrightRenderer instance."""
        return PlaywrightRenderer(
            delay=0.1,
            max_retries=2,
            concurrency=3,
            timeout_ms=5000,
            http_timeout=5.0,
        )

    def test_init_default_values(self):
        """Test default initialization values."""
        renderer = PlaywrightRenderer()
        
        assert renderer.delay == 1.0
        assert renderer.max_retries == 3
        assert renderer.concurrency == 5
        assert renderer.timeout_ms == 30_000
        assert renderer.http_timeout == 30.0

    def test_init_custom_values(self):
        """Test custom initialization values."""
        renderer = PlaywrightRenderer(
            delay=2.0,
            max_retries=5,
            concurrency=10,
            timeout_ms=10000,
            http_timeout=15.0,
        )
        
        assert renderer.delay == 2.0
        assert renderer.max_retries == 5
        assert renderer._semaphore._value == 10
        assert renderer.timeout_ms == 10000
        assert renderer.http_timeout == 15.0

    @pytest.mark.asyncio
    async def test_start_initializes_browser(self, renderer):
        """Test that start() initializes browser and HTTP client."""
        with patch("web_scrapper.infrastructure.playwright_renderer.async_playwright") as mock_playwright:
            mock_browser = AsyncMock()
            mock_playwright.return_value.start = AsyncMock(return_value=MagicMock())
            mock_playwright.return_value.start.return_value.chromium.launch = AsyncMock(return_value=mock_browser)
            
            await renderer.start()
            
            assert renderer._playwright is not None
            assert renderer._browser is not None
            assert renderer._http_client is not None
            assert isinstance(renderer._http_client, httpx.AsyncClient)

    @pytest.mark.asyncio
    async def test_stop_closes_resources(self, renderer):
        """Test that stop() closes all resources."""
        mock_playwright = AsyncMock()
        mock_browser = AsyncMock()
        mock_http_client = AsyncMock()
        
        renderer._playwright = mock_playwright
        renderer._browser = mock_browser
        renderer._http_client = mock_http_client
        
        await renderer.stop()
        
        mock_http_client.aclose.assert_called_once()
        mock_browser.close.assert_called_once()
        mock_playwright.stop.assert_called_once()

    @pytest.mark.asyncio
    async def test_render_pdf_once_creates_context_and_page(self, renderer):
        """Test PDF rendering creates and cleans up context/page."""
        mock_context = AsyncMock()
        mock_page = AsyncMock()
        mock_page.pdf = AsyncMock(return_value=b"pdf_bytes")
        
        mock_browser = AsyncMock()
        mock_browser.new_context = AsyncMock(return_value=mock_context)
        mock_context.new_page = AsyncMock(return_value=mock_page)
        
        renderer._browser = mock_browser
        
        result = await renderer._render_pdf_once("https://example.com")
        
        assert result == b"pdf_bytes"
        mock_browser.new_context.assert_called_once()
        mock_context.new_page.assert_called_once()
        mock_page.goto.assert_called_once()
        mock_page.pdf.assert_called_once()
        mock_page.close.assert_called_once()
        mock_context.close.assert_called_once()

    @pytest.mark.asyncio
    async def test_render_pdf_once_cleanup_on_error(self, renderer):
        """Test that context/page are cleaned up on error."""
        mock_context = AsyncMock()
        mock_page = AsyncMock()
        mock_page.goto = AsyncMock(side_effect=Exception("Navigation failed"))
        
        mock_browser = AsyncMock()
        mock_browser.new_context = AsyncMock(return_value=mock_context)
        mock_context.new_page = AsyncMock(return_value=mock_page)
        
        renderer._browser = mock_browser
        
        with pytest.raises(Exception, match="Navigation failed"):
            await renderer._render_pdf_once("https://example.com")
        
        mock_page.close.assert_called_once()
        mock_context.close.assert_called_once()

    @pytest.mark.asyncio
    async def test_fetch_html_once(self, renderer):
        """Test HTML fetching."""
        mock_response = MagicMock()
        mock_response.text = "<html><body>Test</body></html>"
        mock_response.raise_for_status = MagicMock()
        
        mock_client = AsyncMock()
        mock_client.get = AsyncMock(return_value=mock_response)
        
        renderer._http_client = mock_client
        
        result = await renderer._fetch_html_once("https://example.com")
        
        assert result == "<html><body>Test</body></html>"
        mock_client.get.assert_called_once_with("https://example.com")

    @pytest.mark.asyncio
    async def test_fetch_markdown_uses_jina_api(self, renderer):
        """Test Markdown fetching uses Jina.ai API."""
        mock_response = MagicMock()
        mock_response.text = "# Test Content"
        mock_response.raise_for_status = MagicMock()
        
        mock_client = AsyncMock()
        mock_client.get = AsyncMock(return_value=mock_response)
        
        renderer._http_client = mock_client
        
        result = await renderer.fetch_markdown("https://example.com")
        
        assert result == "# Test Content"
        mock_client.get.assert_called_once_with("https://r.jina.ai/https://example.com")

    @pytest.mark.asyncio
    async def test_with_retry_succeeds_first_attempt(self, renderer):
        """Test retry wrapper succeeds on first attempt."""
        mock_fn = AsyncMock(return_value="success")
        
        result = await renderer._with_retry(mock_fn, "https://example.com", label="Test")
        
        assert result == "success"
        mock_fn.assert_called_once()

    @pytest.mark.asyncio
    async def test_with_retry_retries_on_failure(self, renderer):
        """Test retry wrapper retries on failure."""
        call_count = 0
        
        async def flaky_fn(url):
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise Exception("Temporary error")
            return "success"
        
        result = await renderer._with_retry(flaky_fn, "https://example.com", label="Test")
        
        assert result == "success"
        assert call_count == 3

    @pytest.mark.asyncio
    async def test_with_retry_exhausts_retries(self, renderer):
        """Test retry wrapper raises after exhausting retries."""
        async def failing_fn(url):
            raise Exception("Always fails")
        
        with pytest.raises(RuntimeError, match="All 2 Test attempts failed"):
            await renderer._with_retry(failing_fn, "https://example.com", label="Test")

    @pytest.mark.asyncio
    async def test_semaphore_limits_concurrency(self):
        """Test that semaphore limits concurrent operations."""
        renderer = PlaywrightRenderer(concurrency=2)
        
        concurrent_calls = 0
        max_concurrent = 0
        
        async def track_concurrency(url):
            nonlocal concurrent_calls, max_concurrent
            concurrent_calls += 1
            max_concurrent = max(max_concurrent, concurrent_calls)
            await asyncio.sleep(0.1)
            concurrent_calls -= 1
            return "done"
        
        renderer._semaphore = asyncio.Semaphore(2)
        
        tasks = [renderer._with_retry(track_concurrency, f"https://example.com/{i}", "Test") for i in range(5)]
        await asyncio.gather(*tasks)
        
        assert max_concurrent <= 2
