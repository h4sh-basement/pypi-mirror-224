"""Base class for Amadeus tools."""
from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import Field

from oplangchain.tools.amadeus.utils import authenticate
from oplangchain.tools.base import BaseTool

if TYPE_CHECKING:
    from amadeus import Client


class AmadeusBaseTool(BaseTool):
    """Base Tool for Amadeus."""

    client: Client = Field(default_factory=authenticate)
