import json
from typing import List
from pathlib import Path
from . import __init__  # ensure package
from launcher.models.game import Game
from launcher.utils.paths import DATA_DIR

LIB_FILE = DATA_DIR / "library.json"

def load_games() -> List[Game]:
    if not LIB_FILE.exists():
        return []
    data = json.loads(LIB_FILE.read_text(encoding="utf-8"))
    return [Game(**g) for g in data.get("games", [])]

def save_games(games: List[Game]) -> None:
    payload = {"games": [g.model_dump() for g in games]}
    LIB_FILE.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
