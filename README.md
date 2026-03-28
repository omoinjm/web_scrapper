# 🕷️ Web Scraper & Archiver

A production-grade, async website crawler that saves every page as a **PDF screenshot** and **Markdown document**.

---

## Features

| Feature | Details |
|---|---|
| PDF screenshots | Playwright Chromium, full background rendering |
| Markdown conversion | Jina.ai reader API (`https://r.jina.ai/<url>`) |
| Async + concurrent | `asyncio` + `Semaphore` concurrency control |
| Retry logic | Exponential back-off, configurable attempts |
| Depth limiting | Configurable BFS depth |
| Skip existing | Re-runs are incremental by default |
| Clean file layout | One folder per page, `page.pdf` + `page.md` |
| Polite crawling | Configurable delay between requests |
| Robots.txt support | Optional respect for `robots.txt` rules |
| PDF-only mode | Skip Markdown generation for offline archiving |

---

## Project Structure

```
web_scrapper/
├── main.py                          # Entry point (runs CLI)
├── pyproject.toml                   # Package configuration
├── requirements.txt                 # Production dependencies
├── requirements-dev.txt             # Development dependencies
├── README.md
├── tests/
│   ├── test_crawler.py
│   ├── test_storage.py
│   ├── test_archiver.py
│   ├── test_renderer.py
│   └── test_robots_checker.py
└── src/web_scrapper/
    ├── __init__.py
    ├── cli.py                       # CLI argument parsing & orchestration
    ├── core/
    │   ├── __init__.py
    │   ├── archiver.py              # SiteArchiver - main orchestrator
    │   ├── crawler.py               # CrawlQueue - BFS queue management
    │   ├── models.py                # Data classes (CrawlItem)
    │   ├── robots_checker.py        # RobotsTxtChecker - robots.txt compliance
    │   └── tracker.py               # ProgressTracker - progress logging
    ├── infrastructure/
    │   ├── __init__.py
    │   ├── local_storage.py         # LocalStorage - filesystem operations
    │   └── playwright_renderer.py   # PlaywrightRenderer - PDF + HTML fetching
    └── interfaces/
        ├── __init__.py
        ├── renderer.py              # AbstractRenderer interface
        └── storage.py               # AbstractStorage interface
```

---

## Setup

### 1. Prerequisites

- Python 3.8 or later
- pip

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Playwright browser (Chromium)

```bash
playwright install chromium
```

> Only Chromium is needed; skip Firefox/WebKit to save space.

### 4. (Optional) Install development dependencies

```bash
pip install -r requirements-dev.txt
```

---

## Usage

### Quick Start

**Option 1: Run directly with Python** (recommended for development)

```bash
# From the project root directory
python main.py https://example.com
```

**Option 2: Install as a package and use the CLI command** (recommended for production)

```bash
# Install the package (creates the `web-scrapper` executable)
pip install -e .

# Verify installation
web-scrapper --help

# Run from anywhere
web-scrapper https://example.com
```

**Option 3: Run as a module**

```bash
python -m web_scrapper.cli https://example.com
```

### Basic

```bash
python main.py https://example.com
```

### With options

```bash
python main.py https://example.com \
    --depth 3 \
    --delay 1.5 \
    --concurrency 4 \
    --retries 3 \
    --output ./archive
```

### Force re-download (ignore cached pages)

```bash
python main.py https://example.com --no-skip
```

### PDF only (skip Markdown generation)

```bash
python main.py https://example.com --no-markdown
```

### Respect robots.txt

```bash
python main.py https://example.com --respect-robots
```

### Verbose / debug logging

```bash
python main.py https://example.com --verbose
```

### Root page only (depth 0)

```bash
python main.py https://example.com --depth 0
```

---

## CLI Reference

```
usage: web-scrapper [-h] [--depth N] [--delay SECS] [--concurrency N]
                    [--retries N] [--output DIR] [--no-skip] [--no-markdown]
                    [--respect-robots] [--verbose]
                    URL

positional arguments:
  URL                  Root URL to crawl (e.g. https://example.com)

options:
  --depth, -d N        Maximum crawl depth (default: 3)
  --delay SECS         Politeness delay between requests (default: 1.0)
  --concurrency, -c N  Maximum simultaneous requests (default: 5)
  --retries N          Per-request retry count (default: 3)
  --output, -o DIR     Root output directory (default: .)
  --no-skip            Re-download even if already archived
  --no-markdown        Skip Markdown generation (PDF only)
  --respect-robots     Respect robots.txt rules
  --verbose, -v        Enable DEBUG logging
```

---

## Output Structure

```
./
└── example.com/
    ├── index/
    │   ├── page.pdf
    │   └── page.md
    ├── about/
    │   ├── page.pdf
    │   └── page.md
    └── blog/
        └── my-first-post/
            ├── page.pdf
            └── page.md
```

- The top-level folder is the **domain name**.
- Each URL path maps to a subdirectory.
- Root `/` → `index/`
- `/about/team` → `about/team/`

---

## Architecture

### Design Pattern

This project follows a **ports-and-adapters** (hexagonal) architecture:

- **Interfaces** (`interfaces/`): Define abstract contracts for rendering and storage
- **Core** (`core/`): Business logic independent of external implementations
- **Infrastructure** (`infrastructure/`): Concrete implementations of interfaces

### Components

#### `CrawlQueue` (`core/crawler.py`)
- BFS traversal using a `deque`
- URL normalisation (strips fragments, trailing slashes, lowercases host)
- Domain comparison strips `www.` prefix
- Ignores `mailto:`, `tel:`, `javascript:`, `data:` schemes

#### `PlaywrightRenderer` (`infrastructure/playwright_renderer.py`)
- Single shared Playwright browser
- Semaphore-limited concurrency prevents browser crashes
- `httpx.AsyncClient` with `follow_redirects=True` for HTML/Markdown fetching
- Retries with `2^(attempt-1)` second back-off (1s → 2s → 4s)

#### `LocalStorage` (`infrastructure/local_storage.py`)
- Deterministic path derivation from URL
- Query strings safely encoded into folder names
- `is_downloaded()` checks both files before skipping

#### `SiteArchiver` (`core/archiver.py`)
- Orchestrates queue, renderer, storage
- Task-based concurrency: each page is an `asyncio.Task`
- Uses `FIRST_COMPLETED` pattern for responsive link discovery
- Non-raising wrappers ensure one bad page never kills the crawl

#### `RobotsTxtChecker` (`core/robots_checker.py`)
- Fetches and caches `robots.txt` per domain
- Optional compliance checking via `--respect-robots` flag

#### `ProgressTracker` (`core/tracker.py`)
- Real-time progress logging
- Elapsed time tracking
- Summary statistics on completion

---

## Robustness

| Concern | Mitigation |
|---|---|
| Network timeouts | 30s default; caught per-attempt |
| Jina API failures | Retried independently from PDF |
| Playwright crashes | Browser context isolated per page |
| File system errors | Logged; crawl continues |
| Already-crawled pages | Visited set prevents re-enqueue |
| Malformed URLs | Caught at normalisation stage |
| Browser overload | Semaphore limits concurrent contexts |
| robots.txt violations | Optional compliance checking |

---

## Development

### Running Tests

```bash
pytest tests/ -v
```

### With Coverage

```bash
pytest tests/ --cov=web_scrapper --cov-report=html
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

## Tips

- **Rate limiting**: Increase `--delay` for well-behaved crawling on real sites.
- **Large sites**: Lower `--depth` (e.g. `2`) and `--concurrency` (e.g. `2`).
- **Resuming**: The default `--skip-existing` means re-running picks up where you left off.
- **Jina API**: Works best with publicly accessible URLs. Authentication-gated pages will return limited content.
- **PDF-only mode**: Use `--no-markdown` for fully offline archiving without external API calls.
- **Robots.txt**: Enable `--respect-robots` for ethical crawling of third-party sites.

---

## License

MIT
