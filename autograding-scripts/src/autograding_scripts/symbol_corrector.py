"""Correct OCR symbols based on predefined mappings."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

from loguru import logger


@dataclass
class SymbolCorrector:
    """Apply symbol corrections to OCR text."""

    mappings: Dict[str, str]

    def correct(self, text: str) -> str:
        """Return text after applying symbol corrections."""
        corrected = text
        for wrong, right in self.mappings.items():
            if wrong in corrected:
                logger.debug(f"Replacing '{wrong}' with '{right}'")
                corrected = corrected.replace(wrong, right)
        return corrected
