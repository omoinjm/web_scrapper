"""Tests for the ProgressTracker component."""

import time

from web_scrapper.core.tracker import ProgressTracker


class TestProgressTracker:
    """Tests for the ProgressTracker class."""

    def test_init(self):
        """Test initialization."""
        tracker = ProgressTracker()
        
        assert tracker.total_queued == 0
        assert tracker.succeeded == 0
        assert tracker.skipped == 0
        assert tracker.failed == 0
        assert tracker.processed == 0

    def test_processed_property(self):
        """Test processed property calculation."""
        tracker = ProgressTracker()
        tracker.succeeded = 5
        tracker.skipped = 3
        tracker.failed = 2
        
        assert tracker.processed == 10

    def test_elapsed_format(self):
        """Test elapsed time formatting."""
        tracker = ProgressTracker()
        # Elapsed should be very small, but format should be correct
        elapsed = tracker.elapsed()
        
        # Format should be XmYYs
        assert "m" in elapsed
        assert "s" in elapsed

    def test_elapsed_accuracy(self):
        """Test elapsed time is approximately correct."""
        tracker = ProgressTracker()
        time.sleep(0.1)
        elapsed = tracker.elapsed()
        
        # Should show at least 0m00s
        assert elapsed is not None

    def test_log_status(self, caplog):
        """Test log_status outputs correct format."""
        tracker = ProgressTracker()
        tracker.succeeded = 5
        tracker.skipped = 2
        tracker.failed = 1
        tracker.total_queued = 10
        
        tracker.log_status("https://example.com/test")
        
        assert "5 succeeded" in caplog.text
        assert "2 skipped" in caplog.text
        assert "1 failed" in caplog.text
        assert "https://example.com/test" in caplog.text

    def test_summary(self, caplog):
        """Test summary outputs correct format."""
        tracker = ProgressTracker()
        tracker.succeeded = 10
        tracker.skipped = 5
        tracker.failed = 2
        tracker.total_queued = 17
        
        tracker.summary()
        
        assert "Crawl complete" in caplog.text
        assert "10 succeeded" in caplog.text
        assert "5 skipped" in caplog.text
        assert "2 failed" in caplog.text
        assert "17 total unique URLs" in caplog.text

    def test_summary_with_zero_failures(self, caplog):
        """Test summary when all pages succeed."""
        tracker = ProgressTracker()
        tracker.succeeded = 10
        tracker.skipped = 0
        tracker.failed = 0
        tracker.total_queued = 10
        
        tracker.summary()
        
        assert "0 failed" in caplog.text
