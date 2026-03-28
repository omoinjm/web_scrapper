"""Tests for the LocalStorage component."""

import pytest
from pathlib import Path

from web_scrapper.infrastructure.local_storage import LocalStorage


class TestLocalStorage:
    """Tests for the LocalStorage class."""

    def test_init_creates_output_dir(self, tmp_path):
        """Test that initialization creates the output directory."""
        output_dir = tmp_path / "new_dir"
        storage = LocalStorage(output_dir=output_dir)
        
        assert output_dir.exists()
        assert output_dir.is_dir()

    def test_init_with_string_path(self, tmp_path):
        """Test initialization with string path."""
        storage = LocalStorage(output_dir=str(tmp_path))
        
        assert storage._output_dir == tmp_path

    def test_page_dir_basic(self, tmp_path):
        """Test basic page directory generation."""
        storage = LocalStorage(output_dir=tmp_path)
        url = "https://example.com/about"
        page_dir = storage.page_dir(url)

        assert page_dir == tmp_path / "example.com" / "about"

    def test_page_dir_root(self, tmp_path):
        """Test page directory for root URL."""
        storage = LocalStorage(output_dir=tmp_path)
        url = "https://example.com/"
        page_dir = storage.page_dir(url)

        assert page_dir == tmp_path / "example.com" / "index"

    def test_page_dir_with_query(self, tmp_path):
        """Test page directory with query parameters."""
        storage = LocalStorage(output_dir=tmp_path)
        url = "https://example.com/search?q=test&page=1"
        page_dir = storage.page_dir(url)

        # Query params should be sanitized
        assert page_dir.relative_to(tmp_path) == Path("example.com/search_q_test_page_1")

    def test_page_dir_with_nested_path(self, tmp_path):
        """Test page directory with nested path."""
        storage = LocalStorage(output_dir=tmp_path)
        url = "https://example.com/blog/2024/post-title"
        page_dir = storage.page_dir(url)

        assert page_dir == tmp_path / "example.com" / "blog" / "2024" / "post-title"

    def test_page_dir_sanitizes_special_chars(self, tmp_path):
        """Test that special characters are sanitized."""
        storage = LocalStorage(output_dir=tmp_path)
        url = "https://example.com/path/with spaces!and@special#chars"
        page_dir = storage.page_dir(url)

        # Special chars should be replaced with underscores
        path_str = str(page_dir)
        assert " " not in path_str
        assert "!" not in path_str
        assert "@" not in path_str
        assert "#" not in path_str

    def test_is_downloaded_false(self, tmp_path):
        """Test is_downloaded returns False when files don't exist."""
        storage = LocalStorage(output_dir=tmp_path)
        url = "https://example.com/page"

        assert storage.is_downloaded(url) is False

    def test_is_downloaded_true(self, tmp_path):
        """Test is_downloaded returns True when both files exist."""
        storage = LocalStorage(output_dir=tmp_path)
        url = "https://example.com/page"

        page_dir = storage.page_dir(url)
        page_dir.mkdir(parents=True)
        (page_dir / "page.pdf").write_bytes(b"pdf")
        (page_dir / "page.md").write_text("md")

        assert storage.is_downloaded(url) is True

    def test_is_downloaded_partial_pdf_only(self, tmp_path):
        """Test is_downloaded returns False when only PDF exists."""
        storage = LocalStorage(output_dir=tmp_path)
        url = "https://example.com/page"

        page_dir = storage.page_dir(url)
        page_dir.mkdir(parents=True)
        (page_dir / "page.pdf").write_bytes(b"pdf")

        assert storage.is_downloaded(url) is False

    def test_is_downloaded_partial_md_only(self, tmp_path):
        """Test is_downloaded returns False when only MD exists."""
        storage = LocalStorage(output_dir=tmp_path)
        url = "https://example.com/page"

        page_dir = storage.page_dir(url)
        page_dir.mkdir(parents=True)
        (page_dir / "page.md").write_text("md")

        assert storage.is_downloaded(url) is False

    def test_save_pdf(self, tmp_path):
        """Test saving PDF file."""
        storage = LocalStorage(output_dir=tmp_path)
        url = "https://example.com/page"
        pdf_bytes = b"%PDF-1.4 test pdf content"

        result_path = storage.save_pdf(url, pdf_bytes)

        assert result_path.exists()
        assert result_path.name == "page.pdf"
        assert result_path.read_bytes() == pdf_bytes

    def test_save_markdown(self, tmp_path):
        """Test saving Markdown file."""
        storage = LocalStorage(output_dir=tmp_path)
        url = "https://example.com/page"
        markdown_text = "# Test\n\nThis is test content."

        result_path = storage.save_markdown(url, markdown_text)

        assert result_path.exists()
        assert result_path.name == "page.md"
        assert result_path.read_text() == markdown_text

    def test_get_archive_root(self, tmp_path):
        """Test getting archive root for a domain."""
        storage = LocalStorage(output_dir=tmp_path)
        
        result = storage.get_archive_root("example.com")
        
        assert result == tmp_path / "example.com"

    def test_get_archive_root_lowercase(self, tmp_path):
        """Test that domain is lowercased."""
        storage = LocalStorage(output_dir=tmp_path)
        
        result = storage.get_archive_root("EXAMPLE.COM")
        
        assert result == tmp_path / "example.com"

    def test_ensure_dir_creates_parents(self, tmp_path):
        """Test that _ensure_dir creates parent directories."""
        storage = LocalStorage(output_dir=tmp_path)
        url = "https://example.com/deep/nested/path"

        page_dir = storage._ensure_dir(url)

        assert page_dir.exists()
        assert page_dir.is_dir()

    def test_sanitise_segment(self, tmp_path):
        """Test segment sanitization."""
        storage = LocalStorage(output_dir=tmp_path)
        
        # Valid chars preserved
        assert storage._sanitise_segment("abc123") == "abc123"
        assert storage._sanitise_segment("test-name") == "test-name"
        assert storage._sanitise_segment("file.txt") == "file.txt"
        
        # Invalid chars replaced
        assert storage._sanitise_segment("test name") == "test_name"
        assert storage._sanitise_segment("test@name") == "test_name"
        assert storage._sanitise_segment("test!name") == "test_name"
        assert storage._sanitise_segment("test/name") == "test_name"
