"""OCR processing using Pix2Text with basic preprocessing."""
from __future__ import annotations

from pathlib import Path
from typing import Optional

from loguru import logger
from PIL import Image
import numpy as np
import cv2


class OCRProcessor:
    """Handle OCR extraction from scanned assignments."""

    def __init__(self) -> None:
        try:
            from pix2text import Pix2Text
            self.ocr_engine = Pix2Text()
            logger.debug("Pix2Text loaded successfully")
        except Exception as exc:
            logger.warning(f"Pix2Text not available: {exc}. Using fallback text.")
            self.ocr_engine = None

    def preprocess(self, image: Image.Image) -> Image.Image:
        """Perform simple image preprocessing."""
        img = np.array(image)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        img = cv2.GaussianBlur(img, (3, 3), 0)
        img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        return Image.fromarray(img)

    def extract_text(self, path: str | Path) -> str:
        """Extract text from an image path."""
        img = Image.open(path)
        processed = self.preprocess(img)

        if self.ocr_engine:
            try:
                result = self.ocr_engine(processed)
                if isinstance(result, list):
                    text = "\n".join(res['text'] for res in result)
                else:
                    text = str(result)
                logger.debug("OCR extraction complete")
                return text
            except Exception as exc:
                logger.error(f"OCR processing failed: {exc}")
        # Fallback
        logger.warning("Using fallback OCR output")
        return "Unable to perform OCR on the provided image."
