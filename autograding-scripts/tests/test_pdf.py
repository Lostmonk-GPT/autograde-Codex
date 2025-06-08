from pathlib import Path
from PIL import Image
from autograding_scripts.pdf_generator import PDFGenerator


def test_pdf_generation(tmp_path):
    image_path = tmp_path / "sample.png"
    img = Image.new("RGB", (50, 50), color=(255, 255, 255))
    img.save(image_path)

    gen = PDFGenerator(tmp_path)
    result = {"score": 5, "comments": "Good job"}
    pdf = gen.generate(image_path, result)
    assert pdf.exists()
