"""Tests for the CrawlQueue component."""

import pytest

from web_scrapper.core.crawler import CrawlQueue


class TestCrawlQueue:
    """Tests for the CrawlQueue class."""

    def test_crawl_queue_normalise_url(self):
        """Test URL normalization."""
        # Strip fragments
        assert CrawlQueue.normalise_url("https://example.com/path#fragment") == "https://example.com/path"
        # Lowercase scheme and host
        assert CrawlQueue.normalise_url("HTTPS://EXAMPLE.COM/PATH/") == "https://example.com/path"
        # Strip trailing slash
        assert CrawlQueue.normalise_url("https://example.com/path/") == "https://example.com/path"
        # Keep query string
        assert CrawlQueue.normalise_url("https://example.com/path?q=1") == "https://example.com/path?q=1"
        # Strip fragment but keep query
        assert CrawlQueue.normalise_url("https://example.com/path?q=1#section") == "https://example.com/path?q=1"

    def test_crawl_queue_initialization(self):
        """Test queue initialization with root URL."""
        queue = CrawlQueue(root_url="https://example.com", max_depth=1)
        
        assert len(queue) == 1
        assert queue.root_url == "https://example.com"
        assert queue.max_depth == 1
        assert queue.domain == "example.com"
        
        item = queue.pop()
        assert item.url == "https://example.com/"
        assert item.depth == 0

    def test_crawl_queue_enqueue_links(self):
        """Test enqueueing links from HTML."""
        html = '<a href="/about">About</a><a href="https://external.com">External</a>'
        queue = CrawlQueue(root_url="https://example.com", max_depth=1)
        added = queue.enqueue_links("https://example.com", html, current_depth=0)

        assert added == 1
        assert len(queue) == 2  # root + about

    def test_crawl_queue_enqueue_links_respects_depth(self):
        """Test that links are not enqueued beyond max depth."""
        html = '<a href="/page">Page</a>'
        queue = CrawlQueue(root_url="https://example.com", max_depth=0)
        
        # At depth 0, should not enqueue (max_depth=0 means root only)
        added = queue.enqueue_links("https://example.com", html, current_depth=0)
        
        assert added == 0
        assert len(queue) == 1  # Only root

    def test_crawl_queue_avoids_duplicates(self):
        """Test that duplicate URLs are not enqueued."""
        html = '<a href="/page">Page</a><a href="/page">Page Again</a>'
        queue = CrawlQueue(root_url="https://example.com", max_depth=2)
        
        added = queue.enqueue_links("https://example.com", html, current_depth=0)
        
        assert added == 1  # Only one unique URL
        assert len(queue.visited) == 2  # root + /page

    def test_crawl_queue_ignores_invalid_schemes(self):
        """Test that mailto, tel, javascript links are ignored."""
        html = '''
            <a href="mailto:test@example.com">Email</a>
            <a href="tel:+1234567890">Phone</a>
            <a href="javascript:void(0)">JS</a>
            <a href="data:text/plain,hello">Data</a>
            <a href="/valid">Valid</a>
        '''
        queue = CrawlQueue(root_url="https://example.com", max_depth=2)
        added = queue.enqueue_links("https://example.com", html, current_depth=0)
        
        assert added == 1  # Only the valid link

    def test_crawl_queue_ignores_external_domains(self):
        """Test that external domain links are ignored."""
        html = '''
            <a href="https://example.com/internal">Internal</a>
            <a href="https://other.com/external">External</a>
            <a href="https://www.example.com/with-www">With WWW</a>
        '''
        queue = CrawlQueue(root_url="https://example.com", max_depth=2)
        added = queue.enqueue_links("https://example.com", html, current_depth=0)
        
        assert added == 2  # Internal and with-www (www stripped)

    def test_crawl_queue_bare_domain(self):
        """Test _bare_domain strips www prefix."""
        assert CrawlQueue._bare_domain("www.example.com") == "example.com"
        assert CrawlQueue._bare_domain("EXAMPLE.COM") == "example.com"
        assert CrawlQueue._bare_domain("www.EXAMPLE.com") == "example.com"
        assert CrawlQueue._bare_domain("sub.example.com") == "sub.example.com"

    def test_crawl_queue_len_and_bool(self):
        """Test __len__ and __bool__ methods."""
        queue = CrawlQueue(root_url="https://example.com", max_depth=1)
        
        assert len(queue) == 1
        assert bool(queue) is True
        
        queue.pop()
        
        assert len(queue) == 0
        assert bool(queue) is False

    def test_crawl_queue_depth_increment(self):
        """Test that enqueued links have correct depth."""
        html = '<a href="/page1">Page 1</a><a href="/page2">Page 2</a>'
        queue = CrawlQueue(root_url="https://example.com", max_depth=3)
        
        # Enqueue from root (depth 0)
        queue.enqueue_links("https://example.com", html, current_depth=0)
        
        # Pop and check depths
        root = queue.pop()
        assert root.depth == 0
        
        page1 = queue.pop()
        assert page1.depth == 1
        
        page2 = queue.pop()
        assert page2.depth == 1
