# Web Scraper & Archiver - Project Context

## Project Overview

A production-grade, asynchronous website crawler that archives web pages as **PDF screenshots** and **Markdown documents**. Built with Python 3.8+ using modern async patterns.

### Key Technologies

| Component | Technology |
|-----------|------------|
| Language | Python 3.8+ |
| Async | `asyncio`, `async/await` |
| HTTP Client | `httpx` (async) |
| Browser Automation | Playwright (Chromium) |
| HTML Parsing | BeautifulSoup4 + lxml |
| Architecture | Ports & Adapters (Hexagonal) |

### Core Features

- **PDF screenshots**: Full-page rendering via Playwright Chromium
- **Markdown conversion**: Via Jina.ai reader API (`r.jina.ai/<url>`)
- **BFS crawling**: Configurable depth limiting with URL normalization
- **Concurrency control**: Semaphore-limited to prevent browser crashes
- **Retry logic**: Exponential backoff (1s → 2s → 4s)
- **Robots.txt support**: Optional compliance checking
- **Incremental runs**: Skip already-archived pages by default

---

## Project Structure

```
web_scrapper/
├── main.py                          # Entry point (runs CLI)
├── pyproject.toml                   # Package configuration
├── requirements.txt                 # Production dependencies
├── requirements-dev.txt             # Development dependencies
├── pytest.ini                       # Pytest configuration
├── README.md                        # User documentation
├── QWEN.md                          # Developer context (this file)
├── tests/
│   ├── conftest.py                  # Shared pytest fixtures
│   ├── test_archiver.py
│   ├── test_crawler.py
│   ├── test_renderer.py
│   ├── test_robots_checker.py
│   ├── test_storage.py
│   └── test_tracker.py
└── src/web_scrapper/
    ├── __init__.py
    ├── cli.py                       # CLI argument parsing & orchestration
    ├── core/
    │   ├── __init__.py
    │   ├── archiver.py              # SiteArchiver - main orchestrator
    │   ├── crawler.py               # CrawlQueue - BFS queue management
    │   ├── models.py                # Data classes (CrawlItem)
    │   ├── robots_checker.py        # RobotsTxtChecker
    │   └── tracker.py               # ProgressTracker
    ├── infrastructure/
    │   ├── __init__.py
    │   ├── local_storage.py         # LocalStorage - filesystem operations
    │   └── playwright_renderer.py   # PlaywrightRenderer - PDF + HTML
    └── interfaces/
        ├── __init__.py
        ├── renderer.py              # AbstractRenderer interface
        └── storage.py               # AbstractStorage interface
```

---

## Architecture

### Hexagonal Architecture Pattern

```
┌─────────────────────────────────────────────────────────┐
│                      Core (Business Logic)               │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐  │
│  │ SiteArchiver│  │ CrawlQueue  │  │ RobotsTxtChecker│  │
│  └─────────────┘  └─────────────┘  └─────────────────┘  │
└─────────────────────────────────────────────────────────┘
              │                       │
              ▼                       ▼
┌─────────────────────┐   ┌─────────────────────────────┐
│   Interfaces        │   │   Infrastructure            │
│  - AbstractRenderer │   │  - PlaywrightRenderer       │
│  - AbstractStorage  │   │  - LocalStorage             │
└─────────────────────┘   └─────────────────────────────┘
```

### Key Components

| Component | Responsibility |
|-----------|----------------|
| `SiteArchiver` | Orchestrates crawl, manages tasks with `FIRST_COMPLETED` pattern |
| `CrawlQueue` | BFS traversal, URL normalization, visited tracking |
| `PlaywrightRenderer` | Browser management, PDF rendering, HTTP fetching |
| `LocalStorage` | Filesystem operations, deterministic path derivation |
| `RobotsTxtChecker` | Fetches/caches `robots.txt`, compliance checking |
| `ProgressTracker` | Real-time progress logging, summary statistics |

---

## Building and Running

### Setup

```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Playwright browser (Chromium only)
playwright install chromium

# Optional: Install dev dependencies
pip install -r requirements-dev.txt
```

### Running the Scraper

```bash
# Option 1: Run directly (recommended for development)
python main.py https://example.com

# Option 2: Install as package, run from anywhere
pip install -e .
web-scrapper https://example.com

# Option 3: Run as module
python -m web_scrapper.cli https://example.com
```

### Common CLI Options

```bash
python main.py https://example.com \
    --depth 3 \
    --delay 1.0 \
    --concurrency 5 \
    --retries 3 \
    --output ./archive \
    --no-skip \
    --no-markdown \
    --respect-robots \
    --verbose
```

| Option | Default | Description |
|--------|---------|-------------|
| `--depth`, `-d` | 3 | Maximum crawl depth |
| `--delay` | 1.0 | Politeness delay (seconds) |
| `--concurrency`, `-c` | 5 | Max simultaneous requests |
| `--retries` | 3 | Per-request retry count |
| `--output`, `-o` | `.` | Output directory |
| `--no-skip` | false | Re-download existing pages |
| `--no-markdown` | false | Skip Markdown (PDF only) |
| `--respect-robots` | false | Respect robots.txt |
| `--verbose`, `-v` | false | Enable DEBUG logging |

### Output Structure

```
./
└── example.com/
    ├── index/
    │   ├── page.pdf
    │   └── page.md
    ├── about/
    │   ├── page.pdf
    │   └── page.md
    └── blog/my-first-post/
        ├── page.pdf
        └── page.md
```

---

## Development Commands

### Testing

```bash
# Run all tests
pytest tests/ -v

# With coverage
pytest tests/ --cov=web_scrapper --cov-report=html

# Run specific test file
pytest tests/test_crawler.py -v
```

### Type Checking

```bash
mypy src/
```

### Linting

```bash
ruff check src/ tests/
```

---

## Development Conventions

### Code Style

- **Type hints**: Full type annotations using `typing` module (Python 3.8 compatible)
- **Imports**: Grouped as stdlib → third-party → local; use `from __future__ import annotations`
- **Naming**: `snake_case` for functions/variables, `PascalCase` for classes
- **Docstrings**: Google-style for public APIs

### Testing Practices

- **Test files**: `test_*.py` in `tests/` directory
- **Fixtures**: Shared fixtures in `conftest.py`
- **Async tests**: Uses `pytest-asyncio` with `asyncio_mode = auto`
- **Coverage target**: Core logic in `src/web_scrapper/core/`

### Async Patterns

- Use `async/await` throughout; no blocking calls in async functions
- Context managers for resource cleanup (`async with`)
- `asyncio.Semaphore` for concurrency limiting
- `asyncio.wait(..., return_when=FIRST_COMPLETED)` for responsive task management

### Error Handling

- Non-raising wrappers in `SiteArchiver._process_page()` ensure one failure doesn't kill the crawl
- Retry logic with exponential backoff in `PlaywrightRenderer._with_retry()`
- Logging at appropriate levels: `DEBUG` for details, `INFO` for progress, `WARNING/ERROR` for failures

---

## Key Implementation Details

### URL Normalization

```python
# Strips fragments, trailing slashes, lowercases
"https://Example.COM/page/" → "https://example.com/page"
```

### Concurrency Control

- Single `asyncio.Semaphore` limits concurrent browser operations
- Prevents Chromium crashes under heavy load
- Configurable via `--concurrency` flag

### Retry Strategy

- Exponential backoff: `2^(attempt-1)` seconds
- Independent retry for PDF, HTML, and Markdown operations
- Configurable via `--retries` flag

### Robots.txt Compliance

- Fetches and caches `robots.txt` per domain
- Optional via `--respect-robots` flag
- Uses `urllib.robotparser` under the hood

---

## Common Tasks

### Adding a New Renderer

1. Implement `AbstractRenderer` interface in `interfaces/renderer.py`
2. Add new class in `infrastructure/`
3. Update `cli.py` to instantiate the new renderer

### Adding a New Storage Backend

1. Implement `AbstractStorage` interface in `interfaces/storage.py`
2. Add new class in `infrastructure/`
3. Update `cli.py` to use the new storage

### Modifying Crawl Behavior

- **Queue logic**: Edit `core/crawler.py` (`CrawlQueue.enqueue_links()`)
- **Page processing**: Edit `core/archiver.py` (`SiteArchiver._process_page()`)
- **URL filtering**: Add schemes to `_IGNORED_SCHEMES` in `core/crawler.py`

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Playwright browser crashes | Lower `--concurrency`, ensure `playwright install chromium` |
| Jina API timeouts | Increase `--retries` or `--delay` |
| Pages not archiving | Check `--verbose` output, verify URL scheme |
| Tests failing | Ensure `pytest-asyncio` is installed, check `asyncio_mode` |
