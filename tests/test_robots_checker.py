"""Tests for the RobotsTxtChecker component."""

from unittest.mock import MagicMock, patch

import httpx
import pytest

from web_scrapper.core.robots_checker import RobotsTxtChecker


class TestRobotsTxtChecker:
    """Tests for the RobotsTxtChecker class."""

    @pytest.fixture
    def checker(self):
        """Create a RobotsTxtChecker instance."""
        return RobotsTxtChecker(http_timeout=5.0)

    def test_init_default_values(self):
        """Test default initialization values."""
        checker = RobotsTxtChecker()
        assert checker.http_timeout == 10.0
        assert checker._parsers == {}
        assert checker._http_client is None

    def test_init_custom_values(self):
        """Test custom initialization values."""
        checker = RobotsTxtChecker(http_timeout=15.0)
        assert checker.http_timeout == 15.0

    def test_get_domain(self, checker):
        """Test domain extraction from URL."""
        assert checker._get_domain("https://example.com/page") == "https://example.com"
        assert checker._get_domain("https://example.com/page?q=1") == "https://example.com"
        assert checker._get_domain("http://sub.example.com/path") == "http://sub.example.com"

    def test_context_manager(self, checker):
        """Test context manager creates and closes HTTP client."""
        with checker as c:
            assert c._http_client is not None
            assert isinstance(c._http_client, httpx.Client)
        
        assert checker._http_client is None

    @patch("httpx.Client")
    def test_fetch_robots_success(self, mock_client_class, checker):
        """Test successful robots.txt fetching."""
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "User-agent: *\nDisallow: /admin"
        mock_client.get.return_value = mock_response
        mock_client_class.return_value = mock_client
        
        with checker:
            parser = checker._fetch_robots("https://example.com")
            
            mock_client.get.assert_called_once_with("https://example.com/robots.txt")
            assert parser is not None

    @patch("httpx.Client")
    def test_fetch_robots_404(self, mock_client_class, checker):
        """Test handling of 404 robots.txt (allowed by default)."""
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_client.get.return_value = mock_response
        mock_client_class.return_value = mock_client
        
        with checker:
            parser = checker._fetch_robots("https://example.com")
            
            # Should not raise, parser should allow all
            assert parser.mtime() == 0  # No rules parsed

    @patch("httpx.Client")
    def test_fetch_robots_request_error(self, mock_client_class, checker):
        """Test handling of network error."""
        mock_client = MagicMock()
        mock_client.get.side_effect = httpx.RequestError("Network error")
        mock_client_class.return_value = mock_client
        
        with checker:
            parser = checker._fetch_robots("https://example.com")
            
            # Should not raise, parser should allow all
            assert parser is not None

    @patch("httpx.Client")
    def test_can_fetch_allowed(self, mock_client_class, checker):
        """Test can_fetch returns True for allowed URLs."""
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 200
        # Allow all paths
        mock_response.text = "User-agent: *\nDisallow:"
        mock_client.get.return_value = mock_response
        mock_client_class.return_value = mock_client
        
        with checker:
            # First call fetches robots.txt
            result = checker.can_fetch("https://example.com/public")
            assert result is True

    @patch("httpx.Client")
    def test_can_fetch_disallowed(self, mock_client_class, checker):
        """Test can_fetch returns False for disallowed URLs."""
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 200
        # Disallow /admin
        mock_response.text = "User-agent: *\nDisallow: /admin"
        mock_client.get.return_value = mock_response
        mock_client_class.return_value = mock_client
        
        with checker:
            result = checker.can_fetch("https://example.com/admin/secret")
            assert result is False

    @patch("httpx.Client")
    def test_can_fetch_no_robots_txt(self, mock_client_class, checker):
        """Test can_fetch returns True when no robots.txt exists."""
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_client.get.return_value = mock_response
        mock_client_class.return_value = mock_client
        
        with checker:
            result = checker.can_fetch("https://example.com/anything")
            assert result is True

    def test_can_fetch_without_context_manager(self, checker):
        """Test can_fetch when HTTP client not initialized."""
        # Should not raise, should return True (permissive)
        result = checker.can_fetch("https://example.com/test")
        assert result is True

    def test_is_allowed_alias(self, checker):
        """Test is_allowed is an alias for can_fetch."""
        # Both should return True when no HTTP client
        assert checker.can_fetch("https://example.com") == checker.is_allowed("https://example.com")

    @patch("httpx.Client")
    def test_caches_parser_per_domain(self, mock_client_class, checker):
        """Test that parsers are cached per domain."""
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "User-agent: *\nDisallow:"
        mock_client.get.return_value = mock_response
        mock_client_class.return_value = mock_client
        
        with checker:
            checker.can_fetch("https://example.com/page1")
            checker.can_fetch("https://example.com/page2")
            checker.can_fetch("https://other.com/page1")
            
            # Should have fetched robots.txt twice (once per domain)
            assert mock_client.get.call_count == 2
