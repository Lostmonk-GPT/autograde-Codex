"""GPT prompt formatting and manual response parsing."""
from __future__ import annotations

import json
from typing import Any, Dict, Optional

from loguru import logger

PROMPT_HEADER = "=== COPY TO GPT ==="
PROMPT_FOOTER = "=== END COPY ==="


def format_prompt(ocr_text: str, rubric_id: str, rubrics: Dict[str, Any]) -> str:
    """Format the GPT prompt using OCR text and rubric."""
    rubric = rubrics.get(rubric_id, {})
    prompt = [PROMPT_HEADER]
    prompt.append("You are a grading assistant for mathematics assignments.")
    prompt.append(f"Rubric: {json.dumps(rubric, indent=2)}")
    prompt.append("Student Submission:\n" + ocr_text)
    prompt.append("Return JSON in the form: { 'score': int, 'comments': '...' }")
    prompt.append(PROMPT_FOOTER)
    return "\n".join(prompt)


def parse_gpt_response(response: str) -> Dict[str, Any]:
    """Parse GPT JSON response with error handling."""
    cleaned = response.strip()
    try:
        data = json.loads(cleaned)
        if not isinstance(data, dict):
            raise ValueError('Response JSON must be an object')
        return data
    except json.JSONDecodeError as exc:
        logger.error(f"JSON decode error: {exc}")
        raise


def interactive_gpt_workflow(ocr_text: str, rubric_id: str, rubrics: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Manual copy-paste workflow for GPT grading."""
    prompt = format_prompt(ocr_text, rubric_id, rubrics)

    print("\n" + "=" * 60)
    print("COPY THE FOLLOWING TO CHATGPT:")
    print("=" * 60)
    print(prompt)
    print("=" * 60)
    print("\n1. Copy the above text")
    print("2. Paste it into ChatGPT")
    print("3. Copy the JSON response")
    print("4. Paste it below when prompted")
    print("-" * 60)

    while True:
        try:
            print("Paste GPT response here:")
            user_input = input('> ')
            if not user_input.strip():
                print("Please paste the GPT response.")
                continue
            parsed = parse_gpt_response(user_input)
            return parsed
        except Exception as exc:  # broad catch to allow manual retry
            logger.error(f"Error parsing response: {exc}")
            print("Error parsing response. Please ensure the JSON is valid.")
            retry = input("Try again? (y/n): ")
            if retry.lower() != 'y':
                return None
