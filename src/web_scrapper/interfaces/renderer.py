from __future__ import annotations

from abc import ABC, abstractmethod
from types import TracebackType
from typing import Optional, Type

class AbstractRenderer(ABC):
    """
    Interface for page rendering and fetching.
    """

    @abstractmethod
    async def start(self) -> None:
        """Initialise the renderer resources."""
        pass

    @abstractmethod
    async def stop(self) -> None:
        """Shut down the renderer resources."""
        pass

    @abstractmethod
    async def render_pdf(self, url: str) -> bytes:
        """Render page as PDF."""
        pass

    @abstractmethod
    async def fetch_html(self, url: str) -> str:
        """Fetch raw HTML for link extraction."""
        pass

    @abstractmethod
    async def fetch_markdown(self, url: str) -> str:
        """Fetch page as Markdown."""
        pass

    async def __aenter__(self) -> AbstractRenderer:
        await self.start()
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        await self.stop()
