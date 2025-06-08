"""PDF generation for graded assignments."""
from __future__ import annotations

from pathlib import Path
from typing import Dict

from loguru import logger
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


class PDFGenerator:
    """Create graded PDFs with feedback overlays."""

    def __init__(self, output_dir: Path) -> None:
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate(self, image_path: str | Path, result: Dict[str, str]) -> Path:
        """Generate a graded PDF and return the path."""
        img = Image.open(image_path)
        pdf_path = self.output_dir / (Path(image_path).stem + '_graded.pdf')
        c = canvas.Canvas(str(pdf_path), pagesize=letter)

        width, height = letter
        img = img.resize((int(width), int(height)))
        c.drawInlineImage(img, 0, 0, width=width, height=height)

        c.setFont("Helvetica-Bold", 14)
        c.setFillColorRGB(1, 0, 0)
        c.drawString(40, height - 40, f"Score: {result.get('score', 'N/A')}")

        c.setFont("Helvetica", 12)
        c.setFillColorRGB(0, 0, 0)
        text_obj = c.beginText(40, height - 80)
        comments = str(result.get('comments', ''))
        for line in comments.splitlines():
            text_obj.textLine(line)
        c.drawText(text_obj)

        c.showPage()
        c.save()
        logger.debug(f"Generated PDF at {pdf_path}")
        return pdf_path
