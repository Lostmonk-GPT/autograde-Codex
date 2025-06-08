"""Entry point for the autograding system."""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import List

from loguru import logger

from .config import load_settings
from .ocr_processor import OCRProcessor
from .symbol_corrector import SymbolCorrector
from .gpt_formatter import interactive_gpt_workflow
from .pdf_generator import PDFGenerator


def process_file(file_path: Path, settings) -> None:
    """Process a single assignment file."""
    ocr = OCRProcessor()
    text = ocr.extract_text(file_path)

    corrector = SymbolCorrector(settings.symbol_mappings)
    corrected = corrector.correct(text)

    gpt_result = interactive_gpt_workflow(corrected, settings.rubric, settings.rubric_definitions)
    if not gpt_result:
        print(f"Skipping {file_path} due to GPT error")
        return

    pdf_gen = PDFGenerator(settings.output_dir)
    pdf_path = pdf_gen.generate(file_path, gpt_result)
    print(f"Generated graded PDF: {pdf_path}")


def batch_process(files: List[Path], settings) -> None:
    """Process multiple files with manual GPT steps."""
    for idx, file_path in enumerate(files, 1):
        print(f"\n{'='*50}")
        print(f"ASSIGNMENT {idx}/{len(files)}: {file_path}")
        print(f"{'='*50}")
        process_file(file_path, settings)
        print(f"\nProgress: {idx}/{len(files)} completed")


def main(argv: List[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Handwritten Math Autograder")
    parser.add_argument('files', nargs='*', help='Image files to grade')
    parser.add_argument('-b', '--batch', action='store_true', help='Batch mode for multiple files')
    parser.add_argument('-r', '--rubric', default=None, help='Rubric ID to use')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable debug logging')

    args = parser.parse_args(argv)

    if args.verbose:
        logger.remove()
        logger.add(lambda msg: print(msg, end=''))
        logger.level('DEBUG')

    settings = load_settings()
    if args.rubric:
        settings.rubric = args.rubric

    files = [Path(f) for f in args.files] if args.files else list(settings.input_dir.glob('*.png'))

    if not files:
        print("No input files provided.")
        return

    if args.batch:
        batch_process(files, settings)
    else:
        for file_path in files:
            process_file(file_path, settings)


if __name__ == '__main__':
    main()
