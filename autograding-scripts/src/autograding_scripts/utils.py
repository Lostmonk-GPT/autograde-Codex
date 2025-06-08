"""Utility functions for the autograding system."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from loguru import logger


def load_yaml(path: str | Path) -> Any:
    """Load a YAML file and return its data."""
    import yaml
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as exc:
        logger.error(f"Failed to load YAML from {path}: {exc}")
        raise


def save_json(data: Any, path: str | Path) -> None:
    """Save data to a JSON file."""
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
    except Exception as exc:
        logger.error(f"Failed to save JSON to {path}: {exc}")
        raise


def ensure_dir(path: str | Path) -> Path:
    """Ensure a directory exists and return the Path."""
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p

