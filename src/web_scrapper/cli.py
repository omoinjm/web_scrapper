from __future__ import annotations

import argparse
import asyncio
import logging
import sys
from pathlib import Path
from urllib.parse import urlparse

from web_scrapper.core.archiver import SiteArchiver
from web_scrapper.infrastructure.local_storage import LocalStorage
from web_scrapper.infrastructure.playwright_renderer import PlaywrightRenderer

def _configure_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    fmt = "%(asctime)s [%(levelname)-8s] %(name)s — %(message)s"
    datefmt = "%H:%M:%S"
    logging.basicConfig(level=level, format=fmt, datefmt=datefmt, stream=sys.stderr)
    for noisy in ("httpx", "httpcore", "playwright", "asyncio"):
        logging.getLogger(noisy).setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

def _build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="web-scrapper",
        description="Crawl a website and archive each page as PDF + Markdown.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("url", metavar="URL", help="Root URL to crawl (e.g. https://example.com)")
    parser.add_argument("--depth", "-d", type=int, default=3, help="Maximum crawl depth")
    parser.add_argument("--delay", type=float, default=1.0, help="Politeness delay between requests")
    parser.add_argument("--concurrency", "-c", type=int, default=5, help="Max simultaneous requests")
    parser.add_argument("--retries", type=int, default=3, help="Per-request retry count")
    parser.add_argument("--output", "-o", type=Path, default=Path("."), help="Output directory")
    parser.add_argument("--no-skip", action="store_true", help="Re-download pages even if already archived")
    parser.add_argument("--no-markdown", action="store_true", help="Skip Markdown generation (PDF only)")
    parser.add_argument("--respect-robots", action="store_true", help="Respect robots.txt rules")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable debug logging")
    return parser

async def _async_main(args: argparse.Namespace) -> int:
    _configure_logging(verbose=args.verbose)

    parsed = urlparse(args.url)
    if not parsed.scheme or not parsed.netloc:
        logger.error("Invalid URL: %s", args.url)
        return 1

    renderer = PlaywrightRenderer(
        delay=args.delay,
        max_retries=args.retries,
        concurrency=args.concurrency,
    )
    storage = LocalStorage(output_dir=args.output)

    archiver = SiteArchiver(
        renderer=renderer,
        storage=storage,
        root_url=args.url,
        max_depth=args.depth,
        skip_existing=not args.no_skip,
        fetch_markdown=not args.no_markdown,
        respect_robots=args.respect_robots,
    )

    progress = await archiver.run()
    return 0 if progress.failed == 0 else 1

def main() -> None:
    parser = _build_arg_parser()
    args = parser.parse_args()
    try:
        sys.exit(asyncio.run(_async_main(args)))
    except KeyboardInterrupt:
        sys.stderr.write("\nInterrupted by user\n")
        sys.exit(130)

if __name__ == "__main__":
    main()
