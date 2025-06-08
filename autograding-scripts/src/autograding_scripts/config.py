"""Configuration management."""
from __future__ import annotations

import os
from pathlib import Path
from dataclasses import dataclass
from typing import Any, Dict

from dotenv import load_dotenv
from loguru import logger

from .utils import load_yaml, ensure_dir

ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = ROOT / 'config'
DEFAULT_SETTINGS = CONFIG_DIR / 'settings.yaml'
DEFAULT_RUBRICS = CONFIG_DIR / 'rubrics.yaml'
DEFAULT_SYMBOLS = CONFIG_DIR / 'symbol_mappings.yaml'


def load_env(env_path: str | Path | None = None) -> None:
    """Load environment variables from .env file."""
    env_file = env_path or ROOT / '.env'
    if Path(env_file).exists():
        load_dotenv(env_file)
        logger.debug(f"Loaded environment variables from {env_file}")
    else:
        logger.debug("No .env file found; using system environment variables")


@dataclass
class Settings:
    """Application settings."""
    input_dir: Path
    output_dir: Path
    log_dir: Path
    rubric: str
    rubric_definitions: Dict[str, Any]
    symbol_mappings: Dict[str, str]


def load_settings(settings_file: str | Path = DEFAULT_SETTINGS) -> Settings:
    """Load configuration from YAML files and environment variables."""
    load_env()

    settings = load_yaml(settings_file)
    rubrics = load_yaml(DEFAULT_RUBRICS)
    symbols = load_yaml(DEFAULT_SYMBOLS)

    input_dir = Path(os.getenv('INPUT_DIR', settings.get('input_dir', 'input')))
    output_dir = Path(os.getenv('OUTPUT_DIR', settings.get('output_dir', 'output')))
    log_dir = Path(os.getenv('LOG_DIR', settings.get('log_dir', 'logs')))

    ensure_dir(input_dir)
    ensure_dir(output_dir)
    ensure_dir(log_dir)

    return Settings(
        input_dir=input_dir,
        output_dir=output_dir,
        log_dir=log_dir,
        rubric=settings.get('rubric', 'default'),
        rubric_definitions=rubrics,
        symbol_mappings=symbols,
    )
