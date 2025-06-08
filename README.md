# Autograding System

This repository contains a simplified handwriting autograder for mathematics assignments. The system uses Pix2Text for OCR, a manual GPT workflow for grading, and generates graded PDFs.

## Setup

1. Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r autograding-scripts/requirements.txt
```

2. Copy `.env.example` to `.env` and modify paths if required.

```bash
cp autograding-scripts/.env.example autograding-scripts/.env
```

## Usage

Run the main script with one or more image files:

```bash
python -m autograding_scripts.main path/to/image.png
```

Use batch mode to process multiple images:

```bash
python -m autograding_scripts.main -b path/to/img1.png path/to/img2.png
```

During processing, the program will display a prompt marked with `=== COPY TO GPT ===` that should be pasted into ChatGPT. After receiving the JSON response, paste it back into the terminal when prompted. A graded PDF will be produced in the output directory.

## Testing

Install test dependencies (same as requirements) and run:

```bash
pytest autograding-scripts/tests
```

## Notes

- No direct ChatGPT API calls are made. All GPT interactions happen via manual copy‑paste.
- Output files are stored in `autograding-scripts/output` by default.
