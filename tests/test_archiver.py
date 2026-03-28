"""Tests for the SiteArchiver component."""

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from web_scrapper.core.archiver import SiteArchiver
from web_scrapper.core.models import CrawlItem


class TestSiteArchiver:
    """Tests for the SiteArchiver class."""

    @pytest.fixture
    def mock_renderer(self):
        """Create a mock renderer."""
        renderer = AsyncMock()
        renderer.fetch_html = AsyncMock(return_value="<html><body><a href='/test'>Test</a></body></html>")
        renderer.render_pdf = AsyncMock(return_value=b"pdf_bytes")
        renderer.fetch_markdown = AsyncMock(return_value="# Test")
        renderer.__aenter__ = AsyncMock(return_value=renderer)
        renderer.__aexit__ = AsyncMock(return_value=None)
        return renderer

    @pytest.fixture
    def mock_storage(self):
        """Create a mock storage."""
        storage = MagicMock()
        storage.is_downloaded = MagicMock(return_value=False)
        storage.save_pdf = MagicMock()
        storage.save_markdown = MagicMock()
        storage.get_archive_root = MagicMock(return_value=MagicMock())
        return storage

    @pytest.fixture
    def archiver(self, mock_renderer, mock_storage):
        """Create a SiteArchiver instance with mocked dependencies."""
        return SiteArchiver(
            renderer=mock_renderer,
            storage=mock_storage,
            root_url="https://example.com",
            max_depth=1,
            skip_existing=True,
            fetch_markdown=True,
            respect_robots=False,
        )

    @pytest.mark.asyncio
    async def test_process_page_success(self, archiver, mock_renderer, mock_storage):
        """Test successful page processing."""
        item = CrawlItem(url="https://example.com/test", depth=0)
        
        await archiver._process_page(item)
        
        mock_renderer.fetch_html.assert_called_once()
        mock_renderer.render_pdf.assert_called_once()
        mock_renderer.fetch_markdown.assert_called_once()
        mock_storage.save_pdf.assert_called_once()
        mock_storage.save_markdown.assert_called_once()
        assert archiver._progress.succeeded == 1

    @pytest.mark.asyncio
    async def test_process_page_skip_existing(self, archiver, mock_storage):
        """Test skipping already downloaded pages."""
        mock_storage.is_downloaded = MagicMock(return_value=True)
        item = CrawlItem(url="https://example.com/test", depth=0)
        
        await archiver._process_page(item)
        
        assert archiver._progress.skipped == 1

    @pytest.mark.asyncio
    async def test_process_page_pdf_failure(self, archiver, mock_renderer):
        """Test handling of PDF render failure."""
        mock_renderer.render_pdf = AsyncMock(side_effect=Exception("PDF failed"))
        item = CrawlItem(url="https://example.com/test", depth=0)
        
        await archiver._process_page(item)
        
        assert archiver._progress.failed == 1

    @pytest.mark.asyncio
    async def test_process_page_markdown_failure(self, archiver, mock_renderer):
        """Test handling of Markdown fetch failure."""
        mock_renderer.fetch_markdown = AsyncMock(side_effect=Exception("MD failed"))
        item = CrawlItem(url="https://example.com/test", depth=0)
        
        await archiver._process_page(item)
        
        assert archiver._progress.failed == 1

    @pytest.mark.asyncio
    async def test_process_page_no_markdown(self, mock_renderer, mock_storage):
        """Test processing with markdown disabled."""
        archiver = SiteArchiver(
            renderer=mock_renderer,
            storage=mock_storage,
            root_url="https://example.com",
            max_depth=1,
            fetch_markdown=False,
        )
        item = CrawlItem(url="https://example.com/test", depth=0)
        
        await archiver._process_page(item)
        
        mock_renderer.fetch_markdown.assert_not_called()
        assert archiver._progress.succeeded == 1

    @pytest.mark.asyncio
    async def test_safe_fetch_html_error(self, archiver, mock_renderer, caplog):
        """Test HTML fetch error handling."""
        mock_renderer.fetch_html = AsyncMock(side_effect=Exception("Network error"))
        
        result = await archiver._safe_fetch_html("https://example.com/test")
        
        assert result is None
        assert "HTML fetch failed" in caplog.text

    @pytest.mark.asyncio
    async def test_safe_render_pdf_error(self, archiver, mock_renderer, caplog):
        """Test PDF render error handling."""
        mock_renderer.render_pdf = AsyncMock(side_effect=Exception("Render error"))
        
        result = await archiver._safe_render_pdf("https://example.com/test")
        
        assert result is False
        assert "PDF render failed" in caplog.text

    @pytest.mark.asyncio
    async def test_safe_fetch_markdown_error(self, archiver, mock_renderer, caplog):
        """Test Markdown fetch error handling."""
        mock_renderer.fetch_markdown = AsyncMock(side_effect=Exception("MD error"))
        
        result = await archiver._safe_fetch_markdown("https://example.com/test")
        
        assert result is False
        assert "Markdown fetch failed" in caplog.text
