# ==========================================
# Project: PyRetroGUI
# File: utils
# Author: Davide Sattin 
# Created: 25/01/2026 18:20
# Description:Utils for project paths.
# ==========================================
from pathlib import Path

# project_root = assets/, pyretrogui/, tests/
PROJECT_ROOT = Path(__file__).resolve().parents[2]

ASSETS_DIR = PROJECT_ROOT / "assets"


def asset_path(*parts: str) -> Path:
    """
    Get the absolute path for assets folder.
    """
    return ASSETS_DIR / Path(*parts)
